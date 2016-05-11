#! /usr/bin/env python3
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy import ndimage


def writePos(ax):
    for i in range(0,100):
        ax.text(Eyepos[i][0], Eyepos[i][1], '%d' % i, verticalalignment='center', horizontalalignment='center', color='red', fontsize=12)


#width = 320
#height = 240
#execfile('final_mapping.py')    
#img1 = mpimg.imread('/home/manish/bugeye/image_manip/fiber_320_240.jpg')

width = 640
height = 480
execfile('mapping_640_480.py')    
#img1 = mpimg.imread('/home/manish/bugeye/image_manip/image2_640_480.jpg')
img1 = mpimg.imread('/home/manish/bugeye/image_manip/validate_mapping_image.jpg')

print(img1.shape)
print(img1.dtype)


fig = plt.figure()
ax = fig.gca()
ax.set_xticklabels(np.arange(0,width,5), fontsize=6)
ax.set_yticklabels(np.arange(0,height,5), fontsize=6)
ax.set_xticks(np.arange(0,width,5))
ax.set_yticks(np.arange(0,height,5))

writePos(ax)

plt.imshow(img1,cmap=plt.cm.gray,vmin=0.3,vmax=0.7)
plt.grid()
plt.show()

raise SystemExit

