
data "archive_file" "lambda_kinesis" {
  type        = "zip"
  source_file = "${path.module}/script-lambda-kinesis.py"
  output_path = "${path.module}/script-lambda-kinesis.py.zip"
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda-to-kinesis.function_name
  principal     = "events.amazonaws.com"
  source_arn    = "arn:aws:events:eu-west-1:111122223333:rule/RunDaily"
  qualifier     = aws_lambda_alias.lambda_kinesis_alias.name

}

resource "aws_lambda_alias" "lambda_kinesis_alias" {
  name             = "lambdakinesisalias"
  description      = "Função Lambda para alimentar o Kinesis Stream"
  function_name    = aws_lambda_function.lambda-to-kinesis.function_name
  function_version = "$LATEST"
}

resource "aws_lambda_function" "lambda-to-kinesis" {
  filename      = data.archive_file.lambda_kinesis.output_path
  function_name = "lambda-to-kinesis"
  role          = aws_iam_role.iam_for_lambda_kinesis.arn
  handler       = "main.lambda_handler"
  runtime       = "python3.7"
  timeout       = 120
}

resource "aws_iam_role" "iam_for_lambda_kinesis" {
  name = "iam_for_lambda_kinesis"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

}

resource "aws_lambda_event_source_mapping" "example" {
  event_source_arn  = aws_kinesis_stream.kinesis_stream.arn
  function_name     = aws_lambda_function.lambda-to-kinesis.arn
  starting_position = "LATEST"

  depends_on = [
    aws_iam_role_policy_attachment.kinesis_processing
  ]
}