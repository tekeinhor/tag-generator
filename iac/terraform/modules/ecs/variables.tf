variable "subnets" {
  description = "Subnets creation info"
  type = map(object({
    cidr_block        = string
    availability_zone = string
    name              = string
    type              = string
    idx               = number
  }))

  default = {
    key1 = {
      cidr_block        = "10.0.0.0/24"
      availability_zone = "eu-west-3a"
      name              = "Public Subnet 1"
      type              = "public"
      idx               = 1

    }
    key2 = {
      cidr_block        = "10.0.1.0/24"
      availability_zone = "eu-west-3b"
      name              = "Public Subnet 2"
      type              = "public"
      idx               = 2
    }
    key3 = {
      cidr_block        = "10.0.2.0/23"
      availability_zone = "eu-west-3a"
      name              = "Private Subnet 1"
      idx               = 1
    }
    key4 = {
      cidr_block        = "10.0.4.0/23"
      availability_zone = "eu-west-3b"
      name              = "Private Subnet 2"
      idx               = 2
    }
  }
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


