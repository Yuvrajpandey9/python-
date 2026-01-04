import pandas as pd
s={'id':["@#123abs4","@#fgh444","#@8jk8l8"],'name':["john","sam","raju"],'salary':[20000,40000,8000],'city':["jaipur","noida","delhi"]}
dg={'school':["vbps","dps","smc","bhs"],'fee':[5000,12000,7000,9000],'bus service':["yes","no","yes","yes"]}
df=pd.DataFrame(s)
d=pd.DataFrame(dg)
print(df)
print(d)
df.to_csv("libraries1.csv",index=False)
d.to_csv("libraries.csv")