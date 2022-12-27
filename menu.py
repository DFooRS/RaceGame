from ursina import *


class MainMenu(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
            )
        self.start_menu = Entity(parent=self)
        self.game = 0
        self.place = 2

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

        def quit_game():
            application.quit()

        exit_button.on_click = Func(quit_game)
        start_button.on_click = Func(play_game)

    def finish(self, car, e1_car):
        application.pause()
        if car.y > e1_car.y:
            self.place -= 1
        empty = Text('\n\n\n')
        t = Text(f'Congratulates!\nYou took the {self.place} place',
                 x=0,
                 y=0
                 )
        play_again_button = Button(text="Play again",
                                   color=color.black,
                                   pressed_color=color.dark_gray,
                                   scale=(0.1, 0.05),
                                   y=0.06)

        exit_button = Button(text="Exit",
                             color=color.black,
                             pressed_color=color.dark_gray,
                             scale=(0.1, 0.05),
                             y=-0.06)

        exit_button.on_click = application.quit
        pied = Entity(model='quad', texture='assets/pied.png', scale=3)
        wp = WindowPanel(
            title='F I N I S H!',
            content=(
                empty,
                pied,
                t,
                play_again_button,
                exit_button
            ),
            y=0.4,
            color=color.black
        )


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
