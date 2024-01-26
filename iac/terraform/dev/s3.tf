provider "aws" {
  region = local.region

  default_tags {
    tags = local.tags
  }
}


module "s3_bucket_dev" {
  source = "../modules/s3"

  bucket_name = "tek-tag-generator-dev"
}
