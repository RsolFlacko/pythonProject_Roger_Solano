#   Prueba creación de primer videojuego

import pygame
import sys
import random


ANCHO = 1000
LARGO = 600
color_blue = (0,0,255)
color_black = (0,0,0)
color_purple = (172, 51, 255)
color_white = (255,255,255)

#   Player
player_size = 60
player_pos = [ANCHO / 2,LARGO - player_size * 2]

#   Villain(s)
villain_size = 60
villain_pos = [random.randint(0, ANCHO - villain_size),0]

ventana = pygame.display.set_mode((ANCHO,LARGO))

game_over = False
clock = pygame.time.Clock()

def crash(player_pos,villain_pos):
    px = player_pos[0]
    py = player_pos[1]
    vx = villain_pos[0]
    vy = villain_pos[1]

    if (vx >= px and vx < (px + player_size)) or (px >= vx and px < (vx + villain_size)):
        if (vy >= py and vy < (py + player_size)) or (py >= vy and py < (vy + villain_size)):
            return True
        else:
            return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_size
            if event.key == pygame.K_RIGHT:
                x += player_size

            player_pos[0] = x

    ventana.fill(color_black)

    if villain_pos[1] >= 0 and villain_pos[1] < LARGO:
        villain_pos[1] += 20
    else:
        villain_pos[0] = random.randint(0, ANCHO - villain_size)
        villain_pos[1] = 0

    #   Crash
    if crash(player_pos,villain_pos):
        game_over = True

        ventana = pygame.display.set_mode((ANCHO, LARGO))
        pygame.display.set_caption("Game Over")

    #   Draw villain(s)
    pygame.draw.rect(ventana, color_purple, (villain_pos[0], villain_pos[1], villain_size, villain_size))

    #   Draw player
    pygame.draw.rect(ventana, color_blue, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    pygame.display.update()
