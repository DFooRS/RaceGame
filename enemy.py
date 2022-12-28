from ursina import *
import random


class Enemy(Entity):
    def __init__(self, texture='assets/car8.png', scale=(2.9, 5.9), x=2):
        super().__init__(
            model='quad',
            texture=texture,
            collidar='box',
            scale=scale,
            collision=True,
            x=x
        )

    def update(self):

        if self.x >= 6.2:
            self.x = 6.2
            self.shake()

        if self.x <= -6.2:
            self.x = -6.2
            self.shake()
