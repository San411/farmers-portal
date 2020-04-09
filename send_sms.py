from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACfbf43b9d2f8e9a3b4a3d6c719a0c6121", "2ba4e19ad6f8c43cb6f0bc1ddc84832d")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+9483574894", 
                       from_="+12569987543", 
                       body="Quarentine is over")