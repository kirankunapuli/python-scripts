import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 2, 3, 4, np.nan, 6, 7, 8, 9])

print(s)

dates = pd.date_range('2016-02-15', periods=6)

print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print(df)
