from ursina import *


class Car(Entity):
    def __init__(self, scale=(3, 6), x=2):
        super().__init__(
            model='quad',
            texture='assets/car5.png',
            #collider=BoxCollider(self, center=Vec3(0, 0, 0), size=Vec3(2, 5)),
            scale=scale,
            x=x,
        )
        self.collider = BoxCollider(self, center=Vec3(0, 0), size=Vec3(0.85, 0.95))

    def update(self):

        if held_keys['w']:
            self.rotation_z = 0
            camera.y = self.y
            self.y += held_keys['w'] * 7 * time.dt

        if held_keys['s']:
            self.rotation_z = 0
            camera.y = self.y
            self.y += held_keys['s'] * -2 * time.dt

        if held_keys['d']:
            self.x += held_keys['d'] * 3 * time.dt
            self.rotation_z = 7

        if held_keys['a']:
            self.x -= held_keys['a'] * 3 * time.dt
            self.rotation_z = -7

        if self.x >= 6.2:
            self.x = 6.2
            self.shake()

        if self.x <= -6.2:
            self.x = -6.2
            self.shake()

        if self.intersects().hit:
            self.shake()
