import aiohttp
import asyncio
import httpx
from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api

"""
Coroutines are a special type of function in Python that allow you to pause and resume execution at certain points, 
making them ideal for asynchronous programming. 
They are a fundamental concept in asyncio, 
enabling you to write code that performs multiple tasks seemingly at the same time without needing multiple threads.
"""

# 1. Setting Up Async Functions with async and await
async def my_async_function():
    print("Starting task...")
    await asyncio.sleep(1)  # Simulating an async I/O task
    print("Task complete!")

# 2. Running Async Code with asyncio.run
async def main():
    await my_async_function()

asyncio.run(main())

# 3. Running Multiple Async Tasks Concurrently with asyncio.gather
async def task1():
    await asyncio.sleep(1)
    print("Task 1 complete")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 complete")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# 4. Working with Async Generators
async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())

# 5. Example: Fetching Multiple URLs Asynchronously

# By default, Flask is a synchronous web framework. 
# It handles requests one at a time per worker process. 
# Using async/await won't provide benefits unless Flask itself is running in an asynchronous context 
# (e.g., using gevent, eventlet, or an ASGI server like uvicorn)

app = Flask(__name__)
api = Api(app)

# the * operator is known as the "unpacking" or "splat" operator. 
# It takes an iterable (like a list or tuple) and expands it into individual elements
class AsyncClass(Resource):
    async def fetch_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
            
    async def fetch_url_httpx(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.json()

    async def get(self):
        urls = ['http://example.com', 'http://example.org', 'http://example.net']
        tasks = [self.fetch_url(url) for url in urls]
        results = await asyncio.gather(*tasks)
        return jsonify(results)

api.add_resource(AsyncClass, "/async")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

# Using httpx instead of aiohttp

app = Flask(__name__)

@app.route('/async-get', methods=['GET'])
async def async_get():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return jsonify(data)

# you can skip jsonify() if you use return data, status_code with Content-Type explicitly set
@app.route('/skip-jsonify')
def skip_jsonify():
    data = {"message": "Hello, world"}
    response = make_response(data, 200)
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
