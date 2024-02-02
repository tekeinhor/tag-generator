variable "vpc_id" {
  description = "Id of the existing VPC."
  type        = string
}

variable "cluster_name" {
  description = "Id of the existing VPC."
  type        = string
}

variable "cluster_service_name" {
  description = "ECS service name."
  type        = string
}

variable "cluster_service_task_name" {
  description = "ECS task name."
  type        = string
}

variable "image_id" {
  description = "Id of the container image."
  type        = string
}

variable "vpc_id_subnet_list" {
  description = "Subnets of the existing VPC."
  type        = list(string)
}

variable "bucket_name" {
  description = "Name of bucket that should be accesed by the docker in the ECS task."
  type        = string
}

