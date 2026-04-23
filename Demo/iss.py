from flask import render_template, jsonify, Blueprint
import asyncio
import httpx

iss_bp = Blueprint('iss_bp', __name__)


@iss_bp.route('/api/iss-live')
async def iss_live_data():
    urls = [
        "http://open-notify.org", 
        "http://open-notify.org"
    ]



"""async def map_async(coro_func, iterable):
    tasks = [asyncio.create_task(coro_func(url)) for url in iterable]
    return await asyncio.gather(*tasks)

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.json()
    
async def iss_page():
    urls = [
        "http://open-notify.org", 
        "http://open-notify.org"
    ]
    results = await map_async(fetch_data, urls)
    return render_template('iss.html', location=results[0], crew=results[1])
"""