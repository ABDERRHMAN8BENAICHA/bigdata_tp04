# TP04 – Docker for IoT Systems 🌐

This project simulates a complete IoT system using **Docker** and **MQTT**:
- A **sensor** generates temperature and humidity data.
- An **MQTT broker** (Mosquitto) forwards the messages.
- A **server** receives, displays, and alerts if the temperature exceeds 30°C.

Each component runs in its own Docker container, orchestrated by `docker-compose`.

---

## 📁 Project Structure

```
.
├── docker-compose.yml
├── mosquitto.conf
├── sensor/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── sensor.py
└── server/
    ├── Dockerfile
    ├── requirements.txt
    └── server.py
```

---

## 📝 Step 1: Theoretical Questions (Answers)

### 1. What is the difference between a Docker **Image** and a **Container**?

| **Image** | **Container** |
|-----------|----------------|
| 📄 Static (read-only) template | 🏃 Running instance |
| Like a **recipe** or an `.exe` file | Like the **prepared dish** or a launched process |
| Does not change | Can be started, stopped, deleted |
| Stored on disk | Runs in RAM |

👉 From a single image, you can run multiple containers.

### 2. Why is Docker useful in IoT?

- **Portability**: the same container runs on a Raspberry Pi, a PC, or a cloud server.
- **Isolation**: each service (sensor, broker, server) is independent.
- **Fast deployment**: just `docker run` or `docker-compose up`.
- **Easy updates**: change the image, restart.
- **Lightweight**: suitable for resource‑constrained devices.

### 3. Difference between a **Virtual Machine (VM)** and a **Docker Container**?

| **VM** | **Container** |
|--------|----------------|
| Each VM includes its own operating system | Shares the host’s kernel |
| Heavy (several GB) | Lightweight (a few MB to a few hundred MB) |
| Slow startup (minutes) | Fast startup (seconds) |
| Strong isolation | Lighter isolation |

👉 In IoT, containers are preferred because they consume fewer resources.

### 4. What does the `docker build` command do?

It builds a **Docker image** from a `Dockerfile`.  
The `Dockerfile` contains a series of instructions (`FROM`, `RUN`, `COPY`, `CMD`…).  
`docker build -t my_image .` reads the file, executes each step, and produces an image ready to run.

### 5. What is the role of **MQTT** in an IoT system?

MQTT (Message Queuing Telemetry Transport) is a **lightweight** messaging protocol suited for constrained networks (low bandwidth, high latency).

- **Publish/Subscribe**: sensors publish data to **topics**.
- **Broker**: centralizes and distributes messages to subscribers.
- Advantages: very low overhead, ideal for connected objects.

In our project:  
`Sensor` → publishes to `iot/sensor/data`  
`Server` → subscribes to that topic and receives the data.

---

## 🐳 Quick Start

### Prerequisites
- Docker and Docker Compose installed

### 1. Clone or create the files
Make sure the directory structure above is respected.

### 2. Start all services

```bash
docker-compose up --build
```

### 3. Watch the logs

- The **sensor** sends data every 3 seconds.
- The **server** displays each received message and an **alert** if temperature > 30°C.
- The **broker** manages connections.

### 4. Stop

```bash
docker-compose down
```

---

## 🧪 Tests and Checks

### Show logs of a specific service

```bash
docker-compose logs sensor
docker-compose logs server
docker-compose logs broker
```

### List running containers

```bash
docker ps
```

### Run a command inside a container (debugging)

```bash
docker exec -it iot-sensor bash
docker exec -it iot-server bash
```

---

## 📤 Publishing to Docker Hub (optional)

1. Create an account on [hub.docker.com](https://hub.docker.com)
2. Log in from the command line: `docker login`
3. Build the images with your username:

```bash
docker build -t benaichaabderrahmane/iot-sensor:v1 ./sensor
docker build -t benaichaabderrahmane/iot-server:v1 ./server
```

4. Push the images:

```bash
docker push benaichaabderrahmane/iot-sensor:v1
docker push benaichaabderrahmane/iot-server:v1
```

5. Edit `docker-compose.yml` to use these images (replace `build:` with `image:`).

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Sensor or server logs are empty | Make sure `requirements.txt` contains `paho-mqtt==2.1.0` and the code uses `mqtt.CallbackAPIVersion.VERSION1` (see provided files). |
| `Echec envoi: 4` (connection loss) | Add `client.reconnect_delay_set()` and use `client.loop_forever()` in the server, `loop_start()` in the sensor. |
| Broker refuses connection | Ensure `mosquitto.conf` contains `listener 1883` and `allow_anonymous true`. |
| Containers exit immediately | Run `docker-compose logs` to see the error. Check that port 1883 is free on the host. |

---

## 📜 Key Files (excerpts)

### `sensor/sensor.py` (publisher)

```python
client = mqtt.Client(client_id="sensor-01")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(BROKER_HOST, BROKER_PORT)
client.loop_start()
# Sending loop every 3 seconds
```

### `server/server.py` (subscriber)

```python
client = mqtt.Client(client_id="server-01")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_HOST, BROKER_PORT)
client.loop_forever()
```

### `docker-compose.yml`

Uses a bridge network `iot-network`.  
The broker uses the `eclipse-mosquitto` image with a configuration file mounted as a volume.

---

## ✅ Expected Output

```
iot-server  | ✅ Serveur connected to MQTT broker
iot-server  | 📥 Subscribed to topic: iot/sensor/data
iot-sensor  | ✅ Sensor connected to MQTT broker
iot-sensor  | 📤 Data sent: {"temperature": 27.3, "humidity": 62.1, ...}
iot-server  | ==================================================
iot-server  | 📨 New message received!
iot-server  | 🌡️  Temperature : 27.3°C
iot-server  | 💧 Humidity    : 62.1%
...
```