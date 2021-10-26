import os

class Config:
    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
    API_IDENTIFIER = os.environ.get('AUTH0_IDENTIFIER')
    ALGORITHMS = [os.environ.get('ALGORITHM')]
    AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
    AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')
    
