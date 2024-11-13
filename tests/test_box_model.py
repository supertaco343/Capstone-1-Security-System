import sys
import os

# Add the parent directory to the path so that we can import the model module
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from model import Model

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "package.pt")
IMG_PATH = os.path.join(BASE_DIR, "images", "test.jpg")

box_model = Model(None, MODEL_PATH)

box_model.predict(IMG_PATH)

for result in box_model.results:
    result.show()