from PIL import Image
import numpy as np

def pas(w, h):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(w/3)
    for k in range(3):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.save("3_2.bmp")
    obraz.show()

pas(300,500)