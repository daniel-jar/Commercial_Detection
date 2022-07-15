#visuelle merkmale
from ast import And
from logging import getLoggerClass
from pickle import NONE
from queue import Empty
from cv2 import SIFT
import pyautogui
import pygetwindow
import re #get numbers from string
import PIL #save images
from PIL import ImageGrab, Image,  ImageStat
import time
import cv2 as cv
import numpy as np
from csv import writer
import winsound
import os
from os.path import exists
from getLogoConfidence import getLogoConfidence

import motionVectorLength_MVL as mvl
import edgeChangeRatio_ECR as ECR
import farbintensität as farbchange
import SIFT_RATIO as SR
import currentDate as cd
import getLogoConfidence as LogoConfidence

#extract MFCC, RMS, ZCR
#https://stackoverflow.com/questions/70502339/how-would-i-find-the-current-decibel-level-and-set-it-as-a-variable/70514219#70514219
import pyaudio
import time
from math import log10
import audioop  
import librosa

from numpy.linalg import norm

start = time.time()

#audio merkmale
p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
decoded = []
MFCC = []
RMS = 0
DB = 0
ZCR = 0

#Application Relative Position
APPLICATION_POSITION = [0,0,0,0]

#define Variables
PREFFERED_WINDOW_SIZE_OF_TV_APPLICATION=(1301,849)
TV_APPLICATION_NAME = "Hauppauge WinTV"
COUNT_OF_ITERATIONS = 0
CONSECUTIVE_FRAMES_FOR_SWITCHING = 7
CONSECUTIVE_COUNTER = 0
CONSECUTIVE_FRAME_COOLDOWN_COUNTER = 0
CONSECUTIVE_COOLDOWN = 20

#Debugging to check if the correct region is searched for
FOUND_LOGO_LOCATION=r"screenshots\foundLogo.png"
SEARCHED_LOGO_LOCATION=r"screenshots\searchLogo.png"

#searchingForLogo
PICTURE_TV_LOGO_UPPER = cv.imread("locators\pro7.png",cv.IMREAD_GRAYSCALE)

#PICTURE_TV_LOGO_LOWER = cv.imread("locators\pro7_small.png",cv.IMREAD_GRAYSCALE)

PICTURE_TV_LOGO_NEWSTIME = cv.imread("locators\pro7_newstime.png",cv.IMREAD_GRAYSCALE)

PICTURE_TV_LOGO = PICTURE_TV_LOGO_UPPER
PICTURE_TV_LOGO_LOWER = PICTURE_TV_LOGO_UPPER


#indicate if logo found
LOGO_GEFUNDEN = 0
STATE = "WERBUNG"

#prevFrame for Visuelle Merkmale
PREV_FRAME = []
ECR_RATIO = 0
MVL_VALUES = []
FARBWECHSEL_RATIO = 0
SIFT_RATIO = 0
PYAUTOGUI_LOCATION = None
CONFIDENCE = 0.3
LIMIT_CHECK_NEW_LOGO = 50
BRIGHTNESS_EDGE = 190
BRIGHTNESS_LIMIT = 240
BRIGHTNESS_BOOLEAN= False

#REGION MAPPING
UPPER,LOWER,NEWSTIME,WIDER = 0,1,2,3
REGION_NAMES=["UPPER","LOWER","NEWSTIME","WIDER"]


#DATASet Export
FILEPATH_DATASET="dataset\logoDetection1.csv"

#Get Window Handle of TV App and Resize
windowHandle = pyautogui.getWindowsWithTitle(TV_APPLICATION_NAME)[0]
windowHandle.size = PREFFERED_WINDOW_SIZE_OF_TV_APPLICATION

#Get Relative Window Position
APPLICATION_POSITION = LogoConfidence.getRelativeWindowPosition(str(windowHandle).split(","),re)


#Calculate Offset for Video Without Borders
regionTVApplicationFullScreenshot,edgeTVAPPwidth,edgeTVAPPheight=\
LogoConfidence.getTVApplicationWithoutEdgesRegion(APPLICATION_POSITION)

#regions for opencv
regions =\
LogoConfidence.getRegions(APPLICATION_POSITION[2])
currentSelectedExpectedRegion=regions[UPPER]

#regions for pyautogui
regionsPYAUTOGUI =\
LogoConfidence.getRegionsPYAUTOGUI(APPLICATION_POSITION)
currentSelectedExpectedRegionPYAUTOGUI=regionsPYAUTOGUI[UPPER]

imageApplicationVideoStream = ImageGrab.grab(bbox=regionTVApplicationFullScreenshot)
#debug regions with CV and PYAuto
for i in range(len(regions)):
    print("Taking Screenshot for Region: "+REGION_NAMES[i])
    selectedRegion = regions[i]
    selectedRegionPYAUTOGUI = regionsPYAUTOGUI[i]
    newimg = imageApplicationVideoStream.crop((selectedRegion))
    newimg.save("debugging/region"+REGION_NAMES[i]+".png")
    im1=pyautogui.screenshot(region=selectedRegionPYAUTOGUI)
    im1.save("debugging/regionPYAUTO"+REGION_NAMES[i]+".png")

#Data will be appended into file
file_exists = exists(FILEPATH_DATASET)
with open(FILEPATH_DATASET, 'a', newline='') as f_object: 
    writer_object = writer(f_object)
    if not file_exists:
        list_data=["COUNT_OF_ITERATIONS","logoIndicationBooleanSQDIFF","resTM_SQDIFF_NORMED.max()","logoIndicationBooleanCCOEFF","resTM_CCOEFF_NORMED.max()","ECR_RATIO","MVL SUM","MVL ABS","RMS","DB","ZCR","MFCC","FARBWECHSEL RATIO","SIFT RATIO","BRIGHTNESS_BOOLEAN","brightness","Tag","Zeit","LABEL"]
        writer_object.writerow(list_data) 

    print("=== Soundmeter Started ===")
    print(p.get_default_input_device_info())

    def callback(in_data, frame_count, time_info, status):
        global RMS
        global decoded
        #decoded = numpy.frombuffer(in_data, dtype=numpy.float)
        decoded = np.frombuffer(in_data, dtype=np.short).astype(float)
        rms = audioop.rms(in_data, WIDTH) / 32767
        return in_data, pyaudio.paContinue

    stream = p.open(format=p.get_format_from_width(WIDTH),
                    input_device_index=DEVICE,
                    channels=1,
                    rate=RATE,
                    input=True,
                    output=False,
                    stream_callback=callback)

    stream.start_stream()

    print("###Code Starting For each Frame ###")
    ###Code Starting For each Frame ###
    while stream.is_active(): 
        COUNT_OF_ITERATIONS += 1
        ZCR = (np.where(np.sign(decoded[:-1]) != np.sign(decoded[1:]))[0] + 1).size
        MFCC = (librosa.feature.mfcc(y=np.array(decoded), sr=RATE)).std()
        if RMS!=0:
            DB = 20 * log10(RMS)
            
        imageApplicationVideoStream = ImageGrab.grab(bbox=regionTVApplicationFullScreenshot)

        currentFrame = np.array(imageApplicationVideoStream,dtype="uint8")
        if len(PREV_FRAME) != 0 and (PREV_FRAME.max()!=PREV_FRAME.min() and currentFrame.max()!=currentFrame.min()): #and (PREV_FRAME != currentFrame).all()
            MVL_VALUES = mvl.lucas_kanade_method_mvl(currentFrame,PREV_FRAME,cv,np)
            ECR_RATIO = ECR.ECR(currentFrame,PREV_FRAME, edgeTVAPPwidth, edgeTVAPPheight, crop=False, dilate_rate = 5)
            FARBWECHSEL_RATIO = farbchange.deltaE(currentFrame,PREV_FRAME,cv,np)
            SIFT_RATIO = SR.SIFT_RATIO(currentFrame,PREV_FRAME,np,cv)
            t=1
        else:
            print("Check Frame Values?")
            MVL_VALUES=[0,0]
            ECR_RATIO=0
            FARBWECHSEL_RATIO=0
            SIFT_RATIO=1
        #save prev frame
        PREV_FRAME = np.array(imageApplicationVideoStream,dtype="uint8")

        logoIndicationBooleanSQDIFF, logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
        = LogoConfidence.getLogoConfidence(currentSelectedExpectedRegion,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,None)

        #im = Image.open(imageExpectedLogo)
        brightness = (ImageStat.Stat(imageExpectedLogo)).mean[0]

        #set to true if logo to bright
        BRIGHTNESS_BOOLEAN = (resTM_CCOEFF_NORMED > 0.05 and brightness>BRIGHTNESS_EDGE) or brightness>BRIGHTNESS_LIMIT

        TempCurrentState = LOGO_GEFUNDEN
            #Switching to Programm gefunden
        if (CONSECUTIVE_FRAME_COOLDOWN_COUNTER==0):
            if logoIndicationBooleanSQDIFF and logoIndicationBooleanCCOEFF and LOGO_GEFUNDEN==0:
                CONSECUTIVE_COUNTER+=1
                if CONSECUTIVE_COUNTER>=CONSECUTIVE_FRAMES_FOR_SWITCHING:
                    PYAUTOGUI_LOCATION=pyautogui.locateOnScreen(PICTURE_TV_LOGO,grayscale=True,confidence=CONFIDENCE, region=currentSelectedExpectedRegionPYAUTOGUI)
                    if PYAUTOGUI_LOCATION!=None:
                        STATE = "Programm"
                        LOGO_GEFUNDEN = 1
                    else:
                        print("Logo durch Merkmale gefunden aber PYAUTOGUI Fand das Logo nicht")
                        CONSECUTIVE_COUNTER = 0
        
            #Switching to Werbung gefunden
            elif not logoIndicationBooleanSQDIFF and not logoIndicationBooleanCCOEFF and LOGO_GEFUNDEN==1 and not BRIGHTNESS_BOOLEAN:
                    CONSECUTIVE_COUNTER+=1
                    if CONSECUTIVE_COUNTER>=CONSECUTIVE_FRAMES_FOR_SWITCHING:
                        PYAUTOGUI_LOCATION=pyautogui.locateOnScreen(PICTURE_TV_LOGO,grayscale=True,confidence=CONFIDENCE, region=currentSelectedExpectedRegionPYAUTOGUI)
                        #Confirmed that Logo is not visible
                        if  not(logoIndicationBooleanCCOEFF or logoIndicationBooleanSQDIFF) and PYAUTOGUI_LOCATION==None:
                            STATE = "Werbung"
                            LOGO_GEFUNDEN = 0
                        else:   
                            print("Werbung durch Merkmale gefunden aber PYAUTOGUI Fand ein Logo")
                            CONSECUTIVE_FRAME_COOLDOWN_COUNTER = CONSECUTIVE_COOLDOWN
                            CONSECUTIVE_COUNTER = 0

            #Check other places for Logo when Werbung is activated
            if COUNT_OF_ITERATIONS%LIMIT_CHECK_NEW_LOGO==0 and not logoIndicationBooleanSQDIFF and not logoIndicationBooleanCCOEFF and not BRIGHTNESS_BOOLEAN:
                    currentSelectedExpectedRegion,selectedRegionInteger,logoIndicationBooleanCCOEFF,logoIndicationBooleanSQDIFF\
                    =LogoConfidence.getExpectedLogoRegion(currentSelectedExpectedRegion,regionExpectedLogoLower,regionExpectedLogoNewsTime,regionExpectedLogoUpper,imageApplicationVideoStream,PICTURE_TV_LOGO_UPPER,PICTURE_TV_LOGO_LOWER,PICTURE_TV_LOGO_NEWSTIME,cv,np)
                    if selectedRegionInteger==0:
                        currentSelectedExpectedRegionPYAUTOGUI=regionExpectedLogoUpperPYAUTOGUI
                        PICTURE_TV_LOGO=PICTURE_TV_LOGO_UPPER
                        CONFIDENCE=0.3
                    elif selectedRegionInteger==1:
                        currentSelectedExpectedRegionPYAUTOGUI=regionExpectedLogoLowerPYAUTOGUI
                        PICTURE_TV_LOGO=PICTURE_TV_LOGO_LOWER
                        CONFIDENCE=0.3
                    elif selectedRegionInteger==2:
                        currentSelectedExpectedRegionPYAUTOGUI=regionExpectedLogoNewsTimePYAUTOGUI
                        PICTURE_TV_LOGO=PICTURE_TV_LOGO_NEWSTIME
                        CONFIDENCE=0.7
                    #print("Changed Selected Region: "+str(selectedRegionInteger))

            if TempCurrentState!=LOGO_GEFUNDEN:
                end = time.time()
                print("time elapsed: "+str(end - start))
                print(COUNT_OF_ITERATIONS)
                print("In den Status "+STATE+" gewechselt")
                list_data=[COUNT_OF_ITERATIONS,logoIndicationBooleanSQDIFF,resTM_SQDIFF_NORMED,logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,ECR_RATIO,MVL_VALUES[0],MVL_VALUES[1],RMS,DB,ZCR,MFCC,FARBWECHSEL_RATIO,SIFT_RATIO,BRIGHTNESS_BOOLEAN,brightness,cd.day(),cd.time(),"PROGRAMM"]
                writer_object.writerow(list_data) 
                imageExpectedLogo.save("screenshots/"+STATE+str(COUNT_OF_ITERATIONS)+".png")
                #Reset Counters
                CONSECUTIVE_COUNTER = 0
                CONSECUTIVE_FRAME_COOLDOWN_COUNTER = CONSECUTIVE_COOLDOWN
        else:
            CONSECUTIVE_FRAME_COOLDOWN_COUNTER-=1
            
        #print(COUNT_OF_ITERATIONS)

    f_object.close()
    stream.stop_stream()
    stream.close()
    p.terminate()