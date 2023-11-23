#read csv file
import csv
import json
import boto3
import io


def read_csv(file):
    csv_reader = csv.reader(io.StringIO(file))
    next(csv_reader)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tbl_samuel')
    
    
    for row in csv_reader:
        print(row)
        
        item = {
            'id': row[0],
            'nombre':row[1],
            'apellido':row[2]
        }
        
        table.put_item(Item=item)
            
def lambda_handler(event, context):
    print(event)
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    objeto = event['Records'][0]['s3']['object']['key']
    
    # print(f'Bucket {bucket}')
    # print(f'Objeto {objeto}')
   
    s3 = boto3.client('s3')
   
    response = s3.get_object(Bucket=bucket, Key=objeto)
    csvfile = response['Body'].read().decode('utf-8')
   
    read_csv(csvfile)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    