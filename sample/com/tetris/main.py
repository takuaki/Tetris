from tkinter import *

from sample.com.tetris.controller import Controller
from sample.com.tetris.view import PlayView

'''
    Tetris の実行関数
'''


def main():
    window = Tk()
    controller = Controller()
    view = PlayView(window, controller)
    view.animate()
    window.mainloop()

if __name__ == "__main__":
    main()
