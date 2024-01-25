locals {
  region          = "eu-west-3"
  owner           = "Tatia"
  account_id      = "637423196893"
  environment     = terraform.workspace
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