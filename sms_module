import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(URL, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(URL, req_params)

# get response
# response = sendPostRequest(URL, 'Z8SQ3MGQEU6FQ3MNSC8Z86M5J3QIMI3U', '9QAAWR93VT4XNQTV', 'stage', 'RECIEVER_NUM', 'YOUR_EMAIL_ID', 'MESSAGE' )
