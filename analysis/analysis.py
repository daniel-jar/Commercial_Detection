from tkinter import Y
from async_generator import yield_from_
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np
import time

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

PATH_DATA_TO_BE_JOINED = "dataToBeJoined/"
COLOR_FOR_WERBUNG = "tab:orange"
COLOR_FOR_PROGRAMM ="tab:blue"

print(os.getcwd())
df = pd.read_csv('analysis/logoDetection.csv')
print(df.head(1))


dfWerbung = df[df['LABEL'] == "Werbung"]
dfProgramm = df[df['LABEL'] == "Programm"]

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


x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title("main")
axs[1, 0].plot(x, y**2)
axs[1, 0].set_title("shares x with main")
axs[1, 0].sharex(axs[0, 0])
axs[0, 1].plot(x + 1, y + 1)
axs[0, 1].set_title("unrelated")
axs[1, 1].plot(x + 2, y + 2)
axs[1, 1].set_title("also unrelated")
fig.tight_layout()

plt.show()


