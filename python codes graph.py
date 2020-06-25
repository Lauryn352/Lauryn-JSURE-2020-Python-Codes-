
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
### Basic Graph
x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]

# Resize your Graph
plt.figure(figsize=(5,3), dpi=150)

plt.plot(x,y, label='2x', color='purple', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='yellow')

## Line Number Two
x2 = np.arange(0,4.5,0.5)
plt.plot(x2, x2**2, 'r', label='x^2')


plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis!')
plt.ylabel('Y Axis!')

plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10])

plt.savefig('mygraph.png', dpi=200)

plt.legend()

