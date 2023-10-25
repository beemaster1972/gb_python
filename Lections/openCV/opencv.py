import cv2

capture = cv2.VideoCapture("test.mp4")
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

while True:
    success, frame = capture.read()
    if success:
        frame_for_detect = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame_for_detect)
        for (x, y, width, heigth) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + heigth), (0, 0, 255), 3)
        cv2.imshow("Kiddy", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
