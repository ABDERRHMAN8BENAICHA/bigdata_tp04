import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, host: str, port: int = 1883):
        self.client = mqtt.Client()
        self.client.connect(host, port, 60)

    def publish(self, topic: str, message: str):
        print(f"[MQTT] Publishing: {message}")
        self.client.publish(topic, message)