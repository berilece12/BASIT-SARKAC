import pygame
import math
pygame.init()

#sarkacı tanımlamak gerekiyor.
#önce ekran
SIZE = WIDTH, HEIGHT = 1250, 800
APP_NAME = "Sarkaç"
FPS = 60
GRAVITY = 9.8


ROPE_LENGTH_START = 400
ROPE_LEN_DIVIDER = 200
ROPE_CONNECTION_POS = (HEIGHT // 2, 20)
SCREEN = pygame.display.set_mode(SIZE)

#  sarkaç, saniyedeki görüntü sayısı, yerçelkimi ve ipi tanımladık
#arka planı tanımla
