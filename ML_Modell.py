import pandas as pd
from chefboost import Chefboost as chef
import shutil
import sys



# sys.stdout = open("machineLearning/learningLog.txt", "w")

SOURCE_FILE = "analysis/output/zusammenGeführte.csv"
DEST_FILE = "machineLearning/learningDataset/learningDataset.csv"
CROSS_VALIDATION_FILE = "machineLearning/datensatzKreuzvalidierung/datensatzKreuzvalidierung.csv"

EVALUATION_DATAFRAME = pd.DataFrame(columns=["Method",'Postive',"Negative","Sum","Accuracy"])

SOURCE_MODEL = r"outputs/"
DESTINATION_MODEL =r"machineLearning/trainedModels/"

PATH_OUTPUT = "/machineLearning/output/"
METHODS=["C4.5","ID3","CART","CHAID","Regression"]
TEST_INSTANCE_PRORGRAMM = [0.200774984229972,-0.1762085,1.9467163,0.0300912503433332,-25.932773660599228,23,175.62573670168138,0.0110108653559198,0.1876172607879924,3,1446]
TEST_INSTANCE_WERBUNG = [0.3295492265816902,-0.85956573,4.3736343,0.0235908078249458,-28.496519466265845,102,171.53235835878542,0.0275269652343746,0.1470588235294117,4,1018]

shutil.copyfile(SOURCE_FILE, DEST_FILE)

df = pd.read_csv(DEST_FILE)
df.drop(columns=df.columns[0], axis=1, inplace=True)
newFrame=df.replace({':': ''}, regex=True).copy()
df=newFrame
df["Zeit"]=df["Zeit"].astype("int64")


dfCross_Validation = pd.read_csv(CROSS_VALIDATION_FILE)
dfCross_Validation.drop(columns=dfCross_Validation.columns[0], axis=1, inplace=True)
newFrame=dfCross_Validation.replace({':': ''}, regex=True).copy()
dfCross_Validation=newFrame
dfCross_Validation["Zeit"]=dfCross_Validation["Zeit"].astype("int64")
COLUMN_ARRAY=["ECR_RATIO","MVL SUM","MVL ABS","RMS","DB","ZCR","MFCC","FARBWECHSEL RATIO","SIFT RATIO","Tag","Zeit","LABEL"]
dfCross_Validation = dfCross_Validation[COLUMN_ARRAY]

print(len(df))
print(len(dfCross_Validation))
for method in METHODS:
    if method=="Regression":
        newFrame=df.replace({'Programm': 1}, regex=True).copy()
        df=newFrame
        newFrame=df.replace({'Werbung': 0}, regex=True).copy()
        df=newFrame
    config = {'algorithm': method,'enableParallelism': False}
    model = chef.fit(df, config = config, target_label = 'LABEL')
    chef.save_model(model, method+"trained_model.pkl")
    shutil.copytree(SOURCE_MODEL, DESTINATION_MODEL+method)
    countPositive=0
    countNegative=0
    sum=len(dfCross_Validation)
    for index,instance in dfCross_Validation.iterrows():
        prediction = chef.predict(model,instance)
        actual = instance['LABEL']
        if actual == prediction or (method == "Regression" and (( actual=="Programm" and prediction == 1) or (actual == "Werbung" and prediction==0))) :
            countPositive+=1
        else:
            countNegative+=1
    accuracy = str((countPositive/sum)*100)+"%"
    print("____________________________________")
    print("METHOD: "+method+" COUNTPOSITIVE: "+str(countPositive)+" COUNTNEGATIVE: "+str(countNegative)+" SUM: "+str(sum)+" ACCURACY: "+accuracy)
    new_row = pd.DataFrame({'Method':[method], 'Postive':[countPositive], 'Negative':[countNegative], 'Sum':[sum],'Accuracy':[accuracy]}) 
    EVALUATION_DATAFRAME = pd.concat([EVALUATION_DATAFRAME, new_row])
    print("____________________________________")
#sys.stdout.close()

EVALUATION_DATAFRAME.to_csv("results.csv")