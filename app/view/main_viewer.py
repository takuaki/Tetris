import tkinter as tk


class MainViewer(tk.Canvas):
    Width = 800
    Height = 600

    def __init__(self, master, controller=None):
        super().__init__(master, bg="white", width=self.Width, height=self.Height)

        gw = GameWindow(self)
        sw = StatusWindow(self)

        gw.grid(column=0, row=0)
        sw.grid(column=1, row=0)
        self.pack()

    def animate(self):
        pass


class GameWindow(tk.Frame):
    Width = 600
    Height = 600

    def __init__(self, master):
        super().__init__(master, bg="black", width=self.Width, height=self.Height)


class StatusWindow(tk.Frame):
    Width = 200
    Height = 600

    def __init__(self, master):
        super().__init__(master, bg="white", width=self.Width, height=self.Height)
