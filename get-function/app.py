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
        site_visits = response['Item']['visitor_count']
    else: 
        site_visits = 1

    return {
        "isBase64Encoded": "false",
        "statusCode": "200",
        "headers": {
			"Access-Control-Allow-Origin":  "*",
			"Access-Control-Allow-Methods": "*",
			"Access-Control-Allow-Headers": "*",
        },
        "body": json.dumps({
            "count": str(site_visits),
            # "location": ip.text.replace("\n", "")
        }),
    }