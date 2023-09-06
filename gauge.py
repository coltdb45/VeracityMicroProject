import numpy as np
import matplotlib.pyplot as plt


colorslist = ['#22751b','#17fc03','#f8fc03','#fc8803','#fc0303']

### Defines the Basic Formating of the Dial
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_rmax(2)

ax.set_title("TFOM", va='bottom')
ax.set_rticks([])
# ax.set_xticks([])  


ax.vlines(5*np.pi/4,0,2) # Angle, Starting Point, Radius

plt.grid('off')
plt.show()



