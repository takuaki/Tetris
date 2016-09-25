import tkinter as tk

from app.view import MainViewer


def main():
    window = tk.Tk()
    view = MainViewer(window, None)
    view.animate()
    view.mainloop()

if __name__ == '__main__':
    main()
