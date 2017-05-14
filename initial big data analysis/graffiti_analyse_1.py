import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime

#chunksize = 5
data = pd.read_csv('/home/karan/graffiti.csv')
data1=data['Media URL']
df3=data1.fillna(0)
print df3
df3.to_csv('grafitti_links.csv',mode='w')