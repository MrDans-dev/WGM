from PIL import Image
import numpy as np


def rysuj_ramke_kolor(w, h, dzielnik, r, g, b):
    tab = np.ones((h, w, 3), dtype=np.uint8)
    tab[:] = 150
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = (r, g, b)
    return tab


Image.fromarray(rysuj_ramke_kolor(100, 60, 3, 100, 200, 300)).show()