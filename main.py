#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ursina import *
from car import Car
from road import Road
from menu import MainMenu
from RaceGame.enemy import Enemy


def update():
    if menu.game == 1:
        car.enable()
        road1.enable()
        e1_car.enable()

        if not held_keys['w']:
            e1_car.y += 10 * time.dt

        e1_car.y += random.uniform(2.7, 5) * time.dt

        if car.y > 90:
            road1.disable()
            road2.enable()


if __name__ == '__main__':
    app = Ursina()
    window.title = "Race"
    camera.ortographic = True
    camera.fov = 40

    menu = MainMenu()

    car = Car()
    car.disable()

    road1 = Road()
    road1.disable()
    road2 = Road(texture='assets/road1.png')
    road2.disable()

    e1_car = Enemy(x=-2)
    e1_car.disable()

    app.run()
