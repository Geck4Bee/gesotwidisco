import sys
sys.path.append('lib')

import requests
import os
import json
import datetime


def shaping_data(event):
    return {
        'ja': event['ja'],
        'createdAt': event['createdAt'],
        'url': event['url'],
        'webhook': event['webhook']
    }

def sendWebHook(obj):
    content = obj['ja'] + '\n' + obj['createdAt'] + '\n' + obj['url']
    try:
        print('shot webhook!')
        response = requests.post(
            obj['webhook'],
            json.dumps({"content": content}),
            headers={'Content-Type': 'application/json'}
        )
        print(response)
    except Exception as ew:
        sys.stderr.write("*** error *** in SendWebHook ***\n")
        sys.stderr.write(str(ew) + "\n")
    else:
        return response

def handler(event, context):
    obj = shaping_data(event)
    sendWebHook(obj)
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
