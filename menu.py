from ursina import *


class MainMenu(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
            )
        self.start_menu = Entity(parent=self, enabled=True)
        self.game = 0

        b1 = Button(text="Start",
                    color=color.gray,
                    pressed_color=color.black,
                    scale=(0.2, 0.1),
                    y=0.06,
                    parent=self.start_menu)
        b2 = Button(text="Exit",
                    color=color.gray,
                    pressed_color=color.black,
                    scale=(0.2, 0.1),
                    y=-0.06,
                    parent=self.start_menu)

        def play_game():
            self.start_menu.disable()
            self.game = 1

        def quit_game():
            application.quit()

        b2.on_click = Func(quit_game)
        b1.on_click = Func(play_game)
