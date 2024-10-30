#used for reading the config files, will have separate functions for each module/case
import configcreator as CC

def vidconfig():

    try:
        with open("vidconfig.txt", "r") as file:
            config = file.read
            #need to parse and 
            print(config) #does not work lol
    except IOError:
        CC.vidconfiginit()
        print("Initial Configuration file has been created, please go and change the parameters to fit the current configuration you wish to use.")
    
    
vidconfig()
    
