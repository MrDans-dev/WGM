from PIL import Image
import numpy as np


def rysuj_ramke_kolor(w, h, dzielnik, r, g, b):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = [255, 0, 0]
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2, 0] = r
    tab[grub:z1, grub:z2, 1] = g
    tab[grub:z1, grub:z2, 2] = b
    return tab


Image.fromarray(rysuj_ramke_kolor(100, 60, 3, 100,200, 300)).show()