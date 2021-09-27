# beer

arquitetura que consome a Punk Api no
endpoint https://api.punkapi.com/v2/beers/random e ingere em um Kinesis Stream que teM 2 consumidores.
1. Um CloudWatch Event que dispara a cada 5 minutos uma função Lambda para alimentar o Kinesis Stream que terá como saída:
● Um Firehose agregando todas as entradas para guardar em um bucket S3 com o nome de raw.
● Outro Firehose com um Data Transformation que pega somente os id,name, abv, ibu, target_fg, target_og, ebc, srm e ph das cervejas e guarda
em um outro bucket S3 com o nome de cleaned em formato csv.
2. Tabela com os dados do bucket cleaned.
3. um modelo de machine learning que classifique as cervejas em seus respectivos ibus.



Dependências 
- Terraform 
- Conta amazon
Como executar

terraform init
terraform plan
terraform apply

Proximos passos:
- melhorar a organização das pastas
- abstrair partes que estão chubadas no codigo para o arquivo variables.tf 
- Retirar permissões excessivas 
- Dar permissão para o lambda no cloudwacth
- Integrar Kinesis Stream, Firehose e glue
- Melhorar o modelo 
    - Clusterizar as cervejas e tentar desenvolver uma forma de ter mais similaridade entre os atributos para cada Clusterizar
- Retirar duplicidade de linhas que o lambda grava nas chamadas para a api
