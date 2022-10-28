import json
import requests

def handler(event, context):
    body = json.loads(event['body'])
    QR = body['message']['text']
    url = "https://apipy1.herokuapp.com/QR/" + body['message']['text']
    payload = ""
    response = requests.request("POST", url, data=payload)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'method': 'sendMessage',
            'chat_id': body['message']['chat']['id'],
            'text':  body['message']['text']
        }),
        'isBase64Encoded': False
    }
