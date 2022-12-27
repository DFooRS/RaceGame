#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ursina import *
from car import Car
from road import Road
from menu import MainMenu
from menu import PauseMenu
from enemy import Enemy


def pause_handler_input(key):
    if key == 'escape':
        application.paused = not application.paused
        pause.pause_menu.enable()
        if not application.paused:
            pause.pause_menu.disable()


def update():
    if menu.game == 1:
        car.enable()
        road1.enable()
        e1_car.enable()

        if not held_keys['w']:
            e1_car.y += 17 * time.dt

        e1_car.y += random.uniform(5, 7.5) * time.dt

        if car.y > 178:
            road1.disable()
            road2.enable()

        if car.y > 180:
            menu.finish(car, e1_car)


if __name__ == '__main__':
    app = Ursina()
    window.title = "Race"
    camera.ortographic = True
    camera.fov = 40
    pause_handler = Entity(ignore_paused=True)
    #window.fullscreen = True

    menu = MainMenu()
    pause = PauseMenu()
    pause.pause_menu.disable()

    car = Car()
    car.disable()

    road1 = Road()
    road1.disable()
    road2 = Road(texture='assets/road1.png')
    road2.disable()

    e1_car = Enemy(x=-2)
    e1_car.disable()
    pause_handler.input = pause_handler_input
    app.run()
