from smsverification.Actions.UserActions import UserActions
from smsverification.Actions.DisposableActions import DisposableActions
from smsverification.Actions.RentalActions import RentalActions
from smsverification.Actions.SenderActions import SenderActions
from smsverification.HttpClient.HttpClient import HttpClient


class SMSVerification:
    def __init__(self, token):
        self.httpClient = HttpClient(token)
        self.userActions = UserActions(self.httpClient)
        self.disposableActions = DisposableActions(self.httpClient)
        self.rentalActions = RentalActions(self.httpClient)
        self.senderActions = SenderActions(self.httpClient)

    def get_user_actions(self):
        return self.userActions

    def get_disposable_actions(self):
        return self.disposableActions

    def get_rental_actions(self):
        return self.rentalActions

    def get_sender_actions(self):
        return self.senderActions
