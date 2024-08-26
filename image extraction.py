import cv2
import os
from tkinter import Tk, filedialog
 
#Read the video from specified path
root = Tk()
root.withdraw()
 
sourcePath = filedialog.askopenfilename(title="Select the video file")
destinyPath = filedialog.askdirectory(title="Select the folder where you want to save the images")
 
source = cv2.VideoCapture(sourcePath)
 
#Get the frame rate of the video
fps = source.get(cv2.CAP_PROP_FPS)
 
#Calculate the time in seconds where you want to start frame extraction
desired_start_time = float(input("Enter the desired start time in seconds: "))
 
#Calculate the corresponding frame number
start_frame = int(desired_start_time * fps)
 
#Set the current frame to the calculated start frame
currentframe = start_frame
 
#Set the desired capture rate in frames per second
capture_rate_fps = int(input("Enter the desired capture rate in fps (0-" + str(int(fps)) + "): "))
 
#Calculate the number of frames to skip between captures
frames_to_skip = round(fps / capture_rate_fps)
 
#Skip frames until the desired start frame is reached
while currentframe > 0:
    ret, frame = source.read()
    currentframe -= 1
 
while True:
    #Read the next frame
    ret, frame = source.read()
 
    if ret:
        #If video is still left, continue creating images
        if currentframe % frames_to_skip == 0:
            name = destinyPath + '/frame' + str(currentframe) + '.png'
            print('Creating...' + name)
 
            #Write the extracted images
            cv2.imwrite(name, frame)
 
        #Increase the counter to show how many frames are created
        currentframe += 1
    else:
        break
 
#Release all space and windows once done
source.release()
cv2.destroyAllWindows()