from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel
from kivy.clock import Clock
from kivy.lang import Builder

import time

KV = '''
<ClockLabel>:
    font_size: "50dp"
    font_blended: True
    bold: True
    shorten: True
    color: self.col
'''

Builder.load_string(KV)

class ClockLabel(Label):
    col = 1, 0, 1, 1

    def __init__(self):
        super(ClockLabel, self).__init__()
        Clock.schedule_interval(self.update, 1)

    def update(self, delta):
        self.text = time.asctime()
