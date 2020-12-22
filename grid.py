import pygame as pg
import numpy as np
import config


class Grid:
    def __init__(self, camera):
        self.color = config.grid_color
        self.camera = camera
        self.font = pg.font.Font("font.ttf", 17)
    
    def draw(self):
        scale = 1
        size = 50
        for x in np.arange(0, size, scale):
            self.camera.draw_line(self.color, np.array([x, 0]), np.array([x, size]))
        for y in np.arange(0, size, scale):
            self.camera.draw_line(self.color, np.array([0, y]), np.array([size, y]))