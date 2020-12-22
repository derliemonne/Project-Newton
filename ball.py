"""
Physical circle body that has radius, mass and velocity
"""


from camera import Camera
import math
import numpy as np

class Ball:
    def __init__(self, pos, radius, mass, color, velocity):
        """
        You may input one of characteristics: only mass or only radius. The other will be calculated automatically.
        :param pos: numpy 2d vector: Absolute position in space
        :param radius: Radius of ball (meters)
        :param mass: Mass (kg)
        :param color: Color understandable by pygame (hex or tuple)
        :param velocity: --numpy 2d vector or just 0
        """
        assert mass or radius
        self.pos = pos
        if radius and mass:
            self.radius = radius
            self.mass = mass
        elif radius and not mass:
            self.radius = radius
            self.mass = 4 * math.pi * self.radius * self.radius / 3
        elif not radius and mass:
            self.mass = mass
            self.radius = ((3 * mass) / (4 * math.pi)) ** 0.5
        self.color = color
        self.velocity = velocity or np.array([0.0, 0.0])
        self.alive = True


    def move(self, dt):
        """
        Moves the ball in space
        :param dt: delta time
        :return:
        """
        self.pos += self.velocity * dt

    def draw(self, camera: Camera):
        camera.draw_circle(self.color, self.pos, self.radius)

    def distance_to(self, ball):
        return np.linalg.norm(self.pos - ball.pos)

    def eat(self, ball):
        """
        Calculates eating another ball
        Self mass and self radius gets bigger depending on eaten ball
        This method doesn't actually delete eaten ball!
        :param ball: Ball: supposed to be eaten
        :return: None
        """
        self.mass += ball.mass
        self.radius = ((3 * self.mass) / (4 * math.pi)) ** 0.5
