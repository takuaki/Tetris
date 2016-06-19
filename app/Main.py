import tkinter as tk
from app.view import EntryViewer

'''テトリスの実行'''


def main():
    window = tk.Tk()
    view = EntryViewer(window, None)
    view.animate()
    window.mainloop()

if __name__ == '__main__':
    main()
