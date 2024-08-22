# Create an load balancer:
resource "aws_lb" "lb" {
  name               = "load-balancer-${var.env_suffix}" #load balancer name
  load_balancer_type = "application"
  subnets            = [for subnet in aws_subnet.publics : subnet.id]
  internal           = false
  # security group
  security_groups = [aws_security_group.lb_security_group.id]
}

# Configure the load balancer with the VPC network
resource "aws_lb_target_group" "target_group" {
  name        = "UI-target-group-${var.env_suffix}"
  port        = var.ui.container_port # ALB forward traffic target group on port UI port
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = aws_vpc.tag_gen_vpc.id
}

resource "aws_lb_listener" "listener" { # ALB listen to traffic on port 80
  load_balancer_arn = aws_lb.lb.arn     #  load balancer
  port              = tostring(var.ui.container_port)
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target_group.arn # target group
  }
}

