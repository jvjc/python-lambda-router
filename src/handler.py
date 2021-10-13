import traceback

from src.router import Router
from src.controller import TestController
from src.utils import response


def hello(event, context):
    try:
        test = TestController()
        router = Router(event)

        router.add("GET", "/", test.index)
        router.add("GET", "/{id:[0-9]+}", test.get_by_id)
        router.add("GET", "/{user}/{role}", test.get_by_id)
        router.add("GET", "/{id:[a-z]+}", test.get_by_name)

    except Exception as e:
        traceback.print_exc()
        return response(500, str(e))

    return router.response()
