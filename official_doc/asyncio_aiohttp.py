import aiohttp
import asyncio
from flask import Flask
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

# the * operator is known as the "unpacking" or "splat" operator. 
# It takes an iterable (like a list or tuple) and expands it into individual elements

app = Flask(__name__)
api = Api(app)

class AsyncClass(Resource):
    async def fetch_url(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    async def main():
        urls = ['http://example.com', 'http://example.org', 'http://example.net']
        tasks = [fetch_url(url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

api.add_resource(AsyncClass, "/async")

if __name__ == "__main__":
    app.run(debug=True)