from PIL import Image
import numpy as np


def rysuj_ramke_kolor(w, h, dzielnik, kolor):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = [255, 0, 0]
    grub = min(w, h) / dzielnik
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = kolor
    return tab

kolor = 100, 200, 300
Image.fromarray(rysuj_ramke_kolor(100, 60, 3, kolor)).show()