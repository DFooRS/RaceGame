#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ursina import *
import random


def update():
    global offset

    car.x -= held_keys['a'] * 3 * time.dt
    car.x += held_keys['d'] * 3 * time.dt

    if held_keys['w']:
        camera.y = car.y
        car.y += held_keys['w'] * 5 * time.dt
        road1.y = camera.y
        offset += time.dt * 1
        setattr(road1, "texture_offset", (0, offset))

    if held_keys['s']:
        camera.y = car.y
        car.y += held_keys['s'] * -2 * time.dt
        road1.y = camera.y
        offset += time.dt * -0.3
        setattr(road1, "texture_offset", (0, offset))

    if car.x >= 6.2:
        car.x = 6.2
        car.shake()
    if car.x <= -6.2:
        car.x = -6.2
        car.shake()

    e1_car.y += random.uniform(3, 6) * time.dt
    e2_car.y += random.uniform(3, 6) * time.dt
    e3_car.y += random.uniform(3, 6) * time.dt


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


e1_car = duplicate(car, x = -5, y = 0)
e2_car = duplicate(car, x = -2, y = 0)
e3_car = duplicate(car, x = 5, y = 0)

offset = 0
app.run()