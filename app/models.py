from app import db

class Camera(db.Model):
    __tablename__ = "camera"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Camera {self.id}>"
    

class Recording(db.Model):
    __tablename__ = "recording"
    id = db.Column(db.Integer, primary_key=True)
    camera_id = db.Column(db.String(50), db.ForeignKey("camera.id"), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    file_path = db.Column(db.String(50), nullable=False)

    def __init__(self, camera_id, timestamp, file_path):
        self.camera_id = camera_id
        self.timestamp = timestamp
        self.file_path = file_path

    def __repr__(self):
        return f"<Recording {self.id}>"
    