import requests
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