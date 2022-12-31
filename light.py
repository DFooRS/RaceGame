from ursina import *


class Light(Entity):
    def __init__(self, scale=(2, 2.5)):
        super().__init__(
            model='quad',
            texture='assets/svetofor.png',
            collidar='box',
            scale=scale,
            y=2.5
        )

    def set_red(self):
        self.texture = 'assets/red.png'

    def set_yellow(self):
        self.texture = 'assets/yellow.png'

    def set_green(self):
        self.texture = 'assets/green.png'

    def delete_light(self):
        self.disable()
