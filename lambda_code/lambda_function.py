import json
import boto3

def lambda_handler(event, context):
    # Sample Lambda function logic
    print("Received event: " + json.dumps(event, indent=2))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
