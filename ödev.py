import pygame
import math
pygame.init()

#sarkacı tanımlamak gerekiyor.
#önce ekran

boyutlar = genişlik, uzunluk = 1250, 800
APP_NAME = "Sarkaç"
FPS = 60
yer_çekimi = 9.8

ipin_başlangiç_uzunluğu = 400
ip_uzunluğu_bölücü = 200
ip_bağlanti_konumu = (uzunluk // 2, 20)
ekran = pygame.display.set_mode(boyutlar)
pygame.display.set_caption(APP_NAME)

#  sarkaç, saniyedeki görüntü sayısı, yerçelkimi ve ipi tanımladık
#arka planı tanımla

BACKGROUND = pygame.image.load(os.path.join("image", "background.jpg"))
BACKGROUND_IMAGE = pygame.transform.scale(
  BACKGROUND, (HEIGHT, HEIGHT))
BACKGROUND_IMAGE.set_alpha(50)

top_için_başlangiç_x, top_için_başlangiç_y = uzunluk / 2, ipin_başlangiç_uzunluğu + 20


değer_çubuğu_uzunluğu = 250 


class Slider:
  def __init__(self, x, y, metin, minVal, maxVal):
    self.x = x
    
  
    
    
    
    
    self.y = y
    self.text = metin
    self.min = minVal
    self.max = maxVal
    self.yüzde = 50
    self.valueRect = pygame.Rect(
      self.x + değer_çubuğu_uzunluğu + 15, self.y - 15, 70, 30)
    self.writing = False
    self.writingBuffer = ""

def get_value(self):

  return self.min + (self.max - self.min) * self.yüzde / 100
