# 🌿 IoT Greenhouse - 🏗 Work in Progress
This project was created with the goal of exploring and implementing the essential parts of an IoT system, using the greenhouse monitoring case. It provides real-time monitoring of devices through a web dashboard and also access to historical data.

## Stack and Technologies
The system covers communication between devices, data processing in the back-end, a management interface in the front-end, infrastructure setup for deployment, and the firmware necessary for the devices.

### Back-end (Go, Redis, MQTT, WebSocket, PostgreSQL)
For the back-end, I chose to use microservices in Go to ensure scalability and performance. The architecture consists of:

* save_data_service: Receives device data via MQTT and stores it in the PostgreSQL database.
* stream_data_service: Streams real-time device data to clients via WebSocket.
* api_service: Manages data queries and user authentication.

For session control, I used Redis and the PostgreSQL database to store login and authentication information.

<p align="left" >
  <img src="https://skillicons.dev/icons?i=go,redis,postgresql" />
</p>

### Front-end (Next.js, TypeScript, Chakra UI)
On resource-limited devices, server-side rendering can improve user experience. To achieve this goal, I used Next.js and Chakra UI as the component library.

<p align="left">
  <img src="https://skillicons.dev/icons?i=nextjs,typescript" />
  <img src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/chakra_ui.png" width="50" height="auto"/>
</p>

### Infrastructure (Docker Compose, Traefik, Eclipse Mosquitto, Python)
All services are containerized with Docker, and orchestration is simplified using Docker Compose and Traefik. Eclipse Mosquitto was chosen as the MQTT broker, while Python is used for automation scripts and auxiliary tasks.

<p align="left">
  <img src="https://skillicons.dev/icons?i=docker" /> 
  <img src="media/icons/traefik.logo-dark.png" width="50" height="auto"/>
  <img src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/mosquitto.png" width="50" height="auto"/>
  <img src="https://skillicons.dev/icons?i=python" />
</p>

### Firmware (ESP32, C++, ESP-IDF)
To ensure low-cost connectivity and excellent control of devices, I used the ESP32 along with the ESP-IDF framework, providing more precise and optimized control over the device.

<p align="left">
  <img src="media/icons/espressif_icon.png" width="50" height="auto"/>
  <img src="https://skillicons.dev/icons?i=cpp" />
</p>
