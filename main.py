import json

import urllib3

client = urllib3.PoolManager()


class SMSVerification:
    def __init__(self, username, password):
        self.auth = {
            "username": username,
            "password": password
        }

    def get_user_balance(self):
        data = {
            "auth": {
                "username": self.auth["username"],
                "password": self.auth["password"]
            }
        }

        payload = json.dumps(data).encode('utf-8')
        res = client.request('GET', 'https://smsverification.xyz/api/v2/balance', body=payload,
                             headers={'Content-Type': 'application/json'})
        return json.loads(res.data.decode('utf-8'))

    def get_disposable_price(self, country, service):
        data = {
            "auth": {
                "username": self.auth["username"],
                "password": self.auth["password"]
            },
            "country": country,
            "service": service
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('GET', 'https://smsverification.xyz/api/v2/disposable/price', body=payload,
                             headers={'Content-Type': 'application/json'})
        return json.loads(res.data.decode('utf-8'))

    def order_disposable_number(self, country, service):
        data = {
            "auth": {
                "username": self.auth["username"],
                "password": self.auth["password"]
            },
            "country": country,
            "service": service
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('POST', 'https://smsverification.xyz/api/v2/disposable/', body=payload,
                             headers={'Content-Type': 'application/json'})
        return json.loads(res.data.decode('utf-8'))

    def cancel_disposable_number(self, number_id):
        data = {
            "auth": {
                "username": self.auth["username"],
                "password": self.auth["password"]
            },
            "id": number_id
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('DELETE', 'https://smsverification.xyz/api/v2/disposable/cancel', body=payload,
                             headers={'Content-Type': 'application/json'})
        return json.loads(res.data.decode('utf-8'))

    def update_disposable_number(self, number_id):
        data = {
            "auth": {
                "username": self.auth["username"],
                "password": self.auth["password"]
            },
            "id": number_id
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('PUT', 'https://smsverification.xyz/api/v2/disposable/sent', body=payload,
                             headers={'Content-Type': 'application/json'})
        return json.loads(res.data.decode('utf-8'))

    def check_disposable_number(self, number_id):
        data = {
            "auth": {
                "username": self.auth["username"],
                "password": self.auth["password"]
            },
            "id": number_id
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('GET', 'https://smsverification.xyz/api/v2/disposable/check', body=payload,
                             headers={'Content-Type': 'application/json'})
        return json.loads(res.data.decode('utf-8'))


api = SMSVerification('demo', 'demo')
print(api.get_user_balance()["data"]["balance"])
print(api.get_disposable_price("Russia", "ProtonMail")["data"]["phone"]["price"])
