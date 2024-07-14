output "kinesis_stream_arn" {
  value = aws_kinesis_stream.my_stream.arn
}

output "lambda_function_arn" {
  value = aws_lambda_function.kinesis_lambda.arn
}

output "s3_bucket_name" {
  value = aws_s3_bucket.model_bucket.bucket
}
