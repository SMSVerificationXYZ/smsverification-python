import json

from pip._vendor import urllib3


class HttpClient:
    def __init__(self, token):
        self.client = urllib3.PoolManager()
        self.headers = {
            "Content-Type": "application/json",
            "Authentication": token
        }

    def request(self, destination, data=None, method='GET'):
        if data is None:
            data = {}
        payload = json.dumps(data).encode('utf-8')
        res = self.client.request(method, f'https://smsverification.xyz/api/v2/{destination}', body=payload,
                                  headers=self.headers)
        return json.loads(res.data.decode('utf-8'))

    def handle_error(self, response):
        if response is None:
            return {
                "status": False,
                "error": "UNKNOWN",
                "content": "Unknown error occurred."
            }
        return {
            "status": False,
            "error": response["error_type"],
            "content": response["content"]
        }
