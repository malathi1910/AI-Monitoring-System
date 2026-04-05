import cv2

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Start video capture (webcam)
cap = cv2.VideoCapture(0)

# Tracking variables
prev_center = None
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1  # Frame-by-frame analysis

    # Convert to grayscale (Image Processing step)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # FACE DETECTION
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # If no face → out of frame
    if len(faces) == 0:
        cv2.putText(frame, "Face Not Detected!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        prev_center = None

    for (x, y, w, h) in faces:
        # Draw bounding box (Object Tracking visualization)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Find center point
        center = (x + w//2, y + h//2)

        # Draw center
        cv2.circle(frame, center, 5, (255, 0, 0), -1)

        # OBJECT TRACKING (movement detection)
        if prev_center is not None:
            dx = center[0] - prev_center[0]
            dy = center[1] - prev_center[1]

            movement_text = f"dx: {dx}, dy: {dy}"
            cv2.putText(frame, movement_text, (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        prev_center = center

    # FRAME-BY-FRAME ANALYSIS DISPLAY
    cv2.putText(frame, f"Frame: {frame_count}", (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Show output
    cv2.imshow("Image & Video Processing Project", frame)

    # Exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
