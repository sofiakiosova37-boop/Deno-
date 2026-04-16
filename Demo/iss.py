from flask import render_template
import urllib2
import json

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)
obj = json.loads(response.read())
print(obj['timestamp'])
print(obj['iss_position']['latitude'], obj['data']['iss_position']['latitude'])

"""
async def iss_page():
    urls = [
        "http://open-notify.org", # location
        "http://open-notify.org" # people number
    ]
    """