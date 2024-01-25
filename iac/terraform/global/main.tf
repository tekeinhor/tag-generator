data "aws_ssoadmin_instances" "this" {}

locals {
  projects = yamldecode(file("${path.module}/teams.yaml"))["teams"]

  all_members = flatten([
    for project in local.projects : project.members
  ])

  m = {
    for index, member in local.all_members :
    member.email => member.name
  }

  admin = {
    for name, project in local.projects :
    name => "${project.admin? "a" : "b"}"
    # name => "${project.admin? aws_ssoadmin_permission_set.admin : (aws_ssoadmin_permission_set.read_only)}"
  }

  ops_members = coalesce(local.projects.Ops.members, [])
  # x = toset([for member in local.ops_members: member.email])
}



## Create Users and Groups
resource "aws_identitystore_user" "this" {
  for_each = {
    for index, member in local.all_members :
    member.email => member.name
  }
  identity_store_id = tolist(data.aws_ssoadmin_instances.this.identity_store_ids)[0]

  display_name = each.value
  user_name    = each.key

  name {
    given_name  = split(" ", each.value)[0]
    family_name = split(" ", each.value)[1]
  }

  emails {
    value = each.key
  }
}

resource "aws_identitystore_group" "group" {
  for_each          = local.projects
  display_name      = each.key
  description       = "Group for ${each.key}"
  identity_store_id = tolist(data.aws_ssoadmin_instances.example.identity_store_ids)[0]
}

# Create permissions and policy to attach to permissions

resource "aws_ssoadmin_permission_set" "read_only" {
  name             = "ReadOnlyAccess"
  instance_arn     = tolist(data.aws_ssoadmin_instances.this.arns)[0]
  session_duration = "PT1H"
}
resource "aws_ssoadmin_managed_policy_attachment" "read_only" {
  instance_arn       = tolist(data.aws_ssoadmin_instances.this.arns)[0]
  managed_policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
  permission_set_arn = aws_ssoadmin_permission_set.read_only.arn
}



resource "aws_ssoadmin_permission_set" "admin" {
  name             = "AdministratorAccess"
  instance_arn     = tolist(data.aws_ssoadmin_instances.this.arns)[0]
  session_duration = "PT1H"
}


resource "aws_ssoadmin_managed_policy_attachment" "admin" {
  instance_arn       = tolist(data.aws_ssoadmin_instances.this.arns)[0]
  managed_policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
  permission_set_arn = aws_ssoadmin_permission_set.admin.arn
}



resource "aws_ssoadmin_account_assignment" "assignment" {
  for_each = {
    for name, project in local.projects :
    name => "${project.admin? aws_ssoadmin_permission_set.admin : aws_ssoadmin_permission_set.read_only}"
  }
  instance_arn       = each.value.instance_arn
  permission_set_arn = each.value.arn

  principal_id   = aws_identitystore_group.group[each.key].group_id
  principal_type = "GROUP"

  target_id   = local.account_id
  target_type = "AWS_ACCOUNT"
}
