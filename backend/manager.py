from backend.functions import composed
from backend.functions import core
from typing import Any, Dict
from rest_framework.request import Request

Chainable = Any


class RequestManager:

    def __init__(self):
        self.request = None
        self.post_data = None

    def set_request(self, request: Request) -> Chainable:
        self.request = request
        self.post_data = self.request.data
        return self