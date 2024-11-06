import cv2 #used to use the camera(s)

def CameraRecord(CamID, TempPath, TempType, Resolution, FrameRate, TimeLimit):
    CamID = 0 #HARDCODED BECAUSE CV2 DOESNT LIKE DEVICE ID, WILL BE FIXED LATER ON
    
    cv2.namedWindow("Test")
    cam = cv2.VideoCapture(CamID)

    Res = [Resolution.split("x")[0], Resolution.split("x")[1]]
    print(Res[0], Res[1])
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(frame_width, frame_height)
    
    # Define the codec and create VideoWriter object
    print(TempType[0], TempType[1], TempType[2], TempType[3])
    fourcc = cv2.VideoWriter_fourcc(TempType[0], TempType[1], TempType[2], TempType[3])
    #out = cv2.VideoWriter('output.mp4', fourcc, int(FrameRate), (int(Res[0]), int(Res[1])))
    out = cv2.VideoWriter('output.mp4', fourcc, 5, (640, 480))
    
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    
    print(rval)
    
    while rval:
        print("here")
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
