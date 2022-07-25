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
import seaborn as sns
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.patches as mpatches
from os import listdir

#graveyard
#df["Zeit"] = pd.to_datetime(df["Zeit"]).dt.time
#print(df.head(1))
# dfWerbung = specificDataFrame[df['LABEL'] == "Werbung"]
# dfProgramm = specificDataFrame[df['LABEL'] == "Programm"]
#columnArray=[5,6,7,8,9,10,11,12,13,16,17]
#print(os.getcwd())
# #def createSumHistograms():
#     fig, axes = plt.subplots(len(columnArray)//3, 4, figsize=(12, 48))

#     i = 0
#     for triaxis in axes:
#         for axis in triaxis:
#             if i!=11:
#                 if i==10:
#                     minute_locator = mdates.MinuteLocator(interval=240)
#                     hour_locator = mdates.HourLocator(interval=6)
#                     axis.xaxis.set_major_locator(minute_locator)
#                     myFmt = mdates.DateFormatter('%HH')
#                     axis.xaxis.set_major_formatter(myFmt)
#                     specificDataFrame.hist(column = specificDataFrame.columns[i], bins = 100, ax=axis) # Locator for major axis only.)
#                 else:
#                     specificDataFrame.hist(column = specificDataFrame.columns[i], bins = 100, ax=axis)
#                 i = i+1
        
#     plt.show()
def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ PATH_DATA_TO_BE_JOINED+"\\"+filename for filename in filenames if filename.endswith( suffix ) ]

def returnJoinedDataFrame(files):
    # list of merged files returned
    files = glob.glob(files)
    print("Result CSV after joining all CSV files at a particular location...");
    # joining files with concat and read_csv
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    print(df)
    return df

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

PATH_DATA_TO_BE_JOINED = os.getcwd()+"\\analysis\\input"
COLOR_FOR_WERBUNG = "orange"
COLOR_FOR_PROGRAMM ="cornflowerblue"
STATUSES=[["Programm",COLOR_FOR_PROGRAMM],["Werbung",COLOR_FOR_WERBUNG]]

#files = find_csv_filenames(PATH_DATA_TO_BE_JOINED, suffix=".csv" )
df = returnJoinedDataFrame(PATH_DATA_TO_BE_JOINED)
df["Zeit"]=df["Zeit"].astype("datetime64[ns]")
columnArray=["ECR_RATIO","MVL SUM","MVL ABS","RMS","DB","ZCR","MFCC","FARBWECHSEL RATIO","SIFT RATIO","Tag","Zeit","LABEL"]
specificDataFrame = df[columnArray]

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
   
def createSumWerbungProgramHistograms(arrDf,STATUSES):
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
    fig.legend(loc='upper center')    
    plt.show()

def createHeatmap(heatmap):
    ##createHeatmap(specificDataFrame.corr())
    plt.figure(figsize=(13, 6))
    sns.heatmap(heatmap, vmax=1, annot=True, linewidths=.5)
    plt.xticks(rotation=30, horizontalalignment="right")
    plt.show()

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

def createScatterTime(dfWerbung,dfProgramm,columnName1,columnName2):


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=60))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    ax.scatter(dfWerbung[columnName1],dfWerbung[columnName2],color=COLOR_FOR_WERBUNG,label="Werbung",alpha=0.5,s=4)
    ax.scatter(dfProgramm[columnName1],dfProgramm[columnName2],color=COLOR_FOR_PROGRAMM,label="Programm",alpha=0.5,s=4)
    fig.autofmt_xdate()
    # minute_locator = mdates.MinuteLocator(interval=240)
    # hour_locator = mdates.HourLocator(interval=6)
    # axis.xaxis.set_major_locator(minute_locator)
    # myFmt = mdates.DateFormatter('%HH')
    # axis.xaxis.set_major_formatter(myFmt)
    # plt.scatter(dfWerbung[columnName1],dfWerbung[columnName2],color=COLOR_FOR_WERBUNG,label="Werbung",alpha=0.5,s=4)
    # plt.scatter(dfProgramm[columnName1],dfProgramm[columnName2],color=COLOR_FOR_PROGRAMM,label="Programm",alpha=0.5,s=4)
    ax.legend()
    plt.show()

def createScatterTimeY(dfWerbung,dfProgramm,columnName1,columnName2):


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.yaxis.set_major_locator(mdates.MinuteLocator(interval=60))
    ax.yaxis.set_major_formatter(mdates.DateFormatter('%H'))
    ax.scatter(dfWerbung[columnName1],dfWerbung[columnName2],color=COLOR_FOR_WERBUNG,label="Werbung",alpha=0.5,s=4)
    ax.scatter(dfProgramm[columnName1],dfProgramm[columnName2],color=COLOR_FOR_PROGRAMM,label="Programm",alpha=0.5,s=4)
    # minute_locator = mdates.MinuteLocator(interval=240)
    # hour_locator = mdates.HourLocator(interval=6)
    # axis.xaxis.set_major_locator(minute_locator)
    # myFmt = mdates.DateFormatter('%HH')
    # axis.xaxis.set_major_formatter(myFmt)
    # plt.scatter(dfWerbung[columnName1],dfWerbung[columnName2],color=COLOR_FOR_WERBUNG,label="Werbung",alpha=0.5,s=4)
    # plt.scatter(dfProgramm[columnName1],dfProgramm[columnName2],color=COLOR_FOR_PROGRAMM,label="Programm",alpha=0.5,s=4)
    ax.legend()
    plt.show()

def createScatter(dfWerbung,dfProgramm,columnName1,columnName2):


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(dfWerbung[columnName1],dfWerbung[columnName2],color=COLOR_FOR_WERBUNG,label="Werbung",alpha=0.5,s=4)
    ax.scatter(dfProgramm[columnName1],dfProgramm[columnName2],color=COLOR_FOR_PROGRAMM,label="Programm",alpha=0.5,s=4)
    # minute_locator = mdates.MinuteLocator(interval=240)
    # hour_locator = mdates.HourLocator(interval=6)
    # axis.xaxis.set_major_locator(minute_locator)
    # myFmt = mdates.DateFormatter('%HH')
    # axis.xaxis.set_major_formatter(myFmt)
    # plt.scatter(dfWerbung[columnName1],dfWerbung[columnName2],color=COLOR_FOR_WERBUNG,label="Werbung",alpha=0.5,s=4)
    # plt.scatter(dfProgramm[columnName1],dfProgramm[columnName2],color=COLOR_FOR_PROGRAMM,label="Programm",alpha=0.5,s=4)
    ax.legend()
    plt.show()
## REMOVE OUTLIERS AND FALSE NUMBERS ## 
specificDataFrame = removeOutliers(specificDataFrame)

## SPLIT INTO Programm and WERBUNG Frames ##
dfWerbung = specificDataFrame[specificDataFrame['LABEL'] == "Werbung"]
dfProgramm = specificDataFrame[specificDataFrame['LABEL'] == "Programm"]



## PRINT SUM Histograms ##
createSumWerbungProgramHistograms([dfProgramm,dfWerbung],STATUSES)
#createHeatMaps
#createDescriptions


#createHeatmap(specificDataFrame.corr())
#createHeatmap(dfWerbung.corr())
#createHeatmap(dfProgramm.corr())
#createScatterTime(dfWerbung,dfProgramm,'Zeit','ECR_RATIO')
#createScatterTimeY(dfWerbung,dfProgramm,'ECR_RATIO','Zeit')
#createScatter(dfWerbung,dfProgramm,'ECR_RATIO','FARBWECHSEL RATIO')
#createScatter(dfWerbung,dfProgramm,'SIFT RATIO','FARBWECHSEL RATIO')
#createScatter(dfWerbung,dfProgramm,'MVL SUM','MVL ABS')

dfWerbung.describe().to_csv("analysis\output\WerbungDescribe.csv")
dfProgramm.describe().to_csv("analysis\output\ProgrammDescribe.csv")









