from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

def send_sms(msg):
    client = Client(account_sid, auth_token)  
    message = client.messages.create(
        from_= my_twilio,  
        body= msg,      
        to=my_cell  
        ) 
    print("Message sent!")
