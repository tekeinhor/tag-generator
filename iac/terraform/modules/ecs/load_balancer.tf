# Create an load balancer:
resource "aws_lb" "lb" {
  name               = "load-balancer-${var.env_suffix}" #load balancer name
  load_balancer_type = "application"
  subnets            = var.vpc_id_subnet_list
  internal           = false
  # security group
  security_groups = [aws_security_group.lb_security_group.id]
}

# Configure the load balancer with the VPC network
resource "aws_lb_target_group" "target_group" {
  name        = "target-group-${var.env_suffix}"
  port        = var.ui.container_port
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = data.aws_vpc.default.id
}

resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_lb.lb.arn #  load balancer
  port              = tostring(var.ui.container_port)
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target_group.arn # target group
  }
}

