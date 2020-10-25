import pygame as pg
from code import Grid
from code import Renderer
from collections import namedtuple
from code import constants_parameters as C
import numpy as np
import sys
import random as rd
import copy


class Game(object):
	def __init__(self, surface):
		self.renderer = Renderer.Renderer(C.SURFACE_WIDTH, C.SURFACE_HEIGHT, C.SURFACE_BACKGROUND_COLOR, surface)
		self.grid = Grid.Grid(C.DIM, pg.Rect(20, 20, C.DIM[0]*C.PPC, C.DIM[1]*C.PPC))


	def update(self):
		with self.renderer:
			self.renderer.draw_grid(self.grid, C.GRID_COLOUR)

		self.grid.get_next_state(self.grid)

		return self.handle_events()

	def handle_events(self):
		for ev in pg.event.get():
			if ev.type == pg.QUIT or ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE:
				return False

		return True