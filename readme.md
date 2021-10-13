```python
import traceback

from router import Router

# utils and functions
def response(status_code, body=None, headers=None):
    return {"statusCode": status_code, "body": json.dumps(body)}

def index(self, request):
        return response(200, request)

def get_by_id(self, request):
        return response(200, request)

def get_by_name(self, request):
    return response(200, request)

# Lambda
def hanlder(event, context):
    try:
        router = Router(event)

        router.add("GET", "/", index)
        router.add("GET", "/{id:[0-9]+}", get_by_id)
        router.add("GET", "/{name:[a-z]+}", get_by_name)

    except Exception as e:
        traceback.print_exc()
        return response(500, str(e))

    return router.match()
```
