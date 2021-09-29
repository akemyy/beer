import urllib3
import boto3
import json
import logging
import time
client = boto3.client('kinesis')

url = 'https://api.punkapi.com/v2/beers/random'
http = urllib3.PoolManager()
S3_BUCKET = "cleaned-000" 
cervejas = []
kinesis_name = 'terraform-kinesis-000'

def lambda_handler(event, context):
    for i in range(3):
        r = http.request('GET',url)
        cerveja = json.loads(r.data.decode("utf8"))
        cervejas.append(cerveja)

    decricao = client.describe_stream(
        StreamName=kinesis_name,
        Limit=123,
        ExclusiveStartShardId=kinesis_name)
    print(decricao)
    
    resposta  =  client.put_record ( 
    StreamName = kinesis_name , 
    Data = json.dumps(cervejas) , 
    PartitionKey = 'lista_cerveja_json'
)