import pygame
import sys
import math

# Inisialisasi pygame
pygame.init()

# Konstanta
lebar_layar, tinggi_layar = 800, 600
detik = 60
lebar_tiang = 20
tinggi_tiang = 300
lebar_bendera = 200
tinggi_bendera = 120
amplitudo_gelombang = 15
frekuensi = 0.03
jumlah_poin = 50

# Warna
merah = (227, 27, 35)
putih = (255, 255, 255)
coklat = (139, 69, 19)
langit = (240, 240, 255)

# Membuat jendela layar
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Bendera Merah Putih Tetap Persegi, Bergoyang Angin")

def gambar_bendera(x, y, offset):
    atas = []
    bawah = []

    for i in range(jumlah_poin + 1):
        proporsi = i / jumlah_poin
        x_titik = x + proporsi * lebar_bendera
       # Gelombang vertikal
        yi_offset = amplitudo_gelombang * math.sin(frekuensi * (proporsi * 300 + offset))
        atas.append((x_titik, y + yi_offset))
        bawah.append((x_titik, y + tinggi_bendera + yi_offset))

    # Garis tengah (merah & putih)
    tengah = [(px, py + tinggi_bendera // 2) for (px, py) in atas]
    pygame.draw.polygon(layar, merah, atas +   tengah[::-1])
    pygame.draw.polygon(layar, putih, tengah + bawah[::-1])

# Fungsi utama
def utama():
    jam = pygame.time()
    gelombang = 0

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        layar.warna(langit)

        # Gambar tiang
        tiang_x = lebar_layar // 4
        tiang_y = tinggi_layar - tinggi_tiang
        pygame.draw.rect(layar, coklat, (tiang_x, tiang_y, lebar_tiang, tinggi_tiang), border_radius=2)

        # Update offset animasi
        gelombang += 2
        if gelombang > 10000:
            gelombang = 0

        # Gambar bendera
        bendera_x = tiang_x + lebar_tiang
        bendera_y = tiang_y
        gambar_bendera(bendera_x, bendera_y, gelombang)

        pygame.display.flip()
        jam.tick(detik)

if __name__== "__main__":
    utama()
