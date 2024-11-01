#used for reading the config files, will have separate functions for each module/case
import configcreator as CC

def vidconfig():
    try:
        with open("vidconfig.txt", "r") as file:
            numcams = int(file.readline().split(" ")[1])
            #print (numcams) #for testing
            
            if numcams == 0:
                print("ERROR, CONFIG FILE DOES NOT DISPLAY ANY CAMERAS, WILL NOT START VIDEO MODULE")
                return 0, ["numcams = 0"] #for videomodulemanager to catch properly
            
            else:
                settings = [] #list of the settings
                try:
                    for x in range(numcams):
                        for y in range(6): #range is the number of settings to every camera
                            settings.append(file.readline().split(" ")[1].split('\n')[0]) #pulls each line, removes the initial setting name, and removes the endline character
                            #print(x, y) #for testing
                    print(settings) #for testing
                    return numcams, settings
                    
                except IndexError: #this will catch if the config file is not formatted properly
                    print("ERROR, CONFIG FILE DOES NOT HAVE THE CORRECT NUMBER OF SETTINGS OR CAMERAS STATED.  PLEASE CHECK THE CONFIG FILE.")
                    return 0, ["index error, most likely config file is incorrect"] #for videomodulemanager to catch properly
            
    except IOError: #this will catch if the vidconfig.txt does not currently exist
        CC.vidconfiginit()
        print("Initial Configuration file has been created, please go and change the parameters to fit the current configuration you wish to use.")
        return 0, ["Config Created"]
    
    
#vidconfig()
    
