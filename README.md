# 🚗 Vehicle Anti-Theft Security System Using Raspberry Pi and IoT

A smart Python + IoT based vehicle security system designed to prevent unauthorized access using **face recognition, GPS tracking, and automated email alerts**.

## 📌 Features
- Face recognition using OpenCV
- Real-time GPS tracking
- Automated email alerts
- Raspberry Pi GPIO integration
- Relay, buzzer, and LCD control
- Multithreading for parallel processing

## 🛠️ Tech Stack
- Python
- OpenCV
- Raspberry Pi
- GPS Module
- GPIO
- SMTP
- Multithreading
- IoT

## 🧠 How It Works
1. User tries to start the vehicle
2. Camera captures face
3. Authorized face → vehicle access granted
4. Unauthorized face:
   - buzzer alert
   - relay lock
   - GPS location fetched
   - email alert sent
   - LCD warning shown

## ▶️ How to Run
```bash
python main.py