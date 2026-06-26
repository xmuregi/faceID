import cv2

try:
    from src.detection.face_detector import HaarCascadeFaceDector
except ModuleNotFoundError:
    from detection.face_detector import HaarCascadeFaceDector

def main():
    cam = cv2.VideoCapture(0)
    detector = HaarCascadeFaceDector()

    if not cam.isOpened():
        print("Error: Could not open camera.")
        return

    while(True):
        ret, frame = cam.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        faces = detector.detect(frame=frame)

        if faces:
            for face in faces:
                cv2.rectangle(frame, *face, (255, 0,0),2)

        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
