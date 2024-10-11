from ultralytics import YOLO
import os

class Model:
    def __init__(self, model_name='yolo11n.yaml'):
        self.model = YOLO(model_name)

    def train(self, epochs=10):
        data_path = os.getcwd() + "/../data/Doorbell Camera Alert.v4i.yolov11/data.yaml"
        self.results = self.model.train(data=data_path, epochs=epochs)

    def evaluate(self):
        data_path = os.getcwd() + "/../data/Doorbell Camera Alert.v4i.yolov11/data.yaml"
        self.results = self.model.evaluate(data=data_path)

    def predict(self, image_path):
        self.results = self.model(image_path)

# testing
model = Model()
model.train()