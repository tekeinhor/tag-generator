# Create a load balancer:
resource "aws_lb" "application_load_balancer" {
  name               = "load-balancer" #load balancer name
  load_balancer_type = "application"
  subnets            = var.vpc_id_subnet_list
  internal           = false
  # security group
  security_groups = [aws_security_group.load_balancer_security_group.id]
}

# Configure the load balancer with the VPC network
resource "aws_lb_target_group" "target_group" {
  name        = "target-group"
  port        = 8080
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = data.aws_vpc.default.id
}

resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_lb.application_load_balancer.arn #  load balancer
  port              = "8080"
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target_group.arn # target group
  }
}

# Create a security group for the load balancer:
resource "aws_security_group" "load_balancer_security_group" {
  name        = "lb_sg"
  description = "security group for the load_balancer"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    description = "Permit incoming HTTP requests from the internet"
    cidr_blocks = ["0.0.0.0/0"] # Allow traffic in from all sources
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    description = "Permit all outgoing requests to the internet"
    cidr_blocks = ["0.0.0.0/0"]
  }
}