# pandas
# pip install pandas  # installation
import pandas as pd

# df = pd.DataFrame({"a" : [4, 5 , 6],
#                     "b" : [7, 8, 9],
#                     "c" : [10, 11, 12]},
#                     index=[1, 2, 3])

df = pd.DataFrame([[4, 7, 10],
                   [5, 8, 11],
                   [6, 9, 12]],
                   index=[1, 2, 3],
                   columns=['a', 'b', 'c'])

print(df)
#print(df.loc[:,['a', 'c']])
print(df.loc[df['b']>8,['a', 'c']])

df1 = (pd.melt(df)
        .rename(columns={
                'variable' : 'var',
                'value' : 'val'})
        .iloc[:,[1]]
        #.iloc[:5]
        #.query('val >= 7')
)
print(df1)
print(df1.sort_values('val', ascending=False))
