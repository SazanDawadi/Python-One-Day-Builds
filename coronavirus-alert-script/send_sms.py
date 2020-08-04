from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio
# make a new python file and add variable account_sid, auth_token, my_cell, my_twilio
# assign it value and import it in this file
# you can get your api key and auth token from twilio website

def send_sms(msg):
    client = Client(account_sid, auth_token)  
    message = client.messages.create(
        from_= my_twilio,  
        body= msg,      
        to=my_cell  
        ) 
    print("Message sent!")
