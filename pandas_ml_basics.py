import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'],
                   'B': ['one', 'one', 'two', 'three'],
                   'C': np.random.randn(4),
                   'D': np.random.rand(4)})

print df

print df.groupby('B').agg({'C': np.mean, 'D': np.size})

print df.groupby(['A', 'B']).agg({'C': np.mean, "D": np.size})
