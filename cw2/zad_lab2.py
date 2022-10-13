from PIL import Image
import numpy as np


def wstaw_obraz(obraz_wstawiany, w_m, h_m, wsp):
    h0, w0 = obraz_wstawiany.shape
    t = (int(wsp * h0), int(wsp * w0))
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h_m, h_m + h0):
        for j in range(w_m, w_m + w0):
            if i < (wsp * h0) and j < (wsp * w0):
                tab[i][j] = obraz_wstawiany[i - h_m][j - w_m]
    return Image.fromarray(tab.astype(bool))


def z3_1(w, h, dzielnik):
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


def z3_2(w, h, dzielnik):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.save("3_2.bmp")
    obraz.show()


def z3_3(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[n:h, m:w] = 0
    tab[0:n, 0:m] = 0
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.save("3_1.bmp")
    obraz.show()


def schody_do_nieba(w, h, dokładnosc):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for r in range(h):
        for c in range(r+1):
            tab[r][c] = c % dokładnosc != 0
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.save("schody_do_nieba.bmp")
    obraz.show()

inicjaly = Image.open("inicialy.bmp")
t_inicjaly = np.asarray(inicjaly)
ob1 = wstaw_obraz(t_inicjaly, 130, 75, 2)
ob2 = wstaw_obraz(t_inicjaly, 250, 250, 10)
ob3 = wstaw_obraz(t_inicjaly, 10, 10, 3)
ob1.save("ob1.bmp")
ob2.save("ob2.bmp")
ob3.save("ob3.bmp")
ob1.show()
ob2.show()
ob3.show()
tab = z3_1(480, 320, 16)
im_ramka = Image.fromarray(tab)
im_ramka.save("z3_1.bmp")
im_ramka.show()
z3_2(480, 320, 8)
z3_3(480, 320, 100, 50)
schody_do_nieba(480, 480, 50)


