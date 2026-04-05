# 🤖 Smart AI Monitoring System

---

## 📌 Project Overview

This project is an AI-powered monitoring system designed to demonstrate practical implementation of **Computer Vision, Object Detection, API Development, and AI-based evaluation**.  
It processes real-time data using a webcam, detects objects and faces, and provides structured outputs through APIs.

---

## 🚀 Key Features

### 👀 1. Face Detection & Tracking (OpenCV)
- Detects human faces in real-time using webcam  
- Tracks face position across frames  
- Highlights face with bounding box  
- Generates alert when face is not visible  

---

### 🤖 2. Object Detection System (YOLOv8)
- Identifies multiple objects (person, phone, etc.)  
- Performs real-time detection  
- Counts number of people in the frame  
- Displays labels with confidence scores  

---

### 🌐 3. REST API Backend (FastAPI)
- `/` endpoint → Welcome message  
- `/test` endpoint → verifies API functionality  
- `/submit` endpoint → accepts and processes JSON input  
- Returns structured JSON responses  

---

### 🧠 4. AI Evaluation Module (LLM Logic)
- Accepts user input as answer  
- Compares with predefined correct answer  
- Outputs result in structured format:
  - ✅ correct  
  - ❌ wrong  

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- FastAPI  
- Uvicorn  

---

## ▶️ How to Run the Project

```bash
pip install opencv-python ultralytics fastapi uvicorn
🔹 Step 2: Run Face Detection Module
python face_tracking.py
🔹 Step 3: Run Object Detection Module
python yolo_detection.py
🔹 Step 4: Start API Server
uvicorn main:app --reload

### 🔹 Step 1: Install Required Libraries
```bash
pip install opencv-python ultralytics fastapi uvicorn
