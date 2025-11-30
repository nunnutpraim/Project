import pygame
import sys
pygame.init()   #เป็นการบอกว่าเริ่มรันโค้ดตรงนี้
#--3 Screen dimention
screen_width = 800
screen_height = 600
#--4 Color definition
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
#--5 Create the Screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My Game")
#--6 Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():    # event คือเช่นการกดปุ่ม ขยับจอยเกม
        if event.type == pygame.QUIT:
             running = False
        pygame.draw.line(screen, black, (200,200), (600,200),3)  #3 คือความหนา
        pygame.draw.line(screen, black, (200,400), (600,400),3)
        pygame.draw.line(screen, black, (200,200), (200,400),3)
        pygame.draw.line(screen, black, (600,200), (600,400),3)
        pygame.draw.rect(screen,red,(100,100, 600,400),1) #0คือระบายสี 1 คือไม่ระบาย
        pygame.draw.circle(screen,blue,(400,300),50,1) #0คือระบายสี 1 คือไม่ระบาย
        pygame.display.flip()
        clock.tick(80)
pygame.quit()
sys.exit()