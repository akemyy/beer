provider "aws" {
  region = "us-east-1"
}

#module "raw-000" {
#  source  = "terraform-aws-modules/s3-bucket/aws"
#  version = "2.9.0"
#  bucket = "raw-000"
#  acl    = "private"
# insert the 5 required variables here
#}

/* module "cleaned-000" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "2.9.0"
  bucket = "cleaned-000"
  acl    = "private"
  # insert the 5 required variables here
}
 */

resource "aws_iam_role" "firehose_role" {
  name = "firehose_test_role"

  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Action" : "sts:AssumeRole",
        "Principal" : {
          "Service" : "firehose.amazonaws.com"
        },
        "Effect" : "Allow",
        "Sid" : ""
      }
    ]
  })
}
resource "aws_iam_role_policy" "firehose_role" {
  role = aws_iam_role.firehose_role.name

  policy = jsonencode({
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : ["s3:*"],
        "Resource" : [aws_s3_bucket.raw-000.arn]
      },

      {
        "Effect" : "Allow",
        "Action" : [
          "logs:PutLogEvents"
        ],
        "Resource" : [
          "arn:aws:logs:*:*:log-group:*:log-stream:*"
        ]
      },
    ],
  })
}