# Image Captioning 

This repository contains a FastAPI application that utilizes the VGG16 model from TensorFlow's Keras applications. The application is containerized using Docker and can be easily set up using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/AbhijithMallya/18AIP83_Project.git

cd your-repository
```

### 2. Build and Run the Docker Container

Use Docker Compose to build and start the application. This will also download the VGG16 model weights during the build process:

```sh
docker-compose up --build
```

### 3. APIs

To check if the server is running, navigate to [http://localhost:8000](http://localhost:8000) in your web browser.

### 4. To stop

Press Ctrl + C

```sh
docker-compose down 
```



