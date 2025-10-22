import sys #玩家退出时，使用该模块退出游戏

import pygame #包含游戏开发所需功能
from pygame.sprite import Group 

from settings import Settings
from ship import Ship
import game_function as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创造一个屏幕对象
    pygame.init() #初始化背景设置
    ai_settings=Settings()  
    screen=pygame.display.set_mode(                                            
            (ai_settings.screen_width,ai_settings.screen_height))
        #创建一个名为screen的显示窗口
        #实参(1200,800)是一个元组，指定游戏窗口尺寸
        #对象screen是一个surface。
        #在pygame中，surface是屏幕的一部分，用于显示游戏元素
        #display.set_mode()返回的surface表示整个游戏窗口
        #激活游戏的动画循环后，每次循环都会重绘surface

    pygame.display.set_caption("Alice invasion")

    #创建一个用于存储游戏统计信息的实例
    stats=GameStats(ai_settings)

    #创建计分板
    score=Scoreboard(ai_settings,screen,stats)

    #创建一艘飞船
    ship=Ship(ai_settings,screen)               
    
    #创建一个用于存储子弹的编组
    bullets=Group()  #这个类类似于列表，但有一些额外功能

    #创建一个外星人编组
    aliens=Group()

    #创建外星人群
    #gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建play按钮
    play_button=Button(ai_settings,screen,"Play")

    #开始游戏的主循环
    while True:                 #游戏由一个while循环控制
                                #其中包含一个事件循环以及管理屏幕更新的代码

        gf.check_events(ai_settings,screen,stats,score,
                        play_button,ship,aliens, bullets)  #重构代码使其更简洁           
        
        if stats.game_active:
            ship.update()                  

            gf.update_bullets(ai_settings,screen,stats,score,ship,aliens,bullets)

            gf.update_aliens(ai_settings,stats,screen,score,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,score,ship,aliens,bullets,play_button)

run_game()                                 #初始化游戏并开始主循环