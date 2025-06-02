import json
import os

def lambda_handler(event, context):
    method = event.get("httpMethod")

    if method == "GET":
        print("Get method used")
        return {
            'statusCode': 200,
            'body': json.dumps({"message": "Hello World"}),
            'headers': {'Content-Type': 'application/json'}
        }

    elif method == "POST":
        print("Post method used")
        body = json.loads(event.get("body", "{}"))
        msg = body.get("message", "No message provided")
        return {
            'statusCode': 200,
            'body': json.dumps({"message": f"Hello World! {msg}"}),
            'headers': {'Content-Type': 'application/json'}
        }

    return {
        'statusCode': 405,
        'body': json.dumps({"error": "Method Not Allowed"}),
        'headers': {'Content-Type': 'application/json'}
    }
