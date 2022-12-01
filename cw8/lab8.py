from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


def histogram_norm(im):
    pl = im.histogram()
    w, h = im.size
    N = w * h
    pl_norm = []
    for item in pl:
        pl_norm.append(item / N)
    return pl, pl_norm


def histogram_cumul(pl, pl_norm):
    pl_cumulative = [pl_norm[0]]
    for i in range(1, len(pl)):
        pl_cumulative.append(pl_cumulative[i - 1] + pl_norm[i])
    return pl_cumulative


def histogram_equalization(im):
    pl, pl_norm = histogram_norm(im)
    pl_cumulative = histogram_cumul(pl, pl_norm)
    im1 = im.point(lambda i: int(255 * pl_cumulative[i]))
    return im1


im = Image.open("rtg.jpg")
print(im.mode)
szary = im.convert("L")
statystyki(szary)

hist_norm = histogram_norm(im)[0]
plt.title("histogram_norm")
plt.bar(range(256), hist_norm[:256], color='r', alpha=0.5)
plt.bar(range(256), hist_norm[256:2 * 256], color='g', alpha=0.4)
plt.bar(range(256), hist_norm[2 * 256:], color='b', alpha=0.3)
plt.show()

hist_cumul = histogram_cumul(histogram_norm(im)[0], histogram_norm(im)[1])
plt.title("histogram_norm")
plt.bar(range(256), hist_cumul[:256], color='r', alpha=0.5)
plt.bar(range(256), hist_cumul[256:2 * 256], color='g', alpha=0.4)
plt.bar(range(256), hist_cumul[2 * 256:], color='b', alpha=0.3)
plt.show()

im_eq = histogram_equalization(im)
im_eq.save("equalized.jpg")
im_eq.show()

im_eq2 = ImageOps.equalize(im, mask=None)
im_eq2.show()


hist_eq = im_eq.histogram()
hist_eq2 = im_eq2.histogram()
plt.figure(figsize=(64, 32))
plt.subplot(1, 1, 1)
plt.imshow(im_eq)
plt.subplot(1, 1, 2)
plt.imshow(im_eq2)
plt.subplot(2, 2, 1)
plt.bar(range(256), hist_eq[:256], color='r', alpha=0.5)
plt.bar(range(256), hist_eq[256:2 * 256], color='g', alpha=0.4)
plt.bar(range(256), hist_eq[2 * 256:], color='b', alpha=0.3)
plt.subplot(2, 2, 2)
plt.bar(range(256), hist_eq2[:256], color='r', alpha=0.5)
plt.bar(range(256), hist_eq2[256:2 * 256], color='g', alpha=0.4)
plt.bar(range(256), hist_eq2[2 * 256:], color='b', alpha=0.3)
plt.show()






