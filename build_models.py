from model import Model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BOX_DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "Packages.v6-raw.yolov11",
    "data.yaml"
)

if __name__ == "__main__":
    # build and train model
    box_model = Model(BOX_DATA_PATH, model_name="yolo11n.pt")
    box_model.train(epochs=100)

    # save model
    if not os.path.exists(os.path.join(BASE_DIR, "models")):
        os.makedirs(os.path.join(BASE_DIR, "models"))
    box_model.save(os.path.join(BASE_DIR, "models", "package.pt"))
