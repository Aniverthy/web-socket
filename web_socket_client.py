
import asyncio
import nest_asyncio
import websockets

nest_asyncio.apply()

# WebSocket client handler
async def websocket_client():
    uri = "ws://localhost:59356"  # Update with the correct server port if necessary
    async with websockets.connect(uri) as websocket:
        while True:
            # Receive JSON data from the server
            json_data = await websocket.recv()
            print(json_data)

# Run the WebSocket client
asyncio.run(websocket_client())