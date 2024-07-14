provider "aws" {
  region = var.aws_region
}

resource "aws_kinesis_stream" "my_stream" {
  name             = "my_kinesis_stream"
  shard_count      = 1
  retention_period = 24
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda-kinesis-role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      }
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole"
}

resource "aws_lambda_function" "kinesis_lambda" {
  filename         = "lambda_function.zip"
  function_name    = "kinesis_lambda"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.lambda_handler"
  source_code_hash = filebase64sha256("lambda_function.zip")
  runtime          = "python3.8"

  environment {
    variables = {
      BUCKET_NAME = var.bucket_name
    }
  }
}

resource "aws_lambda_event_source_mapping" "kinesis_event" {
  event_source_arn = aws_kinesis_stream.my_stream.arn
  function_name    = aws_lambda_function.kinesis_lambda.arn
  starting_position = "LATEST"
}

resource "aws_s3_bucket" "model_bucket" {
  bucket = var.bucket_name
}

//resource "aws_s3_bucket_acl" "model_bucket_acl" {
//  bucket = aws_s3_bucket.model_bucket.id
//  acl    = "private"
//}

resource "aws_s3_object" "model" {
  bucket = aws_s3_bucket.model_bucket.bucket
  key    = "fashion_mnist_model_final.h5"
  source = "/Users/oelghareeb/Fashion_MNIST_MLOps/data/fashion_mnist_model_final.h5"
}
