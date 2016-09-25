import tkinter as tk


class StatusWindow(tk.Canvas):
    Width = 200
    Height = 600

    def __init__(self, master):
        super().__init__(master, bg="black", width=self.Width, height=self.Height)

        self.label_time = StatusLabel(self, label="time:")
        self.label_score = StatusLabel(self, label="score:")
        self.label_level = StatusLabel(self, label="level")
        self.label_highScore = StatusLabel(self, label="highScore:")

    def show_score(self, score):
        self.label_score.set_text(score)

    def show_time(self, time):
        self.label_time.set_text(time)

    def show_level(self, level):
        self.label_level.set_text(level)

    def show_highscore(self, highscore):
        self.label_highScore.set_text(highscore)


class StatusLabel(tk.LabelFrame):
    Width = 100
    Height = 50

    def __init__(self, master, label):
        super().__init__(master, bg="white", width=self.Width, height=self.Height, text=label)
        self.pack()

    def set_text(self, text):
        label = tk.Label(self, text=text)
        label.pack()
