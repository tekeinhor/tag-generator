# This has been commented in order to destroy all the resource related to the API and UI deployment
# and hence, stop any related cost.


locals {
  # read api and ui version and image name from file and use them
  apps = yamldecode(file("${path.module}/apps.yaml"))

  api = local.apps.api
  ui  = local.apps.ui

  api_image_id = "637423196893.dkr.ecr.eu-west-3.amazonaws.com/${local.api.image}:${local.api.tag}"
  ui_image_id  = "637423196893.dkr.ecr.eu-west-3.amazonaws.com/${local.ui.image}:${local.ui.tag}"
}

module "ecs" {
  source       = "../modules/ecs"
  cluster_name = "taggenerator-cluster-dev"
  ui = {
    service_name   = "taggenerator-ui-service-dev"
    task_name      = "taggenerator-ui-task-dev"
    image_id       = local.ui_image_id
    container_name = "taggenerator-ui-container"
    container_port = 8501
    port_name      = "taggenerator-ui-dev"
  }
  api = {
    service_name   = "taggenerator-api-service-dev"
    task_name      = "taggenerator-api-task-dev"
    image_id       = local.api_image_id
    container_name = "taggenerator-api-container"
    container_port = 8080
    port_name      = "taggenerator-api-dev"
    dns_name       = "dev-api"
  }
  subnets = {
    pub1 = {
      cidr_block        = "10.0.0.0/24"
      availability_zone = "eu-west-3a"
      name              = "Public Subnet 1"
      type              = "public"
      idx               = 1

    }
    pub2 = {
      cidr_block        = "10.0.1.0/24"
      availability_zone = "eu-west-3b"
      name              = "Public Subnet 2"
      type              = "public"
      idx               = 2
    }
    priv1 = {
      cidr_block        = "10.0.2.0/23"
      availability_zone = "eu-west-3a"
      name              = "Private Subnet 1"
      type              = "private"
      idx               = 1
    }
    priv2 = {
      cidr_block        = "10.0.4.0/23"
      availability_zone = "eu-west-3b"
      name              = "Private Subnet 2"
      type              = "private"
      idx               = 2
    }
  }

  bucket_name = "tek-tag-generator-dev"
  region      = local.region
  log_group   = "awslogs-tagggenerator"
  env_suffix  = "dev"
}
