terraform {

  required_version = ">=1.7.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.33.0"
    }
  }

  backend "s3" {
    encrypt        = true
    bucket         = "tek-tf-state-storage"
    region         = "eu-west-3"
    key            = "tag-generator-stack-tf/dev/terraform.tfstate"
    dynamodb_table = "tek-tf-state-storage-lock"
  }
}
