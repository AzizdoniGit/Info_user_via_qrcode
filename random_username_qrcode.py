import requests
import json
from pprint import pprint
from qrcode import *

key = 'EpdrsWn0cEb5aIO5KcQTOQ==sECfiKJOQ2nifTNO'
api_url = 'https://api.api-ninjas.com/v1/randomuser'
response = requests.get(api_url, headers={'X-Api-Key': key})

try:

    data = json.loads(response.text)
    pprint(f"Nickname: {data.get('username')}")
    pprint(f"Gender: {data.get('sex')}")
    pprint(f"Location: {data.get('address')}")
    pprint(f"Name: {data.get('name')}")
    pprint(f"Email: {data.get('email')}")
    pprint(f"Birthday: {data.get('birthday')}")
    make = make(data)
    make.save(f"username_info.png")
except Exception as err:
    pprint(f"The error is: {err}. Check your code again, please)")