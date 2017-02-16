import psycopg2
import sys
import pprint
import pandas as pd
import matplotlib.pyplot as plt
from ggplot import *

conn_string = "host ='localhost' user = 'postgres' password='postgres'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
cursor.execute('SELECT * from dimes')
colnames = [desc[0] for desc in cursor.description]
records = cursor.fetchall()

dimes = pd.DataFrame(records, columns=colnames)
pprint.pprint(dimes)
plt.interactive(False)
plt.style.use('ggplot')
dimes.plot.scatter(x='price', y='carat')
#ggplot(dimes, aes(x='price', fill='cut')) + geom_density(alpha=0.25) + facet_wrap("clarity")
plt.show()
