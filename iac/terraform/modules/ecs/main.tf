data "aws_vpc" "default" {
  id = var.vpc_id
}


resource "aws_security_group" "ecs_sg" {
  vpc_id = data.aws_vpc.default.id
  name   = "ecs-security-group"
  # Inbound and outbound rules
  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    #allowing the traffic from load balancer security group
    security_groups = [aws_security_group.load_balancer_security_group.id]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}


resource "aws_ecs_task_definition" "task_definition" {
  family                   = var.cluster_service_task_name
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.this.arn
  container_definitions = jsonencode([
    {
      name   = "tag-generator-api-container"
      image  = var.image_id
      cpu    = 256
      memory = 512
      portMappings = [
        {
          containerPort = 8080
          hostPort      = 8080
          protocol      = "tcp"
        }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-create-group  = "true"
          awslogs-group         = "awslogs-tagggenerator"
          awslogs-region        = var.region
          awslogs-stream-prefix = "awslogs-example"
        }
      }
    }
  ])

}


resource "aws_ecs_cluster" "ecs_cluster" {
  name = var.cluster_name
}

resource "aws_ecs_service" "service" {
  name            = var.cluster_service_name
  cluster         = aws_ecs_cluster.ecs_cluster.id
  task_definition = aws_ecs_task_definition.task_definition.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [var.vpc_id_subnet_list[0], var.vpc_id_subnet_list[1], var.vpc_id_subnet_list[2]]
    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }
}


# create the role that the ECS service should use to run the container
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

resource "aws_iam_role_policy_attachment" "that" {
  role       = aws_iam_role.this.name
  policy_arn = data.aws_iam_policy.ecs_managed_role_policy.arn
}

# create custom inline policy and attached it to our role
data "aws_iam_policy_document" "inline_policy_doc" {

  statement {
    effect    = "Allow"
    actions   = ["ssm:GetParameters", "kms:Decrypt"]
    resources = ["*"]
  }
  statement {
    effect  = "Allow"
    actions = ["s3:GetObject", "s3:ListBucket"]
    resources = [
      "arn:aws:s3:::${var.bucket_name}/*",
      "arn:aws:s3:::${var.bucket_name}"
    ]
  }
}

resource "aws_iam_policy" "inline_policy" {
  name   = "ECSTaskExecutionInlinePolicy"
  policy = data.aws_iam_policy_document.inline_policy_doc.json
}

resource "aws_iam_role_policy_attachment" "this" {
  role       = aws_iam_role.this.name
  policy_arn = aws_iam_policy.inline_policy.arn
}
