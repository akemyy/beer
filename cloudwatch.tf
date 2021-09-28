resource "aws_cloudwatch_event_rule" "console" {
  name        = "CloudWatch-to-lambda"
  description = "Um CloudWatch Event que dispara a cada 5 minutos uma função Lambda para alimentar o Kinesis Stream"
  schedule_expression = "cron(0/3 * ? * FRI *)"
  depends_on = [
    "aws_lambda_function.lambda-to-s3"
  ]
  event_pattern = <<EOF
{
  "detail-type": [
    "AWS Console Sign In via CloudTrail"
  ]
}
EOF
}


resource "aws_cloudwatch_event_target" "yada" {
  rule      = aws_cloudwatch_event_rule.console.name
  target_id = "console"
  arn       = aws_lambda_function.lambda-to-s3.arn
}

data "aws_iam_policy_document" "topic_policy" {
  statement {
    effect  = "Allow"
    actions = ["SNS:Publish"]

    principals {
      type        = "Service"
      identifiers = ["events.amazonaws.com"]
    }

    resources = [aws_cloudwatch_event_rule.console.arn]
  }
} 