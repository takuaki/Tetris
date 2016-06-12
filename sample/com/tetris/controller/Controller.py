from sample.com.tetris.model import Ball

'''
コントローラ
Tkinterに依存してはいけない
'''


class Controller(object):
    def __init__(self):
        self.ball = Ball()
        self.__dx = 10
        self.__dy = 10

    # View->Controllerインターフェース
    def action_push_right_button(self):
        self.ball.x += self.__dx

    def action_push_left_button(self):
        self.ball.x -= self.__dx
        print(self.ball.x)

    def action_push_up_button(self):
        self.ball.y -= self.__dy

    def action_push_down_button(self):
        self.ball.y += self.__dy

    # Controller->View
    def get_ball_position(self):
        return self.ball.x, self.ball.y
