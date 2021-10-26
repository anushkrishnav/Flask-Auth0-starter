from src.api.hello.api import PrivateApi, PublicApi

def initialize_routes(api):
    api.add_resource(PrivateApi, '/api/private')
    api.add_resource(PublicApi, '/api/public')