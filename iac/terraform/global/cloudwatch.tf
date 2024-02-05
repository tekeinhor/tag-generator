resource "aws_cloudwatch_log_group" "yada" {
  name = "awslogs-tagggenerator"

  tags = local.tags
}