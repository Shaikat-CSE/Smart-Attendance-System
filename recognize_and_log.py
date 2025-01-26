import cv2
import pandas as pd
from datetime import datetime
import os

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def recognize_and_log():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    recognizer.read("trainer.yml")
    cap = cv2.VideoCapture(1)

    # Load existing attendance log or create a new one
    if os.path.exists("attendance_log.csv"):
        df = pd.read_csv("attendance_log.csv")
    else:
        df = pd.DataFrame(columns=["User ID", "Name", "Date", "Timestamp"])

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            user_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

            # Calculate percentage match (scaled for better visualization)
            scaling_factor = 1.5  # Adjust this value as needed
            percentage_match = (100 - confidence) * scaling_factor
            percentage_match = min(100, percentage_match)  # Cap at 100%

            # If percentage match is below 50%, label as Unknown
            if percentage_match < 50:
                cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            else:
                # Extract name from the dataset
                name = "Unknown"
                for root, dirs, files in os.walk("dataset"):
                    for file in files:
                        if file.startswith(f"User.{user_id}."):
                            name = file.split(".")[2]
                            break

                # Display Name, ID, and Percentage Match
                cv2.putText(frame, f"{name} (ID: {user_id}) - {percentage_match:.2f}%", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # Log attendance if not already logged for the day
                date = datetime.now().strftime("%Y-%m-%d")
                if not ((df["User ID"] == user_id) & (df["Date"] == date)).any():
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    new_entry = {"User ID": user_id, "Name": name, "Date": date, "Timestamp": timestamp}
                    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
                    df.to_csv("attendance_log.csv", index=False)
                    print(f"Attendance logged for User {user_id} ({name}) at {timestamp}")
        cv2.imshow('Attendance System', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()