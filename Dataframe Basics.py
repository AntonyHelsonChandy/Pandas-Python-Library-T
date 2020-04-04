import pandas as pd
#loading the csv file using the method
df=pd.read_csv("output.csv");

print(df.head())
# creating a dictionary with key values
thisdict={
        'brand':["BMW","Ford"],
        'year':[1947,1423]

        }
#converting it into a Dataframe
print("#################")
df1=pd.DataFrame(thisdict);
print(df1.head())

#Finding the dimension of the Dataframe

print("#################")

print(df.shape)


rows,columns=df.shape

print("Rows:",rows)
print("Columsn:",columns)

#displaying the last element at the df

print(df.tail(1))
#Dsplaying the rows from 5 will 10(excluding 10)

print(df[5:10])

#Prints everting 

print(df[:])

#display the name of the columns


print(df.columns)


#displaying two columns
print(df[['State','Year']])

#findin the maximum value in a column, there are also functions such as mean(),min(),std()
print(df.Year.std())

# lets see the describe() function, which gives all stat values

print(df.describe())


print(df.Year.describe())


#trying out if condiction inside the datframe

print(df[df.Year==df.Year.max()])


#getting other colams value wile making a if


print(df[["Year","Month"]][df.Year==df.Year.max()])

# To see the stepsize of the DF


print(df.index)

#To change the index of the DF, those 0 and 1 stuff


print(df.set_index("Year",inplace=True))
print(df)
#use ilock to lock on a perticular ra



print(df.loc[2009])

# to reset the index
print(df.reset_index(inplace=True))
print(df)
