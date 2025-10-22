#管理飞船的大部分行为

#使用图像时，使用位图(.bmp)文件最为简单，因为pygame默认加载位图

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self,ai_settings,screen):                 #screen指定了飞船将绘制到什么地方
        """初始化飞船并设置初始位置"""
        super().__init__()
        self.screen=screen

        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images\ship.bmp')    #加载图像，pygame.image.load()返回一个表示飞船的surface
        self.rect=self.image.get_rect()            
        self.screen_rect=screen.get_rect()      #用get_rect()获取相应surface的属性rect
                                                #像处理矩形一样处理游戏元素
        self.ai_settings=ai_settings

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx  #把飞船中心的x坐标设为屏幕中心的x坐标
        self.rect.bottom=self.screen_rect.bottom   
        
        #处理时可使用使用矩形四角和中心的x、y坐标
        #要将游戏对象居中，可设置相应rect对象的属性center,centerx或centery
        #要让游戏对象与屏幕边缘对齐，可使用属性top,bottom,left,right
        #要调整游戏元素的水平或垂直位置，可使用属性x和y
        #在pygame中，原点(0,0)位于屏幕左上角，向右下方移动时，坐标增大

        #在飞船的属性center中存储小数值
        self.center=float(self.rect.centerx)

        #移动标志
        self.moving_right=False  #飞船不动时，标记为False
        self.moving_left=False

    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值而不是rect以存储小数
        if self.moving_right and self.rect.centerx<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx>0:
            self.center-=self.ai_settings.ship_speed_factor
        
        #根据self.center更新rect对象
        self.rect.centerx=self.center

    def blitime(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx


