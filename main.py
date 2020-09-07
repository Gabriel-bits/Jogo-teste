# Tem que validar para poder exporta:
#import os, sys

#dirpath = os.getcwd()
#sys.path.append(dirpath)
#if getattr(sys, "frozen", False):
#    os.chdir(sys._MEIPASS)

###
# ===================================================== #
# imports:                                              #
# ===================================================== #

import pygame
import random
import time

from nave import Nave
from asteroid import Asteroid

# ===================================================== #
# inicialização da janela:                              #
# ===================================================== #
pygame.init()

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Meu Teste")
font = pygame.font.SysFont(None, 100)



# ===================================================== #
# Personagem and object:                                #
# ===================================================== #

objectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()

# ===================================================== #
# Draw, text and backgraund:                            #
# ===================================================== #


def desenhar_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw():
    display.fill([255, 255, 255])


def tex1():
    desenhar_text('LOADING', font, (255, 255, 255), display, 100, 100)



def tex2():
    desenhar_text('Game over', font, (255, 255, 255), display, 100, 100)



bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/tela/backg.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()


# ===================================================== #
# Music:                                                #
# ===================================================== #


def play1():
    pygame.mixer.music.load("data/música/awesomeness.wav")
    pygame.mixer.music.play(-1)


def play2():
    pygame.mixer.music.load("data/música/the_field_of_dreams.mp3")
    pygame.mixer.music.play(-1)


play2()
# =====================================================#
# Sounds:                                              #
# =====================================================#


shoot = pygame.mixer.Sound("data/música/Shoot.wav")

# =====================================================#
# loop:                                                #
# =====================================================#

nave = Nave(objectGroup)
asteroid = Asteroid(objectGroup)

gameLoop = True
gameOver = False
clock = pygame.time.Clock()
numero = 10

if __name__ == "__main__":

    while gameLoop:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    shoot.play()

        if not gameOver:

            objectGroup.update()

            numero += 1
            if numero > 15:
                numero = 0
                if random.random() < 0.5:
                    newasteroid = Asteroid(objectGroup, asteroidGroup)

            colisão = pygame.sprite.spritecollide(nave, asteroidGroup, False, pygame.sprite.collide_mask)

            if colisão:
                print("Game Over")
                gameOver = True

        objectGroup.draw(display)

        pygame.display.update()
