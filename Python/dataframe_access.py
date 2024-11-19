import pandas as pd
import numpy as np

f1 = np.array([ 12.3,  45.6,  78.9])
f2 = np.array([ 10.11,  12.13,  14.15])
f3 = np.array([ 1. ,  2.5,  5. ])
s1 = np.array(['foo', 'bar', 'baz'])
d1 = np.array(['2015-04-30T02:58:22.000+0200', '2015-04-30T02:58:22.000+0200',
               '2015-04-30T02:58:22.000+0200'], dtype='datetime64[ms]')
df = pd.DataFrame({
                  'f1':f1,
                  'f2':f2,
                  'f3':f3,
                  'str1':s1,
                  'date':d1
                  })
df.to_csv('out.csv')
print (df)
print(df['f1'])
print (df.iat[0, 0])
print (df.at[0, 'f1'])

col_one_to_list = df['f1'].tolist()
print (col_one_to_list)

col_one_to_list_1 =  df.iloc[:,0].tolist()
print (col_one_to_list_1)


col_one_to_arr = df['f1'].to_numpy()
print (col_one_to_arr)
