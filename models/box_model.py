from ultralytics import YOLO
import os

# absolute path to data directory used to avoid path issues
ABS_DATA_PATH = os.getcwd() + "/datasets/Doorbell Camera Alert.v4i.yolov11/data.yaml"

class Model:
    def __init__(self, model_name="yolo11n.yaml"):
        self.model = YOLO(model_name)

    def train(self, epochs=10):
        self.results = self.model.train(data=ABS_DATA_PATH, epochs=epochs)

    def evaluate(self):
        self.results = self.model.evaluate(data=ABS_DATA_PATH)

    def predict(self, image_path):
        self.results = self.model(image_path)

# TODO: Train and save the model so it can be loaded for use in our application
