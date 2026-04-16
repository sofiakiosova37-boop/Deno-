from flask import render_template

async def iss_page():
    urls = [
        "http://open-notify.org", # location
        "http://open-notify.org" # people number
    ]