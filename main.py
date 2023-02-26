from smsverification import SMSVerification

sms = SMSVerification('API_KEY')
print(sms.get_user_actions().get_balance())
