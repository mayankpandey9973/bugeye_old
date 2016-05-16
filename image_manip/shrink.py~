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
    print(bigR, bigC)
#    R = bigR
#    C = bigC
#smallArr = np.zeros((R, C, 3));
    print(R, C)   
    smallArr = np.zeros((R, C, 3), dtype=np.uint8)
    for i in range(R):
	for j in range(C):
	    smallArr[i][j] = bigArr[i * bigR / R][j * bigC / C]
	    print(i, j, i * bigR / R, j * bigC / C, smallArr[i][j])
    small = Image.fromarray(smallArr, 'RGB')
    small.save(fout)
#



    


make_small('/home/manish/bugeye/sample_images/mid1.jpg', '/home/manish/bugeye/sample_images/mid1Small.jpg', 20, 20)
