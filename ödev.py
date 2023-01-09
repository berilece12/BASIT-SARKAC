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
        self.metin = metin
        self.min = minVal
        self.max = maxVal
        self.yüzde = 50
        self.valueRect = pygame.Rect(
            self.x + değer_çubuğu_uzunluğu + 15, self.y - 15, 70, 30)
        self.writing = False
        self.writingBuffer = ""

    def draw(self, ekran):
        locationX = 900 + self.yüzde * 2.5
        draw_line(ekran, (self.x, self.y), (self.x +
                  değer_çubuğu_uzunluğu, self.y), (0, 0, 0), 5)

        # Draw Slider Circles
        pygame.draw.circle(ekran, (0, 0, 0), (locationX, self.y), 15)

        # Draw Slider Texts
        draw_text(ekran, self.metin, (895, self.y-5),
                  15, (0, 0, 0), alignRight=True, alignCenterHorizontal=True)
        pygame.draw.rect(ekran, (255, 0, 255), self.valueRect, width=1)

        if self.writingBuffer == "":
            val = self.get_value()
            if self.metin == "İp Uzunluğu":
                val /= ip_uzunluğu_bölücü
            draw_text(ekran, str(round(val, 2)), (self.valueRect.centerx, self.valueRect.y),
                      20, (0, 0, 0), alignCenterVertical=True, alignCenterHorizontal=True)
        else:
            draw_text(ekran, self.writingBuffer, (self.valueRect.centerx, self.valueRect.y),
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

        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            if self.valueRect.left < mousePos[0] < self.valueRect.right and self.valueRect.top < mousePos[1] < self.valueRect.bottom:
                self.writing = True
            else:
                self.writing = False


        if self.writing:
            if gameEvents.type == pygame.KEYDOWN:
                if gameEvents.key == pygame.K_RETURN:
                    self.writing = False
                    if self.writingBuffer != "":
                        try:
                            v = float(self.writingBuffer)
                            if self.metin == "İp Uzunluğu":
                                v *= ip_uzunluğu_bölücü
                            v = self.clamp(v)
                            self.yüzde = (v - self.min) / \
                                (self.max - self.min) * 100
                            self.writingBuffer = ""
                        except:
                            self.writingBuffer = ""
                elif gameEvents.key == pygame.K_BACKSPACE:
                    self.writingBuffer = self.writingBuffer[:-1]
                else:
                    self.writingBuffer += gameEvents.unicode

        return self.get_value()

boyutlar = genişlik, uzunluk = 1250, 800
APP_NAME = "Sarkaç"
FPS = 60
yer_çekimi = 9.8

ipin_başlangiç_uzunluğu = 400
ip_uzunluğu_bölücü = 200
ip_bağlanti_konumu = (uzunluk // 2, 20)


def draw_arc(ekran, açı, ip_uzunluğu):
    açı = int(math.degrees(açı))
    if açı == 0:
        return
    l = []
    for i in range(-abs(açı), abs(açı)):
        x = ip_bağlanti_konumu[0] + ip_uzunluğu * math.sin(math.radians(i))
        y = ip_bağlanti_konumu[1] + ip_uzunluğu * math.cos(math.radians(i))
        l.append((x, y))
    pygame.draw.lines(ekran, (0, 0, 0), False, l, 1)
    draw_dashed_line(ekran, ip_bağlanti_konumu, l[0], (0, 0, 0), 1)
    draw_dashed_line(ekran, ip_bağlanti_konumu, l[-1], (0, 0, 0), 1)

def draw_text(ekran, textstr, konum, boyutlar, renk, alignRight=False, alignCenterHorizontal=False, alignCenterVertical=False):

    font = pygame.font.SysFont(pygame.font.get_default_font(), boyutlar)

    text = font.render(textstr, True, renk)


    if alignRight:

        x = konum[0] - text.get_genişlik()
           
    elif alignCenterHorizontal:

        x = konum[0] - text.get_genişlik() // 2
    else:

        x = konum[0]

    if alignCenterVertical:  # Yukarıdan Aşağı

        y = konum[1] + text.get_uzunluk() // 2  

    else:

        y = konum[1]
        
    screen.blit(text, (x, y))


def draw_ball(ekran, konum):
    pygame.draw.circle(ekran, (255, 0, 0), konum, 20)

def draw_line(ekran, konum1, konum2, renk, genişlik=1):
    pygame.draw.line(ekran, renk, konum1, konum2, genişlik)

def draw_rope_attachment(ekran):
    pygame.draw.rect(ekran, (0, 0, 0),
                     (ip_bağlanti_konumu[0] - 7, 0, 14, 25))


def draw(_top_pozisyonu, _ip_genişliği):

    ekran.blit(BACKGROUND_IMAGE, (0, 0))
    # Draw Rope:
    draw_dashed_line(ekran, ip_bağlanti_konumu,
                     (ip_bağlanti_konumu[0], uzunluk * 2 / 3), (0, 0, 0), _ip_genişliği)
    draw_rope_attachment(ekran)
    draw_line(ekran, (ip_bağlanti_konumu[0] - 1, ip_bağlanti_konumu[1]), (_top_pozisyonu[0] - 1,
              _top_pozisyonu[1]), (0, 0, 0), _ip_genişliği)
    # Draw Ball:
    draw_ball(ekran, _top_pozisyonu)
