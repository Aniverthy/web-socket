# WebSocket Server Documentation

This WebSocket server implementation reads a CSV file and sends its contents as JSON to connected clients every second.
Function: convert_csv_to_json(file_path)
•	Input: file_path (string) - The path to the CSV file.
•	Output: JSON representation of the CSV data.
This function reads the CSV file at the specified file_path and converts each row into a JSON object. It returns the JSON representation of the CSV data.
WebSocket Server Handler: websocket_server(websocket, path)
•	Input: ‘websocket’ (WebSocket object) - The WebSocket connection object.
•	Input: ‘path’ (string) - The URL path of the WebSocket connection.
This function is the handler for the WebSocket server. It prompts the user to enter the CSV file path. If the file path is valid and the file is in CSV format, the server continuously sends the CSV data as JSON to the client every second using the WebSocket connection.
Main Execution:
1.	Sets up the WebSocket server to listen on an available port on the local machine.
2.	Starts the WebSocket server and prints the server's address where it is listening for connections.
3.	Runs the server indefinitely.

# WebSocket Client Documentation

This WebSocket client implementation connects to the WebSocket server and receives the JSON data sent by the server.

WebSocket Client Handler: websocket_client()
This function is the handler for the WebSocket client. It establishes a WebSocket connection to the server and continuously receives JSON data from the server. The received JSON data is printed to the console.
Main Execution:
1.	Establishes a WebSocket connection to the server.
2.	Receives JSON data from the server and prints it to the console.
3.	Continues listening for data until termination or disconnection.
Output:
•	WebSocket Server:
•	Prints the address where the WebSocket server is listening, e.g., "WebSocket server started. Listening on 0.0.0.0:59050."
•	Prompts the user to enter the CSV file path.
•	WebSocket Client:
•	Prints the received JSON data from the server to the console, e.g., [{"11": "66", "22": "77", "33": "88", "44": "99", "55": "1010"}, {"11": "1111", "22": "1212", "33": "1313", "44": "1414", "55": "1515"}]
•	Continues printing the received JSON data as it arrives from the server.
