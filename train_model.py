import cv2
import os
import numpy as np

def train_model():
    if not os.path.exists("dataset"):
        print("Dataset folder not found. Please capture images first.")
        return
    
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    faces, ids = [], []
    for root, dirs, files in os.walk("dataset"):
        for file in files:
            if file.endswith("jpg"):
                path = os.path.join(root, file)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                user_id = int(os.path.split(path)[-1].split(".")[1])
                faces.append(img)
                ids.append(user_id)
    recognizer.train(faces, np.array(ids))
    recognizer.save("trainer.yml")
    print("Model trained and saved.")