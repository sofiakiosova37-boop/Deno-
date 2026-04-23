from flask import render_template, jsonify, Blueprint
import asyncio
import httpx

iss_bp = Blueprint('iss_bp', __name__, template_folder='templates')

async def map_async(coro_func, iterable):
    tasks = [asyncio.create_task(coro_func(url)) for url in iterable]
    return await asyncio.gather(*tasks)

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=2)
        return resp.json()

@iss_bp.route('/iss')
async def iss_page():
    return render_template('iss.html')

@iss_bp.route('/api/iss-live')
async def iss_live_data():
    urls = [
        "http://open-notify.org", 
        "http://open-notify.org"
    ]
    results = await map_async(fetch_data, urls)
    return jsonify({"location": results[0], "crew": results[1]})