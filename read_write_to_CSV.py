import pandas as pd
#Skiping a row while importing the df

df=pd.read_csv("output.csv",skiprows=1)


print(df)


#removing the header

df1=pd.read_csv("output.csv",header=None)
print(df1)

#adding names for the columns

df2=pd.read_csv("output.csv",header=None,names=["God","Name","T1","T2","T4"])


print(df2)

# limiting the number of rows
df4=pd.read_csv("output.csv",nrows=4)
print(df4)

#replacing na with NaN
df = pd.read_csv("output.csv", na_values=["n.a.", "not available"])

df = pd.read_csv("output.csv",  na_values={
        'State': ['Mississippi']
    })




print(df)



#to export csv


df.to_csv("new.csv", index=False)




#Export only one colum


df.to_csv("new.csv", columns=["State"], index=False)


