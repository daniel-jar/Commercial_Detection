import pandas as pd
from chefboost import Chefboost as chef
import shutil

SOURCE_FILE = "analysis/output/zusammenGeführte.csv"
DEST_FILE = "machineLearning/learningDataset/learningDataset.csv"
PATH_OUTPUT = "/machineLearning/output/"
METHODS=["C4.5","ID3","CART","CHAID","Regression"]
TEST_INSTANCE_PRORGRAMM = ["0.200774984229972","-0.1762085","1.9467163","0.0300912503433332","-25.932773660599228","23","175.62573670168138","0.0110108653559198","0.1876172607879924","3","14:46"]
TEST_INSTANCE_WERBUNG = ["0.3295492265816902","-0.85956573","4.3736343","0.0235908078249458","-28.496519466265845","102","171.53235835878542","0.0275269652343746","0.1470588235294117","4","10:18"]
shutil.copyfile(SOURCE_FILE, DEST_FILE)



df = pd.read_csv(DEST_FILE)
df.drop(columns=df.columns[0], axis=1, inplace=True)
print(len(df))
config = {'algorithm': 'ID3','enableParallelism': False}
model = chef.fit(df, config = config, target_label = 'LABEL')

resultP = chef.predict(model,TEST_INSTANCE_PRORGRAMM)
resultW = chef.predict(model,TEST_INSTANCE_WERBUNG)

print (resultP)
print (resultW)


#shutil.move("/outputs/", "/machineLearning/outputs/")