# --------------------
# S3 Bucket Resources.
# --------------------

# Description: create aws_s3_bucket, aws_s3_bucket_ownership_control and aws_s3_bucket_public_access_block resources.

resource "aws_s3_bucket" "example" {
  bucket        = var.bucket_name
  force_destroy = false
}

resource "aws_s3_bucket_ownership_controls" "example" {
  bucket = aws_s3_bucket.example.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "example" {
  depends_on = [aws_s3_bucket_ownership_controls.example]

  bucket = aws_s3_bucket.example.id
  acl    = "private"
}
resource "aws_s3_bucket_public_access_block" "example" {
  bucket                  = var.bucket_name
  block_public_acls       = true
  block_public_policy     = true
  restrict_public_buckets = true
  ignore_public_acls      = true
}

