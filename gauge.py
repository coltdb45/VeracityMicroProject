import numpy as np
import matplotlib.pyplot as plt

6
colorslist = ['#fc0303','#fc8803','#f8fc03','#17fc03' ,'#22751b' ]

### Defines the Basic Formating of the Dial
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_rmax(2)

ax.set_title("TFOM", va='bottom')
ax.set_rticks([])
# ax.set_xticks([])  



angle =  float(input("TFOM - "))

angle = (-19.286 * angle ) + 244.292


angle = angle * (np.pi / 180)


ax.bar(x=[-0.78,0.156,1.092,2.028,2.964], width=0.936, height = 1.25, bottom = 2.2, color = colorslist, align = "edge")
ax.vlines(angle,0,2) # Angle, Starting Point, Radius

plt.axis('off')
plt.grid(False)
plt.show()



