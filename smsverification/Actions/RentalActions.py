class RentalActions:
    def __init__(self, http_client):
        self.httpClient = http_client

    def get_price(self, country, service, length):
        res = self.httpClient.request(f'rental/price/{country}/{service}/{length}')
        if "status" not in res or "data" not in res or "phone" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "country": res["data"]["country"],
            "service": res["data"]["service"],
            "length": res["data"]["length"],
            "price": res["data"]["phone"]["price"]
        }

    def order(self, country, service, length):
        res = self.httpClient.request(f'rental/order', {"country": country, "service": service, "length": length},
                                      "POST")
        if "status" not in res or "data" not in res or "phone" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "order": {
                "id": res["data"]["phone"]["id"],
                "number": res["data"]["phone"]["number"],
                "purchased_at": res["data"]["phone"]["purchased_at"],
                "expires_at": res["data"]["phone"]["expires_at"],
                "can_cancel": res["data"]["phone"]["can_cancel"],
                "expired": res["data"]["phone"]["expired"],
                "messages": {},
            }
        }

    def get_orders(self):
        res = self.httpClient.request(f'rental/orders')
        if "status" not in res or "data" not in res or "orders" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["orders"]

    def get_order(self, order_id):
        res = self.httpClient.request(f'rental/orders/{order_id}')
        if "status" not in res or "data" not in res or "order" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["order"]

    def cancel(self, order_id):
        res = self.httpClient.request(f'rental/orders/{order_id}/cancel', None, 'POST')
        if "status" not in res or "data" not in res or "new_balance" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "old_balance": res["data"]["old_balance"],
            "new_balance": res["data"]["new_balance"],
        }

    def get_messages(self, order_id):
        res = self.httpClient.request(f'rental/orders/{order_id}/refresh', None, 'POST')
        if "status" not in res or "data" not in res or "messages" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["messages"]
