"""
Connects simulation, drawing graphics and handling events
"""


import pygame as pg
import numpy as np
from space import Space


class Manager:
    def __init__(self, screen, ppm):
        """

        :param screen: pygame screen
        :param ppm: pixels per in-game meter
        """
        self.space = Space(screen, ppm)

    def process(self, events, dt):
        """
        main loop
        :param events: pygame events
        :param dt: delta time
        :return: True if process if finished. False if continues.
        """
        done = self.handle_events(events)
        self.space.draw()
        self.space.simulate(dt)
        return done

    def handle_events(self, events):
        """

        :param events: pygame events
        :return: True if user closed app. Else: False
        """
        done = False
        for event in events:
            done = done or event.type == pg.QUIT
            if event.type == pg.MOUSEWHEEL:
                self.handle_zooming(event)
            # user holds mouse button to spawn a ball
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == pg.BUTTON_LEFT:
                self.space.start_spawn_ball(self.space.camera.get_abs_pos(np.array(event.pos)))
            # user releases mouse button and ball spawns
            elif event.type == pg.MOUSEBUTTONUP and event.button == pg.BUTTON_LEFT:
                self.space.spawn_ball()
            elif event.type == pg.KEYDOWN:
                self.handle_pan(event)
        return done

    def handle_zooming(self, event):
        """
        Zoom camera's view of the space.
        The algorithm works somehow but i have forgotten how does it work exactly.
        :param event:
        :return:
        """
        scale_factor = 1
        k = 0.1
        if event.y > 0:
            scale_factor = event.y + k
        elif event.y < 0:
            scale_factor = 1 / abs(event.y - k)
        self.space.camera.scale(scale_factor, pg.mouse.get_pos())

    def handle_pan(self, event):
        """
        Camera's view moves across the space.
        :param event:
        :return:
        """
        move_distance = 5
        if event.key == pg.K_LEFT:
            self.space.camera.change_center_pos((-move_distance, 0))
        elif event.key == pg.K_RIGHT:
            self.space.camera.change_center_pos((move_distance, 0))
        elif event.key == pg.K_UP:
            self.space.camera.change_center_pos((0, -move_distance))
        elif event.key == pg.K_DOWN:
            self.space.camera.change_center_pos((0, move_distance))

    def window_coord_to_game(self, coord):
        return coord / self.space.ppm
