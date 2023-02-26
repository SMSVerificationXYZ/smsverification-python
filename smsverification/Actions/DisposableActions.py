class DisposableActions:
    def __init__(self, http_client):
        self.httpClient = http_client

    def get_price(self, country, service):
        res = self.httpClient.request(f'disposable/price/{country}/{service}')
        if "status" not in res or "data" not in res or "phone" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "country": res["data"]["country"],
            "service": res["data"]["service"],
            "price": res["data"]["phone"]["price"]
        }

    def order(self, country, service):
        res = self.httpClient.request(f'disposable', {"country": country, "service": service}, "POST")
        if "status" not in res or "data" not in res or "phone" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "old_balance": res["data"]["old_balance"],
            "new_balance": res["data"]["new_balance"],
            "phone": {
                "number": res["data"]["phone"]["number"],
                "id": res["data"]["phone"]["id"],
                "price": res["data"]["phone"]["price"]
            }
        }

    def sent(self, number_id):
        res = self.httpClient.request(f'disposable/sent/{number_id}', None, "PUT")
        if "status" not in res or "data" not in res or "new_status" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "old_status": res["data"]["old_status"],
            "new_status": res["data"]["new_status"],
            "number_id": res["data"]["id"]
        }

    def check(self, number_id):
        res = self.httpClient.request(f'disposable/check/{number_id}')
        if "status" not in res or "data" not in res or "sms" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "number_id": res["data"]["id"],
            "sms": res["data"]["sms"]
        }

    def cancel(self, number_id):
        res = self.httpClient.request(f'disposable/cancel/{number_id}', None, "DELETE")
        if "status" not in res or "data" not in res or "new_balance" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "old_balance": res["data"]["old_balance"],
            "new_balance": res["data"]["new_balance"]
        }
