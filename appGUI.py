import sys
import os
import threading
import subprocess
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox, QLineEdit, QFormLayout

# This line is to ensure the platform is set to X11
# (App was running fine, PC got restarted, then I would get a Wayland error, this fixes it)
os.environ['QT_QPA_PLATFORM'] = 'xcb'

################################################################################################
##                            START FLASK IN SUBPROCESS                                       ##
################################################################################################

def run_flask_app():
# Set the FLASK_APP environment variable to run.py

    ##### THIS LINE MAY NEED TO BE CHANGED. SET THE LOCATION OF THE FOLDER run.py IS IN #####
    os.chdir('/home/test/Desktop/Capstone-1-Security-System-Project-main') # Have to do this because run.py isn't in root directory
    os.environ['FLASK_APP'] = 'run'
    
    # Run Flask with 'python -m flask run'
    process = subprocess.Popen(
        [sys.executable, "-m", "flask", "run", "--host=127.0.0.1", "--port=5000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("Error starting Flask app:", stderr.decode())
    else:
        print("Flask app started successfully")

# Define the main window class for the PyQt5 application
class TheGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Watchers GUI')
        self.setGeometry(100, 100, 700, 650)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        label = QLabel('Test Label')
        layout.addWidget(label)
        
        ###################################################################################
        ##                            INPUT FIELDS                                       ##
        ###################################################################################

        # Create input fields for camera ID, name, and location
        self.camera_id_input = QLineEdit()
        self.camera_name_input = QLineEdit()
        self.camera_location_input = QLineEdit()
        
        # Set placeholder text to guide the user
        self.camera_id_input.setPlaceholderText("Enter Camera ID")
        self.camera_name_input.setPlaceholderText("Enter Camera Name")
        self.camera_location_input.setPlaceholderText("Enter Camera Location")

        # Add input fields to the layout
        layout.addWidget(QLabel("Camera ID:"))
        layout.addWidget(self.camera_id_input)
        layout.addWidget(QLabel("Camera Name:"))
        layout.addWidget(self.camera_name_input)
        layout.addWidget(QLabel("Camera Location:"))
        layout.addWidget(self.camera_location_input)

        ###################################################################################
        ##                            BUTTONS                                            ##
        ###################################################################################

        add_camera_btn = QPushButton("Add Camera")
        add_camera_btn.clicked.connect(self.add_camera)
        layout.addWidget(add_camera_btn)
        
        get_cameras_btn = QPushButton("Get Cameras")
        get_cameras_btn.clicked.connect(self.get_cameras)
        layout.addWidget(get_cameras_btn)

        central_widget.setLayout(layout)

    #######################################################################################
    ##                               METHODS                                             ##
    #######################################################################################

    # Method to add a camera
    def add_camera(self):
        # Retrieve values from the input fields
        camera_id = self.camera_id_input.text()
        camera_name = self.camera_name_input.text()
        camera_location = self.camera_location_input.text()

        if not camera_id or not camera_name or not camera_location:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields before adding a camera.")
            return

        try:
            # Send a POST request with user-provided data to the /camera route of the Flask server
            response = requests.post("http://127.0.0.1:5000/camera", json={
                "id": camera_id,
                "name": camera_name,
                "location": camera_location
            })
            QMessageBox.information(self, "Camera Added", response.json().get("message"))
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to connect to Flask server: {e}")

    # Method to get cameras
    def get_cameras(self):
        try:
            # Send a GET request for the list of cameras
            response = requests.get("http://127.0.0.1:5000/camera")
            cameras = response.json()  # Assuming the response is a list of cameras
            if cameras:
                cameras_list = "\n".join([f"ID: {camera['id']}, Name: {camera['name']}, Location: {camera['location']}" for camera in cameras])
                QMessageBox.information(self, "List of Cameras", cameras_list)
            else:
                QMessageBox.information(self, "List of Cameras", "No cameras available")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to connect to Flask server: {e}")

# Entry point for the application
if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask_app, daemon=True)
    flask_thread.start()  # Start the Flask server thread

    app = QApplication(sys.argv)
    window = TheGUI()
    window.show()
    sys.exit(app.exec_())

