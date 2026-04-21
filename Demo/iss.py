from flask import render_template
import requests 

"""
response = requests.get("http://api.open-notify.org/iss-now.json")
obj = response.json()
print(obj['timestamp'])
print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])
"""

def iss_page():
    location_res = requests.get("http://api.open-notify.org/iss-now.json").json()
    crew_res = requests.get("http://api.open-notify.org/astros.json").json()
    return render_template('iss.html', location=location_res, crew=crew_res)