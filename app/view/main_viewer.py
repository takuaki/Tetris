import tkinter as tk


class MainViewer(tk.Canvas):
    Width = 800
    Height = 600

    def __init__(self, master, controller=None):
        super().__init__(master, bg="white", width=self.Width, height=self.Height)
        self.pack()
        
    def animate(self):
        pass
