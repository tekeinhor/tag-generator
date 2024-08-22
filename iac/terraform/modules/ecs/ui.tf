# Here we will create for the UI
# - an ECS service
# - an ECS task with task_definition

resource "aws_ecs_service" "ui" {
  name            = var.ui.service_name
  cluster         = aws_ecs_cluster.ecs_cluster.id
  task_definition = aws_ecs_task_definition.ui_task.arn
  desired_count   = 2
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [for subnet in aws_subnet.privates : subnet.id]
    security_groups  = [aws_security_group.ecs_ui_sg.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.target_group.arn
    container_name   = var.ui.container_name
    container_port   = var.ui.container_port
  }

  service_connect_configuration { # configure client service to discover stuff using service connect
    enabled   = true
    namespace = aws_service_discovery_private_dns_namespace.this.arn
  }
}

resource "aws_ecs_task_definition" "ui_task" {
  family                   = var.ui.task_name
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.this.arn
  #   task_role_arn            = the UI doesn't need any specific role
  container_definitions = jsonencode([
    {
      name   = var.ui.container_name # "taggenerator-ui-container"
      image  = var.ui.image_id
      cpu    = 256
      memory = 512
      environment = [
        {
          name  = "API_ENDPOINT_URL"
          value = "http://${var.api.dns_name}:${var.api.container_port}/api/v1/predict" #  should look like this http://dev-api:8080/api/v1/predict
        },
        {
          name  = "STREAMLIT_SERVER_PORT"
          value = tostring(var.ui.container_port)
        }
      ]
      portMappings = [
        {
          name          = var.ui.port_name
          containerPort = var.ui.container_port
          # hostPort      = var.ui.container_port
          protocol = "tcp"
        }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = var.log_group
          awslogs-region        = var.region
          awslogs-stream-prefix = "taggenerator-ui-${var.env_suffix}"
        }
      }
    }
  ])

}

