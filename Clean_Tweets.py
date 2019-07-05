import pandas as pd

'''
data = pd.read_csv("small_file_50000.txt", header=None, error_bad_lines=False, sep='"', usecols = (0,1,3)) #, usecols = (0,1,3)

df = pd.DataFrame(data) #The third Column over here gives the Created_at
#print(df) 

#This gives us specifically the Created_at Column
dt = df.loc[:,3]
df1 = pd.DataFrame(dt) #df1 is Created_at
print(df1)
'''
######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$###############################

data = pd.read_csv("May_8  (19-19 to 19-21)  (13 Approx Tweets).txt", header=None, error_bad_lines=False, sep='"', usecols = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))

df = pd.DataFrame(data)
#print(df2)
#df2.to_csv("Ch.csv")

dt = df.iloc[:,3] #Created_at
df1 = pd.DataFrame(dt)

dt1 = df.iloc[:,9] #ID
df2 = pd.DataFrame(dt1)

dt2 = df.iloc[:,13] #Tweets
df3 = pd.DataFrame(dt2)


print(df1)
print(df2)
print(df3)

fl = pd.concat([df1, df2], axis=1)
df_f = pd.DataFrame(fl)
#print(df_f)

final = pd.concat([fl, df3], axis=1)
print(final)
#df["new"]= df.iloc[:,1].str.split(" ", n = 1, expand = True)
#print(df)

#dt2.to_csv("Input_Tweet.csv")
final.to_csv("Main40.csv")

