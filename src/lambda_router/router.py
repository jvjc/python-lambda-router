import json
import re

from .request import RequestData


class Router:
    def __init__(self, event):
        self.routes = []
        self.method = event.get("requestContext").get("http").get("method")
        self.headers = event.get("headers")
        self.path = event.get("rawPath")
        self.query_string = event.get("queryStringParameters")
        try:
            self.body = (
                json.loads(event.get("body")) if event.get("body") is not None else None
            )
        except:
            raise Exception("Invalid payload")

    def add(self, method, path, handler):
        self.routes.append(
            {
                "method": method.upper(),
                "path": path,
                "handler": handler,
            }
        )

    def not_found_cb(self):
        return {"statusCode": 404, "body": "Not found"}

    def match(self):
        for route in self.routes:
            params = self.check(route.get("path"))
            if route.get("method") and params != False:
                return route.get("handler")(
                    request=RequestData(
                        headers=self.headers,
                        params=params,
                        query_string=self.query_string,
                        body=self.body,
                    )
                )
        return self.not_found_cb()

    def check(self, path):
        regex_route = path

        param_names = re.findall("{(.*?)}", regex_route)
        cleaned_param = []

        regex_builded = "^" + regex_route + "$"

        for param in param_names:
            splitted = param.split(":")
            param_name = splitted[0]
            filter = splitted[1] if len(splitted) > 1 else "[^/]*"

            cleaned_param.append(param_name)
            regex_builded = regex_builded.replace(
                "{" + param + "}", "(?P<" + param_name + ">" + filter + "?)"
            )

        matches = re.match(regex_builded, self.path)

        params = {}

        if matches:
            for name in cleaned_param:
                params[name] = matches.group(name)
            return params
        else:
            return False
