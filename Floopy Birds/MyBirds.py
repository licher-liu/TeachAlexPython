# Developer：licher
# Datetime:2019/10/25 15:36
"""
    使用pygame制作小鸟游戏，练习Pygame的常用方法
"""
import pygame as pg
import sys


class Birds:
    """定义一个游戏角色鸟类"""

    def __init__(self):
        self.bird_rect = pg.Rect(65,50,50,50) #鸟的矩形
        self.bird_status = [pg.image.load("assets/1.png"),
                            pg.image.load("assets/2.png"),
                            pg.image.load("assets/dead.png")]
        self.status = 0     #默认小鸟飞行状态
        self.X = 120        # 鸟所在X轴坐标,即是向右飞行的速度
        self.Y = 350        # 鸟所在Y轴坐标,即上下飞行高度
        self.jump = False   #默认小鸟向下掉落
        self.jump_speed = 10 #跳跃高度
        self.gravity = 5    #重力
        self.dead = False   #默认小鸟存活

    def update(self):
        if self.jump:
            #小鸟跳跃
            self.jump_speed -= 1        # 速度递减，上升越来越慢
            self.Y -= self.jump_speed   # 鸟Y轴坐标减小，小鸟上升

        else:
            # 小鸟坠落
            self.gravity += 0.2 #重力递增，下降越来越快
            self.Y += self.gravity  # 鸟Y轴坐标增加，小鸟下降
        self.bird_rect[1] = self.Y  #更改Y轴位置


class Pipeline:
    """定义一个管道类"""
    def __init__(self):
        self.wall_x = 400
        self.pipe_up = pg.image.load("assets/top.png")
        self.pipe_down = pg.image.load("assets/bottom.png")

    def pipeline_update(self):
        """管道移动方法"""
        self.wall_x -= 5 #管道按移动速度向左移动
        if self.wall_x <= -80: #如果管道运行到最左侧，即代表小鸟飞过了管道，分数加1，并重置管道
            global score
            score += 1
            self.wall_x = 400

def creat_map():
    screen.fill((255, 0, 0))  # 填充颜色
    screen.blit(background, (0, 0))  # 显示背景图片
    #显示管道
    screen.blit(pipeline.pipe_up,(pipeline.wall_x,-300))
    screen.blit(pipeline.pipe_down, (pipeline.wall_x, 500))
    pipeline.pipeline_update()

    # 显示小鸟
    #screen.blit(mybird.bird_status[0], (150, 350))


    pg.display.update()  # 刷新显示


if __name__ == '__main__':
    """主程序"""
    pg.init()                                 #初始化
    # pg.font.init()                            #初始化字体
    # font = pg.font.SysFont("Arial", 50)       #设置字体大小
    size = width, height = 400, 650            #设置窗口大小
    screen = pg.display.set_mode(size)          #显示窗口
    clock = pg.time.Clock()
    score = 0               #统计分数

    mybird = Birds()
    pipeline = Pipeline()


    while True:
        clock.tick(60)                          #刷新率 每秒执行60次
        # 轮询事件
        for event in pg.event.get():
            if event.type == pg.QUIT:           #如果点击关闭按钮则结束程序
                sys.exit()
                # 判断控制按键程序

        background = pg.image.load("assets/background.png")     #加载背景图片
        creat_map()
