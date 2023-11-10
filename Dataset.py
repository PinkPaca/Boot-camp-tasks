import pandas as pd

df=pd.read_csv('balance.txt',delim_whitespace=True)

#Compare the average income based on ethnicity.
print(df.groupby(['Ethnicity'])['Income'].mean())

#Compare the average income based on ethnicity.
print("The average income of married people is ", df[df.Married=="Yes"].loc[:,"Balance"].mean())
print("The average income of single people is ", df[df.Married=="No"].loc[:,"Balance"].mean())
print("Single people have a higher balance on average.")

#What is the highest income in our dataset?
print("The highest income is ",df.loc[:,"Income"].max())
#What is the lowest income in our dataset?
print("The lowest income is ",df.loc[:,"Income"].min())

#How many cards do we have recorded in our dataset?
print("The number of cards we have recorded is ",len(df.columns))

#How many females do we have information for vs how many males? 
print("The number of females whose we have information is ",df[df.Gender=="Female"].loc[:,"Gender"].count())
print("The number of males whose we have information is ",df[df.Gender=="Male"].loc[:,"Gender"].count())