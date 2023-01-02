import pygame
import math
import os
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
  BACKGROUND, (uzunluk, uzunluk))
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

# Draw Slider Texts
draw_text(ekran, self.metin, (895, self.y-5),
            15, (0, 0, 0), alignRight=True, alignCenterHorizontal=True)
      pygame.draw.rect(ekran, (255, 0, 255), self.valueRect, width=1)

# Draw Slider Circles
        pygame.draw.circle(ekran , (0, 0, 0), (locationX, self.y), 15)
<<<<<<< HEAD
  # Draw Slider Texts
        draw_text(screen, self.metin, (895, self.y-5),
                  15, (0, 0, 0), alignRight=True, alignCenterHorizontal=True)
        pygame.draw.rect(screen, (255, 0, 255), self.valueRect, width=1)

         if self.writingBuffer == "":
          val = self.get_value()

if self.metin == "İp Uzunluğu":
                val /= ip_uzunluğu_bölücü
            draw_text(screen, str(round(val, 2)), (self.valueRect.centerx, self.valueRect.y),
                      20, (0, 0, 0), alignCenterVertical=True, alignCenterHorizontal=True)
        else:
            draw_text(screen, self.writingBuffer, (self.valueRect.centerx, self.valueRect.y),
                      20, (0, 0, 0), alignCenterVertical=True, alignCenterHorizontal=True)


 def moveIfColliding(self, mousePos):  # returns true if it was moved
        if pygame.mouse.get_pressed()[0] != 1:
            return False
        locationX = 900 + self.yüzde * 2.5
        if self.x + değer_çubuğu_uzunluğu > mousePos[0] > self.x and self.y + 15 > mousePos[1] > self.y - 15 and locationX + 15 > mousePos[0] > locationX - 15 and self.y + 15 > mousePos[1] > self.y - 15:
            self.yüzde = (mousePos[0] - 900) / 2.5
            return True
        return False

    def update(self, gameEvents):
        mousePos = pygame.mouse.get_pos()
        self.moveIfColliding(mousePos)


