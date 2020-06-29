
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
### Basic Graph
x = [1,2,3,4,5,6]
y = [500,10000,30000,80000,650000,300000]

# Resize your Graph
plt.figure(figsize=(5,3), dpi=150)

plt.plot(x,y, label='2x', color='purple', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')


plt.title('MCF7 Cell Growth', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('Days')
plt.ylabel('Viability')

plt.xticks([0,1,2,3,4,5,6])
plt.yticks([0,100000,200000,300000,400000,500000,600000,700000])

plt.savefig('mygraph.png', dpi=200)

plt.legend()

