# Capstone-1-Security-System-Project
NOTE: This project was copied to my own public repository, the only thing that has been changed from the original project is this readme file.

## Project Description
This is a fully self-hosted home/business security system that can use low cost USB webcams and an AI model to detect packages and send the user real-time alerts.  

## Features
- Real time object detection (packages only currently) using a trained AI model
- Local video storage
- Email notifications (via API)
- Web GUI for accessing video feeds

## Tech Stack
**Backend**: Python, Flask, OpenCV, SQLite
**Frontend**: HTML/CSS, Javascript
**AI Model**: Custom CNN (via Pytorch)
**Database**: SQLite
**Deployment**: Self-Hosted

## Installation and Setup
1. Clone the repo:
```
git clone https://github.com/supertaco343/Capstone-1-Security-System.git  
cd Capstone-1-Security-System
```
2. Install Dependencies:
```
pip install -r requirements.txt
```
3. Create initial configuration file:
```
cd app/modules
python3 videomodulemanager.py
```
4. Find your camera(s) info:
```
python3 teststuff.py
python3 test2.py
uvcdynctl -f
```
The first command will show all USB devices currently connected to the system at this time, and these will be displayed as "Bus #, Device #, ID #".  
The second command will show what OpenCV (one of the packages used) sees in terms of the cameras.  These are typically different from how the USB devices are listed, and it will show "Hurray, device index is #" for those that are found by OpenCV.  Typically one camera will hold 2 indexes in OpenCV, starting at 0, while the USB camera may not use the same index.  
The third command will show ALL camera formats, resolutions, and frame rate supported by that camera.  
All 3 are needed for multi camera systems, you can skip the second command if you are only using 1 camera (as you do not need to worry about which camera is which).  

5. Modify the config file:

You can open the config readme that is generated when first running the command in step 5 to learn more about the config itself (named "vidconfig_readme.txt").  
After reading it, you can change the config settings (found in "vidconfig.txt") based on the info you obtained on step 6.  The "CamID" is found in the first command of step 7, and the "Resolution" and "Framerate" are found in the third command of step 6.  If you are running multiple cameras, you must put the config data in order in which the cameras show up to OpenCV, and this is found in the second command of step 6.

6. Testing the camera setup (optional):

After saving the config changes, you can run the second command in step 5 to open up the camera feed(s) you have entered into the config file.  Please adjust config settings if there are issues (the config is very case and space sensitive, so that might be the first thing to check before further investigation).  You can exit the video feed once you have confirmed the cameras are working.  

7. Running the program:

After setting the cameras up, you can go back to the root directory of the project and run the program
```
cd ..
cd ..
python3 run.py
```
Doing so will start the program and open up the Web GUI, default to "localhost:5000/camera" which can be opened in your web browser.  
