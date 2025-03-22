# Distributed Image Filtering with Docker & NGINX

This project implements a distributed image processing system using multiple Docker containers for different image filters and NGINX as a load balancer.
# Logical Structure 
![Drawing1](https://github.com/user-attachments/assets/1dd8b4f6-5117-4146-a0b6-3874a259d782)

## 🛠 Features
- Supports multiple image processing filters:
  - Grayscale
  - Gaussian Blur
  - Edge Detection
  - Histogram Equalization
  - Unsharp Masking
  - Median Filter
  - Bilateral Filter
  - Sobel Filter
  - Canny Edge Detection
  - Dilation
  - Erosion
  - Sepia Tone
  - Cartoon Effect
  - Oil Painting Effect
- Load-balanced using **NGINX**.
- Microservices architecture with **Flask**.


## Project Structure

├── docker-compose.yaml

├── nginx.conf

├── filters

│   ├── grayscale

│   │   ├── Dockerfile

│   │   └── grayscale_service.py

│   ├── gaussian_blur

│   │   ├── Dockerfile

│   │   └── gaussian_blur_service.py

│   ├── edge_detection

│   │   ├── Dockerfile

│   │   └── edge_detection_service.py




## How to install it
1. Create a Base container for the filters:
  - Create Dockerfile
    ```
    FROM python:3.8-slim
    RUN pip install flask
    ```
  - Save the file as Dockerfile.
  
  - build the Image 
  
    ```
    docker build -t generic_filter .
    ```

3. Go to the downloaded files
4. Run docker compose command:
   ```
   docker compose up --build -d
   ```
![image](https://github.com/user-attachments/assets/d36410ac-5d67-4669-90f3-633441d2da3b)
