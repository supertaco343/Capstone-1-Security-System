from app import app, db
from app.models import Camera, Recording
from flask import request, jsonify, Response
import cv2
from app.detect import detect_package
import threading
from ultralytics import YOLO

def generate_feed(camera_id):
    cap = cv2.VideoCapture(camera_id)

    if not cap.isOpened():
        raise RuntimeError("Could not start camera.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Encode the frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

    cap.release()

# define the route for the root of the site
@app.route("/")
def index():
    return "Hello, World!"

# define the route for adding a new camera
@app.route("/camera", methods=["POST"])
def add_camera():
    # get the data from the request
    data = request.get_json()
    
    # create a new camera object
    camera = Camera(id=data["id"], name=data["name"], location=data["location"])
    
    # add the camera to the database
    db.session.add(camera)
    db.session.commit()
    
    return jsonify({"message": "Camera added successfully"})

# define the route for getting all cameras
@app.route("/camera", methods=["GET"])
def get_cameras():
    # get all the cameras from the database
    cameras = Camera.query.all()
    
    # create a list of cameras
    camera_list = []
    for camera in cameras:
        camera_list.append({"id": camera.id, "name": camera.name, "location": camera.location})
    
    return jsonify(camera_list)

# define the route for deleting a camera
@app.route("/camera/<int:id>", methods=["DELETE"])
def delete_camera(id):
    # get the camera from the database
    camera = Camera.query.get(id)
    
    # delete the camera from the database
    db.session.delete(camera)
    db.session.commit()
    
    return jsonify({"message": "Camera deleted successfully"})

# TODO: add a way to view all recordings for a camera
# define the route for getting all recordings for a camera
@app.route("/recording/<int:camera_id>", methods=["GET"])
def get_recordings(camera_id):
    # get all the recordings for the camera from the database
    recordings = Recording.query.filter_by(camera_id=camera_id).all()
    
    # create a list of recordings
    recording_list = []
    for recording in recordings:
        recording_list.append({"id": recording.id, "camera_id": recording.camera_id, "timestamp": recording.timestamp, "file_path": recording.file_path})
    
    return jsonify(recording_list)

# define the route for viewing a camera
@app.route('/live_feed/<camera_id>')
def live_feed(camera_id):
    return Response(generate_feed(int(camera_id)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# define the route for starting detection
@app.route('/detect')
def detect():
    cameras = Camera.query.all()
    model = YOLO("models/package.pt")
    for camera in cameras:
        thread = threading.Thread(target=detect_package, args=(model, int(camera.id), app.config["MAIL_USERNAME"]))
        thread.start()
    return jsonify({"message": "Detection started for all cameras"})

