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

    def add_html_code(self):
        name = self.post_data.get("name")
        html_code = self.post_data.get("html_code")
        category = self.post_data.get("category")
        code_type = self.post_data.get("code_type")
        status = self.post_data.get("status")
        html = core.add_html_object(name=name, html_code=html_code, category=category, code_type=code_type,
                                    status=status)
        return {
            "signature_code": html.unique_code,
            "name": html.name,
            "message": "Successfully added"
        }
