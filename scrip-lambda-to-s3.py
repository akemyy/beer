import csv
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