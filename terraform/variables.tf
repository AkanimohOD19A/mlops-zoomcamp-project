variable "aws_region" {
  description = "The AWS region to deploy to"
  default     = "us-west-2"
}

variable "bucket_name" {
  description = "mlops-bucket"
  default     = "mlops-zoomcamp-project-bucket"  # Replace with a unique bucket name
}

variable "project_name" {
  type        = string
  description = "Project name"
}

variable "vpc_id" {
  type        = string
  description = "AWS VPC id"
}
