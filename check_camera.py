def camer():
    import cv2


    cascade_face = cv2.CascadeClassifier('haarcascade_default.xml')


    cap = cv2.VideoCapture(1)

    while True:

        _, img = cap.read()


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        faces = cascade_face.detectMultiScale(gray, 1.3, 5, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)


        for (a, b, c, d) in faces:
            cv2.rectangle(img, (a, b), (a + c, b + d), (10,159,255), 2)



        cv2.imshow('Webcam Check', img)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
