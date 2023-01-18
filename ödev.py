import pygame
import os
import math

pygame.init()

#sarkacı tanımlamak gerekiyor.
#önce ekran

screen = genişlik, uzunluk = 1250, 800
APP_NAME = "Sarkaç"
FPS = 60
yer_çekimi = 9.8

ipin_başlangiç_uzunluğu = 400
dönüşüm_sabiti = 200 #pikseli metreye döndürme sabiti
ip_bağlanti_konumu = (uzunluk // 2, 20)
ekran = pygame.display.set_mode(screen)
pygame.display.set_caption(APP_NAME)

# sarkaç, saniyedeki görüntü sayısı, yerçekimi ve ipi tanımladık
#arka planı tanımla

BACKGROUND = pygame.image.load(os.path.join("image", "background.jpg"))
BACKGROUND_IMAGE = pygame.transform.scale(
  BACKGROUND, (uzunluk, uzunluk))
BACKGROUND_IMAGE.set_alpha(50)

top_için_başlangiç_x, top_için_başlangiç_y = uzunluk / 2, ipin_başlangiç_uzunluğu + 20


değer_çubuğu_uzunluğu = 250 
class kaydıraç:
    def __init__(self, x, y, metin, minVal, maxVal):
        self.x = x
        self.y = y
        self.text = metin
        self.min = minVal 
        self.max = maxVal
        self.yüzde = 50 # ip uzunluğumuz 400 yüzde %50si 200 
        self.valueRect = pygame.Rect(
            self.x + değer_çubuğu_uzunluğu + 15, self.y - 15, 70, 30) # kutucuğun konumu
        self.writing = False
        self.writingBuffer = ""
    
# fonksiyonu ile değer aralıklarını minimum ve maksimum değerler arasına sıkıştırdık.
    def clamp(self, val):
        return max(self.min, min(self.max, val))

    def get_value(self): #kaydıraçtaki değeri minval ve maxvala göre
        return self.min + (self.max - self.min) * self.yüzde / 100

    def çiz(self, ekran):
        x_konumu = 900 + self.yüzde * 2.5
        topun_ipi(ekran, (self.x, self.y), (self.x +
                  değer_çubuğu_uzunluğu, self.y), (0, 0, 0), 5) #kaydıçakların kalınlığı

        # Draw Slider Circles (değer çubuğundaki topların genişliği,boyutu)
        pygame.draw.circle(ekran, (0, 0, 0), (x_konumu, self.y), 15)

        # Draw Slider Texts ( değer çubuğu yanı yazılarının büyüklüğü)(ip uzunluğu,yer çekimi)
        metin_yaz(ekran, self.text, (895, self.y-5),
                  15, (0, 0, 0), alignRight=True, yatay_merkez_hizzası=True)
        pygame.draw.rect(ekran, (179, 1, 137), self.valueRect, width=2)

# değer çubuğuna girdiğimiz değerlerin -kutu içindeki- büyüklükleri
        if self.writingBuffer == "":
            val = self.get_value()
            if self.text == "İp Uzunluğu":
                val /= dönüşüm_sabiti
            metin_yaz(ekran, str(round(val, 2)), (self.valueRect.centerx, self.valueRect.y),
                      20, (0, 0, 0), düşey_merkez_hizzası=True, yatay_merkez_hizzası=True) #metin kutuusunu merkeze koyma*
        else:
            metin_yaz(ekran, self.writingBuffer, (self.valueRect.centerx, self.valueRect.y),
                      20, (0, 0, 0), düşey_merkez_hizzası=True, yatay_merkez_hizzası=True)
# mouse hareketleri ve mouse üzerinden yaptığımız işlemlerin sisteme aktarılması
    def moveIfColliding(self, mousePos):  # hareket varsa true 
        if pygame.mouse.get_pressed()[0] != 1:
            return False
        locationX = 900 + self.yüzde * 2.5
        if self.x + değer_çubuğu_uzunluğu > mousePos[0] > self.x and self.y + 15 > mousePos[1] > self.y - 15 and locationX + 15 > mousePos[0] > locationX - 15 and self.y + 15 > mousePos[1] > self.y - 15:
            self.yüzde = (mousePos[0] - 900) / 2.5 #sliderı mouse ile kaydırma miktarı
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

# kullanıcının girdiği değerleri konrtol edip sisteme atar.
        if self.writing:
            if gameEvents.type == pygame.KEYDOWN:
                if gameEvents.key == pygame.K_RETURN:
                    self.writing = False
                    if self.writingBuffer != "":
                        try:
                            v = float(self.writingBuffer)
                            if self.text == "İp Uzunluğu":
                                v *= dönüşüm_sabiti
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

screen = genişlik, uzunluk = 1250, 800
APP_NAME = "Sarkaç"
FPS = 60
yer_çekimi = 9.8

ipin_başlangiç_uzunluğu = 400
dönüşüm_sabiti = 200
ip_bağlanti_konumu = (uzunluk // 2, 20) #ipin takoza uzaklığı


def yay_çiz(ekran, açı, ip_uzunluğu):
    açı = int(math.degrees(açı))
    if açı == 0:
        return
    l = []
    for i in range(-abs(açı), abs(açı)): #abs: kayan noktalı açı
        x = ip_bağlanti_konumu[0] + ip_uzunluğu * math.sin(math.radians(i)) #açının başlangıç konumlar
        y = ip_bağlanti_konumu[1] + ip_uzunluğu * math.cos(math.radians(i)) #
        l.append((x, y))
    pygame.draw.lines(ekran, (255, 62, 150), False, l, 5) # yayın kalınlığı
    kesikli_çizgi_çiz(ekran, ip_bağlanti_konumu, l[0], (255, 62, 150), 1) # eğer 1 yaparsak yay sol eksi açıda daha uzun kalıyo
    kesikli_çizgi_çiz(ekran, ip_bağlanti_konumu, l[-1], (255, 62, 150), 1)

def metin_yaz(screen, textstr, konum, boyutlar, renk, alignRight=False, yatay_merkez_hizzası=False, düşey_merkez_hizzası=False):

    font = pygame.font.SysFont(pygame.font.get_default_font(), boyutlar)
    text = font.render(textstr, True, renk)
    if alignRight:
        x = konum[0] - text.get_width()           
    elif yatay_merkez_hizzası:
        x = konum[0] - text.get_width() // 2
    else:
        x = konum[0]
    if düşey_merkez_hizzası:  # Yukarıdan Aşağı
        y = konum[1] + text.get_height() // 2  
    else:
        y = konum[1]
        
    screen.blit(text, (x, y))

# sarkaç ucu topun genişliği
def top_oluşturma(ekran, konum):
    pygame.draw.circle(ekran, (32, 178, 170), konum, 20)

def topun_ipi(ekran, konum1, konum2, renk, genişlik=1):
    pygame.draw.line(ekran, renk, konum1, konum2, genişlik)

def kesikli_çizgi_çiz(ekran, ilk_konum, son_konum, color, genişlik=1, aralık=70):
    uzunluk = öklid(ilk_konum, son_konum)
    x = (son_konum[0] - ilk_konum[0]) / uzunluk #x ve y lerin hipotenüse bölümü kısaca kesikli çizgileri eşit ve tek tek çizilmesi için
    y = (son_konum[1] - ilk_konum[1]) / uzunluk
    for i in range(0, int(uzunluk), aralık): #kesikli çizgilerin boşluklarını ve aralıklarını ayarlar.
        pygame.draw.line(ekran, color, (ilk_konum[0] + i * x, ilk_konum[1] + i * y), (ilk_konum[0] + (
            i + aralık / 2) * x, ilk_konum[1] + (i + aralık / 2) * y), genişlik)

#ipin bağlı olduğu kalasın boyutlandırması
def topun_bağlantısı(ekran):
    pygame.draw.rect(ekran, (0,0,0),
                     (ip_bağlanti_konumu[0] - 7, 0, 14, 25))

def öklid(konum1, konum2): #öklid
    return math.sqrt((konum1[0] - konum2[0])**2 + (konum1[1] - konum2[1])**2) #sqrt karekök hesaplar.

def çiz(_top_pozisyonu, _ip_genişliği):

    ekran.blit(BACKGROUND_IMAGE, (0, 0))
    # Draw Rope:
    kesikli_çizgi_çiz(ekran, ip_bağlanti_konumu, #merkez eksen kesikli çizgi uzunluğu
                     (ip_bağlanti_konumu[0], uzunluk * 2 / 3), (0, 0, 0), _ip_genişliği)
    topun_bağlantısı(ekran)
    topun_ipi(ekran, (ip_bağlanti_konumu[0] - 1, ip_bağlanti_konumu[1]), (_top_pozisyonu[0] - 1,
              _top_pozisyonu[1]), (0, 0, 0), _ip_genişliği)
    # Draw Ball:
    top_oluşturma(ekran, _top_pozisyonu)
#girdiğimiz değerler ve top hareketi sonucu fonksiyonlardan çekilen değerleri ekranın sol üst kçöşesine yazdırma
def değerlere_ekrana_yaz(max_açı, açı, açısal_hız, ip_uzunluğu, geçen_zaman, periyot):
    metin_yaz(ekran, "Maksimum Açı: " + str(round(math.degrees(max_açı), 2)
                                             ) + "°", (10, 10), 20, (0, 0, 0))
    metin_yaz(ekran, "Anlık Açı: " + str(round(math.degrees(açı), 2)) + "°",
              (10, 30), 20, (0, 0, 0))
    metin_yaz(ekran, "Açısal Hız: " + str(round(açısal_hız, 2)) + " rad/s",
              (10, 50), 20, (0, 0, 0))
    metin_yaz(ekran, "Geçen Süre: " + str(round(geçen_zaman, 2)) + "sn",
              (10, 70), 20, (0, 0, 0))
    metin_yaz(ekran, "Period: " + str(round(periyot, 2)) + "sn",
              (10, 90), 20, (0, 0, 0))
    metin_yaz(ekran, "İp Uzunluğu: " + str(round((ip_uzunluğu / dönüşüm_sabiti), 2)) + "m",
              (10, 110), 20, (0, 0, 0))
    metin_yaz(ekran, "Yer Çekimi: " + str(round(yer_çekimi, 2)) +
              "m/s^2", (10, 130), 20, (0, 0, 0))


def sarkacın_periyodu(ip_uzunluğu): #periyot denklemi T=2pikökl/g
    return 2 * math.pi * math.sqrt((ip_uzunluğu / dönüşüm_sabiti)/yer_çekimi) #sqrt karekök alır.

def mouse_hareketi():
    mousePos = pygame.mouse.get_pos()
    angleRad = math.atan2(
        mousePos[0] - ip_bağlanti_konumu[0], mousePos[1] - ip_bağlanti_konumu[1])
    return angleRad

def top_hareket_denklemi(ip_uzunluğu, açi, geçen_süre): #topun hareket denklemi 
    angleNow = açi * \
        math.cos(math.sqrt(yer_çekimi/(ip_uzunluğu/dönüşüm_sabiti)) * geçen_süre)#sqrt karekök hesaplar.
    angularVelocity = -açi * \
        math.sqrt(yer_çekimi/(ip_uzunluğu/dönüşüm_sabiti)) * \
        math.sin(math.sqrt(yer_çekimi/(ip_uzunluğu/dönüşüm_sabiti)) * geçen_süre)#sqrt karekök hesaplar.
    return angleNow, angularVelocity
  
def topun_konumu(açı, ipin_uzunluğu):
    return (ip_bağlanti_konumu[0] + ipin_uzunluğu * math.sin(açı), ip_bağlanti_konumu[1] + ipin_uzunluğu * math.cos(açı))

def main():
    global yer_çekimi
    ipin_uzunluğu = ipin_başlangiç_uzunluğu
    ip_genişliği = 2
    top = pygame.draw.circle(
        ekran, (0, 0, 0), (top_için_başlangiç_x, top_için_başlangiç_y), 10)

    # Oyun Değişkenleri
    clock = pygame.time.Clock()
    hareket_varsa = True
    geçen_zaman = 0.0

    # Fizik Değişkenleri
    periyot = 0
    top_aktif = False #top oynuyor mu yer değiştirme fonksiyonuna girecek mi onu belirliyor
    açı = 0
    anlık_açı = 0
    açısal_hız = 0
    ballMass =  1

    # Slider Değişkenleri
    ip_uzunluğu_kaydıracı = kaydıraç(900, 100, "İp Uzunluğu", 200, 600) #ip başlanggiç değeri _sağ,sol------ip baslangıç uzunluğu fonk.
    yer_çekimi_kaydıracı = kaydıraç(900, 200, "Yer Çekimi", 0.1, 25)#yerçekimi başlangiç değeri


    while hareket_varsa:
        clock.tick(FPS)
        periyot = sarkacın_periyodu(ipin_uzunluğu)

        for event in pygame.event.get():
            ipin_uzunluğu = ip_uzunluğu_kaydıracı.update(event)
            yer_çekimi = yer_çekimi_kaydıracı.update(event)

            if event.type == pygame.QUIT:
                hareket_varsa = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    top_aktif = not top_aktif
            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] < 900:
                    açı = mouse_hareketi()
                    top_aktif = True
  
        if pygame.mouse.get_pressed()[0]:
            mousePos = pygame.mouse.get_pos()
            if mousePos[0] <= 800:
                top_aktif = False
                açı = anlık_açı = mouse_hareketi()
                periyot = sarkacın_periyodu(ipin_uzunluğu)
                geçen_zaman = 0.0

        if top_aktif:
            anlık_açı, açısal_hız = top_hareket_denklemi(
                ipin_uzunluğu, açı, geçen_zaman)
            t = clock.get_time()
            geçen_zaman = (geçen_zaman + t / 1000) % periyot

        top.centerx, top.centery = topun_konumu(anlık_açı, ipin_uzunluğu)

        ekran.fill((255, 255, 255))
        yay_çiz(ekran, açı, ipin_uzunluğu)
        çiz((top.centerx, top.centery), ip_genişliği)

        ip_uzunluğu_kaydıracı.çiz(ekran)
        yer_çekimi_kaydıracı.çiz(ekran)

        değerlere_ekrana_yaz(açı, anlık_açı, açısal_hız,
                               ipin_uzunluğu, geçen_zaman, periyot)
        pygame.display.update()

    pygame.quit()


main() 