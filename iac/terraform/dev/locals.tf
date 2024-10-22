locals {

  region          = "eu-west-3"
  owner           = "Tatia"
  environment     = "dev"
  managed_by      = "terraform"
  resource_origin = "https://github.com/tekeinhor/tag-generator"

  tags = {
    "owner"           = local.owner,
    "env"             = local.environment,
    "region"          = local.region,
    "managed_by"      = local.managed_by
    "resource_origin" = local.resource_origin
  }
}
