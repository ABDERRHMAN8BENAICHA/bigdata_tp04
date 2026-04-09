from infrastructure.serial_reader import SerialReader
from infrastructure.mqtt_client import MQTTClient
from application.use_cases import ProcessSensorData

import csv
from datetime import datetime
import os


CSV_FILE = "sensor_data.csv"


def save_to_csv(value: int):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        # header (مرة واحدة فقط)
        if not file_exists:
            writer.writerow(["timestamp", "value"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, value])


def main():
    reader = SerialReader("/dev/ttyUSB0")
    mqtt_client = MQTTClient("localhost")
    processor = ProcessSensorData()

    while True:
        raw = reader.read()
        data = processor.execute(raw)

        print(data)

        # publish MQTT
        mqtt_client.publish("iot/sensor", str(data.value))

        # save CSV
        save_to_csv(data.value)


if __name__ == "__main__":
    main()