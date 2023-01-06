from PIL import Image
import numpy as np


def rysuj_ramke_kolor(w, h, dzielnik, kolor):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = [255, 0, 0]
    grub = int(min(w, h) / dzielnik)
    z1 = w - grub
    z2 = h - grub
    tab[grub:z1, grub:z2] = kolor
    return tab

kolor = 100, 200, 300
Image.fromarray(rysuj_ramke_kolor(100, 60, 3, kolor)).show()