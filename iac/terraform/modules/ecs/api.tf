# Here we will create for the API
# - an ECS service
# - an ECS task with task_definition
# - the role that the runnning docker will assume (ex: access to s3)

resource "aws_ecs_service" "api" {
  name            = var.api.service_name
  cluster         = aws_ecs_cluster.ecs_cluster.id
  task_definition = aws_ecs_task_definition.api_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [var.vpc_id_subnet_list[0], var.vpc_id_subnet_list[1], var.vpc_id_subnet_list[2]]
    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }
  service_connect_configuration { # configure client-server service to be reachable using service connect
    enabled   = true
    namespace = aws_service_discovery_private_dns_namespace.this.arn
    service {
      client_alias {
        dns_name = var.api.dns_name # the dns to discover the api: http://dev-api:8080
        port     = var.api.container_port
      }
      discovery_name = "dev-api-service"
      port_name      = var.api.port_name
    }
  }

}

resource "aws_ecs_task_definition" "api_task" {
  family                   = var.api.task_name
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.this.arn
  task_role_arn            = aws_iam_role.api_task.arn
  container_definitions = jsonencode([
    {
      name   = var.api.container_name #"taggenerator-api-container"
      image  = var.api.image_id
      cpu    = 256
      memory = 512
      portMappings = [
        {
          name          = var.api.port_name
          containerPort = var.api.container_port
          hostPort      = var.api.container_port
          protocol      = "tcp"
          appProtocol   = "http"
        }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = var.log_group
          awslogs-region        = var.region
          awslogs-stream-prefix = "taggenerator-api-${var.env_suffix}"
        }
      }
    }
  ])

}


# create role and custom inline policy and attached it to the task role
# (for permissions that the docker run by ECS needs)

resource "aws_iam_role" "api_task" {
  name               = "TaggeneratorApiECSTaskRole"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}
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
  name   = "ECSTaskS3RoleInlinePolicy"
  policy = data.aws_iam_policy_document.inline_policy_doc.json
}

resource "aws_iam_role_policy_attachment" "that" {
  role       = aws_iam_role.api_task.name
  policy_arn = aws_iam_policy.inline_policy.arn
}