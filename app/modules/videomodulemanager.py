import videomodule as VM
import configreader as CR
import threading as T

#defining the thread class
class CameraThread(T.Thread):
    def __init__(self, CamID, TempPath, TempType, Resolution, FrameRate, TimeLimit):
        T.Thread.__init__(self)
        self.CamID = CamID
        self.TempPath = TempPath
        self.TempType = TempType
        self.Resolution = Resolution
        self.FrameRate = FrameRate
        self.TimeLimit = TimeLimit
        
    def run(self):
        print ("Starting Camera with ID: ", self.CamID)
        VM.CameraRecord(self.CamID, self.TempPath, self.TempType, self.Resolution, self.FrameRate, self.TimeLimit)

#first need to grab config file stuff
def vidmodman():
    NumofCameras, CameraSettings = CR.vidconfig()
    print(len(CameraSettings))
    if len(CameraSettings) == 0:
        print("ERROR, SETTINGS WERE NOT GRABBED PROPERLY/AT ALL.")
        return 1
    elif len(CameraSettings) == 1:
        print(CameraSettings[0])
        return 1
    elif len(CameraSettings)%6 != 0:
        print("ERROR, NUMBER OF SETTINGS IS INCORRECT, CHECK CONFIG")
        return 1
    
    thread = CameraThread(CameraSettings[0], CameraSettings[1], CameraSettings[2], CameraSettings[3], CameraSettings[4], CameraSettings[5])
    thread.start()
    #from config, setup each camera and link it properly/spawn a thread for it, find any that are not working/gone, and report to user if there is an issue
    #NOTE: the threading part of this is partially taken (and changed to fit) from: https://stackoverflow.com/questions/29664399/capturing-video-from-two-cameras-in-opencv-at-once
    

vidmodman()
