import pandas as pd

df = pd.DataFrame(
    [(1, 2, None, 4),
     (1, None, None, None),
     (None, 3, 8, None),
     (None, None, 4, None)],
    columns=['a', 'b', 'c', 'd'],
    index=['A', 'B', 'C', 'D'])

print(df)
print('\nNaN occurrences in Columns:')
print(df.isnull().sum(axis=0))
