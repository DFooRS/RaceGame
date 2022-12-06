#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ursina import *
import random


def update():
    global offset

    car.x -= held_keys['a'] * 3 * time.dt
    car.x += held_keys['d'] * 3 * time.dt
    car.y += held_keys['s'] * -2 * time.dt
    car.y += held_keys['w'] * 5 * time.dt

    camera.y = car.y
    if held_keys['w']:
        road1.y = camera.y
        offset += time.dt * 1
        setattr(road1, "texture_offset", (0, offset))



app = Ursina()
camera.ortographic = True
camera.fov = 40

car = Entity(
    model='quad',
    texture='assets\car.png',
    collidar='box',
    scale=(2.2, 4.4),
    x = 2
)
road1 = Entity(
    model="quad",
    texture='assets/road.png',
    scale = 15,
    z = 1
)


offset = 0
app.run()