#read csv file
import csv
import json


def read_csv(file):
    with open(f'{file}.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            
def lamda_handler(event, context):
    #read_csv('data')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    