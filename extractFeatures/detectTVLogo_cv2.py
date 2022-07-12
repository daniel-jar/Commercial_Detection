import pyautogui
import pygetwindow
import re #get numbers from string
import PIL #save images
from PIL import ImageGrab, Image
import time
import cv2 as cv
import numpy as np


import winsound
import os

#define Variables
PREFFERED_WINDOW_SIZE_OF_TV_APPLICATION=(1301,849)
TV_APPLICATION_NAME = "Hauppauge WinTV"
COUNT_OF_ITERATIONS = 0

#Debugging to check if the correct region is searched for
FOUND_LOGO_LOCATION=r"screenshots\foundLogo.png"
SEARCHED_LOGO_LOCATION=r"screenshots\searchLogo.png"

#searchingForLogo
PICTURE_TV_LOGO = cv.imread("locators\pro7.png",cv.IMREAD_GRAYSCALE)
PICTURE_TV_LOGO_SMALL = cv.imread("locators\pro7_small.png",cv.IMREAD_GRAYSCALE)

#logovariables #old margins
# EXPECTED_MARGIN_X = 167
# EXPECTED_MARGIN_Y = 133
# SIZE_OF_EXPECTED_LOGO = 55

# width: 1301
# height: 849
# (1396, 158, 55, 55)
#EDGES WITH Border
EXPECTED_MARGIN_X = 160
EXPECTED_MARGIN_Y = 70
SIZE_OF_EXPECTED_LOGO = 48

#BORDEREDGES for Picture without Appplication Borders
LEFT_BORDER_MARGIN = 9
TOP_BORDER_MARGIN = 33
RIGHT_BORDER_MARGIN = 10
BOTTOM_BORDER_MARGIN = 89

#indicate if logo found
LOGO_GEFUNDEN = 0

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
searchLogoX2 = SIZE_OF_EXPECTED_LOGO+searchLogoX1
searchLogoY2 = SIZE_OF_EXPECTED_LOGO+searchLogoY1

#for PIL ImageGrab
regionExpectedLogo=(searchLogoX1,searchLogoY1,searchLogoX2,searchLogoY2)
print("EXPECTED REGION OF LOGO: " + str(regionExpectedLogo))





while 1:
    time.sleep(1)
    print("NEW DATAPOINT")
    COUNT_OF_ITERATIONS += 1
    imageApplicationVideoStream = ImageGrab.grab(bbox=regionTVApplication)
    imageExpectedLogo = imageApplicationVideoStream.crop((regionExpectedLogo))
    imageExpectedLogoSmall = imageExpectedLogo.crop((2,2,42,42))

    imageExpectedLogoSmall.save(SEARCHED_LOGO_LOCATION)

    imageExpectedLogoAsNumpy = cv.cvtColor(np.array(imageExpectedLogo), cv.COLOR_RGB2GRAY)
    imageExpectedLogoAsNumpySmall = cv.cvtColor(np.array(imageExpectedLogoSmall), cv.COLOR_RGB2GRAY)
    #im1=pyautogui.screenshot(region=regionExpectedLogo)
    #im1.save(SEARCHED_LOGO_LOCATION)
            
    resTM_SQDIFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_SQDIFF_NORMED) #<0.4 quite represantive
    resTM_CCOEFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_CCOEFF_NORMED) #>0.3 quite represantative
    #resTM_CCOEFF = cv.matchTemplate(img_cv, PICTURE_TV_LOGO, cv.TM_CCOEFF) #1000000 quite represamtative
    #resTM_CCORR  = cv.matchTemplate(img_cv, PICTURE_TV_LOGO, cv.TM_CCORR) #not represantative usable
    #resTM_CCORR_NORMED = cv.matchTemplate(img_cv, PICTURE_TV_LOGO, cv.TM_CCORR_NORMED) #not represantative usable 
    #resTM_SQDIFF = cv.matchTemplate(img_cv, PICTURE_TV_LOGO, cv.TM_SQDIFF) #not represantative usable


    print(resTM_SQDIFF_NORMED)
    print(resTM_SQDIFF_NORMED_SMALL)

    print(resTM_CCOEFF_NORMED)
    print(resTM_CCOEFF_NORMED_SMALL)
  

    logoIndicationBooleanSQDIFF = resTM_SQDIFF_NORMED<=0.4 or resTM_SQDIFF_NORMED_SMALL <=0.4
    logoIndicationBooleanCCOEFF = resTM_CCOEFF_NORMED>=0.3 or resTM_SQDIFF_NORMED_SMALL >=0.3

    print(str(resTM_SQDIFF_NORMED)+" "+str(logoIndicationBooleanSQDIFF))
    print(str(resTM_CCOEFF_NORMED)+" "+str(logoIndicationBooleanCCOEFF))
    # cv.TM_CCOEFF_NORMED actually seems to be the most relevant method
    # for method in methods:
    #     print(method)
    #     res = cv.matchTemplate(img_cv, PICTURE_TV_LOGO, method)
    #     print(res)

    # print(res)
    #location=pyautogui.locateOnScreen(PICTURE_TV_LOGO,grayscale=True,confidence=0.7, region=(topLeftX,topLeftY, bottomRightX, bottomRightY))
    #location=pyautogui.locateOnScreen(PICTURE_TV_LOGO,grayscale=True,confidence=0.3, region=(1223,115, 55, 55))
    #location=pyautogui.locateOnScreen(PICTURE_TV_LOGO,grayscale=True,confidence=0.3, region=regionExpectedLogo)
    #print(location)

    #foundBox
    if logoIndicationBooleanSQDIFF and logoIndicationBooleanCCOEFF and LOGO_GEFUNDEN==0 :
        #TV Logo Found => We expect a normal TV Show
        LOGO_GEFUNDEN = 1
        #os.system("start sounds/programm.mp3")
        #im1=pyautogui.screenshot(region=(location[0],location[1], location[2], location[3]))
        #im1.save(FOUND_LOGO_LOCATION)
    elif not logoIndicationBooleanSQDIFF and not logoIndicationBooleanCCOEFF and LOGO_GEFUNDEN==1:
        #TV Logo not Found => We expect Commercial
        #os.system("start sounds/werbung.mp3")
        LOGO_GEFUNDEN = 0
    elif logoIndicationBooleanSQDIFF != logoIndicationBooleanCCOEFF:
        print("Nicht Sicher")
        #os.system("start sounds/algo.mp3")

    if LOGO_GEFUNDEN:
        print(f"Programm! - Datapoint: {COUNT_OF_ITERATIONS}")
    else:
        print(f"Werbung! - Datapoint: {COUNT_OF_ITERATIONS}")


    