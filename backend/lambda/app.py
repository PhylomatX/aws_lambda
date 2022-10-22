import json
import boto3

# Global variables that are reused
sm_runtime_client = boto3.client('sagemaker-runtime')
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin":  "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },
        "body": json.dumps({
            "test": 1,
        }),
    }
