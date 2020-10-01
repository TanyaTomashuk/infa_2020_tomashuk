import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((533, 800))
rect(screen, (201, 215, 221, 255), (0, 0, 533, 467))
rect(screen, (91, 111, 108, 255), (0, 467, 533, 333))
rect(screen, (255, 255, 255, 255), (0, 467, 533, 5))

ellipse_surface_1 = pygame.Surface((250, 290), pygame.SRCALPHA)
ellipse(ellipse_surface_1, (191, 209, 201, 70), (91, 111, 147, 45))
screen.blit(ellipse_surface_1, (-60, 450))

ellipse_surface_2 = pygame.Surface((250, 290), pygame.SRCALPHA)
ellipse(ellipse_surface_2, (191, 209, 201, 100), (91, 111, 147, 45))
screen.blit(ellipse_surface_2, (-170, 400))

ellipse(screen, (221, 227, 221, 255), (-30, 610, 700, 300))

ellipse_surface_3 = pygame.Surface((250, 290), pygame.SRCALPHA)
ellipse(ellipse_surface_3, (191, 209, 201, 130), (91, 111, 140, 40))
screen.blit(ellipse_surface_3, (-10, 500))

#(x_o, y_o) - the back bottom point of the body rect, h - height of the body rect, dir = +-1, direction of the car (1 - left)
def car(x_o, y_o, h, dir):
    a = h / 50
    ellipse(screen, (0, 0, 0, 255), (x_o - 15 * a, y_o + 35 * a, 30 * a, 10 * a))
    rect(screen, (50, 204, 255, 255), (x_o, y_o, dir * 260 * a, h))
    rect(screen, (50, 204, 255, 255), (x_o + dir * 40 * a, y_o - 40 * a, dir * 130 * a, 40 * a))
    rect(screen, (240, 240, 250, 255), (x_o + dir * 50 * a, y_o - 30 * a, dir * 45 * a, 30 * a))
    rect(screen, (240, 240, 250, 255), (x_o + dir * 120 * a, y_o - 30 * a, dir * 48 * a, 30 * a))
    rect(screen, (240, 255, 240, 255), (x_o + dir * 248 * a, y_o + 2 * a, dir * 10 * a, 10 * a))
    circle(screen, (0, 0, 0, 255), (x_o + dir * 220 * a, y_o + 50 * a), 25 * a)
    circle(screen, (0, 0, 0, 255), (x_o + dir * 50 * a, y_o + 50 * a), 25 * a)

car(230, 630, 50, 1)

rect(screen, (240, 248, 250), (400, 20, 120, 480))
rect(screen,(116, 136, 132), (340, 150, 110, 420))

ellipse_surface_4 = pygame.Surface((600, 600), pygame.SRCALPHA)
ellipse(ellipse_surface_4, (191, 201, 191, 100), (-200, 100, 700, 130))
screen.blit(ellipse_surface_4, (-160, -50))

rect(screen, (169, 187, 197), (20, 30, 115, 460))

ellipse_surface_5 = pygame.Surface((600, 600), pygame.SRCALPHA)
ellipse(ellipse_surface_5, (191, 201, 191, 100), (0, 100, 700, 130))
screen.blit(ellipse_surface_5, (100, -100))

ellipse_surface_6 = pygame.Surface((600, 600), pygame.SRCALPHA)
ellipse(ellipse_surface_6, (191, 201, 191, 110), (-200, 400, 650, 110))
screen.blit(ellipse_surface_6, (-130, -80))

rect(screen, (166, 186, 182), (160, 60, 110, 450))
rect(screen, (202, 210, 209), (80, 105, 125, 440))

ellipse_surface_7 = pygame.Surface((600, 600), pygame.SRCALPHA)
ellipse(ellipse_surface_7, (191, 201, 195, 100), (50, 300, 600, 120))
screen.blit(ellipse_surface_7, (100, -100))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()