#创建按钮

import pygame.font  #让python能将文本渲染到屏幕上

class Button():

    def __init__(self,ai_settings,screen,msg):  #msg是将在按钮中显示的文本
        """初始化按钮属性"""
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #设置按钮的尺寸和其他属性
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)   #指定字体，None表示使用默认字体；48指定了文本的字号

        #创建按钮的rect对象，并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #按钮的标签仅需创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染成图像，并使其在按钮上居中"""
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        #font.render()将存储在msg中的文本转换为图像，并存储在self.msg_image中
        #其还接受一个bool实参，指定反锯齿功能的开关，余下的两个实参分别控制文本色和背景色
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)