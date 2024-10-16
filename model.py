from ultralytics import YOLO

# Base class for all ai models
# data needs to point to a data.yaml file like the one in the box dataset
class Model:
    def __init__(self, data, model_name="yolo11n.yaml"):
        self.model = YOLO(model_name)
        self.data = data

    def train(self, epochs=10):
        self.results = self.model.train(data=self.data, epochs=epochs)

    def evaluate(self):
        self.results = self.model.evaluate(data=self.data)

    def predict(self, image_path):
        self.results = self.model(image_path)

    def save(self, model_path="model.pt"):
        self.model.save(model_path)

    def load(self, model_path):
        self.model = YOLO(model_path)
