/* resource "aws_kinesis_firehose_delivery_stream" "extended_s3_cleaned" {
  name        = "terraform-kinesis-firehose-extended-s3-cleaned-000"
  destination = "extended_s3"

  extended_s3_configuration {
    role_arn   = aws_iam_role.firehose_role.arn
    bucket_arn = aws_s3_bucket.cleaned-000.arn

    processing_configuration {
      enabled = "true"

      processors {
        type = "Lambda"

        parameters {
          parameter_name  = "LambdaArn"
          parameter_value = "${aws_lambda_function.lambda-to-s3.arn}:$LATEST"
        }
      }
    }
  }
} */

resource "aws_s3_bucket" "cleaned-000" {
  bucket = "cleaned-000"
  acl    = "private"
}

/* resource "aws_kinesis_stream_consumer" "extended_s3_cleaned" {
  name       = "terraform-kinesis-firehose-extended-s3-cleaned-000"
  stream_arn = aws_kinesis_stream.kinesis_stream.arn
} */

/* START RequestId: cb554fd1-0bf9-406a-a4be-60828a6cf1fa Version: $LATEST
[ERROR] S3UploadFailedError: Failed to upload /tmp/9 to cleaned-000/2021-09-21/14/33/9: An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
Traceback (most recent call last):
  File "/var/task/scrip-lambda-to-s3.py", line 120, in lambda_handler
    s3_client.upload_file(LOCAL_FILE_SYS + "/" + f, S3_BUCKET, key + f)
  File "/var/runtime/boto3/s3/inject.py", line 129, in upload_file
    return transfer.upload_file(
  File "/var/runtime/boto3/s3/transfer.py", line 285, in upload_file
    raise S3UploadFailedError(END RequestId: cb554fd1-0bf9-406a-a4be-60828a6cf1fa
REPORT RequestId: cb554fd1-0bf9-406a-a4be-60828a6cf1fa	Duration: 670.83 ms	Billed Duration: 671 ms	Memory Size: 128 MB	Max Memory Used: 69 MB	Init Duration: 372.17 ms */