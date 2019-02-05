import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.core.window import Window

from clock import ClockLabel

class ClockApp(App):
    def build(self):
        c = ClockLabel()
        #Window.size = c.font_size, c.font_size
        return c

if __name__ == '__main__':
    ClockApp().run()
