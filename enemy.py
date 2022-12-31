import random

from ursina import *


class Enemy(Entity):
    def __init__(self, texture='assets/car8.png', scale=(2.9, 5.9), x=2):
        super().__init__(
            model='quad',
            texture=texture,
            scale=scale,
            x=x,
            y=-1
        )
        self.collider = BoxCollider(self, center=Vec3(0, 0), size=Vec3(0.8, 0.9))

    def update(self):

        if self.x >= 6:
            self.x = 6
            self.shake()

        if self.x <= -6:
            self.x = -6
            self.shake()

        if self.intersects().hit:
            self.shake(0.02, 1, 0.01)
