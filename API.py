import requests
import os

def API(filename,type):

    url = "https://messenger.ibsfintech.com/"

    payload={'Username': 'Prannoy',
    'Type': 'zip'}
    files=[
      ('TextFile',(os.path.basename(filename),open(filename,'rb')))
    ]
    headers = {
      'Authorization': 'Basic UHJhbm5veTpQcmFubm95QDE0'
    }

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    return response.text