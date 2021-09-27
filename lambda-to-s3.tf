data "archive_file" "lambda" {
  type        = "zip"
  source_file = "${path.module}/scrip-lambda-to-s3.py"
  output_path = "${path.module}/scrip-lambda-to-s3.py.zip"
}
/* resource "aws_lambda_permission" "allow_cloudwatch_test" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda-to-s3.function_name
  principal     = "events.amazonaws.com"
  qualifier     = aws_lambda_alias.lambda_s3_alias.name

} */
resource "aws_lambda_alias" "lambda_s3_alias" {
  name             = "lambdakinesisalias"
  description      = "a sample description"
  function_name    = aws_lambda_function.lambda-to-s3.function_name
  function_version = "$LATEST"
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_lambda_function" "lambda-to-s3" {
  function_name = "lambda-to-s3"
  description   = "TODO"
  filename      = data.archive_file.lambda.output_path
  runtime       = "python3.7"
  handler       = "scrip-lambda-to-s3.lambda_handler"
  role          = aws_iam_role.iam_for_lambda.arn
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.cleaned-000.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.lambda-to-s3.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "AWSLogs/"
    filter_suffix       = ".log"
  }

  #depends_on = [aws_lambda_permission.allow_cloudwatch_test]
}

resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda-to-s3.arn
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.cleaned-000.arn
}



resource "aws_s3_bucket_policy" "b" {
  bucket = aws_s3_bucket.cleaned-000.id

  # Terraform's "jsonencode" function converts a
  # Terraform expression's result to valid JSON syntax.
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "PublicReadGetObject",
        "Effect" : "Allow",
        "Principal" : "*",
        "Action" : [
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:GetObject",
          "s3:GetObjectAcl",
          "s3:DeleteObject"
        ],
        "Resource" : "arn:aws:s3:::cleaned-000/*"
      }
    ]
  })
}

/* FailedInvocations */