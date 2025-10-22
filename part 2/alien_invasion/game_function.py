import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien

def ship_hit(ai_settings,stats,screen,score,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left>1:
        #将ships_left减1
        stats.ships_left-=1

        #更新记分牌
        score.prep_ships()

        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)
    
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True   #向右移动飞船 
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        #创建一颗子弹，并加入编组bullets中
        fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    #创建一颗子弹，并加入编组bullets中
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False

def check_events(ai_settings,screen,stats,score,play_button,ship,aliens,bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():     #监视键盘和鼠标事件
        if event.type==pygame.QUIT:      #事件循环。事件：用户执行的操作
            sys.exit()                   #我们使用方法pygame.event.get()访问检测到的事件
                                         #我们将会编写一系列的if语句检测并响应特定事件
                                         #例如，单击游戏窗口的关闭按钮时，将检测到pygame.QUIT
                                         #我们调用sys.exit()来推出游戏

        elif event.type==pygame.KEYDOWN:   #响应按键：每当用户按键时，都将在pygame中注册一个KEYDOWN事件
            check_keydown_events(event,ai_settings,screen,ship,bullets)  
                                              #事件可以通过pygame.event.get()读取
                                              #我们需要指定要检查哪些类型的事件 
            

        elif event.type==pygame.KEYUP:  #检测松开键盘
            check_keyup_events(event,ship)

        elif event.type==pygame.MOUSEBUTTONDOWN:  #检测鼠标点击
            mouse_x,mouse_y=pygame.mouse.get_pos() #返回一个包含玩家点击鼠标位置的x、y坐标的元组
            check_play_button(ai_settings,screen,stats,score,play_button,ship,
                              aliens,bullets,mouse_x,mouse_y)
        
def check_play_button(ai_settings,screen,stats,score,play_button,ship,aliens,
                      bullets,mouse_x,mouse_y):
    """在玩家单击Play时开始游戏"""
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y) #检测鼠标点击位置是否在按钮范围内
    if button_clicked and not stats.game_active: 
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()

        #隐藏光标
        pygame.mouse.set_visible(False)

        stats.game_active=True   
        #重置游戏统计信息
        stats.reset_stats()

        #重置记分牌
        score.prep_score()
        score.prep_high_score()
        score.prep_level()

        score.prep_ships()

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
   

def update_screen(ai_settings,screen,stats,score,ship,aliens,bullets,play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时重回屏幕
    screen.fill(ai_settings.bg_color)   #方法screen.fill():用背景色填充屏幕
                                        #这个方法只接受一个实参：一种颜色
    
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    aliens.draw(screen) #对编组调用draw()时，pygame自动绘制编组的每个元素，位置由元素的rect属性决定

    ship.blitime()   
    #填充背景后调用blitime()绘制飞船到屏幕上 

    #显示得分
    score.show_score()

    #如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    #让最近绘制的屏幕可见
    pygame.display.flip()    
    #这里，它每次执行时都会绘制一个新屏幕并擦去旧屏幕          


def update_bullets(ai_settings,screen,stats,score,ship,aliens,bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()  #对编组调用update()时，将自动对其中的每个精灵调用update()
    #删除已销失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    #print(len(bullets)) 检验是否成功删除
    #因为 python在删除第一个元素后，后面的所有元素会向前移一位， 相应的，索引值也会发生改变。
    #但是循环执行时就相当于有一个指针，它不管列表中的元素位置如何变化，它始终“ 忠贞不渝 ”，
    # 所以它还仍然指在索引值为1的位置，在进行下一次循环时，它就指向索引值为 2 的位置，
    # 对应的元素为原3号位元素。原2号位元素向前移到一位，因此“ 逃过一劫 ”。
    #因此，在for循环中，不应从列表或编组中删除条目，而是利用副本，
    #因为在删除的过程中，我们并没有改变一开始复制的副本

    check_bullet_alien_collisions(ai_settings,screen,stats,score,ship,aliens,bullets)

    

def check_bullet_alien_collisions(ai_settings,screen,stats,score,ship,aliens,bullets):
    """响应外星人和子弹的碰撞"""
    #删除发生碰撞的子弹和外星人
    #检查是否有子弹击中了外星人
    #若有，删除相应的子弹和外星人
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    #方法sprite.groupcollide()将每颗子弹的rect与每个外星人的rect进行比较，并返回一个字典
    #其中包含了发生了碰撞的子弹和外星人
    #在这个字典中，每个键都是一颗字典，而相应的值是被击中的外星人所构成的列表
    #这里，两个实参True告诉pygame删除发生碰撞的子弹和外星人
    #若要模拟能够穿透的子弹，可将第一个True改为False
    
    if collisions:
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_points*len(aliens) #在一颗子弹消灭了两个外星人的情况下正确记分
            score.prep_score()
        check_high_score(stats,score)

    if len(aliens)==0:   #这一批外星人被全部消灭
        #删除现有子弹，加快游戏节奏，创建一群新的外星人
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)

        #等级提高
        stats.level+=1
        score.prep_level()


def get_number_aliens_x(ai_settings,alien_width):
    """计算一行能容纳多少个外星人"""
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y=(ai_settings.screen_height-
                       (3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并放到当前行"""
    #外星人间距为外星人宽度
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行能容纳多少个
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #创建一群外星人
    for row_number in range(number_rows):  #每次创建一行
        #创建一行外星人
        for alien_number in range(number_aliens_x):
            #创建一个外星人并加入当前行
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    """检测外星人是否到达边缘"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

def update_aliens(ai_settings,stats,screen,score,ship,aliens,bullets):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,score,ship,aliens,bullets)

    #方法spritecollideany()接受两个实参：一个精灵和一个编组,它检查编组是否有成员与精灵发生了碰撞
    #这里，它遍历编组aliens，并返回它找到的第一个与飞船发生了碰撞的外星人
    #若没有发生碰撞，其返回None        

    #检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,score,ship,aliens,bullets)

def check_aliens_bottom(ai_settings,stats,screen,score,ship,aliens,bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #像飞船被撞到一样处理
            ship_hit(ai_settings,stats,screen,score,ship,aliens,bullets)
            break
    
def check_high_score(stats,score):
    """检查是否诞生了新的最高得分"""
    if stats.score>stats.highest:
        stats.highest=stats.score
        score.prep_high_score()