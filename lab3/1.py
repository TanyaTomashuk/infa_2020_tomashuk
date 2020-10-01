import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (255, 255, 255, 255), (0, 0, 500, 500))
circle(screen, (255, 255, 0, 255), (250, 250), 200)
circle(screen, (0, 0, 0, 255), (250, 250), 200, 3)
circle(screen, (255, 0, 0, 255), (150, 200), 40)
circle(screen, (0, 0, 0, 255), (150, 200), 40, 1)
circle(screen, (0, 0, 0, 255), (150, 200), 20)
circle(screen, (255, 0, 0, 255), (350, 200), 30)
circle(screen, (0, 0, 0, 255), (350, 200), 30, 1)
circle(screen, (0, 0, 0, 255), (350, 200), 15)
rect(screen, (0, 0, 0, 255), (150, 340, 200, 40))
polygon(screen, (0, 0, 0, 255), [(220, 202.5), (50, 75), (57.5, 65),
                                 (227.5, 192.5)])
polygon(screen, (0, 0, 0, 255), [(300, 210.9), (430, 65.3), (410, 47.4),
                                 (280, 193)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
