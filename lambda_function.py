import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    _basicEnvLogs(event)

    method = event.get("httpMethod")

    if method == "GET":
        return _httpGet()
    

    elif method == "POST":
        return _httpPostString(event)
        

    return {
        'statusCode': 405,
        'body': json.dumps({"error": "Method Not Allowed"}),
        'headers': {'Content-Type': 'application/json'}
    }


def _httpGet():
    logger.info("Get method used")
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "Hello World"}),
        'headers': {'Content-Type': 'application/json'}
    }


def _httpPostString(event):
    logger.info("Post method used")

    body = json.loads(event.get("body", "{}"))
    msg = body.get("message", "No message provided")

    return {
        'statusCode': 200,
        'body': json.dumps({"message": f"Hello World! {msg}"}),
        'headers': {'Content-Type': 'application/json'}
    }

def _basicEnvLogs(event):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ.get('AWS_LAMBDA_LOG_GROUP_NAME', 'LOG_GROUP not found'))
    logger.info(os.environ.get('AWS_LAMBDA_LOG_STREAM_NAME', 'LOG_STREAM not found'))
    logger.info('## EVENT')
    logger.info(event)



