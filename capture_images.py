import cv2
import os

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def capture_images(user_id, user_name, num_samples=50):
    if not os.path.exists("dataset"):
        os.makedirs("dataset")
    
    cap = cv2.VideoCapture(1)
    sample_num = 0
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            sample_num += 1
            cv2.imwrite(f"dataset/User.{user_id}.{user_name}.{sample_num}.jpg", gray[y:y+h, x:x+w])
            cv2.waitKey(100)
        cv2.imshow('Capture Images', frame)
        cv2.waitKey(1)
        if sample_num >= num_samples:
            break
    cap.release()
    cv2.destroyAllWindows()