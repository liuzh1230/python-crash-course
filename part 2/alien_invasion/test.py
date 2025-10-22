import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
pygame.key.stop_text_input() # 停止文本输入模式
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
               print("你按下了右键")
pygame.quit()