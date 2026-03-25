import asyncio
import websockets


async def clientTest():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as ws:
        await ws.send("test")

        received = await ws.recv()
        print("Received " + received)

asyncio.run(clientTest())