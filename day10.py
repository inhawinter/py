import pandas as pd

df = pd.DataFrame([[4, 7, 13],
                   [5, 8, 11],
                   [60, 9, 12]],
                   index=[1, 2, 3],
                   columns=['a', 'b', 'c'])

# def squares(n):
#     return n * n

print(df)
print(df.apply(lambda n: n * n))
# print(df.apply(squares))
# print(df.describe())
