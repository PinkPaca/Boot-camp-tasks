import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

df=pd.read_csv('Advertising.csv') #data set

sns.scatterplot(data=df,x='TV',y='Sales')
plt.show()

x=df['TV'].values
y=df['Sales'].values
reg=LinearRegression()
reg.fit(x,y)

y_pred=reg.predict(x)
plt.figure()
sns.scatterplot(data=df,x='TV',y='Sales')
plt.plot(x,y_pred)
plt.show()

#unknow cofficients
print(reg.coef_)
print(reg.intercept_)
print(reg.predict(np.array([[100]])))

scores=cross_val_score(reg,x.reshape(-1,1),y,cv=6)

print("Cross-validation scores:{}".format(score))

mean_score=np.std(scores)
std_score=np.std(scores)

print("Mean cross-validation score:{:.2f}".format(mean_score))
print("Standard deviation of cross-validation scores: {:.2f}".format(std_score))