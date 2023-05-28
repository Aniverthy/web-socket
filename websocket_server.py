
import asyncio
import csv
import json
import os
import websockets
import nest_asyncio

nest_asyncio.apply()

# Function to read the CSV file and convert its rows into JSON objects
def convert_csv_to_json(file_path):
    rows = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            rows.append(row)
    return json.dumps(rows)

# WebSocket server handler
async def websocket_server(websocket, path):
    # Prompt the user to enter the file path
    file_path = input("Enter the CSV file path: ")
    # Check if the file exists and is a CSV file
    if not os.path.isfile(file_path) or not file_path.endswith('.csv'):
        print("Invalid file path or file is not in CSV format.")
        return

    # Continuously send CSV data as JSON to the client every second
    while True:
        csv_json = convert_csv_to_json(file_path)
        await websocket.send(csv_json)
        await asyncio.sleep(1)

# Start the WebSocket server
start_server = websockets.serve(websocket_server, "", 0)
server = asyncio.get_event_loop().run_until_complete(start_server)
server_address = server.sockets[0].getsockname()
print(f"WebSocket server started. Listening on {server_address[0]}:{server_address[1]}.")

# Run the server indefinitely
asyncio.get_event_loop().run_forever()