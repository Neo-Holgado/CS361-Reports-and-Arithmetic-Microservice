import zmq
import json
import time
from kitchen_converter_v1 import CookingConverter
from battle_logic import battle_logic


# Environment and socket initialization
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")
print("Server running")

# Setup instance of CookingConverter
converter = CookingConverter()

try:
    while True:
        # Receive message
        message = socket.recv_string()
        print(f"Received request: {message}")
        try:
            request = json.loads(message)
        except json.JSONDecodeError:
            socket.send_json({"error": "Invalid JSON"})
            continue

        # Unpack message
        service_key = request.get("service_key")
        data = request.get("data", {})
        response = {}

        # Route request
        if not service_key:
            response = {"error": "Missing service_key"}
        elif service_key == "battle_logic":
            # Unpack data
            player = {}
            enemy = {}
            for key in ['health', 'attack', 'defense']:
                player[key] = data[0][key]
                enemy[key] = data[1][key]

            # call battle_logic.py function
            response = battle_logic(player, enemy)

        elif service_key in ["convert_volume", "convert_weight"]:
            # Unpack data
            amount = data.get("amount")
            unit = data.get("unit")
            to_metric = data.get("to_metric")

            # call convert_volume_or_weight function
            response = {
                "conversion": converter.convert_volume_or_weight(amount, unit, to_metric)
            }

        elif service_key == "convert_temp":
            # Unpack data
            value = data.get("value")
            direction = data.get("direction")

            # Call convert_temperature
            response = {
                "conversion": converter.convert_temperature(value, direction)
            }
        else:
            response = {"error": f"Unknown service_key: {service_key}"}

        time.sleep(2)
        socket.send_json(response)
except KeyboardInterrupt:
    print("\nServer shutting down...")

finally:
    socket.close()
    context.term()
    print("Exit confirmed")
