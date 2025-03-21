# Distributed Image Filtering with Docker & NGINX

This project implements a distributed image processing system using multiple Docker containers for different image filters and NGINX as a load balancer.

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
  - Fourier Transform
  - Sepia Tone
  - Cartoon Effect
  - Oil Painting Effect
- Load-balanced using **NGINX**.
- Microservices architecture with **Flask**.
