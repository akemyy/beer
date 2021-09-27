/* resource "aws_kinesis_stream" "kinesis_stream" {
  name             = "terraform-kinesis-000"
  shard_count      = 1
  retention_period = 48

  shard_level_metrics = [
    "IncomingBytes",
    "OutgoingBytes",
  ]

} */