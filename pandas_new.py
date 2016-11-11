import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('Hello, Kiran!\n')
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print('Printing s: \n', s)
dates = pd.date_range('20160101', periods=6)
print('Printing dates: \n', dates)
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))
print('Printing df: \n', df)
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print('Printing df2: \n', df2)
