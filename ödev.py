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

BACKGROUND = pygame.image.load(os.path.join("image", "background.jpg"))
BACKGROUND_IMAGE = pygame.transform.scale(
  BACKGROUND, (HEIGHT, HEIGHT))
BACKGROUND_IMAGE.set_alpha(50)
BALL_START_X, BALL_START_Y = HEIGHT / 2, ROPE_LENGTH_START + 20


WIDTH_SLIDER = 250
class Slider:
  
    def __init__(self, x, y, text, minVal, maxVal):
 self.x = x
 self.y = y
self.text = text
 self.min = minVal
 self.min = minVal







