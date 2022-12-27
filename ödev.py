import pygame
import math
pygame.init()

#sarkacı tanımlamak gerekiyor.
#önce ekran

boyutlar = genişlik, uzunluk = 1250, 800
APP_NAME = "Sarkaç"
FPS = 60
yer_çekimi = 9.8


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

top_için_başlangiç_x, top_için_başlangiç_y = uzunluk / 2, ipin_başlangiç_uzunluğu + 20
 

değer_çubuğu_uzunluğu = 250 

class Slider:
  
    def __init__(self, x, y, text, minVal, maxVal):
 self.x = x
 self.y = y
self.text = text
 self.min = minVal
 self.max = maxVal
  self.percent = 50
self.valueRect = pygame.Rect(
 self.x + WIDTH_SLIDER + 15, self.y - 15, 70, 30)
 self.writing = False
 self.writingBuffer = ""


