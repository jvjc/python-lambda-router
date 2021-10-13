class RequestData:
    def __init__(self, headers, params, query_string, body):
        self.headers = headers
        self.params = params
        self.query_string = query_string
        self.body = body

    def header(self, name, default=None):
        return self.extract("headers", name, default)

    def param(self, name, default=None):
        return self.extract("params", name, default)

    def query(self, name, default=None):
        return self.extract("query_string", name, default)

    def data(self, name, default=None):
        return self.extract("body", name, default)

    def extract(self, attr, name, default):
        if self[attr] is None:
            return default

        if self[attr][name] is None:
            return default

        return self[attr][name]
