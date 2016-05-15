#! /usr/bin/env python3
import os
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy import ndimage
from PIL import Image


execfile('mapping_640_480.py')
execfile('imagepos_mapping_adjusted_fixed.py')

writeHex = True

def eye2image(inputfile, outputfile):
    debug_on = False
    num_eyes = 100
    #width, height = 80, 88
    width, height = 270, 300
    write_img_data = np.zeros((width, height, 3), dtype=np.uint8)

    read_img = mpimg.imread(inputfile)

    for i in range(0,100):
        single_pixel_sample = False
        red = green = blue = 255
        ex = Eyepos[i][1]
        ey = Eyepos[i][0]
        pixlvalue = read_img[ex,ey]
        if single_pixel_sample:
            red = pixlvalue[0]
            green = pixlvalue[1]
            blue = pixlvalue[2]
        else:
            #Get Image Data for ith bundle - 4 pixels around coordinates
            red =   (int(read_img[ex,ey][0]) + int(read_img[ex+1,ey][0]) + int(read_img[ex-1,ey][0]) + int(read_img[ex,ey+1][0]) + int(read_img[ex,ey-1][0]))/5
            green = (int(read_img[ex,ey][1]) + int(read_img[ex+1,ey][1]) + int(read_img[ex-1,ey][1]) + int(read_img[ex,ey+1][1]) + int(read_img[ex,ey-1][1]))/5
            blue =   (int(read_img[ex,ey][2]) + int(read_img[ex+1,ey][2]) + int(read_img[ex-1,ey][2]) + int(read_img[ex,ey+1][2]) + int(read_img[ex,ey-1][2]))/5
        if(writeHex):
            x = (Imagepos[i][0] - 2)/6 * 12 + 8
            y = (Imagepos[i][1]/3)*7
            verts = np.array([[x-8,y],[x-4,y-7],[x+4,y-7],[x+8,y],[x+4,y+7],[x-4,y+7]])

            #Left Triangle in region [[x-8,y-7],[x-4,y+7]] set points below <[x-8,y][x-4,y+7]> AND above <[x-8,y][x-4,y-7]> to the color.
            slope1 = slope([x-8,y],[x-4,y+7])
            slope2 = slope([x-8,y],[x-4,y-7])
            for j in range(x-8,x-3):
                for k in range(y-7,y+8):
                    if((not above([x-8,y],slope1,[j,k])) and above([x-8,y],slope2,[j,k]) ):
                        write_img_data[j, k] = [red, green, blue]
                        
            #Right Triangle in region [[x+4,y-7],[x+8,y+7]] set points above <[x+4,y-7][x+8,y]> AND below <[x+8,y][x+4,y+7]> to the color.
            slope1 = slope([x+4,y-7],[x+8,y])
            slope2 = slope([x+8,y],[x+4,y+7])
            for j in range(x+4,x+9):
                for k in range(y-7,y+8):
                    if(above([x+4,y-7],slope1,[j,k]) and (not above([x+8,y],slope2,[j,k])) ):
                        write_img_data[j, k] = [red, green, blue]

            #Fill the remaining points in the middle of rectangle
            write_img_data[x-4:x+5,y-7:y+8] = [red, green, blue]
        else:
            for j in range(-2,4):
                for k in range(-2,4):
                    write_img_data[Imagepos[i][1]+j, Imagepos[i][0]+k] = [red, green, blue]
            
                    
    img = Image.fromarray(write_img_data, 'RGB')
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
    liney = float(p[1]) + slope * (float(point[0]) - float(p[0]))
    if (liney < float(point[1])):
        return True
    else:
        return False


def main():

    eye2image('image_640_480.jpg','honeycomb.png')


    if False:
        #Read files in directory train1 with names of form raw%5d.jpg and convert to out%5.jpg
        #eye2image('/home/manish/bugeye/image_manip/image2_640_480.jpg', 'test.png')
        path = '/home/manish/bugeye/image_manip/train2'
        lst = os.listdir(path)
        lst.sort()
        for name in lst:
            if os.path.isfile(os.path.join(path, name)):
                eye2image(path + '/' + name, path + '/' + 'proc_' + name)
                print('Processed %s' % (name))
            
main()


