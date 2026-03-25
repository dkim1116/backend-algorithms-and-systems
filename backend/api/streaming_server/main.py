from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def ws_route(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        await websocket.send_text(f"Sending back {data}")