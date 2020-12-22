from ball import Ball
import nord_colors
import math


class BallSpawner:
    def __init__(self, pos):
        self.pos = pos
        self.radius = 0.1
        self.color = nord_colors.rand_colorful(include_white=True)

    def grow(self):
        """ Increases the ball's radius every iteration """
        self.radius *= 1.03

    def spawn(self) -> Ball:
        """ Creates and returns the ball """
        return Ball(self.pos,
                    self.radius,
                    mass=4 * math.pi * self.radius * self.radius / 3,
                    color=self.color,
                    velocity=0)

    def draw(self, camera):
        camera.draw_circle(self.color, self.pos, self.radius)
