from .utils import response


class TestController:
    def index(self, request):
        return response(200, "index")

    def get_by_id(self, request):
        return response(200, request)

    def get_by_name(self, request):
        return response(200, request)
