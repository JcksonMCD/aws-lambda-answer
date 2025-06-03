import json
import os

def lambda_handler(event, context):
    method = event.get("httpMethod")

    if method == "GET":
        return _httpGet()
    

    elif method == "POST":
        body = json.loads(event.get("body", "{}"))
        msg = body.get("message", "No message provided")
        return _httpPostString(msg)
        

    return {
        'statusCode': 405,
        'body': json.dumps({"error": "Method Not Allowed"}),
        'headers': {'Content-Type': 'application/json'}
    }


def _httpGet():
    print("Get method used")
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "Hello World"}),
        'headers': {'Content-Type': 'application/json'}
    }


def _httpPostString(msg):
    print("Post method used")

    

    return {
        'statusCode': 200,
        'body': json.dumps({"message": f"Hello World! {msg}"}),
        'headers': {'Content-Type': 'application/json'}
    }


