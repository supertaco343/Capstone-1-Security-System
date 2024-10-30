#this one is used in creating a blank config file for the user/system to use
#current cam id: 0c45:6366, current supported types: MJPG 1920x1080 at 30-5, 1280x720 at 30-5, 

def vidconfiginit():
    with open("vidconfig.txt", "w") as file:
        file.write("NumberofCameras: 0\nCam0ID: 0000:0000\nTempPath: ./\nTempType: mp4v\nResolution: 0x0\nFrameRate: 15\nTimeLimit: 10\n")
        
        
        
        #NOTE: this is a template for the config file, please add/change the items here or in the GUI
    
