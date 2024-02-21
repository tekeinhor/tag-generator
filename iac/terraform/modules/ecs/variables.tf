variable "vpc_id" {
  description = "Id of the existing VPC."
  type        = string
}

variable "cluster_name" {
  description = "Id of the existing VPC."
  type        = string
}


variable "ui" {
  description = "An object with info related to the front facing service (ui)."
  type = object({
    service_name   = string
    task_name      = string
    image_id       = string
    container_name = string
    port_name      = string
    container_port = number
  })
}

variable "api" {
  description = "An object with info related to the backend service (api)."
  type = object({
    service_name   = string
    task_name      = string
    image_id       = string
    container_name = string
    port_name      = string
    container_port = number
    dns_name       = string
  })
}


variable "vpc_id_subnet_list" {
  description = "Subnets of the existing VPC."
  type        = list(string)
}

variable "bucket_name" {
  description = "Name of bucket that should be accesed by the docker in the ECS task."
  type        = string
}

variable "region" {
  description = "Region of AWS account."
  type        = string
}

variable "log_group" {
  description = "Log group of the ECS logs."
  type        = string
}


variable "env_suffix" {
  description = "Env suffix for ressources"
  type        = string
}


