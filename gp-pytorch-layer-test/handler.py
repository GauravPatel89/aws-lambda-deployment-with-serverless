try:
    import unzip_requirements
except ImportError:
    pass

import json
import sys


import torch
import torchvision
import PIL 


print('torch version:',torch.__version__)
print('torchvision version:',torchvision.__version__)
print('Pillow version:',PIL.__version__)

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
