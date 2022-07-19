#visuelle merkmale
from ast import And, If
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

#Counter
COUNT_OF_ITERATIONS = 0
CONSECUTIVE_COUNTER = 0
CONSECUTIVE_FRAME_COOLDOWN_COUNTER = 0
COUNTER_UNEINDEUTIG=0

#prevFrame for Visuelle Merkmale
PREV_FRAME = []
ECR_RATIO = 0
MVL_VALUES = []
FARBWECHSEL_RATIO = 0
SIFT_RATIO = 0
PYAUTOGUI_LOCATION = None

#EDGE Values
LIMIT_CHECK_NEW_LOGO = 50
#BRIGHTNESS_EDGE = 190
BRIGHTNESS_LIMIT = 230
BRIGHTNESS_BOOLEAN= False
CONSECUTIVE_COOLDOWN = 50
CONSECUTIVE_FRAMES_FOR_SWITCHING = 5


DATE = cd.run()
DATASET_DIR = "data/"+DATE+"/collectedData/"
SCREENSHOT_DIR = "data/"+DATE+"/screenshots/"
FILEPATH_DATASET=DATASET_DIR+"logoDetection.csv"

os.makedirs(DATASET_DIR)
os.makedirs(SCREENSHOT_DIR)
LOGO_COLLECTION = LogoConfidence.getLogos(cv)
CONFIDENCES = LogoConfidence.getConfindences()

#####Starting Code#####

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

#regions for pyautogui
regionsPYAUTOGUI =\
LogoConfidence.getRegionsPYAUTOGUI(APPLICATION_POSITION)

#debug regions with CV and PYAuto
LogoConfidence.debugMyRegions(regions,regionsPYAUTOGUI,ImageGrab.grab(bbox=regionTVApplicationFullScreenshot),pyautogui)

#decide for region
currentSelectedExpectedRegion,currentSelectedExpectedRegionPYAUTOGUI,CURRENT_PICTURE_TV_LOGO,CURRENT_CONFIDENCE,initialState\
=LogoConfidence.getExpectedLogoRegion(regions[0],regionsPYAUTOGUI[0],LOGO_COLLECTION[0],CONFIDENCES[0],regions,regionsPYAUTOGUI,ImageGrab.grab(bbox=regionTVApplicationFullScreenshot),LOGO_COLLECTION,cv,np)

ImageGrab.grab(bbox=regionTVApplicationFullScreenshot).save("debugging/lastFullScreen.png")

#dont know for now why i do this 
PYAUTOGUI_LOCATION=pyautogui.locateOnScreen(CURRENT_PICTURE_TV_LOGO,grayscale=True,confidence=CURRENT_CONFIDENCE, region=currentSelectedExpectedRegionPYAUTOGUI)
print(currentSelectedExpectedRegionPYAUTOGUI)

if initialState:
    LOGO_GEFUNDEN=1
    STATE="Programm"
else:
    LOGO_GEFUNDEN = 0
    STATE = "Wahrscheinlich Werbung"

print("Initialer Status lautet: "+STATE)

#Data will be appended into file
file_exists = exists(FILEPATH_DATASET)
with open(FILEPATH_DATASET, 'a', newline='') as f_object: 
    writer_object = writer(f_object)
    if not file_exists:
        list_data=["COUNT_OF_ITERATIONS","logoIndicationBooleanSQDIFF","resTM_SQDIFF_NORMED.max()","logoIndicationBooleanCCOEFF","resTM_CCOEFF_NORMED.max()","ECR_RATIO","MVL SUM","MVL ABS","RMS","DB","ZCR","MFCC","FARBWECHSEL RATIO","SIFT RATIO","BRIGHTNESS_BOOLEAN","brightness","Tag","Zeit","LABEL"]
        writer_object.writerow(list_data) 

    print("=== Soundmeter Started ===")
    #print(p.get_default_input_device_info())
    def callback(in_data, frame_count, time_info, status):
        global RMS
        global decoded
        #decoded = numpy.frombuffer(in_data, dtype=numpy.float)
        decoded = np.frombuffer(in_data, dtype=np.short).astype(float)
        RMS = audioop.rms(in_data, WIDTH) / 32767
        return in_data, pyaudio.paContinue
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    input_device_index=DEVICE,
                    channels=1,
                    rate=RATE,
                    input=True,
                    output=False,
                    stream_callback=callback)
    stream.start_stream()

    print("=== Videometer Started ===")
    ###Code Starting For each Frame ###
    while stream.is_active(): 
        COUNT_OF_ITERATIONS += 1
        #Get Sound Features#
        ZCR = (np.where(np.sign(decoded[:-1]) != np.sign(decoded[1:]))[0] + 1).size
        MFCC = (librosa.feature.mfcc(y=np.array(decoded), sr=RATE)).std()
        if RMS!=0 : DB=20*log10(RMS)  

        # print(RMS)
        # print(DB)

        #Get Video Features#    
        imageApplicationVideoStream = ImageGrab.grab(bbox=regionTVApplicationFullScreenshot)
        currentFrame = np.array(imageApplicationVideoStream,dtype="uint8")
        if len(PREV_FRAME) != 0 and (PREV_FRAME.max()!=PREV_FRAME.min() and currentFrame.max()!=currentFrame.min()): #and (PREV_FRAME != currentFrame).all()
            MVL_VALUES = mvl.lucas_kanade_method_mvl(currentFrame,PREV_FRAME,cv,np)
            ECR_RATIO = ECR.ECR(currentFrame,PREV_FRAME, edgeTVAPPwidth, edgeTVAPPheight, crop=False, dilate_rate = 5)
            FARBWECHSEL_RATIO = farbchange.deltaE(currentFrame,PREV_FRAME,cv,np)
            SIFT_RATIO = SR.SIFT_RATIO(currentFrame,PREV_FRAME,np,cv)
            t=1
        else:
            print("Black Frame detected Video Features wont be calculated")
            MVL_VALUES=[0,0]
            ECR_RATIO=0
            FARBWECHSEL_RATIO=0
            SIFT_RATIO=1
        #save prev frame
        PREV_FRAME = np.array(imageApplicationVideoStream,dtype="uint8")

        #search Logo
        logoIndicationBooleanCCOEFF, logoIndicationBooleanSQDIFF,resTM_CCOEFF_NORMED,resTM_SQDIFF_NORMED,imageExpectedLogo\
        = LogoConfidence.getLogoConfidence(currentSelectedExpectedRegion,imageApplicationVideoStream,CURRENT_PICTURE_TV_LOGO,cv,np,None)



        #get Brightness for confidence indicator
        brightness = (ImageStat.Stat(imageExpectedLogo)).mean[0]

        #set to true if logo to bright
        #je eher ein logo gefunden wird desto kleiner wird das Brightness Limit
        reduceBrightnessLimitCCOEFF = resTM_CCOEFF_NORMED*100
        reduceBrightnessLimitSQDIFF = (1-resTM_SQDIFF_NORMED)*100
        newBrightnessLimit = BRIGHTNESS_LIMIT-reduceBrightnessLimitCCOEFF-reduceBrightnessLimitSQDIFF
        BRIGHTNESS_BOOLEAN = brightness>(newBrightnessLimit)
        # print("Helligkeit: "+str(brightness)+" Limit: "+str(newBrightnessLimit))
        # print(newBrightnessLimit)
        # if not BRIGHTNESS_BOOLEAN:
        #     print("Das Bild ist nicht so Hell und es ist wahrschinelich auch kein Logo Drin ich gehe von Werbung aus")
        # else:
        #     print("Das Bild hell und es ist vielleicht auch ein Logo drin")

        #check if we switch Status
        TempCurrentState = LOGO_GEFUNDEN
        #Switching to Programm gefunden
        if (CONSECUTIVE_FRAME_COOLDOWN_COUNTER==0):
            if logoIndicationBooleanSQDIFF and logoIndicationBooleanCCOEFF and LOGO_GEFUNDEN==0:
                CONSECUTIVE_COUNTER+=1
                if CONSECUTIVE_COUNTER>=CONSECUTIVE_FRAMES_FOR_SWITCHING:
                    PYAUTOGUI_LOCATION=pyautogui.locateOnScreen(CURRENT_PICTURE_TV_LOGO,grayscale=True,confidence=CURRENT_CONFIDENCE, region=currentSelectedExpectedRegionPYAUTOGUI)
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
                        PYAUTOGUI_LOCATION=pyautogui.locateOnScreen(CURRENT_PICTURE_TV_LOGO,grayscale=True,confidence=CURRENT_CONFIDENCE, region=currentSelectedExpectedRegionPYAUTOGUI)
                        #Confirmed that Logo is not visible
                        #check other regions there might be a logo
                        currentSelectedExpectedRegion,currentSelectedExpectedRegionPYAUTOGUI,CURRENT_PICTURE_TV_LOGO,CURRENT_CONFIDENCE,currentState\
                        =LogoConfidence.getExpectedLogoRegion(currentSelectedExpectedRegion,currentSelectedExpectedRegionPYAUTOGUI,CURRENT_PICTURE_TV_LOGO,CURRENT_CONFIDENCE,regions,regionsPYAUTOGUI,imageApplicationVideoStream,LOGO_COLLECTION,cv,np)

                        if  not(logoIndicationBooleanCCOEFF or logoIndicationBooleanSQDIFF) and PYAUTOGUI_LOCATION==None and currentState == False:
                            STATE = "Werbung"
                            LOGO_GEFUNDEN = 0
                        else:   
                            print("Werbung durch Merkmale gefunden aber PYAUTOGUI Fand ein Logo")
                            CONSECUTIVE_FRAME_COOLDOWN_COUNTER = CONSECUTIVE_COOLDOWN
                            CONSECUTIVE_COUNTER = 0

            #Check other places for Logo when Werbung is activated
            if COUNT_OF_ITERATIONS%LIMIT_CHECK_NEW_LOGO==0 and not (logoIndicationBooleanSQDIFF and logoIndicationBooleanCCOEFF) and not BRIGHTNESS_BOOLEAN and LOGO_GEFUNDEN==0:
                    currentSelectedExpectedRegion,currentSelectedExpectedRegionPYAUTOGUI,CURRENT_PICTURE_TV_LOGO,CURRENT_CONFIDENCE,initialState\
                    =LogoConfidence.getExpectedLogoRegion(currentSelectedExpectedRegion,currentSelectedExpectedRegionPYAUTOGUI,CURRENT_PICTURE_TV_LOGO,CURRENT_CONFIDENCE,regions,regionsPYAUTOGUI,imageApplicationVideoStream,LOGO_COLLECTION,cv,np)
        else:
            CONSECUTIVE_FRAME_COOLDOWN_COUNTER-=1

        if TempCurrentState!=LOGO_GEFUNDEN:
            end = time.time()
            print("time elapsed: "+str(end - start))
            print(COUNT_OF_ITERATIONS/(end-start))
            print()
            print("In den Status "+STATE+" gewechselt")
            print("Bisher uneindeutige Frames "+str(COUNTER_UNEINDEUTIG))
            list_data=[COUNT_OF_ITERATIONS,logoIndicationBooleanSQDIFF,resTM_SQDIFF_NORMED,logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,ECR_RATIO,MVL_VALUES[0],MVL_VALUES[1],RMS,DB,ZCR,MFCC,FARBWECHSEL_RATIO,SIFT_RATIO,BRIGHTNESS_BOOLEAN,brightness,cd.day(),cd.time(),STATE+" Grenze"]
            print(list_data)
            writer_object.writerow(list_data) 
            imageExpectedLogo.save(SCREENSHOT_DIR+STATE+str(COUNT_OF_ITERATIONS)+".png")
            #Reset Counters
            CONSECUTIVE_COUNTER = 0
            CONSECUTIVE_FRAME_COOLDOWN_COUNTER = CONSECUTIVE_COOLDOWN
        elif (logoIndicationBooleanSQDIFF and logoIndicationBooleanCCOEFF and STATE=="Programm") or (not (logoIndicationBooleanCCOEFF and logoIndicationBooleanSQDIFF) and STATE=="Werbung"):
            list_data=[COUNT_OF_ITERATIONS,logoIndicationBooleanSQDIFF,resTM_SQDIFF_NORMED,logoIndicationBooleanCCOEFF,resTM_CCOEFF_NORMED,ECR_RATIO,MVL_VALUES[0],MVL_VALUES[1],RMS,DB,ZCR,MFCC,FARBWECHSEL_RATIO,SIFT_RATIO,BRIGHTNESS_BOOLEAN,brightness,cd.day(),cd.time(),STATE]
            writer_object.writerow(list_data) 
        else:
            COUNTER_UNEINDEUTIG+=1
            
        #print(COUNT_OF_ITERATIONS)

    f_object.close()
    stream.stop_stream()
    stream.close()
    p.terminate()