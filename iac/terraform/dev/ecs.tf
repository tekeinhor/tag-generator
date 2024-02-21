locals {
  api_image     = "637423196893.dkr.ecr.eu-west-3.amazonaws.com/taggenerator/api"
  api_image_tag = "0.1.2"

  ui_image     = "637423196893.dkr.ecr.eu-west-3.amazonaws.com/taggenerator/ui"
  ui_image_tag = "0.1.2"
}

module "ecs" {
  source       = "../modules/ecs"
  vpc_id       = "vpc-072487b7c91bc9b10"
  cluster_name = "taggenerator-cluster-dev"

  ui = {
    service_name   = "taggenerator-ui-service-dev"
    task_name      = "taggenerator-ui-task-dev"
    image_id       = "${local.ui_image}:${local.ui_image_tag}"
    container_name = "taggenerator-ui-container"
    container_port = 8501
    port_name      = "taggenerator-ui-dev"
  }
  api = {
    service_name   = "taggenerator-api-service-dev"
    task_name      = "taggenerator-api-task-dev"
    image_id       = "${local.api_image}:${local.api_image_tag}"
    container_name = "taggenerator-api-container"
    container_port = 8080
    port_name      = "taggenerator-api-dev"
    dns_name       = "dev-api"
  }

  vpc_id_subnet_list = ["subnet-0de4d1ef85bb6eb27", "subnet-0520e52980fe894b7", "subnet-0ee513191854aaaa5"]
  bucket_name        = "tek-tag-generator-dev"
  region             = local.region
  log_group          = "awslogs-tagggenerator"
  env_suffix         = "dev"
}
