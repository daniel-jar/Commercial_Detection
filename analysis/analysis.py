from itertools import count
from logging import makeLogRecord
from re import X
from tkinter import Y
from turtle import color, xcor
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
OUTLIER_LIMIT_RMS = [0,200]

#Outliers
MVL_SUM = [-1000, 1000]
MVL_ABS = [0,5000]
RMS = [0, 0.2]
SIFT = [0, 1]
ECR = [0.001, 0.999]

# Without Outliers
# MVL_SUM = [-99000, 99000]
# MVL_ABS = [-155000,155000]
# RMS = [0, 1000]
# SIFT = [0, 1000]
# ECR = [0.001, 0.999]

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
    specificDataFrame = specificDataFrame[specificDataFrame['MVL SUM'].between(MVL_SUM[0],MVL_SUM[1])] 
    print("MVL Sum Outliers entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame =specificDataFrame[specificDataFrame['MVL ABS'].between(MVL_ABS[0],MVL_ABS[1])] 
    print("MVL ABS Outliers entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame = specificDataFrame[specificDataFrame['RMS'].between(RMS[0],RMS[1])]  
    print("RMS Outliers entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame = specificDataFrame[specificDataFrame['SIFT RATIO'].between(SIFT[0],SIFT[1])]  
    print("SIFT RATIO Outliers entfernt: "+str(len(specificDataFrame))) 
    specificDataFrame = specificDataFrame[specificDataFrame['ECR_RATIO'].between(ECR[0],ECR[1])]  
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

def make_labels(ax, boxplot):

    # Grab the relevant Line2D instances from the boxplot dictionary
    iqr = boxplot['boxes'][0]
    caps = boxplot['caps']
    med = boxplot['medians'][0]
    fly = boxplot['fliers'][0]

    # The x position of the median line
    xpos = med.get_xdata()

    # Lets make the text have a horizontal offset which is some 
    # fraction of the width of the box
    xoff = 0.10 * (xpos[1] - xpos[0])

    # The x position of the labels
    xlabel = xpos[1] + xoff

    # The median is the y-position of the median line
    median = med.get_ydata()[1]

    # The 25th and 75th percentiles are found from the
    # top and bottom (max and min) of the box
    pc25 = iqr.get_ydata().min()
    pc75 = iqr.get_ydata().max()

    # The caps give the vertical position of the ends of the whiskers
    capbottom = caps[0].get_ydata()[0]
    captop = caps[1].get_ydata()[0]

    # Make some labels on the figure using the values derived above
    ax.text(xlabel, median,
            'Median = {:6.3g}'.format(median), va='center')
    ax.text(xlabel, pc25,
            '25th percentile = {:6.3g}'.format(pc25), va='center')
    ax.text(xlabel, pc75,
            '75th percentile = {:6.3g}'.format(pc75), va='center')
    ax.text(xlabel, capbottom,
            'Bottom cap = {:6.3g}'.format(capbottom), va='center')
    ax.text(xlabel, captop,
            'Top cap = {:6.3g}'.format(captop), va='center')

    # Many fliers, so we loop over them and create a label for each one
    for flier in fly.get_ydata():
        ax.text(1 + xoff, flier,
                'Flier = {:6.3g}'.format(flier), va='center')

def createBoxplots(columnArray,dataFrames):
    ## Create Boxplots ## 
    fig, axes = plt.subplots(nrows=5, ncols=2, sharey=True)
    plotCounter=-1
    medianprops = dict(color='firebrick')
        #dfWerbung.boxplot(x,color=COLOR_FOR_WERBUNG)
    for triaxis in axes:
        for ax in triaxis:
            plotCounter+=1
            x = columnArray[plotCounter]
            if x != "Zeit" and x!= "LABEL" and x!="Tag":
                my_dict = {'Werbung': dataFrames[1][x],'Programm': dataFrames[0][x]}
                red_square = dict(marker="|",mew=0.5,markersize=10,alpha=.1)
                box_dict=ax.boxplot(my_dict.values(),vert=False,labels=("Werbung","Programm"),medianprops=medianprops,showcaps=True,notch=True,flierprops=red_square)
                ax.set(title=x)
                c = COLOR_FOR_WERBUNG
                colors = [COLOR_FOR_WERBUNG,COLOR_FOR_PROGRAMM]
                #newAx[0] = plt.boxplot(dataFrames[0][x], notch=True, patch_artist=False)
                #boxplotWerbung = plt.boxplot(dataFrames[0][x], notch=True, patch_artist=False)
                    # boxprops=dict(facecolor=c, color=c),
                    # capprops=dict(color=c),
                    # whiskerprops=dict(color=c),
                    # flierprops=dict(color=c, markeredgecolor=c),
                    # medianprops=dict(color=c))
                    # medianprops=dict(color=c))
                #print(ax[0])
                    # medianprops=dict(color=c))
                ylabel=0
                plt.rc('font', size=7) 
                for item in ['boxes', 'fliers', 'medians', 'means']:
                    marklabelCounter=-1
                    for sub_item,color in zip(box_dict[item], colors):
                        marklabelCounter+=1
                        if item!="medians":
                            plt.setp(sub_item, color=color)
                        if item!="fliers":
                            ypos = sub_item.get_ydata()
                            yoff = (ypos[1] - ypos[0])
                            ylabel = ypos[1]

                        if item=="boxes":
                            pc25 = sub_item.get_xdata().min()
                            pc75 = sub_item.get_xdata().max()
                            ax.text(pc25, ylabel+yoff*0.8,'Q1:{:6.3g}'.format(pc25), va='center')
                            ax.text(pc75, ylabel+yoff*0.8,'Q3:{:6.3g}'.format(pc75), va='center')        
                        if item == "medians":
                            median = sub_item.get_xdata()[1]
                            ax.text(median, ylabel+yoff*4,u'\u03bc:{:6.3g}'.format(median), va='center')
                            ax.text(median, ylabel-yoff*4,'σ:{:6.3g}'.format(dataFrames[marklabelCounter][x].std()), va='center')
                            

                for item in ['whiskers', 'caps']:
                    for sub_items,color in zip(zip(box_dict[item][::2],box_dict[item][1::2]),colors):
                        plt.setp(sub_items, color=color)
                        if item == "caps":
                            capbottom = sub_item.get_xdata()[0]
                            captop = sub_item .get_xdata()[0]
                            ax.text(-10, ylabel-30,'m:{:6.3g}'.format(capbottom), va='center')
                            ax.text(-10, ylabel-30,'M:{:6.3g}'.format(captop), va='center')
                plt.rc('font', size=10) 

    manager=plt.get_current_fig_manager()
    manager.full_screen_toggle()
    #fig.legend(loc='upper left')
    fig.set_size_inches(SIZE_OF_PLOTS)
    #fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    #plt.yticks((["Programm","Werbung"]))
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.1, 
                    hspace=0.5)
    plt.suptitle("Boxplots für alle Merkmale", fontsize=14)  
    plt.savefig(OUTPUT_PATH+'boxplots.png')             
    plt.show()

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

## CREATE BOXPLOTS ##
createBoxplots(columnArray,[dfProgramm,dfWerbung])

## CREATE HEATMAPS ##
createHeatmaps([dfProgramm.corr(),dfWerbung.corr()])

# ## PRINT SUM Histograms ##
createSumWerbungProgramHistograms([dfProgramm,dfWerbung],STATUSES,columnArray)

for x in columnArray:
    createScatters(dfProgramm,dfWerbung,x,columnArray)

# dfWerbung.describe().to_csv(OUTPUT_PATH+"WerbungDescribe.csv")
# dfProgramm.describe().to_csv(OUTPUT_PATH+"ProgrammDescribe.csv")










