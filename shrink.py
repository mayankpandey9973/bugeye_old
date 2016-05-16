import os
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy import ndimage
from PIL import Image
from timeit import default_timer as timer
import sys, getopt

def make_small(fin, fout, R, C):
    bigArr = mpimg.imread(fin)
    bigR = len(bigArr)
    bigC = len(bigArr[0])
    print("Shrinking from [%d,%d] to [%d,%d]" % (bigR, bigC, R, C))
    smallArr = np.zeros((R, C, 3), dtype=np.uint8)
    for i in range(R):
	for j in range(C):
	    smallArr[i][j] = (bigArr[i * bigR / R][j * bigC / C])*255
	    #print(i, j, i * bigR / R, j * bigC / C, smallArr[i][j])
    small = Image.fromarray(smallArr, 'RGB')
    small.save(fout)
#

path = os.getenv('PWD')
srcpath = path + '/med'
dstpath = path + '/small'

lst = os.listdir(srcpath)
lst.sort()
for name in lst:
    if (name[:8] == 'proc_out' and name[(len(name)-3):] == 'png'):
        print('Shrinking %s' % (name))
        make_small(srcpath + '/' + name, dstpath + '/' + name, 20, 20)


#make_small('/home/manish/bugeye/sample_images/test10.png', '/home/manish/bugeye/sample_images/test10Small.png', 20, 20)
#make_small('/home/manish/bugeye/sample_images/test11.png', '/home/manish/bugeye/sample_images/test11Small.png', 20, 20)

