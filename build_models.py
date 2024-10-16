from model import Model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BOX_DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "Doorbell Camera Alert.v4i.yolov11",
    "data.yaml"
)

if __name__ == "__main__":
    # build and save box detection model
    box_model = Model(BOX_DATA_PATH)
    box_model.train()
    box_model.save(os.path.join(BASE_DIR, "models", "box_model.pt"))
    box_model.evaluate()
