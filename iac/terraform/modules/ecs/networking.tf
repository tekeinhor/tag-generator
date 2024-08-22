locals {

  private = { for k, v in var.subnets : k => v if v.type == "private" } #filter to only have private subnets info
  public  = { for k, v in var.subnets : k => v if v.type == "public" }  #filter to only have public subnets info
}



####### VPC #######

resource "aws_vpc" "tag_gen_vpc" {
  cidr_block = "10.0.0.0/20"
  tags = {
    Name = "TagGen VPC"
  }
}

####### Private and Public Subnet #######
resource "aws_subnet" "publics" {
  for_each          = local.public
  vpc_id            = aws_vpc.tag_gen_vpc.id
  cidr_block        = each.value.cidr_block
  availability_zone = each.value.availability_zone
  tags = {
    Name = each.value.name
  }
}
resource "aws_subnet" "privates" {
  for_each          = local.private
  vpc_id            = aws_vpc.tag_gen_vpc.id
  cidr_block        = each.value.cidr_block
  availability_zone = each.value.availability_zone
  tags = {
    Name = each.value.name
  }
}


####### Internet Gateway and Nat Gateway #######

resource "aws_internet_gateway" "ig" {
  vpc_id = aws_vpc.tag_gen_vpc.id

  tags = {
    Name = "TagGen IG"
  }
}

resource "aws_eip" "elasticips" {
  for_each = local.public
  domain   = "vpc"
}

resource "aws_nat_gateway" "nats" { # nat gateway is created in public subnet, so its has "pub$" id
  for_each      = local.public
  allocation_id = aws_eip.elasticips[each.key].id
  subnet_id     = aws_subnet.publics[each.key].id

  tags = {
    Name = "NatGateway for Public Subnet ${each.value.idx}"
  }
}

####### Route table #######
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.tag_gen_vpc.id

  route {
    cidr_block = "10.0.0.0/20" # route all traffic from those IP add to local
    gateway_id = "local"
  }

  route {
    cidr_block = "0.0.0.0/0" # route all (other) traffic to internet gateway
    gateway_id = aws_internet_gateway.ig.id
  }

  tags = {
    Name = "Public Route"
  }
}

resource "aws_route_table" "privates" {
  for_each = zipmap(keys(local.private), keys(local.public)) # looks like  {"priv1": "pub1", "priv2": "pub2"}
  # these private routable are associated to nat get created with public key $pubs

  vpc_id = aws_vpc.tag_gen_vpc.id

  route {
    cidr_block = "10.0.0.0/20" # route all traffic from those IP add to local
    gateway_id = "local"
  }

  route {
    cidr_block = "0.0.0.0/0" # route all (other) traffic to nat gateway
    gateway_id = aws_nat_gateway.nats[each.value].id
  }

  tags = {
    Name = "Private Route Table ${each.key}"
  }
}

resource "aws_route_table_association" "publics" {
  for_each       = local.public
  subnet_id      = aws_subnet.publics[each.key].id
  route_table_id = aws_route_table.public.id
}

# Associate each private subnet with 
resource "aws_route_table_association" "privates" {
  for_each       = local.private
  subnet_id      = aws_subnet.privates[each.key].id
  route_table_id = aws_route_table.privates[each.key].id
}
