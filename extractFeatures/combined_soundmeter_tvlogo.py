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

#define Variables
PREFFERED_WINDOW_SIZE_OF_TV_APPLICATION=(1301,849)
TV_APPLICATION_NAME = "Hauppauge WinTV"
COUNT_OF_ITERATIONS = 0
CONSECUTIVE_FRAMES_FOR_SWITCHING = 5
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
SIZE_OF_EXPECTED_LOGO_Y = 48

#BORDEREDGES for Picture without Appplication Borders
LEFT_BORDER_MARGIN = 9
TOP_BORDER_MARGIN = 33
RIGHT_BORDER_MARGIN = 10
BOTTOM_BORDER_MARGIN = 89
EXPECTED_LOWER_MARGIN = 64

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
CONFIDENCE = 0.2


FILEPATH_DATASET="dataset\logoDetection.csv"

#Get Window Handle of TV App and Resize
windowHandle = pyautogui.getWindowsWithTitle(TV_APPLICATION_NAME)[0]
windowHandle.size = PREFFERED_WINDOW_SIZE_OF_TV_APPLICATION

#Get Relative Window Position
topLeftX,topLeftY,width,height=LogoConfidence.getRelativeWindowPosition(str(windowHandle).split(","),re)

#Calculate Offset for Video Without Borders
regionTVApplicationFullScreenshot,edgeTVAPPwidth,edgeTVAPPheight=\
LogoConfidence.getTVApplicationWithoutEdgesRegion(topLeftX,topLeftY,LEFT_BORDER_MARGIN,TOP_BORDER_MARGIN,width,height,RIGHT_BORDER_MARGIN,BOTTOM_BORDER_MARGIN)

#regions for opencv
regionExpectedLogoUpper,regionExpectedLogoLower,regionExpectedLogoNewsTime =\
LogoConfidence.getRegions(width,EXPECTED_MARGIN_X,EXPECTED_MARGIN_Y,LEFT_BORDER_MARGIN,TOP_BORDER_MARGIN,EXPECTED_LOWER_MARGIN,SIZE_OF_EXPECTED_LOGO_X,SIZE_OF_EXPECTED_LOGO_Y)
currentSelectedExpectedRegion=regionExpectedLogoUpper

#regions for pyautogui
regionExpectedLogoUpperPYAUTOGUI,regionExpectedLogoLowerPYAUTOGUI,regionExpectedLogoNewsTimePYAUTOGUI =\
LogoConfidence.getRegionsPYAUTOGUI(topLeftX,topLeftY,width,SIZE_OF_EXPECTED_LOGO_X,SIZE_OF_EXPECTED_LOGO_Y,EXPECTED_MARGIN_X,EXPECTED_MARGIN_Y,EXPECTED_LOWER_MARGIN)
currentSelectedExpectedRegionPYAUTOGUI=regionExpectedLogoUpperPYAUTOGUI

#Data will be appended into file
file_exists = exists(FILEPATH_DATASET)
with open(FILEPATH_DATASET, 'a', newline='') as f_object: 
    writer_object = writer(f_object)
    if not file_exists:
        list_data=["COUNT_OF_ITERATIONS","logoIndicationBooleanSQDIFF","resTM_SQDIFF_NORMED.max()","logoIndicationBooleanCCOEFF","resTM_CCOEFF_NORMED.max()","ECR_RATIO","MVL SUM","MVL ABS","RMS","DB","ZCR","MFCC","FARBWECHSEL RATIO","SIFT RATIO","Tag","Zeit","LABEL"]
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
        currentFrame = np.array(imageApplicationVideoStream)
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

        PREV_FRAME = np.array(imageApplicationVideoStream)

        # imageExpectedLogo = imageApplicationVideoStream.crop((currentSelectedExpectedRegion))
        # imageExpectedLogoAsNumpy = cv.cvtColor(np.array(imageExpectedLogo), cv.COLOR_RGB2GRAY)
        # resTM_SQDIFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_SQDIFF_NORMED) #<0.4 quite represantive
        # resTM_CCOEFF_NORMED = cv.matchTemplate(imageExpectedLogoAsNumpy, PICTURE_TV_LOGO, cv.TM_CCOEFF_NORMED) #>0.3 quite represantative
        # logoIndicationBooleanSQDIFF = (resTM_SQDIFF_NORMED<=0.4) or (resTM_CCOEFF_NORMED>=0.9)
        # logoIndicationBooleanCCOEFF = (resTM_CCOEFF_NORMED>=0.3) #or (resTM_SQDIFF_NORMED<=0.05).any()

        logoIndicationBooleanSQDIFF, logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
        = LogoConfidence.getLogoConfidence(currentSelectedExpectedRegion,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np,None)

        # print(resTM_CCOEFF_NORMED)
        # print(resTM_SQDIFF_NORMED)
        # print(logoIndicationBooleanCCOEFF)
        # print(logoIndicationBooleanSQDIFF)

        #im = Image.open(imageExpectedLogo)
        brightness = (ImageStat.Stat(imageExpectedLogo)).mean[0]
        # print(brightness)

        TempCurrentState = LOGO_GEFUNDEN
            #Switching to Programm gefunden
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
        elif not logoIndicationBooleanSQDIFF and not logoIndicationBooleanCCOEFF and LOGO_GEFUNDEN==1 and brightness < 240:
                CONSECUTIVE_COUNTER+=1
                if CONSECUTIVE_COUNTER>=CONSECUTIVE_FRAMES_FOR_SWITCHING:
                    currentSelectedExpectedRegion,selectedRegionInteger,logoIndicationBooleanCCOEFF,logoIndicationBooleanSQDIFF\
                    =LogoConfidence.getExpectedLogoRegion(currentSelectedExpectedRegion,regionExpectedLogoLower,regionExpectedLogoNewsTime,regionExpectedLogoUpper,imageApplicationVideoStream,PICTURE_TV_LOGO,cv,np)

                    if selectedRegionInteger==0:
                        currentSelectedExpectedRegionPYAUTOGUI=regionExpectedLogoUpperPYAUTOGUI
                    elif selectedRegionInteger==1:
                        currentSelectedExpectedRegionPYAUTOGUI=regionExpectedLogoLowerPYAUTOGUI
                    elif selectedRegionInteger==2:
                        currentSelectedExpectedRegionPYAUTOGUI=regionExpectedLogoNewsTimePYAUTOGUI
                    else:
                        PYAUTOGUI_LOCATION=pyautogui.locateOnScreen(PICTURE_TV_LOGO,grayscale=True,confidence=CONFIDENCE, region=currentSelectedExpectedRegionPYAUTOGUI)
                        print("Changed Selected Region: "+str(selectedRegionInteger))

                    #Confirmed that Logo is not visible
                    if  not(logoIndicationBooleanCCOEFF or logoIndicationBooleanSQDIFF) and PYAUTOGUI_LOCATION==None:
                        STATE = "Werbung"
                        LOGO_GEFUNDEN = 0
                    else:   
                        print("Werbung durch Merkmale gefunden aber PYAUTOGUI Fand ein Logo")
                        CONSECUTIVE_COUNTER = 0
                

        if TempCurrentState!=LOGO_GEFUNDEN:
            end = time.time()
            print("time elapsed: "+str(end - start))
            print(COUNT_OF_ITERATIONS)
            print("In den Status "+STATE+" gewechselt")
            list_data=[COUNT_OF_ITERATIONS,logoIndicationBooleanSQDIFF,resTM_SQDIFF_NORMED,logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,ECR_RATIO,MVL_VALUES[0],MVL_VALUES[1],RMS,brightness,ZCR,MFCC,FARBWECHSEL_RATIO,SIFT_RATIO,cd.day(),cd.time(),"PROGRAMM"]
            writer_object.writerow(list_data) 
            imageExpectedLogo.save("screenshots/"+STATE+str(COUNT_OF_ITERATIONS)+".png")
            #Reset Counters
            CONSECUTIVE_COUNTER = 0
            CONSECUTIVE_COOLDOWN_COUNTER = CONSECUTIVE_FRAME_COOLDOWN
            
        #print(COUNT_OF_ITERATIONS)

    f_object.close()
    stream.stop_stream()
    stream.close()
    p.terminate()