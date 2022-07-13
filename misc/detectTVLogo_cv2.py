from pickle import NONE
import pyautogui
import pygetwindow
import re #get numbers from string
import PIL #save images
from PIL import ImageGrab, Image
import time
import cv2 as cv
import numpy as np
import motionVectorLength_MVL as mvl
import edgeChangeRatio_ECR as ECR
from csv import writer
import winsound
import os
from os.path import exists

#define Variables
PREFFERED_WINDOW_SIZE_OF_TV_APPLICATION=(1301,849)
TV_APPLICATION_NAME = "Hauppauge WinTV"
COUNT_OF_ITERATIONS = 0
CONSECUTIVE_FRAMES_FOR_SWITCHING = 25
CONSECUTIVE_COUNTER = 0
CONSECUTIVE_FRAME_COOLDOWN = 0
CONSECUTIVE_COOLDOWN_COUNTER = 0

#Debugging to check if the correct region is searched for
FOUND_LOGO_LOCATION=r"screenshots\foundLogo.png"
SEARCHED_LOGO_LOCATION=r"screenshots\searchLogo.png"

#searchingForLogo
PICTURE_TV_LOGO = cv.imread("locators\pro7.png",cv.IMREAD_GRAYSCALE)
PICTURE_TV_LOGO_SMALL = cv.imread("locators\pro7_small.png",cv.IMREAD_GRAYSCALE)

#EDGES WITH Border
EXPECTED_MARGIN_X = 160
EXPECTED_MARGIN_Y = 70
SIZE_OF_EXPECTED_LOGO_X = 48
SIZE_OF_EXPECTED_LOGO_Y = 144

#BORDEREDGES for Picture without Appplication Borders
LEFT_BORDER_MARGIN = 9
TOP_BORDER_MARGIN = 33
RIGHT_BORDER_MARGIN = 10
BOTTOM_BORDER_MARGIN = 89

#indicate if logo found
LOGO_GEFUNDEN = 0

#prevFrame for Visuelle Merkmale
PREV_FRAME = NONE
ECR_RATIO = 0
MVL_VALUES = []

#Get Window Handle of TV App and Resize
windowHandle = pyautogui.getWindowsWithTitle(TV_APPLICATION_NAME)[0]
windowHandle.size = PREFFERED_WINDOW_SIZE_OF_TV_APPLICATION


#Get Relative Window Position
handleVariables=str(windowHandle).split(",")
topLeftX=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[0].split(" ")[1]))))
print("\ntopleftX of tv application:: "+str(topLeftX))
topLeftY=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[1]))))
print("topleftY of tv application:: "+str(topLeftY))
width=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[2]))))
print("width of tv application: "+str(width))
height=int(''.join(str(x) for x in re.findall('[0-9]+', str(handleVariables[3]))))
print("height of tv application: "+str(height))

print("\ncalculating offset for region of video stream without borders")
edgeTVAppX=topLeftX+LEFT_BORDER_MARGIN
edgeTVAppY=topLeftY+TOP_BORDER_MARGIN
edgeTVAPPwidth=topLeftX+width-RIGHT_BORDER_MARGIN
edgeTVAPPheight=topLeftY+height-BOTTOM_BORDER_MARGIN

#fullscreenshot
regionTVApplication=(edgeTVAppX,edgeTVAppY,edgeTVAPPwidth,edgeTVAPPheight)

#regionTVApplication=(topLeftX+9,topLeftY+33,topLeftX+width-10,topLeftY+height-89)
print("EXPECTED REGION OF TV APP: " + str(regionTVApplication))

#Calculate Region of proposed Logo
print("\ncalculating offset for region of tv logo")
searchLogoX1 = width-EXPECTED_MARGIN_X-LEFT_BORDER_MARGIN
searchLogoY1 = EXPECTED_MARGIN_Y-TOP_BORDER_MARGIN
searchLogoX2 = SIZE_OF_EXPECTED_LOGO_X+searchLogoX1
searchLogoY2 = SIZE_OF_EXPECTED_LOGO_Y+searchLogoY1

#for PIL ImageGrab
regionExpectedLogo=(searchLogoX1,searchLogoY1,searchLogoX2,searchLogoY2)
print("EXPECTED REGION OF LOGO: " + str(regionExpectedLogo))

file_exists = exists("logoDetection.csv")

with open('logoDetection.csv', 'a', newline='') as f_object: 
    writer_object = writer(f_object)
    if not file_exists:
        list_data=["COUNT_OF_ITERATIONS","logoIndicationBooleanSQDIFF","resTM_SQDIFF_NORMED.max()","logoIndicationBooleanCCOEFF","resTM_CCOEFF_NORMED.max()","ECR_RATIO","MVL_VALUES[0]","MVL_VALUES[1]","LABEL"]
        writer_object.writerow(list_data) 
    while 1:
        time.sleep(1)
        COUNT_OF_ITERATIONS += 1
            
        imageApplicationVideoStream = ImageGrab.grab(bbox=regionTVApplication)
        if PREV_FRAME != NONE:
            MVL_VALUES = mvl.lucas_kanade_method_mvl(np.array(imageApplicationVideoStream),np.array(PREV_FRAME),cv,np)
            ECR_RATIO = ECR.ECR(np.array(imageApplicationVideoStream), np.array(PREV_FRAME), edgeTVAPPwidth, edgeTVAPPheight, crop=False, dilate_rate = 5)
            
            print("ecr ratio: "+str(ECR_RATIO))
            print("mvl sum: "+str(MVL_VALUES[0]))
            print("absolute: "+str(MVL_VALUES[1]))

        else:
            print("No Previous Frame Detected")

        PREV_FRAME = imageApplicationVideoStream
        if CONSECUTIVE_COOLDOWN_COUNTER==0:
            imageExpectedLogo = imageApplicationVideoStream.crop((regionExpectedLogo))
            imageExpectedLogoAsNumpy = cv.cvtColor(np.array(imageExpectedLogo), cv.COLOR_RGB2GRAY)

            resTM_SQDIFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_SQDIFF_NORMED) #<0.4 quite represantive
            resTM_CCOEFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_CCOEFF_NORMED) #>0.3 quite represantative

            logoIndicationBooleanSQDIFF = (resTM_SQDIFF_NORMED<=0.4).any() or (resTM_CCOEFF_NORMED>=0.9).any()
            logoIndicationBooleanCCOEFF = (resTM_CCOEFF_NORMED>=0.3).any() or (resTM_SQDIFF_NORMED<=0.05).any()

            print(str(resTM_SQDIFF_NORMED.max())+" "+str(logoIndicationBooleanSQDIFF   ))
            print(str(resTM_CCOEFF_NORMED.max())+" "+str(logoIndicationBooleanCCOEFF))

    
            if logoIndicationBooleanSQDIFF and logoIndicationBooleanCCOEFF and LOGO_GEFUNDEN==0:
                CONSECUTIVE_COUNTER+=1
                if CONSECUTIVE_COUNTER>=CONSECUTIVE_FRAMES_FOR_SWITCHING:
                    LOGO_GEFUNDEN = 1
                    CONSECUTIVE_COUNTER = 0
                    CONSECUTIVE_COOLDOWN_COUNTER = CONSECUTIVE_FRAME_COOLDOWN
                    #os.system("start sounds/programm.mp3")
                    imageExpectedLogo.save("screenshots/foundLogo"+str(COUNT_OF_ITERATIONS)+".png")
                    list_data=[COUNT_OF_ITERATIONS,logoIndicationBooleanSQDIFF,resTM_SQDIFF_NORMED.max(),logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED.max(),ECR_RATIO,MVL_VALUES[0],MVL_VALUES[1],"PROGRAMM"]
                    writer_object.writerow(list_data)  
        
            elif not logoIndicationBooleanSQDIFF and not logoIndicationBooleanCCOEFF and LOGO_GEFUNDEN==1:
                CONSECUTIVE_COUNTER+=1
                if CONSECUTIVE_COUNTER>=CONSECUTIVE_FRAMES_FOR_SWITCHING:
                    LOGO_GEFUNDEN = 0
                    CONSECUTIVE_COUNTER = 0
                    CONSECUTIVE_COOLDOWN_COUNTER = CONSECUTIVE_FRAME_COOLDOWN
                    imageExpectedLogo.save("screenshots/foundWerbung"+str(COUNT_OF_ITERATIONS)+".png")
                    #os.system("start sounds/werbung.mp3")
                    list_data=[COUNT_OF_ITERATIONS,logoIndicationBooleanSQDIFF,resTM_SQDIFF_NORMED.max(),logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED.max(),ECR_RATIO,MVL_VALUES[0],MVL_VALUES[1],"WERBUNG"]
                    writer_object.writerow(list_data)  
            else:
                CONSECUTIVE_COUNTER=0
        else:
            CONSECUTIVE_COOLDOWN_COUNTER-=1

        if LOGO_GEFUNDEN:
            print(f"Programm! - Datapoint: {COUNT_OF_ITERATIONS}")
        else:
            print(f"Werbung! - Datapoint: {COUNT_OF_ITERATIONS}")


    f_object.close()