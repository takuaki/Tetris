import tkinter as tk

'''
メイン画面
ボタンが右下にあり、actionはcontroller/が決定する
'''


class PlayView(tk.Canvas):
    Width = 800  # 画面横幅
    Height = 600  # 画面縦幅
    RADIUS = 10
    __SLEEP_TIME = 100  # 画面更新（ms）

    def __init__(self, master,controller):
        super().__init__(master, bg="white", width=self.Width, height=self.Height)

        # controller
        self.controller = controller

        # Button
        self.button_right = tk.Button(master, text="right", command=lambda: self.controller.action_push_right_button())
        self.button_left = tk.Button(master, text="left", command=lambda: self.controller.action_push_left_button())
        self.button_up = tk.Button(master, text="up", command=lambda: self.controller.action_push_up_button())
        self.button_down = tk.Button(master, text="down", command=lambda: self.controller.action_push_down_button())

        # Ball position
        self.__x = 0
        self.__y = 0

        # pack() 画面にViewComponentを割り当てる作業
        self.pack()
        self.button_right.pack(side=tk.RIGHT)
        self.button_left.pack(side=tk.RIGHT)
        self.button_up.pack(side=tk.RIGHT)
        self.button_down.pack(side=tk.RIGHT)

    def animate(self):
        while True:
            self.after(self.__SLEEP_TIME)
            self.update()
            self.delete("ball")
            self.__x, self.__y = self.controller.get_ball_position()
            self.create_oval(self.__x - self.RADIUS, self.__y - self.RADIUS,
                             self.__x + self.RADIUS, self.__y + self.RADIUS,
                             fill="black",tags="ball")
