import pygame as pg
from code import constants_parameters as C

class Renderer(object):
	def __init__(self, width, height, background_color, surface):
		self.width = width # Set display width.
		self.height = height # Set display height.
		self.background_color = background_color # Set background color.
		self.display_surface = surface
		self.surface = pg.display.get_surface() # Obtain surface object.

	def draw_grid(self, grid, grid_colour):
		for i in range(len(grid.matrix)):
			for j in range(len(grid.matrix[i])):
				cur_cell_rect = (grid.rect[0] + C.PPC*j, grid.rect[1] + C.PPC*i, C.PPC, C.PPC)
				if grid.matrix[i][j]:
					pg.draw.rect(self.surface, grid_colour, cur_cell_rect)


		#pg.draw.rect(self.surface, grid_colour, grid.rect)

	def __enter__(self):
		self.surface.fill(self.background_color) # Fill the surface with a background color.

	def __exit__(self, exc_type, exc_value, exc_trace):
		pg.display.update()

