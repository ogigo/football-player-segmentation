import ultralytics
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

yolo_model = YOLO("best.pt")

def predict(image):
    history = yolo_model.predict(image)[0]
    image = history.plot()
    return image