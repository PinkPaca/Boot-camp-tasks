import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("insurance.csv")

# Plot a scatter plot with age on the x-axis and charges on the y-axis
plt.figure()
sns.scatterplot(data=df, x = 'age', y = 'charges')
plt.show()
plt.close()

# fit a model to data, and make prediction on data
lin_model = LinearRegression()
X = df['age'].values.reshape(-1,1)
y = df['charges'].values

lin_model.fit(X,y)
y_pred = lin_model.predict(X)

# Plot another scatter plot with the best-fit line
plt.figure()
sns.scatterplot(data=df, x = 'age', y = 'charges')
plt.plot(X, y_pred, color = 'r')
plt.show()
plt.close()

