from flask_restful import Resource
from src.auth import requires_auth 


class PrivateApi(Resource):
    method_decorators = {'get': [requires_auth]}
    def get(self):
        return {
            "message": "Hello from private api"
        }
class PublicApi(Resource):
    def get(self):
        return {
            "message": "Hello from public api"
        }