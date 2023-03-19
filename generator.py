import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600, 600), pygame.NOFRAME)

white = (255, 255, 255)
blue = (0, 170, 255)

# Vars
run = True
C = True
P1 = (150, 120)
P2 = (516, 300)
P3 = (450, 480)
P4 = (150, 480)
P5 = (83, 300)
P6 = (450, 120)
points = [P1, P2, P3, P4, P5, P6]
L = (0, 0)
LP = 0

def printThings(c, color=white):
    pygame.draw.rect(tela, color, c + (1, 1))
    pygame.display.update()

for x in points:
    printThings(x, blue)

while C:
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            L = pygame.mouse.get_pos()
            printThings(L)
            C = False
            print("Start")

while run:
    pygame.event.pump()

    P = random.choice(points)
    while P == LP:
        P = random.choice(points)
    LP = P

    # Set Middle Cords
    Np = (int(((L[0] + P[0]) / 2)), int(((L[1] + P[1]) / 2)))
    printThings(Np)
    L = Np
