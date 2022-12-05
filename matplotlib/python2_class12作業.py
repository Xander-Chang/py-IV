# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 04:02:08 2022

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.arange(1,6)
listx = list(np.arange(1,6))
listx1 = list(x - 0.1 for x in range(len(listx)))
listx2 = list(x + 0.1 for x in range(len(listx)))

plt.bar(listx1, [3, 10, 8, 12, 6], width=0.2, ec='#084c61', fc='#e63946')
plt.bar(listx2, [6, 3, 12, 5, 8], width=0.2, ec='none', fc='#7fb069')
plt.title('並列長條圖', fontsize=16)
plt.legend()
plt.xlabel('x軸', fontsize=12)
plt.ylabel('y軸', fontsize=12)


plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' 
plt.rcParams['axes.unicode_minus'] = False
plt.show()