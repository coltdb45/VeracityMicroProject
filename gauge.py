import numpy as np
import matplotlib.pyplot as plt
import math

### Defines the Basic Formating of the Dial
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_rmax(2)

ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.set_title("TFOM", va='bottom')

### Starts Calculating Where to Draw the Line
ypoints = np.array([math.sqrt(2)/-2,math.sqrt(2)/-2])

plt.plot(ypoints, linestyle = '-')
plt.show()



