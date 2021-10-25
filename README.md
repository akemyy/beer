# Beer

###### Descrição
arquitetura que consome a Punk Api no endpoint https://api.punkapi.com/v2/beers/random e ingere em um Kinesis Stream que tem 2 consumidores.
- Um CloudWatch Event que dispara a cada 5 minutos uma função Lambda para alimentar o Kinesis Stream que terá como saída:
- Um Firehose agregando todas as entradas para guardar em um bucket S3 com o nome de raw.
- Outro Firehose com um Data Transformation que pega somente os id,name, abv, ibu, target_fg, target_og, ebc, srm e ph das cervejas e guarda
em um outro bucket S3 com o nome de cleaned em formato csv.
- Tabela com os dados do bucket cleaned.
- Modelo de machine learning que classifique as cervejas em seus respectivos ibus.
![Desenho da arquitetura](Arquitetura.png?raw=true "Desenho da arquitetura")
###### Dependências 
- Terraform 
- Conta amazon
Como executar

```
terraform init
terraform plan
terraform apply
```

###### Próximos passos:
- Melhorar a organização das pastas
- Abstrair partes que estão chubadas no codigo para o arquivo variables.tf 
- Retirar permissões excessivas
- Integrar Kinesis Stream, Firehose e glue
- Melhorar o modelo 
    - Clusterizar as cervejas e tentar desenvolver uma forma de ter mais similaridade entre os atributos para cada Clusterizar
- Retirar duplicidade de linhas que o lambda grava nas chamadas para a api

Obs: O cloudwatch está chamando o lambda-to-s3 pois a integração do kinesis não foi finalizada então essa foi a forma de conseguir o csv para fazer o modelo.