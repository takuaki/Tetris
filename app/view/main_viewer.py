import tkinter as tk

from app.view.game_window import GameWindow
from app.view.status_window import StatusWindow


class MainViewer(tk.Canvas):
    Width = 800
    Height = 600

    def __init__(self, master, controller=None):
        super().__init__(master, bg="white", width=self.Width, height=self.Height)

        self.gw = GameWindow(self)
        self.sw = StatusWindow(self)

        self.gw.grid(column=0, row=0)
        self.sw.grid(column=1, row=0)
        self.pack()

    def animate(self):
        pass
