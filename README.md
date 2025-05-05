# Cubeium Backend

## Overview
This is the backend for Cubeium. A FastAPI-based backend application designed to handle seed data requests for the Cubeium website. This project provides an API for retrieving seed information based on user-provided seeds.

## Project Structure
```
cubeium-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py
│   ├── models/
│   │   └── biome.py
│   ├── services/
│   │   └── biome_service.py
│   └── utils/
│       └── __init__.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation
To set up the project locally, follow these steps:
1. Clone the repository:
   ```sh
   git clone https://github.com/svasim1/cubeium-backend.git
   cd cubeium-backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   uvicorn app.main:app --reload
   ```
4. Access the API at `http://localhost:8000`.   ```

## Usage
Once the application is running, you can access the API at `http://localhost:8000`. The API provides endpoints for handling seed data requests based on Minecraft seeds.