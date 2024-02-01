resource "aws_ecr_repository" "this" {
  name                 = "tag_generator/api"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}