from tkinter import Y
from async_generator import yield_from_
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np
import time
import matplotlib.dates as mdates
from matplotlib.ticker import PercentFormatter

PATH_DATA_TO_BE_JOINED = "dataToBeJoined/"
COLOR_FOR_WERBUNG = "tab:orange"
COLOR_FOR_PROGRAMM ="tab:blue"
#print(os.getcwd())
df = pd.read_csv('analysis/logoDetection.csv')
df["Zeit"]=df["Zeit"].astype("datetime64[ns]")
#df["Zeit"] = pd.to_datetime(df["Zeit"]).dt.time
#print(df.head(1))
columnArray=["ECR_RATIO","MVL SUM","MVL ABS","RMS","DB","ZCR","MFCC","FARBWECHSEL RATIO","SIFT RATIO","Tag","Zeit","LABEL"]
#columnArray=[5,6,7,8,9,10,11,12,13,16,17]
specificDataFrame = df[columnArray]
dfWerbung = specificDataFrame[df['LABEL'] == "Werbung"]
dfProgramm = specificDataFrame[df['LABEL'] == "Programm"]

def returnJoinedDataFrame(path):
    # setting the path for joining multiple files
    files = os.path.join(path, "*.csv")
    # list of merged files returned
    files = glob.glob(files)
    print("Result CSV after joining all CSV files at a particular location...");
    # joining files with concat and read_csv
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    print(df)
    return df
def setTextinPlot(graph,values,plt):
    i=0
    for p in graph:
        width = p.get_width()
        height = p.get_height()/2
        x, y = p.get_xy()
        plt.text(x+width/2,
                y+height*1.01,
                str(values[i])+'',
                ha='center',
                weight='bold')
        i+=1
def setTextAbovePlot(graph,values,plt):
    i=0
    for p in graph:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        plt.text(x+width/2,
                y+height*1.01,
                str(values[i])+'',
                ha='center',
                weight='bold')
        i+=1
def createSumWerbungProgramHistograms():
    fig, axes = plt.subplots(len(columnArray)//4, 4, figsize=(12, 48))
    i = 0
    for triaxis in axes:
        for axis in triaxis:
            if i!=11:
                if i==10:
                    minute_locator = mdates.MinuteLocator(interval=240)
                    hour_locator = mdates.HourLocator(interval=6)
                    axis.xaxis.set_major_locator(minute_locator)
                    myFmt = mdates.DateFormatter('%HH')
                    axis.xaxis.set_major_formatter(myFmt)
                    dfProgramm.hist(column = dfProgramm.columns[i],color = COLOR_FOR_PROGRAMM, bins = 100, ax=axis) # Locator for major axis only.)
                else:
                    dfProgramm.hist(column = dfProgramm.columns[i],color = COLOR_FOR_PROGRAMM, bins = 100, ax=axis)
                i = i+1

    ##werbung
    i = 0
    for triaxis in axes:
        for axis in triaxis:
            if i!=11:
                if i==10:
                    minute_locator = mdates.MinuteLocator(interval=240)
                    hour_locator = mdates.HourLocator(interval=6)
                    axis.xaxis.set_major_locator(minute_locator)
                    myFmt = mdates.DateFormatter('%HH')
                    axis.xaxis.set_major_formatter(myFmt)
                    dfWerbung.hist(column = dfWerbung.columns[i],color = COLOR_FOR_WERBUNG, bins = 100, ax=axis) # Locator for major axis only.)
                else:
                    dfWerbung.hist(column = dfWerbung.columns[i],color = COLOR_FOR_WERBUNG, bins = 100, ax=axis)
                i = i+1
    plt.show()
def createSumHistograms():
    fig, axes = plt.subplots(len(columnArray)//3, 4, figsize=(12, 48))

    i = 0
    for triaxis in axes:
        for axis in triaxis:
            if i!=11:
                if i==10:
                    minute_locator = mdates.MinuteLocator(interval=240)
                    hour_locator = mdates.HourLocator(interval=6)
                    axis.xaxis.set_major_locator(minute_locator)
                    myFmt = mdates.DateFormatter('%HH')
                    axis.xaxis.set_major_formatter(myFmt)
                    specificDataFrame.hist(column = specificDataFrame.columns[i], bins = 100, ax=axis) # Locator for major axis only.)
                else:
                    specificDataFrame.hist(column = specificDataFrame.columns[i], bins = 100, ax=axis)
                i = i+1
    plt.show()
def createCount():
    #df.replace(to_replace ="Boston Celtics", value ="Omega Warrior")
    countDatapointsWerbung = len(dfWerbung)
    countDatapointsProgramm = len(dfProgramm)
    sumDatenpunkte = len(df)
    print(sumDatenpunkte)
    percentageWerbung = (countDatapointsWerbung/sumDatenpunkte)*100
    percentageProgramm = (countDatapointsProgramm/sumDatenpunkte)*100
    AnzahlDerDatenPunkte = [countDatapointsWerbung,countDatapointsProgramm]
    Status = ["Werbung","Programm"]

    #plt.hist([dfWerbung['DB'], dfProgramm['DB']])
    countPlot = plt.bar(Status,AnzahlDerDatenPunkte,color=[COLOR_FOR_WERBUNG, COLOR_FOR_PROGRAMM],label="Anzahl der Datenpunkte für Werbung/Programm")

    setTextAbovePlot(countPlot,[countDatapointsWerbung,countDatapointsProgramm],plt)
    setTextinPlot(countPlot,[percentageWerbung,percentageProgramm],plt)

    plt.xlabel("Status")    
    plt.ylabel("Anzahl der Datenpunkte")
    plt.title("Anzahl der Datenpunkte per Status")
    plt.show()

def createPercentageWerbungProgramHistograms():
    fig, axes = plt.subplots(len(columnArray)//4, 4, figsize=(12, 48))
    i = 0
    for triaxis in axes:
        for axis in triaxis:
            if i!=11:
                if i==10:
                    minute_locator = mdates.MinuteLocator(interval=240)
                    hour_locator = mdates.HourLocator(interval=6)
                    axis.xaxis.set_major_locator(minute_locator)
                    myFmt = mdates.DateFormatter('%HH')
                    axis.xaxis.set_major_formatter(myFmt)
                    dfProgramm.hist(column = dfProgramm.columns[i],color = COLOR_FOR_PROGRAMM, bins = 100, ax=axis) # Locator for major axis only.)
                else:
                    dfProgramm.hist(column = dfProgramm.columns[i],color = COLOR_FOR_PROGRAMM, bins = 100, ax=axis)
                i = i+1

    ##werbung
    i = 0
    for triaxis in axes:
        for axis in triaxis:
            if i!=11:
                if i==10:
                    minute_locator = mdates.MinuteLocator(interval=240)
                    hour_locator = mdates.HourLocator(interval=6)
                    axis.xaxis.set_major_locator(minute_locator)
                    myFmt = mdates.DateFormatter('%HH')
                    axis.xaxis.set_major_formatter(myFmt)
                    dfWerbung.hist(column = dfWerbung.columns[i],color = COLOR_FOR_WERBUNG, bins = 100, ax=axis) # Locator for major axis only.)
                else:
                    dfWerbung.hist(column = dfWerbung.columns[i],color = COLOR_FOR_WERBUNG, bins = 100, ax=axis)
                i = i+1
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()





#createCount()
#createSumHistograms()
#createSumWerbungProgramHistograms()
createPercentageWerbungProgramHistograms()




