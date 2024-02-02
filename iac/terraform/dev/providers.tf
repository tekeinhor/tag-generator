provider "aws" {
  region = local.region

  default_tags {
    tags = local.tags
  }
}

