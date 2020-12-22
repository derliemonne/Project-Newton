import config
import pygame as pg
import numpy as np


class Camera:
    """
    Draw objects in the space on window
    """
    def __init__(self, screen, ppm, center_pos):
        self.screen = screen
        self.ppm = ppm
        self.width = config.RESOLUTION[0] / ppm
        self.height = config.RESOLUTION[1] / ppm
        self.center_pos = center_pos

    def scale(self, scale_factor, mouse_pos):
        """
        Zoom in or zoom out
        Change ppm, width and height
        :param scale_factor: multiply ppm
        :param mouse_pos: relative to window position of the new center of camera
        :return: None
        """
        self.ppm *= scale_factor
        self.width = config.RESOLUTION[0] / self.ppm
        self.height = config.RESOLUTION[1] / self.ppm

    def change_center_pos(self, delta_pos):
        self.center_pos = self.center_pos + delta_pos

    def get_window_pos(self, abs_pos):
        """ Window position is [x, y] of window
            Absolute position is [x, y] of space """
        window_center = np.array(config.RESOLUTION) / 2
        delta_center = abs_pos * self.ppm - self.center_pos * self.ppm
        window_pos = window_center + delta_center
        return window_pos

    def get_abs_pos(self, window_pos):
        """ Relative position is [x, y] of window
            Absolute position is [x, y] of space """
        window_center = [config.RESOLUTION[i] / 2 for i in range(2)]
        absolute_pos_pixels = window_pos - window_center + self.center_pos * self.ppm
        return absolute_pos_pixels / self.ppm

    def draw_circle(self, color, pos, radius):
        """

        :param color:
        :param pos: Absolute position of circle
        :param radius:
        :return:
        """
        pg.draw.circle(self.screen, color,
                       center=self.get_window_pos(np.array(pos)),
                       radius=radius * self.ppm)

    def draw_line(self, color, start_pos, end_pos):
        """

        :param color:
        :param start_pos: Absolute position of A point
        :param end_pos: Absolute position of B point
        :return:
        """
        pg.draw.line(self.screen, color,
                     self.get_window_pos(start_pos),
                     self.get_window_pos(end_pos))
