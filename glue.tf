resource "aws_glue_catalog_database" "databasecleaned" {
  name = "databasecleaned"
}

resource "aws_glue_catalog_table" "cerveja" {
  name          = "cerveja"
  database_name = "databasecleaned"
  depends_on = [aws_glue_catalog_database.databasecleaned]
}
resource "aws_glue_classifier" "example" {
  name = "example"

  csv_classifier {
    allow_single_column    = false
    contains_header        = "PRESENT"
    delimiter              = ","
    disable_value_trimming = false
    header                 = ["example1", "example2"]
    quote_symbol           = "'"
  }
}

#rds


