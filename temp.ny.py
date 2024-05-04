import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r"C:\Users\Vishnuvardhana chary\OneDrive\Desktop\cereal.csv")
data.head()
data.describe()
data.info()
data.isnull().any()
data.drop(["name"], axis =1, inplace = True)

plt.figure(figsize=(14,8))
sns.heatmap(data.corr(),annot=True)
data.corr()
plt.figure(figsize=(10,6))
sns.boxplot(data=data,x="mfr",y="rating")
sns.pairplot(data=data,markers=["^","v"],palette="inferno")
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data["mfr"]=le.fit_transform(data["mfr"])
data["type"]=le.fit_transform(data["type"])
data
x=data.iloc[:,0:14].values
y=data.iloc[:,14:15].values
x
y
from sklearn.preprocessing import OneHotEncoder
one=OneHotEncoder()
a=one.fit_transform(x[:,0:1]).toarray()
x=np.delete(x,[0],axis=1)
x=np.concatenate((a,x),axis=1)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
#model Buliding
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)
lr_pred=lr.predict(x_test)
lr_pred
y_p=lr.predict([[0,0,0,0,1,0,0,0,70,4,1,130,10,5,6,280,25,3,1,0.33]])
y_p
#model eluvation
from sklearn.metrics import r2_score
r2_score(y_test, lr_pred)
import pickle
pickle.dump(lr,open("cerealanalysis.pkl","wb"))


