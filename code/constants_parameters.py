from collections import namedtuple
import pygame as pg
import os, glob

 ### SURFACE SIZE ###

infoObject = pg.display.Info() # Obtain screen resolution
SURFACE_WIDTH = infoObject.current_w
SURFACE_HEIGHT = infoObject.current_h
if SURFACE_WIDTH > 1920: SURFACE_WIDTH = int(SURFACE_WIDTH / 2) # If two screens are attached.

 ### GRID INITIALIZION ###

GRID_WIDTH = 100
GRID_HEIGHT = 100
DIM = (GRID_WIDTH, GRID_HEIGHT)
PPC = 8 # Pixels per cell.


 ### COLOURS

BLACK = (0, 0, 0)
GREY = (150, 150, 150)

GAME_TITLE = 'Cellular Automata'
SURFACE_BACKGROUND_COLOR = BLACK
GRID_COLOUR = GREY

