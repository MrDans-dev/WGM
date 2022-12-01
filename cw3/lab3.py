from PIL import Image  # Python Imaging Library
import numpy as np



def z3_12(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    for i in range(1, int((h / grub))):
        z1 = h - grub * i
        z2 = w - grub * i
        if i % 2 != 0:
            tab[grub * i:z1, grub * i:z2] = 1
        else:
            tab[grub * i:z1, grub * i:z2] = 0
    return tab * 255

ramka1 = Image.fromarray(z3_12(300,150,10))
ramka1.save("obraz1_1.jpg")
ramka1.save("obraz1_1.png")
ramka1.show()

def z3_1(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8) + 3
    grub = int(min(w, h) / dzielnik)
    for i in range(1, int((h / grub))):
        z1 = h - grub * i
        z2 = w - grub * i
        if i % 2 != 0:
            tab[grub * i:z1, grub * i:z2] = 2
        else:
            tab[grub * i:z1, grub * i:z2] = 3
    return tab * 200

ramka1 = Image.fromarray(z3_1(300,150,10))
ramka1.save("obraz1_1N.jpg")
ramka1.save("obraz1_1N.png")
ramka1.show()

#zad1 3.4
def wlasny2(w,h,dokładnosc):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for r in range(h):
        for c in range(r + 1):
            tab[r][c] = c % dokładnosc != 0
    tab = tab * 255
    return tab


wlasny1 = Image.fromarray(wlasny2(300,150,50))
wlasny1.save("obraz2.jpg")
wlasny1.save("obraz2.png")
wlasny1.show()

def wlasny(w,h,dokładnosc):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    tab += tab + 3
    for r in range(h):
        for c in range(r + 1):
            tab[r][c] = c % dokładnosc != 0
    tab = tab * 200
    return tab

wlasny1 = Image.fromarray(wlasny(300,150,50))
wlasny1.save("obraz2N.jpg")
wlasny1.save("obraz2N.png")
wlasny1.show()

def z3_2(w, h, dzielnik):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                if i % dzielnik == 0:
                    tab[j, i] = [200, 0, 0]
    tab = tab
    return tab

wlasny2 = Image.fromarray(z3_2(480, 320, 8))
wlasny2.show()

def koloruj_obraz(obraz, kolor):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t =(h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = kolor
            else:
                tab[i, j] = [255, 255, 255]
    return tab

gwiazdka = Image.open("inicialy.bmp")
obraz2 = Image.fromarray(koloruj_obraz(gwiazdka, [255, 0, 0]))
obraz2.save("obraz3.png")
obraz2.save("obraz3.jpg")
obraz2.show()