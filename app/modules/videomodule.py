import cv2 #used to use the camera(s)

def CameraRecord(CamID, TempPath, TempType, Resolution, FrameRate, TimeLimit):
    CamID = 2 #HARDCODED BECAUSE CV2 DOESNT LIKE DEVICE ID, WILL BE FIXED LATER ON
    
    cv2.namedWindow("Test")
    cam = cv2.VideoCapture(CamID)
    
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(TempType[0], TempType[1], TempType[2], TempType[3]))
    cam.set(cv2.CAP_PROP_FPS, int(FrameRate))
    Res = (int(Resolution.split("x")[0]), int(Resolution.split("x")[1]))
    print(Res[0], Res[1])
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, Res[0])
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, Res[1])
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(frame_width, frame_height) #this is to check to make sure it is the correct size (prints what is in the config, and what is currently set)
    
    # Define the codec and create VideoWriter object
    print(TempType[0], TempType[1], TempType[2], TempType[3])
    fourcc = cv2.VideoWriter_fourcc(TempType[0], TempType[1], TempType[2], TempType[3])
    out = cv2.VideoWriter('output.mjpg', fourcc, int(FrameRate), (Res[0], Res[1]))
    
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    
    print(rval)
    
    while rval:
        #print("here")
        rval, frame = cam.read()

        # Write the frame to the output file
        out.write(frame)

        # Display the captured frame
        cv2.imshow("Test", frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break
    
    # Release the capture and writer objects
    cam.release()
    out.release()
    cv2.destroyAllWindows()
