import os
import cv2
import time
from datetime import datetime, timedelta
from app.alert import send_email
from app.models import Recording, db
from app import app

SAVE_DIR = "detections"

os.makedirs(SAVE_DIR, exist_ok=True)

def can_send_alert(last_alert_time, cooldown_hours=12):
    if last_alert_time is None:
        return True
    return datetime.now() - last_alert_time > timedelta(hours=cooldown_hours)

def save_frame(frame):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    frame_path = os.path.join(SAVE_DIR, f"detection_{timestamp}.jpg")
    cv2.imwrite(frame_path, frame)
    return frame_path

def detect_package(model, camera_id, alert_email):
    with app.app_context():
        cap = cv2.VideoCapture(camera_id)
        last_alert_time = None

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        print("Starting package detection. Press Ctrl+C to stop.")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)

            for box in results[0].boxes:
                label = int(box.cls[0])  
                conf = box.conf[0]

                if label == 0 and conf >= 0.25:  
                    print(f"Package detected with confidence {conf:.2f}")
                    
                    # Save the frame
                    frame_path = save_frame(frame)

                    # Add the frame to the database
                    recording = Recording(camera_id=camera_id, timestamp=datetime.now(), file_path=frame_path)
                    db.session.add(recording)
                    db.session.commit()

                    # Check if it's time to send an alert
                    if can_send_alert(last_alert_time):
                        send_email(alert_email, "Delivery Alert", "You have a delivery waiting for you")
                        save_frame
                        last_alert_time = datetime.now()
                    
                    # Stop processing other boxes if a package is detected
                    break

            time.sleep(1)  # sample every second

        cap.release()
        print("Package detection stopped.")
