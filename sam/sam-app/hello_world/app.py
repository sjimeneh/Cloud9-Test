import json
import pandas

# import requests


def lambda_handler(event, context):
    
    #create dataFrame in pandas
    df = pandas.DataFrame(columns=['name','age'])


    return {
        "statusCode": 200,
        "body": "OK"
    }
