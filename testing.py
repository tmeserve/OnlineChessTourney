import chess
import pygame
import chess.svg
import os, time
import array
import math

import cairo
import cairosvg

pygame.init()

board = chess.Board()

out_file = open(os.path.join(os.getcwd(), 'testing.svg'), 'w+')
squares = board.attacks(chess.E4)
out_file.write(chess.svg.board(board=board, squares=squares))
out_file.close()
cairosvg.svg2png(url=os.path.join(os.getcwd(), 'testing.svg'), write_to='image.png')
img = pygame.image.load(os.path.join(os.getcwd(), 'image.png')).convert()
rect = img.get_rect()

WIDTH = rect.width
HEIGHT = rect.height
size = (WIDTH, HEIGHT)
img = pygame.transform.scale(img, (WIDTH, HEIGHT))

pygame.init()
window = pygame.display.set_mode(size, pygame.RESIZABLE)


clock = pygame.time.Clock()
white = (255, 255, 255)
while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        
        elif event.type == pygame.VIDEORESIZE:
            esize = event.dict['size']
            height = esize[1]
            width = esize[0]
            if esize[0] < WIDTH:
                width = WIDTH
            if esize[1] < HEIGHT:
                height = HEIGHT
            size = (width, height)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            img = pygame.transform.scale(img, size)
            screen.blit(pygame.transform.scale(img, size), [0, 0])
            pygame.display.flip()
        
    screen.fill(white)
    screen.blit(img, [0, 0])
    pygame.display.flip()