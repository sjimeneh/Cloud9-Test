#read csv file
import csv
import json


def read_csv(file):
    with open(f'{file}.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            
def lambda_handler(event, context):
    print(event)
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    objeto = event['Records'][0]['s3']['object']['key']
    
    print(f'Bucket {bucket}')
    print(f'Objeto {objeto}')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    