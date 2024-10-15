from models.box_model import Model

if __name__ == "__main__":
    model = Model()
    model.train()
    model.evaluate()
    model.model.save("doorbell_model.pt")
