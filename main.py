import urllib3
import boto3
import json
import logging
from datetime import time
client = boto3.client('kinesis')
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.describe_stream
#autenticando no kinesis
#auth = {"aws_access_key_id":"id", "aws_secret_access_key":"key"}
#connection = client.connect_to_region('us-east-1',**auth)
# obtenha as informações do fluxo (como quantos fragmentos, se estiver ativo ..)

resposta  =  client . create_stream ( 
    StreamName = 'kinesis_stream' , 
    ShardCount = 123 
)

tries = 0
while tries < 10:
    tries += 1
    time.sleep(1)
    try:
        response = client.describe_stream('stream_name')   
        if response['StreamDescription']['StreamStatus'] == 'ACTIVE':
            break 
    except :
        logging.error('error while trying to describe kinesis stream : %s')
else:
    raise TimeoutError('Stream is still not active, aborting...')
#obtenha todos os ids de shard e, para cada id compartilhado, obtenha o iterador de shard:


shard_ids = []
stream_name = None 
if response and 'StreamDescription' in response:
    stream_name = response['StreamDescription']['StreamName']                   
    for shard_id in response['StreamDescription']['Shards']:
         shard_id = shard_id['ShardId']
         shard_iterator = client.get_shard_iterator(stream_name, shard_id, shard_iterator_type)
         shard_ids.append({'shard_id' : shard_id ,'shard_iterator' : shard_iterator['ShardIterator'] })

#leia os dados para cada fragmento
tries = 0
result = []
while tries < 100:
     tries += 1
     response = client.get_records(shard_iterator = shard_iterator , limit = limit)
     shard_iterator = response['NextShardIterator']
     if len(response['Records'])> 0:
          for res in response['Records']: 
               result.append(res['Data'])                  
          return result , shard_iterator

client.put_record(stream_name, data, partition_key)

url = 'https://api.punkapi.com/v2/beers/random'
http = urllib3.PoolManager()
S3_BUCKET = "cleaned-000" 
cervejas = []

def lambda_handler(event, context):
    for i in range(100):
        r = http.request('GET',url)
        cerveja = json.loads(r.data.decode("utf8"))
        cervejas.append(cerveja)
