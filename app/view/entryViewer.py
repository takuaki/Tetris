import tkinter as tk

'''
エントリー画面
Start  ゲーム開始
Exit   ゲーム終了
Score  スコア表の表示
'''


class EntryViewer(tk.Canvas):
    Width = 800  # 画面横幅
    Height = 600  # 画面縦幅

    def __init__(self, master, controller=None):
        super().__init__(master, bg="white", width=self.Width, height=self.Height)

        # controller
        self.controller = controller

        # button
        self.button_start = tk.Button(master, text="Start", command=lambda: None)
        self.button_exit = tk.Button(master, text="Exit", command=lambda: None)
        self.button_score = tk.Button(master, text="Stop", command=lambda: None)

        # create view
        self.pack()
        self.button_start.pack(anchor=tk.S, side=tk.BOTTOM)
        self.button_exit.pack(anchor=tk.S, side=tk.BOTTOM)
        self.button_score.pack(anchor=tk.S, side=tk.BOTTOM)

    def animate(self):
        pass
