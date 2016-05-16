import pygame, sys
from pygame import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Paddle Movement')


PADDLE_WIDTH = 50
PADDLE_HEIGHT = 10
paddleSpeedX = 0
p1Paddle = pygame.Rect(10, 430, PADDLE_WIDTH, PADDLE_HEIGHT)
PADDLE_COLOR = pygame.color.Color("red")

# clock object that will be used to make the game
# have the same speed on all machines regardless
# of the actual machine speed.
clock = pygame.time.Clock()

while True:
    # limit the demo to 50 frames per second
    clock.tick( 50 );

    # clear screen with black color
    screen.fill( (0,0,0) )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        p1Paddle.left = p1Paddle.left + paddleSpeedX - 5

    if keys[K_RIGHT]:
        p1Paddle.left = p1Paddle.left + paddleSpeedX + 5

    # draw the paddle
    screen.fill( PADDLE_COLOR, p1Paddle );

    pygame.display.update()
    
