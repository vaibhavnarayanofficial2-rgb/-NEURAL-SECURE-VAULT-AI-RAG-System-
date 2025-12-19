import cv2
import os

def verify_user():
    print("Checking camera... (Using Stable OpenCV Mode)")
    
    # Inbuilt XML file for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Camera nahi khul raha.")
        return False

    print("--- Camera ON! Apna face camera ke samne layein ---")

    while True:
        success, img = cap.read()
        if not success: break

        # Face detection logic
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Agar face mil jaye
        if len(faces) > 0:
            print("SUCCESS: Face Detect Ho Gaya!")
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            cv2.imshow("Security Login", img)
            cv2.waitKey(1000) # 1 sec wait
            cap.release()
            cv2.destroyAllWindows()
            return True

        cv2.imshow("Security Login", img)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()
    return False