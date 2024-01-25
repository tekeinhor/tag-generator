variable "bucket_name" {
  description = "Name of the s3 bucket. Must be unique."
  type        = string
}


variable "session_name" {
  description = "Provider assume role session name."
  type        = string
}
