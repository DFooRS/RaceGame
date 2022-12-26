from ursina import *


class Road(Entity):
    def __init__(self, scale=15, z=1):
        super().__init__(
            model="quad",
            texture='assets/road.png',
            scale=scale,
            z=z
        )
