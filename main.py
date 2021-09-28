import urllib3
import boto3
import json
import logging
import time
client = boto3.client('kinesis')
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.describe_stream

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

""" import csv
import urllib3
import boto3
import json
from datetime import datetime, timezone
import io


url = 'https://api.punkapi.com/v2/beers/random'
http = urllib3.PoolManager()
S3_BUCKET = "cleaned-000" 
s3_client = boto3.client("s3")
cervejas = []

def lambda_handler(event, context):
    for i in range(100):
        r = http.request('GET',url)
        cerveja = json.loads(r.data.decode("utf8"))
        cervejas.append(cerveja)

    data = jsontocsv(cervejas)
    s3_client.put_object(Body=data, ContentType='text/csv', Bucket=S3_BUCKET, Key=f'<{_get_key()}.csv>') 

def save_file(cerveja):
    loc = '/tmp'
    file_name = loc + "/" + str(1) + '.json'
    with open(..., 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(cerveja)
    return file_name    

def _get_key():
    dt_now = datetime.now(tz=timezone.utc)
    KEY = (
        dt_now.strftime("%Y-%m-%d")
        + "_("
        + dt_now.strftime("%H")
        + "H"
        + dt_now.strftime("%M")
        + "MIN)"
    )
    return KEY
#CloudWatchEventsInvocationAccess

def jsontocsv(json):
    csvio = io.StringIO()
    writer = csv.writer(csvio)
    writer.writerow(['id','name', 'abv', 'ibu', 'target_fg', 'target_og', 'ebc', 'srm', 'ph'])
    #print(len(json))
    for i in json:
        j = i[0]
        writer.writerow([j.get('id'), j.get('name'),j.get('abv'), j.get('ibu'), j.get('target_fg'), j.get('target_og'), j.get('ebc'), j.get('srm'),j.get('ph')])
    return csvio.getvalue() 
    Test Event Name 
test

Response
null

Function Logs
'49622476570153275004589895959625887524121696524377785730'}}, {'ShardId': 'shardId-000000000089', 'HashKeyRange': {'StartingHashKey': '246220574438727831286506829767702201785', 'EndingHashKey': '248987097747028143997591176169586496186'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570175575749788426582767423242394344885883766162'}}, {'ShardId': 'shardId-000000000090', 'HashKeyRange': {'StartingHashKey': '248987097747028143997591176169586496187', 'EndingHashKey': '251753621055328456708675522571470790588'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570197876494986957205908958960666993247389746594'}}, {'ShardId': 'shardId-000000000091', 'HashKeyRange': {'StartingHashKey': '251753621055328456708675522571470790589', 'EndingHashKey': '254520144363628769419759868973355084990'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570220177240185487829050494678939641608895727026'}}, {'ShardId': 'shardId-000000000092', 'HashKeyRange': {'StartingHashKey': '254520144363628769419759868973355084991', 'EndingHashKey': '257286667671929082130844215375239379392'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570242477985384018452192030397212289970401707458'}}, {'ShardId': 'shardId-000000000093', 'HashKeyRange': {'StartingHashKey': '257286667671929082130844215375239379393', 'EndingHashKey': '260053190980229394841928561777123673794'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570264778730582549075333566115484938331907687890'}}, {'ShardId': 'shardId-000000000094', 'HashKeyRange': {'StartingHashKey': '260053190980229394841928561777123673795', 'EndingHashKey': '262819714288529707553012908179007968196'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570287079475781079698475101833757586693413668322'}}, {'ShardId': 'shardId-000000000095', 'HashKeyRange': {'StartingHashKey': '262819714288529707553012908179007968197', 'EndingHashKey': '265586237596830020264097254580892262598'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570309380220979610321616637552030235054919648754'}}, {'ShardId': 'shardId-000000000096', 'HashKeyRange': {'StartingHashKey': '265586237596830020264097254580892262599', 'EndingHashKey': '268352760905130332975181600982776557000'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476569974869043001650974493601777940509632329942530'}}, {'ShardId': 'shardId-000000000097', 'HashKeyRange': {'StartingHashKey': '268352760905130332975181600982776557001', 'EndingHashKey': '271119284213430645686265947384660851402'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476569997169788200181597635137496213157993835922962'}}, {'ShardId': 'shardId-000000000098', 'HashKeyRange': {'StartingHashKey': '271119284213430645686265947384660851403', 'EndingHashKey': '273885807521730958397350293786545145805'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570019470533398712220776673214485806355341903394'}}, {'ShardId': 'shardId-000000000099', 'HashKeyRange': {'StartingHashKey': '273885807521730958397350293786545145806', 'EndingHashKey': '276652330830031271108434640188429440207'}, 'SequenceNumberRange': {'StartingSequenceNumber': '49622476570041771278597242843918208932758454716847883826'}}], 'HasMoreShards': True, 'RetentionPeriodHours': 24, 'StreamCreationTimestamp': datetime.datetime(2021, 9, 28, 16, 35, 58, tzinfo=tzlocal()), 'EnhancedMonitoring': [{'ShardLevelMetrics': []}], 'EncryptionType': 'NONE'}, 'ResponseMetadata': {'RequestId': 'e2aff4cd-d0ad-d6fd-bb62-a9e306bb7abe', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'e2aff4cd-d0ad-d6fd-bb62-a9e306bb7abe', 'x-amz-id-2': 'SX2ihxx9J9sofP50QBfL5wvW1d6D5Q+AQHzs2xAGk5GJcZEgIxn4E87v35qnozwZfPuwSThzD5KhOoZ0bzqDUDOo3mr4gFcV', 'date': 'Tue, 28 Sep 2021 18:11:58 GMT', 'content-type': 'application/x-amz-json-1.1', 'content-length': '28006'}, 'RetryAttempts': 0}}
END RequestId: aabe0499-d4dc-4aed-abce-6a7697797d8d
REPORT RequestId: aabe0499-d4dc-4aed-abce-6a7697797d8d	Duration: 11137.82 ms	Billed Duration: 11138 ms	Memory Size: 128 MB	Max Memory Used: 70 MB	Init Duration: 449.63 ms

Request ID
aabe0499-d4dc-4aed-abce-6a7697797d8d """