from app import app, db
from app.models import Camera, Recording
from flask import request, jsonify

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
