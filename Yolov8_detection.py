from ultralytics import YOLO
import cv2

# Load YOLOv8 model (pre-trained)
model = YOLO("yolov8n.pt")   # lightweight model

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    # Get annotated frame
    annotated_frame = results[0].plot()

    # Count people
    person_count = 0

    for box in results[0].boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        if label == "person":
            person_count += 1

    # Display count
    cv2.putText(annotated_frame, f"People Count: {person_count}",
                (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
