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
#import statistics

bugeye_dir = os.getenv('BUGEYE')
mapping_file = bugeye_dir + '/image_manip/mapping_640_480.py'
imagepos_file = bugeye_dir + '/image_manip/imagepos_mapping_adjusted_fixed.py'
execfile(mapping_file)
execfile(imagepos_file)
#execfile('/home/manish/bugeye/image_manip/mapping_640_480.py')
#execfile('/home/manish/bugeye/image_manip/imagepos_mapping_adjusted_fixed.py')

writeHex = False
writeMed = False
writeSmall = False
path = ''
intrplBlanks = True
dirname = 'none'


def eye2image(inputfile, outputfile, hexSize, medSize, smallSize):

    debug_on = False
    width, height = 80, 88
    if(hexSize):
        width, height = 350, 370
    elif(medSize):
        width, height = 80, 88
    elif(smallSize):
        width, height = 20, 22
    else:
        print('Error: Invalid Size Option\n')
        sys.exit(2)
        
    write_img_data = np.zeros((width, height, 3), dtype=np.uint8)

    #Interpolate for blank tiles
    if(intrplBlanks):
        Imagepos.append([32,24]) #100
        Imagepos.append([50,27]) #101
        Imagepos.append([68,42]) #102

    read_img = mpimg.imread(inputfile)

    start = timer()

    for i in range(0,103):#    for i in range(0,103):
        single_pixel_sample = False
        red = green = blue = 1.0
        #Index i > 99 only valid for interpolation mode in hex display
        if((i > 99) and (not (intrplBlanks and hexSize))):
            break

        if(i < 100):
            ex = Eyepos[i][1]
            ey = Eyepos[i][0]
            pixlvalue = read_img[ex,ey]
            if single_pixel_sample:
                red = pixlvalue[0]
                green = pixlvalue[1]
                blue = pixlvalue[2]
            else:
                #Get colors from +-2 pixels adjacent to ex and ey

                rsum = gsum = bsum = float(0.0)
                for px in range(ex-2,ex+3):
                    for py in range(ey-2,ey+3):
                        rsum += float(read_img[px,py][0])
                        gsum += float(read_img[px,py][1])
                        bsum += float(read_img[px,py][2])
                red = rsum/25.0
                green = gsum/25.0
                blue = bsum/25.0
                #print("RGB = %f %f %f" % (red, green, blue))
                
                if(False):
                    #Get Image Data for ith bundle - 4 pixels around coordinates
                    red =   (float(read_img[ex,ey][0]) + float(read_img[ex+1,ey][0]) + float(read_img[ex-1,ey][0]) + float(read_img[ex,ey+1][0]) + float(read_img[ex,ey-1][0]))/5
                    green = (float(read_img[ex,ey][1]) + float(read_img[ex+1,ey][1]) + float(read_img[ex-1,ey][1]) + float(read_img[ex,ey+1][1]) + float(read_img[ex,ey-1][1]))/5
                    blue =   (float(read_img[ex,ey][2]) + float(read_img[ex+1,ey][2]) + float(read_img[ex-1,ey][2]) + float(read_img[ex,ey+1][2]) + float(read_img[ex,ey-1][2]))/5
        elif (i==100):
            #Get colors from neighbors 29, 28, 48, 70, 71, 49
            red = (float(read_img[Eyepos[29][1], Eyepos[29][0]][0])
                   + float(read_img[Eyepos[28][1], Eyepos[28][0]][0])
                   + float(read_img[Eyepos[48][1], Eyepos[48][0]][0])
                   + float(read_img[Eyepos[70][1], Eyepos[70][0]][0])
                   + float(read_img[Eyepos[71][1], Eyepos[71][0]][0])
                   + float(read_img[Eyepos[49][1], Eyepos[49][0]][0]))/6.0
            green = (float(read_img[Eyepos[29][1], Eyepos[29][0]][1])
                   + float(read_img[Eyepos[28][1], Eyepos[28][0]][1])
                   + float(read_img[Eyepos[48][1], Eyepos[48][0]][1])
                   + float(read_img[Eyepos[70][1], Eyepos[70][0]][1])
                   + float(read_img[Eyepos[71][1], Eyepos[71][0]][1])
                   + float(read_img[Eyepos[49][1], Eyepos[49][0]][1]))/6.0
            blue = (float(read_img[Eyepos[29][1], Eyepos[29][0]][2])
                   + float(read_img[Eyepos[28][1], Eyepos[28][0]][2])
                   + float(read_img[Eyepos[48][1], Eyepos[48][0]][2])
                   + float(read_img[Eyepos[70][1], Eyepos[70][0]][2])
                   + float(read_img[Eyepos[71][1], Eyepos[71][0]][2])
                   + float(read_img[Eyepos[49][1], Eyepos[49][0]][2]))/6.0
            
        elif (i==101):
            #Get colors from neighbors 12, 26, 45, 46, 27, 13
            red = (float(read_img[Eyepos[12][1], Eyepos[12][0]][0])
                   + float(read_img[Eyepos[26][1], Eyepos[26][0]][0])
                   + float(read_img[Eyepos[45][1], Eyepos[45][0]][0])
                   + float(read_img[Eyepos[46][1], Eyepos[46][0]][0])
                   + float(read_img[Eyepos[27][1], Eyepos[27][0]][0])
                   + float(read_img[Eyepos[13][1], Eyepos[13][0]][0]))/6.0
            green = (float(read_img[Eyepos[12][1], Eyepos[12][0]][1])
                   + float(read_img[Eyepos[26][1], Eyepos[26][0]][1])
                   + float(read_img[Eyepos[45][1], Eyepos[45][0]][1])
                   + float(read_img[Eyepos[46][1], Eyepos[46][0]][1])
                   + float(read_img[Eyepos[27][1], Eyepos[27][0]][1])
                   + float(read_img[Eyepos[13][1], Eyepos[13][0]][1]))/6.0
            blue = (float(read_img[Eyepos[12][1], Eyepos[12][0]][2])
                   + float(read_img[Eyepos[26][1], Eyepos[26][0]][2])
                   + float(read_img[Eyepos[45][1], Eyepos[45][0]][2])
                   + float(read_img[Eyepos[46][1], Eyepos[46][0]][2])
                   + float(read_img[Eyepos[27][1], Eyepos[27][0]][2])
                   + float(read_img[Eyepos[13][1], Eyepos[13][0]][2]))/6.0
            
        else: #i=102
            #Get colors from neighbors 41, 64, 87, 42, 24, 23
            red = (float(read_img[Eyepos[41][1], Eyepos[41][0]][0])
                   + float(read_img[Eyepos[64][1], Eyepos[64][0]][0])
                   + float(read_img[Eyepos[87][1], Eyepos[87][0]][0])
                   + float(read_img[Eyepos[42][1], Eyepos[42][0]][0])
                   + float(read_img[Eyepos[24][1], Eyepos[25][0]][0])
                   + float(read_img[Eyepos[23][1], Eyepos[23][0]][0]))/6.0
            green = (float(read_img[Eyepos[41][1], Eyepos[41][0]][1])
                   + float(read_img[Eyepos[64][1], Eyepos[64][0]][1])
                   + float(read_img[Eyepos[87][1], Eyepos[87][0]][1])
                   + float(read_img[Eyepos[42][1], Eyepos[42][0]][1])
                   + float(read_img[Eyepos[24][1], Eyepos[25][0]][1])
                   + float(read_img[Eyepos[23][1], Eyepos[23][0]][1]))/6.0
            blue = (float(read_img[Eyepos[41][1], Eyepos[41][0]][2])
                   + float(read_img[Eyepos[64][1], Eyepos[64][0]][2])
                   + float(read_img[Eyepos[87][1], Eyepos[87][0]][2])
                   + float(read_img[Eyepos[42][1], Eyepos[42][0]][2])
                   + float(read_img[Eyepos[24][1], Eyepos[25][0]][2])
                   + float(read_img[Eyepos[23][1], Eyepos[23][0]][2]))/6.0
            

        if(hexSize):
            t1 = timer()
            x = (Imagepos[i][0] - 2)/6 * 24 
            y = (Imagepos[i][1]/3)*14
            verts = np.array([[x-16,y],[x-8,y-14],[x+8,y-14],[x+16,y],[x+8,y+14],[x-8,y+14]])

            #Left Triangle in region [[x-8,y-7],[x-4,y+7]] set points below <[x-8,y][x-4,y+7]> AND above <[x-8,y][x-4,y-7]> to the color.
            slope1 = slope([x-16,y],[x-8,y+14])
            slope2 = slope([x-16,y],[x-8,y-14])
            for j in range(x-16,x-7):
                for k in range(y-14,y+15):
                    if((not above([x-16,y],slope1,[j,k])) and above([x-16,y],slope2,[j,k]) ):
                        write_img_data[j, k] = [red*255, green*255, blue*255]
                        
            #Right Triangle in region [[x+4,y-7],[x+8,y+7]] set points above <[x+4,y-7][x+8,y]> AND below <[x+8,y][x+4,y+7]> to the color.
            slope1 = slope([x+8,y-14],[x+16,y])
            slope2 = slope([x+16,y],[x+8,y+14])
            for j in range(x+8,x+17):
                for k in range(y-14,y+15):
                    if(above([x+8,y-14],slope1,[j,k]) and (not above([x+16,y],slope2,[j,k])) ):
                        write_img_data[j, k] = [red*255, green*255, blue*255]

            #Fill the remaining points in the middle of rectangle
            write_img_data[x-8:x+9,y-14:y+15] = [red*255, green*255, blue*255]
            t2 = timer()
            #print('Inner Loop Processing Pime = %f\n' % (t2 - t1))
        elif(medSize):
            for j in range(-2,4):
                for k in range(-2,4):
                    write_img_data[Imagepos[i][1]+j, Imagepos[i][0]+k] = [red*255, green*255, blue*255]
                    #print("pos[%d,%d]=[%f,%f,%f]" % (Imagepos[i][1]+j, Imagepos[i][0]+k, red, green, blue))
        elif(smallSize):
            for j in range(-2,4):
                for k in range(-2,4):
                    write_img_data[(Imagepos[i][1]+j)/4, (Imagepos[i][0]+k)/4] = [red*255, green*255, blue*255]
                    #print("pos[%d,%d]=[%f,%f,%f]" % (Imagepos[i][1]+j, Imagepos[i][0]+k, red, green, blue))
        else:
            print('Error: Unknown Option.\nExiting.' % (path))
            sys.exit(2)
            
                

            
    if(hexSize):
        write_img_data = np.fliplr(np.rot90(write_img_data, 3))
                    
    img = Image.fromarray(write_img_data, mode='RGB')
    end = timer()
    print('Processing time = %f' % (end - start))
    img.save(outputfile)

    if debug_on:
         fig = plt.figure()
         ax = fig.gca()
         ax.set_xticklabels(np.arange(0,height,10), fontsize=6)
         ax.set_yticklabels(np.arange(0,width,10), fontsize=6)
         ax.set_xticks(np.arange(0,height,10))
         ax.set_yticks(np.arange(0,width,10))
         plt.imshow(img)
         plt.grid(b=True, which='major', color='r', linestyle='dotted')
         plt.show()
         raise SystemExit

def slope(p1, p2):
    return (float(p2[1]) - float(p1[1]))/(float(p2[0]) - float(p1[0]))

#Return True if point is above the line
def above(p, slope, point):
    liney = p[1] + (slope * (float)(point[0] - p[0]))
    if (liney < point[1]):
        return True
    else:
        return False



   
def main():

    #Convert images captured in <dirname> to ordered tiles
    #Usage:
    #sequence_converter3.py -dir <dirname> [-hex|-med|-small] [-interpolate|-nointerpolate]
    #
    #Options:
    #-dir: specify directory name to do processing
    #-hex: Specify tiles to be large hex pixels with -hex, or as 6x6 square tiles. Default True
    #-interpolate: Specify if the missing 3 tiles are to be interpolated with color of six neighboring tiles. Default True.

    global writeHex
    global writeMed
    global WriteSmall
    global intrplBlanks
    global dirname
    global path

    writeHex = False
    writeMed = False
    writeSmall = False
    try:
        opts, args = getopt.getopt(sys.argv[1:],"x",["dir=","hex","med","small","interpolate","nointerpolate","help"])
    except getopt.GetoptError:
        print("sequence_converter4.py --dir=<dirname> [--help][--hex|--med|--small] [--interpolate|--nointerpolate]")
        sys.exit(2)
    for opt, arg in opts:
       if opt == '--help':
           print('sequence_converter4.py -dir=<dirname> [--help][--hex|--med|--small] [--interpolate|--nointerpolate]')
           sys.exit()
       elif opt in ("-d", "--dir"):
           dirname = arg
       elif opt in ("-h", "--hex"):
           writeHex = True
       elif opt in ("--med"):
           writeMed = True
       elif opt in ("--small"):
           writeSmall = True
       elif opt in ("-i", "--interpolate"):
           intrplBlanks = True
       elif opt in ("--nointerpolate"):
           intrplBlanks = False

    #    basepath = '/home/manish/bugeye/image_manip'
    basepath = ''
    path = 'foo'
    print("Running with options:")
    print('   Dirname: %s' % (dirname))
    print('   Hex: %r' % (writeHex))
    print('   Med: %r' % (writeMed))
    print('   Small: %r' % (writeSmall))
    print('   Intrpl: %r' % (intrplBlanks))


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

    #path appended by raw
    rawpath = path + '/raw'
    dstpath = ''
    
    print('PATH = %s' % (path))

    #Read files in directory specified with names of form raw/out%5d.jpg and convert to (hex|med|small)/proc_out%5.jpg

    if(not os.path.isdir(path)):
        print('Error: Directory %s does not exist.\nExiting.' % (path))
        sys.exit(2)

    if(not os.path.isdir(rawpath)):
        print('Error: Directory %s does not exist.\nExiting.' % (rawpath))
        sys.exit(2)

    if(writeHex):
        dstpath = path + '/hex'
    elif(writeMed):
        dstpath = path + '/med'
    elif(writeSmall):
        dstpath = path + '/small'
    else:
        print('Error: Invalid Path Option\n')
        sys.exit(2)
        
    if(not os.path.isdir(dstpath)):
        print('Error: Directory %s does not exist.\nExiting.' % (dstpath))
        sys.exit(2)

    lst = os.listdir(rawpath)
    lst.sort()
    for name in lst:
        if (name[:3] == 'out' and name[(len(name)-3):] == 'png'):
            if os.path.isfile(os.path.join(rawpath, name)):
                print('Processing %s' % (name))
                eye2image(rawpath + '/' + name, dstpath + '/' + 'proc_' + name[:-3] + 'png', writeHex, writeMed, writeSmall)
            

main()


