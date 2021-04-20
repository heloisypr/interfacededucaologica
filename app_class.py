import tkinter as tk
from typing import List


class Assistente:
    def __init__(self,root,label,display,buttons: List[List[tk.Button]]):
        self.root: tk.Tk = root
        self.label: tk.Label = label
        self.display: tk.Entry = display
        self.buttons = buttons

    def start(self):
        self._config_buttons()
        self._config_display()
        self.root.mainloop()

    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']

                if button_text == 'Apagar':
                    button.bind('<Button-1>',self.clear)

                if button_text in '~^v<->':
                    button.bind('<Button->',self.add_to_display)

                if button_text == 'Avançar':
                    button.bind('<Button-1>',self.clear)

    def _config_display(self):
        pass


    def clear(self,event=None):
        self.display.delete(0,'end')

    def add_to_display(self,event=None):
        self.display.insert('5',event.widget['text'])