# 🌿 IoT Greenhouse - 🏗 Work in Progress
This project was created with the goal of exploring and implementing the key components of an IoT system, using a greenhouse monitoring scenario. 
It offers real-time device monitoring through a web dashboard, as well as access to historical data.

## Stack and Technologies
The system covers communication between devices, data processing and storage, a real-time management interface, infrastructure setup for deployment, and the firmware required for the devices.

### Back-end (Node.js, TypeScript, NestJS, Redis, MQTT, WebSocket, Prisma, PostgreSQL)
For the back-end, I developed two services using Node.js and TypeScript — one structured with NestJS, and the other implemented with a custom setup without a framework. 
This approach ensures scalability, performance, and flexibility according to each service's needs.
The architecture consists of:

- device_service: Receives data from devices via MQTT and stores it in a PostgreSQL database. It also streams real-time device data to clients via WebSocket.
- api_service: Handles data queries and user authentication.

Session management is handled using Redis, and login/authentication data is stored in PostgreSQL.

<img src="https://skillicons.dev/icons?i=nodejs,ts,nestjs,redis,prisma,postgres" />

### Front-end (Next.js, TypeScript, Shadcn/ui, Tailwind)
For resource-constrained devices, server-side rendering (SSR) can enhance the user experience. To achieve this, I used Next.js, Tailwind, and Shadcn/ui as the component library.

<p align="left">
  <img src="https://skillicons.dev/icons?i=nextjs,typescript,tailwind" />
  <img src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/shadcn_ui.png" width="50" height="auto"/>
</p>

### Infrastructure (Docker Compose, Nginx, Eclipse Mosquitto, Python, Turborepo)
All services are containerized using Docker, with orchestration handled via Docker Compose. Nginx is used as a reverse proxy, while Eclipse Mosquitto acts as the MQTT broker. Python is utilized for automation scripts and auxiliary tasks. 
Additionally, Turborepo is employed to manage the monorepo structure, enhancing code organization and improving build performance across the project.

<p align="left">
  <img src="https://skillicons.dev/icons?i=docker,nginx" /> 
  <img src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/mosquitto.png" width="50" height="auto"/>
  <img src="https://skillicons.dev/icons?i=python" />
  <img src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/turborepo.png" width="50" height="auto"/>
</p>

### Firmware (ESP32, C++, ESP-IDF)
To ensure low-cost connectivity and excellent control of devices, I used the ESP32 along with the ESP-IDF framework, providing more precise and optimized control over the device.

<p align="left">
  <img src="media/icons/espressif_icon.png" width="50" height="auto"/>
  <img src="https://skillicons.dev/icons?i=cpp" />
</p>
