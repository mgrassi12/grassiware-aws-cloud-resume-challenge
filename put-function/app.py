import json
import boto3
# import requests

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge-sam')

def lambda_handler(event, context):
    response = table.get_item(Key={
        'ID':'resume'
    })

    if 'Item' in response:
        record_count = response['Item']['visitor_count']
        record_count = record_count + 1
    else:
        record_count = 1
    
    response = table.put_item(Item={
            'ID':'resume',
            'visitor_count': record_count
    })

    return {
        "isBase64Encoded": "false",
        "statusCode": "200",
        "headers": {
			"Access-Control-Allow-Origin":  "*",
			"Access-Control-Allow-Methods": "*",
			"Access-Control-Allow-Headers": "*",
        },
        "body": json.dumps({
            "response": response
        }),
    }