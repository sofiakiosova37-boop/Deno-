import os
from flask import render_template, jsonify, Blueprint
import asyncio
from library.lib.my_decorator import log
from library.lib.client import BaseHttpClient, AuthProxy, ApiKeyStrategy, IssService

iss_bp = Blueprint('iss_bp', __name__, template_folder='templates')

base_client = BaseHttpClient()
auth_logic = ApiKeyStrategy(os.getenv("NASA_API_KEY", "default_key"))
proxy = AuthProxy(base_client, auth_logic)
iss_service = IssService(proxy)

async def map_async(coro_func, iterable):
    tasks = [asyncio.create_task(coro_func(url)) for url in iterable]
    return await asyncio.gather(*tasks)

@iss_bp.route('/iss')
async def iss_page():
    return render_template('iss.html')

@iss_bp.route('/api/iss-live')
@log(level="DEBUG")
async def iss_live_data():
    urls = [
        "http://api.open-notify.org/iss-now.json",  
        "http://api.open-notify.org/astros.json"
    ]

    try:
        results = await map_async(iss_service.get_data, urls)
        return jsonify({
            "location": results[0], 
            "crew": results[1]
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500