#import pandas as pd
#import numpy as np
# data={"Name":["John","Peter","Lisa"],"Age":[25,28,31],"Salary":[30000,4859,20384]}
# df=pd.DataFrame(data)
# print(df)
# data1=pd.read_csv("company.csv")
# print(data1)
#data2=pd.read_excel("Orders-With-Nulls.xlsx")
#exploring data
# print(data2)
# print(data2.head())
# print(data2.tail())
# print(data2.info())
# print(data2.describe())
# print(data2.isnull())
# #dealing with duplicate values
# data3=pd.read_excel("Orders-With-Nulls.xlsx")
# print(data3)
# print(data3["Order ID"].duplicated())
# dataa=pd.read_csv("companyy.csv")
# print(dataa["ID"].duplicated())
#data3=pd.read_csv("company.csv")
# print(data3["ID"].duplicated())
#working with missing data in 
#print(data1.isnull().sum())
#print(data3.isnull())
#print(data3.dropna())
#print(data3.replace(np.nan,"hi"))
#data3["Salary"] = data3["Salary"].replace(np.nan,"834759")
#print(data3)
#print(data3.fillna(method="bfill"))
#print(data3.fillna(method="ffill"))
#print(data3.fillna("sriyanka"))
#print(data3["Salary"].mean())
#data3["Salary"] = data3["Salary"].replace(np.nan,"350000")
#column transformation in pandas
#print(data2)
#data2.loc[(data2["Order ID %"] >10 ,"bigger")]="hsd"
#data2.loc[(data2["Order ID %"] <10 ,"smaller")]="eye"
#print(data3.head(10))
#data2["Concatenated"]= data2["Customer Segment"].str.capitalize() +" "+ data2["Product Category"].str.capitalize()
#print(data2)
#column transformation in padas 2
#data=pd.read_excel("account.xlsx")
#print(data)
#data["bonus"] = (data["Sno"]/100)*10
#print(data)
# def extract(value):
#     return value[0:3]
# data={"months":["janauary","february","march","april"]}
# a=pd.DataFrame(data)
# print(a)
# a["short_months"]=a["months"].map(extract)
# print(a)
#group by pandas
#print(data.head(10))
# gp= data.groupby("Sno").agg({"Progress":"max"})
# print(gp)
#merge,join and concatenate in pandas
# #print(data)
# data1={"Balance":["1898.10 Cr","1962.76 Cr","327.52 Cr","257.11 Cr"],"Sno":[1,2,3,4]}
# data2={"Sno":[1,2,3,4],"Balance":["1800.10 Cr","1960.76 Cr","300.52 Cr","200.11 Cr"]}
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)
# print(df1)
# print(df2)
#print(pd.merge(df1,df2,on ="Sno",how="left"))
# print(pd.concat([df1,df2]))
#pandas compare dataframes
# dict={"Fruits":["mango","apples","banana","papaya"],
# "price":[100,150,50,35],"Quantity":[15,10,19,2]}
# df=pd.DataFrame(dict)
# print(df)
# df2=df.copy()
# df2.loc[0,"price"]=120
# df2.loc[1,"price"]=100
# df2.loc[3,"price"]=70
# df2.loc[0,"Quantity"]=3
# df2.loc[1,"Quantity"]=23
# df2.loc[2,"Quantity"]=10
# print(df2)
# print(df.compare(df2))
#pivoting
 #{
#dict={"keys":["k1","k2","k1","k2"],
#"names":["john","ben","david","peter"],
#"houses":["red","blue","green","red"]}
#df=pd.DataFrame(dict)
# print(df)
# print (df.pivot(index="keys",columns="names",values="houses"))
# dict={"keys":["k1","k2","k1","k2"],
# "names":["john","ben","david","peter"],
# "houses":["red","blue","green","red"]}
# df=pd.DataFrame(dict)
# print(df)
# print(pd.melt(df,id_vars=["names"],value_vars=["houses","keys"]))
# print(pd.melt(df,id_vars=["names"],value_vars=["houses","keys"],var_name="houses and grades",value_name="values"))
