class SenderActions:
    def __init__(self, http_client):
        self.httpClient = http_client

    def add_contact(self, name, number):
        res = self.httpClient.request(f'sender/contact', {"name": name, "number": number}, "POST")
        if "status" not in res or "data" not in res or "contact" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["contact"]

    def get_contacts(self):
        res = self.httpClient.request(f'sender/contacts')
        if "status" not in res or "data" not in res or "contacts" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["contacts"]

    def get_contact(self, contact_id):
        res = self.httpClient.request(f'sender/contacts/{contact_id}')
        if "status" not in res or "data" not in res or "contact" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["contact"]

    def delete_contact(self, contact_id):
        res = self.httpClient.request(f'sender/contact/{contact_id}/delete', None, 'POST')
        if "status" not in res or "data" not in res:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["status"] == "success"

    def edit_contact_name(self, contact_id, name):
        res = self.httpClient.request(f'sender/contact/{contact_id}/edit', {"name": name}, "PUT")
        if "status" not in res or "data" not in res or "new_name" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "old_name": res["data"]["old_name"],
            "new_name": res["data"]["new_name"]
        }

    def edit_contact_number(self, contact_id, number):
        res = self.httpClient.request(f'sender/contact/{contact_id}/edit', {"number": number}, "PUT")
        if "status" not in res or "data" not in res or "new_number" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "old_number": res["data"]["old_number"],
            "new_number": res["data"]["new_number"]
        }

    def order(self, frm, rcpt, message):
        res = self.httpClient.request(f'sender/order', {"from": frm, "rcpt": rcpt, "message": message}, "POST")
        if "status" not in res or "data" not in res or "message" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return {
            "message": res["data"]["message"]
        }

    def get_orders(self):
        res = self.httpClient.request(f'sender/orders')
        if "status" not in res or "data" not in res or "orders" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["orders"]

    def get_order(self, order_id):
        res = self.httpClient.request(f'sender/orders/{order_id}')
        if "status" not in res or "data" not in res or "order" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["order"]
