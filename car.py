from ursina import *


class Car(Entity):
    def __init__(self, scale=(3, 6), x=2):
        super().__init__(
            model='quad',
            texture='assets/car5.png',
            scale=scale,
            x=x,
            y=-1
        )
        self.collider = BoxCollider(self, center=Vec3(0, 0), size=Vec3(0.8, 0.9))
        self.nitro = 1
        self.speed = 6

    def off_nitro(self):
        self.nitro = 0
        self.speed = 6

    def update(self):

        if held_keys['w']:
            if self.y > 0:
                camera.y = self.y
            self.rotation_z = 0
            self.y += held_keys['w'] * self.speed * time.dt

        if held_keys['s']:
            self.rotation_z = 0
            camera.y = self.y
            self.y += held_keys['s'] * self.speed / 3 * time.dt

        if held_keys['d']:
            self.x += held_keys['d'] * 3 * time.dt
            self.rotation_z = 7

        if held_keys['a']:
            self.x -= held_keys['a'] * 3 * time.dt
            self.rotation_z = -7

        if self.x >= 6:
            self.x = 6

        if self.x <= -6:
            self.x = -6

        if self.intersects().hit:
            self.shake(0.02, 1, 0.01)

        if self.nitro == 1:
            if held_keys['k']:
                self.speed = 10
                invoke(self.off_nitro, delay=3)
