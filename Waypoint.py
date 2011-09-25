# WayPoint, a simple pyGame game.
# Created by Matthew Keating
# Contact: matthewkeating007@gmail.com
# THIS IS A WORK IN PROGRESS, COMMITS MAY BE INFREQUENT!!


import random
import time
import pygame
import sys
from pygame.locals import *

# Constants for Game
FPS = 30
WINDOWHEIGHT = 480
WINDOWWIDTH = 640

# Color Tuples that will be used.

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (200, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = (255,255,255)

# Main Loop Initializes everything.

def main():
    
    global MAINCLOCK, MAINSURF, BASICFONT
    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Waypoint')

    startScreen()

# While True will eventually go to gameloop()

    while True:
        print "Sucess!"


def startScreen():

# Declares fonts and surfaces.
    
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf = titleFont.render('Waypoint!', True, RED)
    pressKeySurf = BASICFONT.render('Press any key to start.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 210, WINDOWHEIGHT - 30)
    titleSurfRect = titleSurf.get_rect()
    titleSurfRect.topleft = (WINDOWWIDTH - 560, WINDOWHEIGHT - 300)

# Infinite loop until keypress.
    
    while True:
        MAINSURF.fill(BGCOLOR)
        MAINSURF.blit(pressKeySurf, pressKeyRect)
        MAINSURF.blit(titleSurf, titleSurfRect)
        
        if checkForKeyPress():
            return
        
        pygame.display.update()
        MAINCLOCK.tick(FPS)
        
# Checks for keypress.

def checkForKeyPress():
    for event in pygame.event.get(QUIT):
        terminate()

    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        return event.key

# Exits Pygame and Python Shell
    
def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
