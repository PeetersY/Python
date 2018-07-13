from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2a6eaa13b311f6329cd36775c1be16a5"
# Your Auth Token from twilio.com/console
auth_token  = "get one yourself ;-)"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+32476598190", #my phone number
    from_="+32460241335", #Twilio phone number
    body="Hello from Python!")

print(message.sid)
