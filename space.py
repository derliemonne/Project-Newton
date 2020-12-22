"""
Class that handles physical simulation of objects
and contains physical bodies.
Also contains Grid and BallSpawner
"""


import numpy as np
import config
from ball_spawner import BallSpawner
from grid import Grid
from ball import Ball
from camera import Camera


class Space:
    def __init__(self, screen, ppm):
        """
        :param screen: pygame screen to draw on
        :param ppm: pixels per in-game meter
        """
        self.G = config.G
        self.screen = screen
        self.ppm = ppm
        self.camera = Camera(screen, ppm, np.array([0, 0]))
        self.grid = Grid(self.camera)
        self.balls = []
        self.ball_spawner = None

    def start_spawn_ball(self, pos):
        """
        Function to simulate ball spawning by user.
        This function starts ball spawning process.
        :param pos: Numpy 2D array: where a ball will appear.
        :return:
        """
        self.ball_spawner = BallSpawner(pos)

    def spawn_ball(self):
        """
        Completes the ball spawning process.
        :return:
        """
        self.add_ball(self.ball_spawner.spawn())
        self.ball_spawner = None

    def draw(self):
        self.grid.draw()
        for ball in self.balls:
            ball.draw(self.camera)
        if self.ball_spawner:
            # player holds button mouse to spawn bigger ball, so it grows ball to spawn every tick.
            self.ball_spawner.grow()
            self.ball_spawner.draw(self.camera)

    def simulate(self, dt):
        """
        Newton's 2nd law and the law of gravitation + some math.
        :param dt: delta time
        :return:
        """
        for ball1 in self.balls:
            for ball2 in self.balls:
                if ball1 is ball2:
                    # ball acts on other balls; it does not influence itself
                    pass
                elif self.handle_balls_collision(ball1, ball2):
                    pass
                else:
                    distance = ball1.distance_to(ball2)
                    grav_force = (self.G * ball1.mass * ball2.mass) / (distance ** 2)
                    ball1.velocity += dt * (ball2.pos - ball1.pos) * grav_force / (distance * ball1.mass)
        self.move_balls(dt)

    def handle_balls_collision(self, ball1: Ball, ball2: Ball):
        """
        Checks whether two balls collide with each other
        And if collide the bigger eats the smaller
        :param ball1: Ball
        :param ball2: Ball
        :return:
        """
        if ball1.distance_to(ball2) < ball1.radius and ball1.mass >= ball2.mass:
            ball1.eat(ball2)
            self.balls.remove(ball2)
            return True
        return False

    def move_balls(self, dt):
        for ball in self.balls:
            ball.move(dt)

    def add_ball(self, ball):
        self.balls.append(ball)
