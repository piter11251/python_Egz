import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y1 = x+4
y2 = -x-6
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, color='r')
ax2.plot(x, y2, color='b')
plt.show()