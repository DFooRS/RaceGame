from ursina import *
from light import Light


class MainMenu(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
            )
        self.start_menu = Entity(parent=self, model = 'quad', texture='assets/background.png', scale=(2, 1.5))
        self.game = 0
        self.place = 4

        start_button = Button(text="Start",
                              color=color.black,
                              pressed_color=color.dark_gray,
                              scale=(0.2, 0.1),
                              y=0.06,
                              parent=self.start_menu)
        exit_button = Button(text="Exit",
                             color=color.black,
                             pressed_color=color.dark_gray,
                             scale=(0.2, 0.1),
                             y=-0.06,
                             parent=self.start_menu)

        def play_game():
            self.start_menu.disable()
            self.game = 1
            light = Light()
            invoke(light.set_red, delay=1)
            invoke(light.set_yellow, delay=2)
            invoke(light.set_green, delay=3)
            invoke(light.delete_light, delay=3.2)

        def quit_game():
            application.quit()

        exit_button.on_click = Func(quit_game)
        start_button.on_click = Func(play_game)

    def finish(self, car, e1_car, e2_car, e3_car):
        application.pause()
        if car.y > e1_car.y:
            self.place -= 1

        if car.y > e2_car.y:
            self.place -= 1

        if car.y > e3_car.y:
            self.place -= 1

        empty = Text('\n\n\n')

        if self.place == 1:
            t = Text('Congratulates!\nYou took the 1 place',
                     x=0,
                     y=0,
                     )

        if self.place == 2:
            t = Text('Not bad!\nYou took the 2 place',
                     x=0,
                     y=0,
                     )

        if self.place == 3:
            t = Text('You can do better!\nYou took the 3 place',
                     x=0,
                     y=0,
                     )

        if self.place == 4:
            t = Text("Don't get upset!\nYou took the 4 place",
                     x=0,
                     y=0,
                     )

        exit_button = Button(text="Exit",
                             color=color.black,
                             pressed_color=color.dark_gray,
                             scale=(0.1, 0.05),
                             y=-0.06)

        exit_button.on_click = application.quit

        pied = Entity(model='quad', texture='assets/cup.png', scale=(10, 6))
        wp = WindowPanel(
            title='F I N I S H!',
            content=(
                empty,
                pied,
                t,
                exit_button
            ),
            y=0.4,
            color=color.black,
        )

    def set_game(self):
        self.game = 2


class PauseMenu(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
            )
        empty = Text('\n\n')
        flag = Entity(model='quad', texture='assets/yellow_flag.png', scale=3)

        pause_button_resume = Button(text="Resume",
                                     color=color.black,
                                     pressed_color=color.dark_gray,
                                     scale=(0.1, 0.05),
                                     y=0.06)

        pause_button_exit = Button(text="Exit",
                                   color=color.black,
                                   pressed_color=color.dark_gray,
                                   scale=(0.1, 0.05),
                                   y=-0.06)

        self.pause_menu = WindowPanel(parent=self,
                                      title='P A U S E',
                                      content=(
                                          empty,
                                          flag,
                                          pause_button_resume,
                                          pause_button_exit
                                      ),
                                      y=0.3,
                                      color=color.black
                                      )

        def quit_game():
            application.quit()

        def resume():
            self.pause_menu.disable()
            application.resume()

        pause_button_exit.on_click = Func(quit_game)
        pause_button_resume.on_click = Func(resume)
