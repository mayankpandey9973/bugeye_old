# Examples of the math.sin() and math.cos() trig functions
# Al Sweigart al@inventwithpython.com

# You can learn more about Pygame with the
# free book "Making Games with Python & Pygame"
#
# http://inventwithpython.com/pygame
#http://inventwithpython.com/blog/2012/07/18/using-trigonometry-to-animate-bounces-draw-clocks-and-point-cannons-at-a-target/

import sys, pygame, math
from pygame.locals import *

# set up a bunch of constants
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
RED      = (255,   0,   0)

BGCOLOR = WHITE

RADIUS = 300
OBJSIZE = 40

WINDOWWIDTH = 1280 # width of the program's window, in pixels
WINDOWHEIGHT = 1024 # height in pixels
WIN_CENTERX = int(WINDOWWIDTH / 2)
WIN_CENTERY = int(WINDOWHEIGHT / 2)

FPS = 6


# standard pygame setup code
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Counter Clock Movement')


def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
    angle = math.atan2(x1 - x2, y1 - y2) # get the angle in radians
    angle = angle * (180 / math.pi) # convert to degrees
    angle = (angle + 90) % 360 # adjust for a right-facing sprite
    return angle


counter = 0

# main application loop
count = 0
while True:
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    # fill the screen to draw from a blank state
    DISPLAYSURF.fill(BGCOLOR)

    count = (count+1)%60
    degrees = count * 6


    # draw the big circle on the edge
    xPos = math.cos(degrees * (math.pi / 180)) * RADIUS
    yPos = math.sin(degrees * (math.pi / 180)) * RADIUS
    pygame.draw.circle(DISPLAYSURF, BLACK, (int(xPos) + WIN_CENTERX, -1 * int(yPos) + WIN_CENTERY), OBJSIZE)


    pygame.display.update()
    FPSCLOCK.tick(FPS)
    
