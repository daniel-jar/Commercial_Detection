import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import numpy as np

PATH_DATA_TO_BE_JOINED = "dataToBeJoined/"

print(os.getcwd())
df = pd.read_csv('analysis/logoDetection.csv')
print(df.head(1))



df['color'] = np.where(df['LABEL'] == "Programm","green","red")
df['color']=df['color'].astype(float)
df['color'].plot(kind='hist')
plt.show()




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