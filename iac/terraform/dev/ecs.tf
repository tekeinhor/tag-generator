module "ecs" {
  source                    = "../modules/ecs"
  vpc_id                    = "vpc-072487b7c91bc9b10"
  cluster_name              = "taggenerator-cluster-dev"
  cluster_service_name      = "taggenerator-api-service-dev"
  cluster_service_task_name = "taggenerator-api-task-dev"
  vpc_id_subnet_list        = ["subnet-0de4d1ef85bb6eb27", "subnet-0520e52980fe894b7", "subnet-0ee513191854aaaa5"]
  image_id                  = "637423196893.dkr.ecr.eu-west-3.amazonaws.com/tag_generator/api:0.1.2"
  bucket_name               = "tek-tag-generator-dev"
  region                    = local.region
  log_group                 = "awslogs-tagggenerator"
  env_suffix                = "dev"
}
