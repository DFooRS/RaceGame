#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ursina import *
from car import Car
from road import Road
from menu import MainMenu


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


if __name__ == '__main__':
    app = Ursina()
    window.title = "Race"
    camera.ortographic = True
    camera.fov = 40

    road1 = Road()
    road1.disable()

    car = Car()
    e1_car = Car(x=-2)
    e2_car = Car(x=-5)
    e3_car = Car(x=5)
    cars = [car, e1_car, e2_car, e3_car]
    for car in cars:
        car.disable()

    menu = MainMenu()

    offset = 0
    app.run()
