#!/usr/bin/python2.7
##!/usr/bin/env python3
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

dirname=''
writeHex = False
writeMed = False
writeSmall = False
intrplBlanks=True

def diffimage(infile1, infile2, difffile):

    img1 = mpimg.imread(infile1)
    img2 = mpimg.imread(infile2)
    #print(img1[200,200])
    #print("\n")
    #print(img2[200,200])
    diffimg = np.absolute(img1 - img2)
    #print(diffimg[200,200])
    for elt in np.nditer(diffimg, op_flags=['readwrite']):
        y += 3
    for x in range(len(img1)):
        for y in range(len(img1[x])):
            diffimg[x,y,2] = diffimg[x,y,2]*0.3
            for z in range(len(img1[x,y])):
                if(img1[x,y,z] != 0):
                    if(diffimg[x,y,z]/img1[x,y,z] < 0.03):
                        diffimg[x,y,z] = 0
               # diffimg[x,y,z] = 10*diffimg[x,y,z]
               # if(diffimg[x,y,z] > 1):
               #     diffimg[x,y,z]=1
                
    #diffimg[200,200]=[1,0.01,0.01]
    misc.imsave(difffile, diffimg)


    
def diffimage2(infile1, infile2, difffile):

    img1 = mpimg.imread(infile1)
    img2 = mpimg.imread(infile2)
    #print(img1[200,200])
    print("\n")
    #print(img2[200,200])
    diffimg = np.absolute(img1 - img2)
    #print(diffimg[200,200])
    for x in range(len(img1)):
        for y in range(len(img1[x])):
            diffimg[x,y,2] = diffimg[x,y,2]*0.15
            for z in range(len(img1[x,y])):
                if(img1[x,y,z] != 0):
                    if(diffimg[x,y,z]/img1[x,y,z] < 0.06):
                        diffimg[x,y,z] = 0
                diffimg[x,y,z] = 10*diffimg[x,y,z]
                if(diffimg[x,y,z] > 1):
                    diffimg[x,y,z]=1
                
    #diffimg[200,200]=[1,0.01,0.01]
    misc.imsave(difffile, diffimg)

#Semi-related, but I had the same issue with matplotlib.image.imsave -
#it would save an 8-bit grayscale image as 16-bit, which ballooned the size,
#even after using scipy.misc.bytescale to make sure it was an 8-bit array.
#However, scipy.misc.imsave saved it correctly as an 8-bit image.


   
def main():

    #Given sequence of form proc_out00001.png to proc_out<N>.png, create diff00001.png to diff<N-1>.png
    #Convert images captured in <dirname> 
    #Usage:
    #diff_sequence.py --dir=<dirname> [--med | --small | --hex]
    #
    #Options:
    #-dir: specify directory name to do processing
    global dirname
    global writeHex
    global writeMed
    global writeSmall

    try:
        opts, args = getopt.getopt(sys.argv[1:],"x",["dir=","hex","med","small"])
    except getopt.GetoptError:
        print("diff_sequence.py --dir=<dirname> [--med | --small | --hex]")
        sys.exit(2)
    for opt, arg in opts:
       if opt == '--help':
           print('diff_sequence.py -dir=<dirname> [--med | --small | --hex]')
           sys.exit()
       elif opt in ("--dir"):
           dirname = arg
       elif opt in ("--hex"):
           writeHex = True
       elif opt in ("--med"):
           writeMed = True
       elif opt in ("--small"):
           writeSmall = True
       else:
        print('Option Error: unknown option specified')
        sys.exit(2)
           
    path = ""

    #if directory name begins with /, then it is the absolute name.
    #if the dirname begins with ~, then replace ~ with home dir
    #if the dirname is ., then choose cwd as the dir name
    #else append thedirname to basepath
    if(dirname[0] == '/'):
        path = dirname
    elif(dirname[0] == '~'):
        homedir = os.getenv('HOME')
        path = homedir + '/' + dirname[1:]
    elif(dirname[0] == '.'):
        path = os.getenv('PWD')

    print('PATH = %s\n' % (path))

    if(not os.path.isdir(path)):
        print('Error: Directory %s does not exist.\nExiting.' % (path))
        sys.exit(2)

    dstpath = ""
    diffdir = ""
    
    if(writeHex):
        dstpath = path + '/hex'
        diffdir = '/hex_diff/'
    elif(writeMed):
        dstpath = path + '/med'
        diffdir = '/med_diff/'
    elif(writeSmall):
        dstpath = path + '/small'
        diffdir = '/small_diff/'

    else:
        print('Error: Invalid Path Option\n')
        sys.exit(2)

    if(not os.path.isdir(dstpath)):
        print('Error: Directory %s does not exist.\nExiting.' % (dstpath))
        sys.exit(2)


    lst = os.listdir(dstpath)
    #lst = ['proc_out00100.png', 'proc_out00101.png']
    filt_lst=[]
    for name in lst:
        if(name[:8] == 'proc_out' and name[(len(name)-3):] == 'png'):
            filt_lst.append(name)
    filt_lst.sort()
#    for index, name in enumerate(filt_lst[84:107],start=84):
    for index, name in enumerate(filt_lst,start=0):
        if(index>0):
            print("Diff %s %s" % (name, filt_lst[index-1]))
            diffimage2(dstpath + '/' + name, dstpath + '/' + filt_lst[index-1], path + diffdir + 'diff_' + filt_lst[index-1])
            
main()

