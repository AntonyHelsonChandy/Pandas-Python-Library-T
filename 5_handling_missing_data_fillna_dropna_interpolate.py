import pandas as pd

pf=pd.read_csv("stock_data.csv")


print(pf)


#used to fill the NaN with some value

s=pf.fillna("fuck you")


print(s)
pf1=pd.read_csv("stock_data.csv")
ew_df = pf1.fillna({
        'price':555555555 ,
        'eps': 0
    })
print(pf1)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print(ew_df)

print("%%%%%%%%%%%%")



#used to interpulate NaN its good stuff

pf2=pd.read_csv("weather_data.csv")
print(pf2)
new_df = pf2.interpolate()
print(new_df)





new_df = df.dropna()
new_df







new_df = df.dropna(how='all')
new_df





new_df = df.dropna(thresh=1)
new_df






