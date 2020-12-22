"""
Run this file. This is the main file of project.
All physical quantities in the SI system!
"""


import config
import pygame as pg
from manager import Manager


pg.init()
pg.font.init()
screen = pg.display.set_mode(config.RESOLUTION)
manager = Manager(screen, config.PPM)
pg.display.set_caption("Newton's Gravity Project")

done = False
clock = pg.time.Clock()

while not done:
    dt = clock.tick(config.FPS) * 0.001 * config.time_multiplier
    screen.fill(config.BACKGROUND_COLOR)
    done = manager.process(pg.event.get(), dt)
    pg.display.flip()

pg.quit()
