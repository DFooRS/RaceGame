from ursina import *


class Road(Entity):
    def __init__(self, scale=15, z=1):
        super().__init__(
            model="quad",
            texture='assets/road.png',
            scale=scale,
            z=z,
            offset=0
        )

    def update(self):

        if held_keys['w']:
            self.y = camera.y
            self.offset += time.dt * 1
            setattr(self, "texture_offset", (0, self.offset))

        if held_keys['s']:
            self.y = camera.y
            self.offset += time.dt * -0.3
            setattr(self, "texture_offset", (0, self.offset))
