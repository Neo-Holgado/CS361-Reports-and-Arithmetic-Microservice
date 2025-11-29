import zmq


# Set up environment and sockets
context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)

# Connect to server socket
socket.connect("tcp://localhost:5556")

# Setup request for battle_logic service
request_dmg = {
    "service_key": "battle_logic",
    "data": [
        {'health': 100,
         'attack': 10,
         'defense': 5},
        {'health': 100,
         'attack': 8,
         'defense': 2}
    ]
}

# Send request
print("Sending request...")
socket.send_json(request_dmg)

# Get the reply
response = socket.recv_json()

# Print response
print("Received response from server:")
print(response)

# Setup request for convert_volume
request_volume = {
    "service_key": "convert_volume",
    "data": {
        "amount": 2,    # Correct response should be: 30
        "unit": "tablespoon",
        "to_metric": True
        }
    }

# Setup request for convert_weight
request_weight = {
    "service_key": "convert_weight",
    "data": {
        "amount": 1,    # Correct response should be: 454
        "unit": "pound",
        "to_metric": True
        }
    }

# Setup request for convert_temperature
request_temp_CtoF = {
    "service_key": "convert_temp",
    "data": {
        "value": 180,   # Correct response should be: 356.0
        "direction": "C_to_F"
        }
    }


def run_test(request_dict):
    socket.connect("tcp://localhost:5556")
    print('sending request...')
    socket.send_json(request_dict)
    response = socket.recv_json()
    print("Received response: ")
    print(response)


run_test(request_volume)
run_test(request_weight)
run_test(request_temp_CtoF)
