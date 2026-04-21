from flask import render_template
import asyncio
import httpx
import requests

async def map_async(coro_func, iterable):
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
