import paho.mqtt.client as mqtt
import time
import random
import json
from datetime import datetime

BROKER_HOST = "broker"
BROKER_PORT = 1883
TOPIC = "iot/sensor/data"

def generate_sensor_data():
    return {
        "sensor_id": "sensor-01",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 80.0), 2),
        "status": "active"
    }

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Sensor connecté au broker MQTT")
    else:
        print(f"❌ Erreur connexion: {rc}")

def on_publish(client, userdata, mid):
    print(f"✅ Message confirmé par le broker (mid={mid})")

def main():
    client = mqtt.Client(client_id="sensor-01")
    client.on_connect = on_connect
    client.on_publish = on_publish

    # إعادة الاتصال تلقائياً
    client.reconnect_delay_set(min_delay=1, max_delay=5)

    print(f"🔄 Connexion au broker: {BROKER_HOST}:{BROKER_PORT}")
    client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)

    # ← الفرق: loop_start بدل loop_forever
    client.loop_start()

    print("⏳ Attente du serveur...")
    time.sleep(3)
    print("📡 Début de l'envoi des données...")

    try:
        while True:
            if client.is_connected():
                data = generate_sensor_data()
                payload = json.dumps(data)
                result = client.publish(TOPIC, payload, qos=1)  # ← qos=1 مهم!
                result.wait_for_publish()  # ← انتظر التأكيد
                print(f"📤 Données envoyées: {payload}")
            else:
                print("⚠️ Pas de connexion, attente...")
            time.sleep(3)

    except KeyboardInterrupt:
        print("\n🛑 Sensor arrêté")
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()