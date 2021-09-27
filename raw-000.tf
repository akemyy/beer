/* resource "aws_kinesis_firehose_delivery_stream" "extended_s3_raw" {
  name        = "terraform-kinesis-firehose-extended-s3-raw-000"
  destination = "extended_s3"


  extended_s3_configuration {
    role_arn   = aws_iam_role.firehose_role.arn
    bucket_arn = aws_s3_bucket.raw-000.arn
  }
} */
resource "aws_s3_bucket" "raw-000" {
  bucket = "raw-000"
  acl    = "private"
}

/* resource "aws_kinesis_stream_consumer" "extended_s3_raw" {
  name       = "terraform-kinesis-firehose-extended-s3-raw-000"
  stream_arn = aws_kinesis_stream.kinesis_stream.arn
} */