import json

import urllib3

client = urllib3.PoolManager()


class SMSVerification:
    def __init__(self, token):
        self.auth = {
            "Content-Type": "application/json",
            "authentication": token
        }

    def get_user_balance(self):
        res = client.request('GET', 'https://smsverification.xyz/api/v2/balance',
                             headers=self.auth)
        return json.loads(res.data.decode('utf-8'))

    def get_disposable_price(self, country, service):
        data = {
            "country": country,
            "service": service
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('GET', 'https://smsverification.xyz/api/v2/disposable/price', body=payload,
                             headers=self.auth)
        return json.loads(res.data.decode('utf-8'))

    def order_disposable_number(self, country, service):
        data = {
            "country": country,
            "service": service
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('POST', 'https://smsverification.xyz/api/v2/disposable/', body=payload,
                             headers=self.auth)
        return json.loads(res.data.decode('utf-8'))

    def cancel_disposable_number(self, number_id):
        data = {
            "id": number_id
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('DELETE', 'https://smsverification.xyz/api/v2/disposable/cancel', body=payload,
                             headers=self.auth)
        return json.loads(res.data.decode('utf-8'))

    def update_disposable_number(self, number_id):
        data = {
            "id": number_id
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('PUT', 'https://smsverification.xyz/api/v2/disposable/sent', body=payload,
                             headers=self.auth)
        return json.loads(res.data.decode('utf-8'))

    def check_disposable_number(self, number_id):
        data = {
            "id": number_id
        }
        payload = json.dumps(data).encode('utf-8')
        res = client.request('GET', 'https://smsverification.xyz/api/v2/disposable/check', body=payload,
                             headers=self.auth)
        return json.loads(res.data.decode('utf-8'))



# example
api = SMSVerification('demo', 'demo')

balance = api.get_user_balance()["data"]["balance"]  # getting the user balance (float)
phone_price = api.get_disposable_price("Russia", "ProtonMail")["data"]["phone"][
    "price"]  # getting the phone price (float)

print(balance)
print(phone_price)
