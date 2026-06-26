from abc import ABC, abstractmethod
import numpy as np
import cv2

try:
    from src.config import settings
except ModuleNotFoundError:
    from config import settings

Point = tuple[int, int]
FaceBox = tuple[Point, Point]

class IFaceDetector(ABC):
    """Detects faces from frames"""
    @abstractmethod
    def detect(self, frame: np.ndarray) -> list[FaceBox] | None:
        pass
    

class HaarCascadeFaceDector(IFaceDetector):
    """Uses HaarCascades to detect faces in frames"""
    
    face_cascade = cv2.CascadeClassifier(str(settings.face_cascade_path))

    def detect(self, frame: np.ndarray) -> list[FaceBox] | None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(120, 120))
        coordinates: list[FaceBox] = []

        for (x,y,w,h) in faces:
            coordinates.append(((x, y), (x + w, y + h)))

        return coordinates
