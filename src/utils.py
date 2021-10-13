import json


def response(status_code, body=None):
    return {"statusCode": status_code, "body": json.dumps(body)}
