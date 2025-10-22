import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):  #通过使用精灵，可以将游戏中相关的元素编组，进而同时操作编组中的所有元素
    """一个对飞船发射的子弹进行管理的类"""
    
    def __init__(self, ai_settings,screen,ship):
        """在飞船所处位置创建一个子弹对象"""
        super().__init__()
        self.screen=screen

        #在(0,0)创建一个表示子弹的矩形，再设置正确的位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
                              ai_settings.bullet_height)  
            #子弹并未基于图像，因此必须使用pygame.Rect()类从空白开始创建一个矩形
            #创建这个类的实例时，必须提供左上角的x、y坐标，以及矩形的长宽
        
        self.rect.centerx=ship.rect.centerx 
        self.rect.centery=ship.rect.centery #将子弹移到飞船的位置
        #存储用小数表示的子弹位置,便于精细调控
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y-=self.speed_factor

        self.rect.y=self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)