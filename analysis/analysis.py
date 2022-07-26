from itertools import count
from re import X
from tkinter import Y
from turtle import xcor
from async_generator import yield_from_
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np
import time
import matplotlib.dates as mdates
from matplotlib.ticker import PercentFormatter
import seaborn as sns
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.patches as mpatches
from os import listdir

PATH_DATA_TO_BE_JOINED = os.getcwd()+"\\analysis\\input"
OUTPUT_PATH = "analysis\output\\"
COLOR_FOR_WERBUNG = "orange"
COLOR_FOR_PROGRAMM ="cornflowerblue"
STATUSES=[["Programm",COLOR_FOR_PROGRAMM],["Werbung",COLOR_FOR_WERBUNG]]
ALPHA_VAL = 0.3
SIZE_OF_PLOTS = [24,13.5]

def returnJoinedDataFrame(path):
    #join data paths
    # setting the path for joining multiple files
    files = os.path.join(path, "*.csv")
    # list of merged files returned
    files = glob.glob(files)
    print("Result CSV after joining all CSV files at a particular location...");
    # joining files with concat and read_csv
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    print(df)
    return df

def removeOutliers(specificDataFrame):
    print("Outliers werden entfernt")
    print("Länge der Daten: "+str(len(specificDataFrame)))
    specificDataFrame["LABEL"].replace(to_replace ="Programm Grenze",value ="Programm")
    print("Programm Grenze in Programm verwandelt "+str(len(specificDataFrame)))
    specificDataFrame["LABEL"].replace(to_replace ="Werbung Grenze",value ="Werbung")
    print("Werbung Grenze in Werbung verwandelt "+str(len(specificDataFrame)))
    specificDataFrame.dropna(subset=['SIFT RATIO'])
    print("Leere Values in SIFT Ratio entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame.drop(specificDataFrame[specificDataFrame['SIFT RATIO'] == 0.0037703].index)
    print("Error Values in SIFT Ratio Entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame.drop(specificDataFrame[specificDataFrame['MVL SUM'] == 0.0037703].index)
    specificDataFrame = specificDataFrame[specificDataFrame['MVL SUM'] != 0.0037703]
    print("Error Values in MVL Sum Entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame.drop(specificDataFrame[specificDataFrame['MVL ABS'] == 0.0037703].index)
    print("Error Values in MVL ABS Entfernt: "+str(len(specificDataFrame))) 
    #remove error values!
    specificDataFrame = specificDataFrame[specificDataFrame['MVL SUM'].between(-1000, 1000)] 
    print("MVL Sum Outliers entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame =specificDataFrame[specificDataFrame['MVL ABS'].between(0, 5000)] 
    print("MVL ABS Outliers entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame = specificDataFrame[specificDataFrame['RMS'].between(0, 0.2)]  
    print("RMS Outliers entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame = specificDataFrame[specificDataFrame['SIFT RATIO'].between(0, 1)]  
    print("SIFT RATIO Outliers entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame = specificDataFrame[specificDataFrame['ECR_RATIO'].between(0.001, 0.999)]  
    print("ECR RATIO Outliers entfernt: "+str(len(specificDataFrame)))
    print(specificDataFrame.describe())
    return specificDataFrame

def setTextinPlot(graph,values):
    i=0
    for p in graph:
        width = p.get_width()
        height = p.get_height()/2
        x, y = p.get_xy()
        plt.text(x+width/2,
                y+height*1.01,
                str(round(values[i],2))+'',
                ha='center',
                weight='normal')
        i+=1

def setTextAbovePlot(graph,values):
    i=0
    for p in graph:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        plt.text(x+width/2,
                y+height*1.01,
                str(values[i])+'',
                ha='center',
                weight='normal')
        i+=1

def createCount(countDatapointsProgramm,countDatapointsWerbung):
    #df.replace(to_replace ="Boston Celtics", value ="Omega Warrior")
    sumDatenpunkte = countDatapointsWerbung+countDatapointsProgramm
    percentageWerbung = (countDatapointsWerbung/sumDatenpunkte)*100
    percentageProgramm = (countDatapointsProgramm/sumDatenpunkte)*100
    AnzahlDerDatenPunkte = [countDatapointsProgramm,countDatapointsWerbung]
    percentage = [percentageProgramm,percentageWerbung]
    return [AnzahlDerDatenPunkte,percentage]
   
def createSumWerbungProgramHistograms(arrDf,STATUSES,columnArray):
    fig, axes = plt.subplots(len(columnArray)//4, 4, figsize=(12, 48))
    countOfData = 0
    for x in STATUSES:
        specificDataFrame = arrDf[countOfData]
        counterForPlots = 0
        for triaxis in axes:
            for axis in triaxis:
                    if columnArray[counterForPlots]=="Zeit":
                        minute_locator = mdates.MinuteLocator(interval=240)
                        hour_locator = mdates.HourLocator(interval=6)
                        axis.xaxis.set_major_locator(minute_locator)
                        myFmt = mdates.DateFormatter('%HH')
                        axis.xaxis.set_major_formatter(myFmt)
                        specificDataFrame.hist(column = specificDataFrame.columns[counterForPlots],color = STATUSES[countOfData][1], bins = 100, ax=axis) # Locator for major axis only.)
                    elif counterForPlots < 11:
                        if columnArray[counterForPlots]=="ECR_RATIO":
                            specificDataFrame.hist(column = specificDataFrame.columns[counterForPlots],color = STATUSES[countOfData][1], bins = 100, ax=axis,label=x)
                        else:
                            specificDataFrame.hist(column = specificDataFrame.columns[counterForPlots],color = STATUSES[countOfData][1], bins = 100, ax=axis)
                    elif counterForPlots == 11 and countOfData==1:
                        certainCounts = createCount(len(arrDf[0]),len(arrDf[1]))
                        countPlot = plt.bar(["Programm","Werbung"],certainCounts[0],color=[COLOR_FOR_PROGRAMM, COLOR_FOR_WERBUNG])
                        setTextAbovePlot(countPlot,[certainCounts[0][0],certainCounts[0][1]])
                        setTextinPlot(countPlot,[certainCounts[1][0],certainCounts[1][1]])
                        plt.title("Anzahl der Datenpunkte")
                    counterForPlots +=1
        countOfData+=1  
    manager=plt.get_current_fig_manager()
    manager.full_screen_toggle()    
    fig.legend(loc='upper left')
    fig.suptitle("Histogramme für alle Merkmale", fontsize=14) 
    fig.set_size_inches(SIZE_OF_PLOTS)   
    plt.savefig(OUTPUT_PATH+'histogramme.png')
    #plt.show()

def createHeatmaps(dataframes):
    ##createHeatmap(specificDataFrame.corr())
    fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(SIZE_OF_PLOTS))  
    sns.heatmap(dataframes[0],ax=axes[0],cbar=False,vmax=1, annot=True, linewidths=.5,xticklabels=True, yticklabels=True)
    sns.heatmap(dataframes[0],ax=axes[1],cbar=True,vmax=1, annot=True, linewidths=.5,xticklabels=True, yticklabels=True)
    axes[0].set_xticklabels(dataframes[0].columns,rotation=30,horizontalalignment="right")
    axes[1].set_xticklabels(dataframes[1].columns,rotation=30,horizontalalignment="right")

    #axes[0].set_yticklabels(dataframes[1].columns,rotation=30,horizontalalignment="right")
    #axes[1].set_yticklabels(dataframes[1].columns,rotation=30,horizontalalignment="right")

    axes[0].set(title="Datenpunkte des Programms")
    axes[1].set(title="Datenpunkte der Werbung")
    fig.suptitle("Korrelationen der Merkmale", fontsize=14)
    manager=plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.savefig(OUTPUT_PATH+'heatmaps.png')
    #plt.show()

def createScatters(dfWerbung,dfProgramm,columnName1,columnArray):
    fig, axes = plt.subplots(len(columnArray)//4, 4, figsize=(12, 48))
    cArr = columnArray.copy()
    cArr.remove("LABEL")
    if columnName1 in cArr: cArr.remove(columnName1)
    counterForPlots = 0
    for triaxis in axes:
        for axis in triaxis:
            if counterForPlots<len(cArr):
                if columnName1 == "Zeit":
                    axis.xaxis.set_major_locator(mdates.MinuteLocator(interval=120))
                    axis.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
                    #axis.xticks(rotation = -45) # Rotates X-Axis Ticks by 45-degrees
                elif cArr[counterForPlots] == "Zeit":
                    axis.yaxis.set_major_locator(mdates.MinuteLocator(interval=120))
                    axis.yaxis.set_major_formatter(mdates.DateFormatter('%H'))
                    #axis.yticks(rotation = -45) # Rotates Y-Axis Ticks by 45-degrees
                axis.set_xlabel(columnName1)
                axis.set_ylabel(cArr[counterForPlots])
                if counterForPlots==0:
                    axis.scatter(dfWerbung[columnName1],dfWerbung[cArr[counterForPlots]],color=COLOR_FOR_WERBUNG,label="Werbung",alpha=ALPHA_VAL,s=4)
                    axis.scatter(dfProgramm[columnName1],dfProgramm[cArr[counterForPlots]],color=COLOR_FOR_PROGRAMM,label="Programm",alpha=ALPHA_VAL,s=4)
                else:
                    axis.scatter(dfWerbung[columnName1],dfWerbung[cArr[counterForPlots]],color=COLOR_FOR_WERBUNG,alpha=ALPHA_VAL,s=4)
                    axis.scatter(dfProgramm[columnName1],dfProgramm[cArr[counterForPlots]],color=COLOR_FOR_PROGRAMM,alpha=ALPHA_VAL,s=4) 

            counterForPlots+=1
    manager=plt.get_current_fig_manager()
    manager.full_screen_toggle()
    fig.legend(loc='upper left')
    fig.set_size_inches(SIZE_OF_PLOTS)
    plt.suptitle("Streungsdiagramme für "+columnName1, fontsize=14)
    plt.savefig(OUTPUT_PATH+'scatter'+columnName1+'.png')
    #plt.show()

## GET DATA FRAMES ##
df = returnJoinedDataFrame(PATH_DATA_TO_BE_JOINED)
## Convert Time Column ##
df["Zeit"]=df["Zeit"].astype("datetime64[ns]")
## Columns for Learning Modell ##
columnArray=["ECR_RATIO","MVL SUM","MVL ABS","RMS","DB","ZCR","MFCC","FARBWECHSEL RATIO","SIFT RATIO","Tag","Zeit","LABEL"]
specificDataFrame = df[columnArray]

## REMOVE OUTLIERS AND FALSE NUMBERS ## 
specificDataFrame = removeOutliers(specificDataFrame)

## SPLIT INTO Programm and WERBUNG Frames ##
dfWerbung = specificDataFrame[specificDataFrame['LABEL'] == "Werbung"]
dfProgramm = specificDataFrame[specificDataFrame['LABEL'] == "Programm"]

## CREATE HEATMAPS ##
createHeatmaps([dfProgramm.corr(),dfWerbung.corr()])

## PRINT SUM Histograms ##
createSumWerbungProgramHistograms([dfProgramm,dfWerbung],STATUSES,columnArray)

for x in columnArray:
    createScatters(dfProgramm,dfWerbung,x,columnArray)

dfWerbung.describe().to_csv(OUTPUT_PATH+"WerbungDescribe.csv")
dfProgramm.describe().to_csv(OUTPUT_PATH+"ProgrammDescribe.csv")









