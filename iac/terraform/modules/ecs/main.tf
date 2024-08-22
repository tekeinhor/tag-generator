resource "aws_ecs_cluster" "ecs_cluster" {
  name = var.cluster_name
}

resource "aws_service_discovery_private_dns_namespace" "this" {
  name = "taggenerator.${var.env_suffix}"
  vpc  = aws_vpc.tag_gen_vpc.id
}


# create the role that the ECS service permissions (read ECR etc...)
resource "aws_iam_role" "this" {
  name               = "ECSTaskExecutionRole"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

# use managed policy and attached to our role
data "aws_iam_policy" "ecs_managed_role_policy" {
  arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy_attachment" "this" {
  role       = aws_iam_role.this.name
  policy_arn = data.aws_iam_policy.ecs_managed_role_policy.arn
}
