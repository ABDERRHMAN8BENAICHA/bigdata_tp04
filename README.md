# 🚀 TP04: Docker for IoT Systems

## 🎯 Objective
This project demonstrates the use of Docker and MQTT to build a simple IoT system with real hardware.

---

## 🧠 Technologies Used
- Docker 🐳  
- MQTT (Mosquitto)  
- Python 🐍  
- Arduino Uno R3 🔌  
- Serial Communication  

---

## 🏗️ Architecture
Arduino → Serial → Python Bridge → MQTT → Docker Server

---

## 🔌 System Components

### 1. Arduino (Sensor)
- Reads analog values (0–1023)
- Sends data via Serial (USB)

### 2. Python Bridge
- Reads serial data from Arduino
- Converts raw values to temperature
- Publishes data to MQTT

### 3. MQTT Broker
- Eclipse Mosquitto running in Docker
- Enables communication between components

### 4. Server (Docker Container)
- Subscribes to MQTT topic `iot/sensor`
- Receives and displays data

---

## 📊 Data Processing
Voltage = value * (5.0 / 1023)  
Temperature = Voltage * 100 (LM35)

---

## 💾 Data Storage
Data is saved in CSV file with timestamp.

---

## 🐳 Docker Usage
docker compose up --build

---

## ☁️ Docker Hub
docker pull benaichaabderrahmane/tp04-server:latest

---

## ❓ Answers (Part 2)

- Image: blueprint  
- Container: running instance  

- Docker in IoT: lightweight & portable  

- VM: heavy / Container: lightweight  

- docker build: creates image  

- MQTT: publish/subscribe communication  

---

## 🎯 Mini Project
Sensor + Server + MQTT communication ✔

---

## ✅ Conclusion
Complete IoT system using Docker and MQTT with real Arduino.

---

## 👨‍💻 Author
Benaicha Abderrahmane
