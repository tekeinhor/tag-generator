module "s3_bucket_dev" {
  source = "../modules/s3"

  bucket_name = "tek-tag-generator-dev"
}
