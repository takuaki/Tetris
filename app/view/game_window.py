import tkinter as tk


class GameWindow(tk.Frame):
    Width = 600
    Height = 600

    def __init__(self, master):
        super().__init__(master, bg="black", width=self.Width, height=self.Height)
