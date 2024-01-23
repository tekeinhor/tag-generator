variable "bucket_name" {
  description = "Name of the s3 bucket. Must be unique."
  type        = string
}

variable "tags" {
  description = "Tags to set on the bucket."
  type        = map(string)
  default     = {}
}

variable "region" {
  description = "Region of your bucket."
  type        = string
}

variable "session_name" {
  description = "Provider assume role session name."
  type        = string
}
