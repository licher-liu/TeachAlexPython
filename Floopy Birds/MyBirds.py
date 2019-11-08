# Developer：licher
# Datetime:2019/10/25 15:36
"""
    使用pygame制作小鸟游戏，练习Pygame的常用方法
    V1.O  实现小鸟飞行，管道移动，记录分数，小鸟碰撞管道死亡功能

"""
import pygame as pg
import sys


class Birds:
    """定义一个游戏角色鸟类"""

    def __init__(self):
        self.bird_rect = pg.Rect(65,50,50,50) #鸟的矩形
        # 定义鸟的三种状态
        self.bird_status = [pg.image.load("assets/1.png"), #滑行
                            pg.image.load("assets/2.png"), #飞起
                            pg.image.load("assets/dead.png")] #死亡
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
    #screen.blit(mybird.bird_status[0], (my, 350))
    if mybird.dead:         #撞到管道状态
        mybird.status = 2
    elif mybird.jump:       #起飞状态
        mybird.status =1
    screen.blit(mybird.bird_status[mybird.status], (mybird.X, mybird.Y))
    mybird.update()         #刷新鸟的动作


    pg.display.update()  # 刷新显示


def check_dead():
    up_rect = pg.Rect(pipeline.wall_x, -300,
                      pipeline.pipe_up.get_width() - 10,
                      pipeline.pipe_up.get_height())

    # 下方管子的矩形位置
    down_rect = pg.Rect(pipeline.wall_x, 500,
                        pipeline.pipe_down.get_width() - 10,
                        pipeline.pipe_down.get_height())

    #检查小鸟是否跟管道碰撞了
    if up_rect.colliderect(mybird.bird_rect) or down_rect.colliderect(mybird.bird_rect):
        mybird.dead = True
    # 检查小鸟是飞出边界
    if not 0< mybird.bird_rect[1] < height:
        mybird.dead = True
        return True
    else:
        return False

def get_result():
    final_text1 = "Game Over"
    final_text2 = "Your final score is:  " + str(score)
    ft1_font = pg.font.SysFont("Arial", 70)                                      # 设置第一行文字字体
    ft1_surf = font.render(final_text1, 1, (242, 3, 36))                             # 设置第一行文字颜色
    ft2_font = pg.font.SysFont("Arial", 50)                                      # 设置第二行文字字体
    ft2_surf = font.render(final_text2, 1, (253, 177, 6))                            # 设置第二行文字颜色
    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  # 设置第一行文字显示位置
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置第二行文字显示位置
    pg.display.flip()

def main():
    """主程序"""


    while True:
        clock.tick(60)  # 刷新率 每秒执行60次
        # 轮询事件
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 如果点击关闭按钮则结束程序
                sys.exit()
                # 判断控制按键程序
            if (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN) and not mybird.dead:
                mybird.jump = True  # 跳跃
                mybird.gravity = 5  # 重力
                mybird.jump_speed = 10  # 跳跃速度


        if check_dead():
            get_result()
        else:
            creat_map()
    pg.quit()


if __name__ == '__main__':
    # 初始化变量
    pg.init()  # 初始化
    pg.font.init()  # 初始化字体
    font = pg.font.SysFont("Arial", 50)  # 设置字体大小
    size = width, height = 400, 650  # 设置窗口大小
    screen = pg.display.set_mode(size)  # 显示窗口
    clock = pg.time.Clock()
    score = 0  # 统计分数
    background = pg.image.load("assets/background.png")  # 加载背景图片
    mybird = Birds()
    pipeline = Pipeline()


    main()


