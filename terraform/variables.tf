variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "project_name" {
  type    = string
  default = "task-manager"
}

variable "container_port" {
  type    = number
  default = 8000
}

variable "image_uri" {
  type = string
}