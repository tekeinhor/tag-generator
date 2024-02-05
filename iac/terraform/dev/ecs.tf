module "ecs" {
  source                    = "../modules/ecs"
  vpc_id                    = "vpc-072487b7c91bc9b10"
  cluster_name              = "taggenerator-cluster"
  cluster_service_name      = "taggenerator-api-service"
  cluster_service_task_name = "taggenerator-api-task"
  vpc_id_subnet_list        = ["subnet-0de4d1ef85bb6eb27", "subnet-0520e52980fe894b7", "subnet-0ee513191854aaaa5"]
  image_id                  = "637423196893.dkr.ecr.eu-west-3.amazonaws.com/tag_generator/api:593d00fd239f0a45e2a7c74a977c707ddddd4501"
  bucket_name               = "tek-tag-generator-dev"
  region                    = local.region
}
