import pygame
from pygame.draw import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def street(x_o, y_o, h, dir):
    '''
    (x_o, y_o) - the left top point of the left house, h - height of the left house,
    dir = +-1, direction of the street (1 - as before)
    '''
    a = h / 460
    rect(screen, (169, 187, 197), (x_o, y_o, dir * 115 * a, 460 * a))
    rect(screen, (166, 186, 182), (x_o + dir * 140 * a, y_o + 30 * a, dir * 110 * a, 450 * a))
    rect(screen, (202, 210, 209), (x_o + dir * 60 * a, y_o + 75 * a, dir * 125 * a, 440 * a))
    rect(screen, (240, 248, 250), (x_o + dir * 380 * a, y_o - 10 * a, dir * 120 * a, 480 * a))
    rect(screen, (116, 136, 132), (x_o + dir * 320 * a, y_o + 120 * a, dir * 110 * a, 420 * a))



def car(x_o, y_o, h, dir):
    '''
    (x_o, y_o) - the back bottom point of the body rect, h - height of the body rect,
    dir = +-1, direction of the car (1 - left)
    '''
    a = h / 50
    ellipse(screen, (0, 0, 0, 255), (x_o - 15 * a, y_o + 35 * a, 30 * a, 10 * a))
    rect(screen, (50, 204, 255), (x_o, y_o, dir * 260 * a, h))
    rect(screen, (50, 204, 255), (x_o + dir * 40 * a, y_o - 40 * a, dir * 130 * a, 40 * a))
    rect(screen, (240, 240, 250), (x_o + dir * 50 * a, y_o - 30 * a, dir * 45 * a, 30 * a))
    rect(screen, (240, 240, 250), (x_o + dir * 120 * a, y_o - 30 * a, dir * 48 * a, 30 * a))
    rect(screen, (240, 255, 240), (x_o + dir * 248 * a, y_o + 2 * a, dir * 10 * a, 10 * a))
    circle(screen, BLACK, (x_o + dir * int(220 * a), y_o + int(50 * a)), int(25 * a))
    circle(screen, BLACK, (x_o + dir * int(50 * a), y_o + int(50 * a)), int(25 * a))


FPS = 30
screen = pygame.display.set_mode((533, 800))
rect(screen, (91, 111, 108, 255), (0, 550, 533, 250))

rect(screen, (191, 191, 191), (-10, -10, 410, 210))
rect(screen, WHITE, (-10, -10, 410, 210), 3)

rect(screen, (121, 121, 121), (400, -10, 140, 210))

rect(screen, (161, 161, 161, 0.2), (0, 0, 50, 188))

rect_1 = pygame.Surface((800, 800), pygame.SRCALPHA)
rect(rect_1, (1, 1, 1, 170), (0, 88, 100, 100))
rect(rect_1, (31, 31, 31, 80), (150, 20, 80, 180))
rect(rect_1, (1, 1, 1, 100), (250, 0, 200, 200))
screen.blit(rect_1, (0, 0))

rect_2 = pygame.Surface((800, 800), pygame.SRCALPHA)
rect(rect_2, (1, 1, 1, 130), (180, 100, 100, 100))
rect(rect_2, (1, 1, 1, 150), (290, 0, 100, 200))
rect(rect_2, (1, 1, 1, 120), (320, 0, 100, 200))
rect(rect_2, (1, 1, 1, 130), (480, 0, 100, 200))
screen.blit(rect_2, (0, 0))

ellipse_1 = pygame.Surface((800, 800), pygame.SRCALPHA)
ellipse(ellipse_1, (1, 1, 1, 70), (130, -20, 600, 100))
ellipse(ellipse_1, (1, 1, 1, 80), (430, 100, 600, 100))
ellipse(ellipse_1, (1, 1, 1, 80), (-350, 140, 620, 100))
screen.blit(ellipse_1, (0, 0))

ellipse_2 = pygame.Surface((800, 800), pygame.SRCALPHA)
ellipse(ellipse_2, (1, 1, 1, 30), (-300, -20, 650, 100))
screen.blit(ellipse_2, (0, 0))

ellipse_3 = pygame.Surface((800, 800), pygame.SRCALPHA)
ellipse(ellipse_3, (1, 1, 1, 50), (90, 20, 480, 100))
screen.blit(ellipse_3, (0, 0))

rect(screen, WHITE, (400, -10, 140, 210), 3)

rect(screen, (211, 218, 218), (190, 170, 500, 380))
rect(screen, WHITE, (190, 170, 500, 380), 3)

ellipse_4 = pygame.Surface((800, 800), pygame.SRCALPHA)
ellipse(ellipse_4, (181, 191, 191, 100), (120, 0, 500, 100))
screen.blit(ellipse_4, (205, 225))

street(570, 200, 350, -1)

rect(screen, (201, 215, 221), (-10, 190, 300, 390))
rect(screen, WHITE, (-10, 190, 300, 390), 3)

street(-100, 223, 350, 1)

ellipse_5 = pygame.Surface((800, 800), pygame.SRCALPHA)
ellipse(ellipse_5, (201, 215, 221, 40), (50, 0, 235, 50))
ellipse(ellipse_5, (201, 215, 221, 30), (100, 180, 192, 50))
screen.blit(ellipse_5, (0, 225))

car(110, 600, 10, -1)
car(290, 620, 15, -1)
car(383, 590, 10, -1)
car(495, 630, 15, -1)
car(40, 665, 35, 1)
car(480, 710, 40, -1)

for i in range(1, 200, 4):
    ellipse_i = pygame.Surface((800, 800), pygame.SRCALPHA)
    ellipse(ellipse_i, (250, 250, 250, 10 - i / 100), (200 - (i - 1) / 2, 200 - (i - 1) / 2, 2 * i, i))
    screen.blit(ellipse_i, (0, 500))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
