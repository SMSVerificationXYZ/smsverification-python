class UserActions:
    def __init__(self, http_client):
        self.httpClient = http_client

    def get_balance(self):
        res = self.httpClient.request('user/balance')
        if "status" not in res or "data" not in res or "balance" not in res["data"]:
            return self.httpClient.handle_error(None)
        if res["status"] == "error":
            return self.httpClient.handle_error(res)
        return res["data"]["balance"]
