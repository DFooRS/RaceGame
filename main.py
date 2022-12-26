#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ursina import *
from car import Car
from road import Road
from menu import MainMenu


def update():
    if menu.game == 1:
        car.visible = True
        road1.visible = True


if __name__ == '__main__':
    app = Ursina()
    window.title = "Race"
    camera.ortographic = True
    camera.fov = 40

    menu = MainMenu()
    car = Car()
    car.visible = False
    road1 = Road()
    road1.visible = False
    #road1.offset = 0

    app.run()
