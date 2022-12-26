from ursina import *


class Car(Entity):
    def __init__(self, scale=(2.2, 4.4), x=2):
        super().__init__(
            model='quad',
            texture='assets\car.png',
            collidar='box',
            scale=scale,
            x=x
        )