from flask import render_template
import requests 

response = requests.get("http://api.open-notify.org/iss-now.json")
obj = response.json()
print(obj['timestamp'])
print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])

"""
async def iss_page():
    urls = [
        "http://open-notify.org", # location
        "http://open-notify.org" # people number
    ]
    """