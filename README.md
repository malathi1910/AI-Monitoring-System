The system captures video from a webcam, detects faces, tracks their movement, and identifies when the face goes out of frame.

#🎯 Features
🎥 Real-time webcam video processing
🙂 Face detection using Haar Cascade
📍 Face movement tracking (dx, dy)
⚠️ Detects when face leaves the frame
🔢 Frame-by-frame video analysis
🛠️ Technologies Used
Python
OpenCV
##📦 Installation
Clone the repository:
git clone https://github.com/your-username/face-tracking-opencv.git
Navigate to project folder:
cd face-tracking-opencv
Install dependencies:
pip install opencv-python

##▶️ Usage

Run the script:

python face_tracking.py
📷 Output
Webcam window opens
Face is detected with bounding box
Movement (dx, dy) is displayed
Frame count shown
Alert appears when face is not detected
##🧠 How It Works
Captures video using webcam
Converts each frame to grayscale
Detects face using Haar Cascade classifier
Tracks face center position
Calculates movement between frames
Displays results in real-time
##🚀 Future Improvements
Multi-face tracking
Face recognition
Emotion detection
Integration with AI models (MediaPipe / YOLO)
##📌 Applications
Security systems
Attendance monitoring
Human-computer interaction
Surveillance systems
