#创建设置类
#给游戏新添加功能时，通常也将引入一些新设置
#将所有设置存储在一个地方，便于维护代码

class Settings():
    """存储alien_invasion的所有设置"""

    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230) #设置背景色

        #飞船设置
        self.ship_limit=3 #限制数量

        # 子弹设置
        self.bullet_width=3
        self.bullet_height=45
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3 #限制子弹数量

        #外星人设置
        self.fleet_drop_speed=5 #向下移动速度
        

        #以什么样的节奏加快游戏节奏
        self.speedup_scale=1.1
        #得分提高速度
        self.score_scale=1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        #设置飞船的速度使其每次移动1.5个像素
        self.ship_speed_factor=1.5
        #然而，rect的centerx等属性仅能存储整数值
        
        self.bullet_speed_factor=1

        self.alien_speed_factor=1
        
        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction=1

        #记分
        self.alien_points=50

    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        #print(self.alien_points)
        