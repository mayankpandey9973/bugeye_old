#! /usr/bin/env python3
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy import ndimage

def onclick(event):
    eyenum = int(input("#eyenum: "))
    print('Eyepos[%d] = [%d, %d]' %
          (eyenum, event.xdata, event.ydata))
    target.write('Eyepos[%d] = [%d, %d]\n' %
          (eyenum, event.xdata, event.ydata))


#xsize = 320
#ysize = 240
#img1 = mpimg.imread('/home/manish/bugeye/image_manip/fiber_320_240.jpg')

xsize = 640
ysize = 480
img1 = mpimg.imread('/home/manish/bugeye/image_manip/image2_640_480.jpg')

print(img1.shape)
print(img1.dtype)


fig = plt.figure()
ax = fig.gca()
ax.set_xticklabels(np.arange(0,xsize,20), fontsize=10)
ax.set_yticklabels(np.arange(0,ysize,20), fontsize=10)
ax.set_xticks(np.arange(0,xsize,20))
ax.set_yticks(np.arange(0,ysize,20))

cid = fig.canvas.mpl_connect('button_press_event', onclick)
#filename = string(input("filename: "))
filename = "mapping.py"
print("Opening file %s" % (filename))
target = open(filename, 'w')
target.write('Eyepos = [None]*100\n')

plt.imshow(img1,cmap=plt.cm.gray,vmin=0.3,vmax=0.7)
plt.grid(b=True, which='major', color='r', linestyle='dotted')
plt.show()

target.close()
raise SystemExit

