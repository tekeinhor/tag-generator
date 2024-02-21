data "aws_vpc" "default" {
  id = var.vpc_id
}

resource "aws_security_group" "ecs_sg" {
  vpc_id = data.aws_vpc.default.id
  name   = "ecs-sg"
  # Inbound and outbound rules
  ingress {
    description = "rule for inbound UI call"
    from_port   = var.ui.container_port
    to_port     = var.ui.container_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    #allowing the traffic from load balancer security group
    security_groups = [aws_security_group.lb_security_group.id]
  }
  ingress {
    description = "rule for inbound API call"
    from_port   = var.api.container_port
    to_port     = var.api.container_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    #allowing the traffic from load balancer security group
    security_groups = [aws_security_group.lb_security_group.id]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}

# Create a security group for the load balancer:
resource "aws_security_group" "lb_security_group" {
  name        = "lb-sg-${var.env_suffix}"
  description = "security group for the load_balancer"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = var.ui.container_port
    to_port     = var.ui.container_port
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