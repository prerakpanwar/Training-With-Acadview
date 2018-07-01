import pandas as pd


#Q1-Create a dataframe with your name, age, mail-id and phone number and add your friends’s information to the same.

data = {'Name':['Prerak'],'Age':[21],'mail id':['panwarprerak98@gmail.com'],'phone no':['8126xxxxxx']}
df = pd.DataFrame(data)
df.loc[1]=['Shitiz',21,'shitiz11@gmail.com','8129xxxxxx']       #Add detail of friend 1
df.loc[2]=['Ramu',21,'ramu456788@gmail.com','7033xxxxxx']       #Add detail of friend 2
print(df)
print("\n")



#Q2-Import the data from "https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv" and print:

df=pd.read_csv('weather.csv')
#print(df)

#a.) First 5 rows of Dataframe
print(df.head(5))

#b.) First 10 rows of the Dataframe
print(df.head(10))

#c.) Find basic statistics on the particular dataset.
print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())

#d.) Find the last 5 rows of the dataframe
print(df.tail(5))

#e.) Extract the 2nd column and find basic statistics on it.
finaldata=[df.iloc[:,2].sum(),
df.iloc[:,2].mean(),
df.iloc[:,2].median(),
df.iloc[:,2].nunique(),
df.iloc[:,2].max(),
df.iloc[:,2].min()]
print(finaldata) 