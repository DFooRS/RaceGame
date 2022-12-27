from ursina import *
import random


class Enemy(Entity):
    def __init__(self, scale=(2.3, 5), x=2):
        super().__init__(
            model='quad',
            texture='assets\car4.png',
            collidar='box',
            scale=scale,
            color=color.random_color(),
            x=x
        )

    def update(self):

        if self.x >= 6.2:
            self.x = 6.2
            self.shake()

        if self.x <= -6.2:
            self.x = -6.2
            self.shake()
