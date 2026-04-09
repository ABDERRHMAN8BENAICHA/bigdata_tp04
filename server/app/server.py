import paho.mqtt.client as mqtt

TOPIC = "iot/sensor"

def on_connect(client, userdata, flags, rc):
    print("[SERVER] Connected to MQTT")
    client.subscribe(TOPIC)
    print(f"[SERVER] Subscribed to {TOPIC}")

def on_message(client, userdata, msg):
    print(f"[SERVER] Received: {msg.payload.decode()}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

print("🚀 Connecting to MQTT...")

client.connect("mqtt", 1883, 60)

print("🔥 START LOOP")

client.loop_forever()