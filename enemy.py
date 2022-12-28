from ursina import *
import random


class Enemy(Entity):
    def __init__(self, texture='assets/car8.png', scale=(2.9, 5.9), x=2):
        super().__init__(
            model='quad',
            texture=texture,
            #collider=,
            scale=scale,
            x=x
        )
        self.collider = BoxCollider(self, center=Vec3(0, 0), size=Vec3(0.85, 0.95))

    def update(self):

        if self.x >= 6.2:
            self.x = 6.2
            self.shake()

        if self.x <= -6.2:
            self.x = -6.2
            self.shake()

        if self.intersects().hit:
            self.shake()