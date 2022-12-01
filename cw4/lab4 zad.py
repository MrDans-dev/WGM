from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

im1 = Image.open("obraz.jpg")
T = np.array(im1)
t_r = T[:, :, 0]
im_r = Image.fromarray(t_r)
im_r.save("im_r.jpg")
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g)
im_g.save("im_g.jpg")
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b)
im_b.save("im_b.jpg")


im2 = Image.merge('RGB', (im_r, im_g, im_b))
t2 = np.array(im2)
print(T.all() == t2.all())
im2.save("obraz2.jpg")
diff = ImageChops.difference(im1, im2)



r, g, b = im1.split()
im3 = Image.merge("RGB", (b, g, r))
im3.save("im3.png")
im3.save("im3.jpg")
diff = ImageChops.difference(im1, im3)
#diff.show()

plt.figure(figsize=(32, 16))
plt.subplot(3,4,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(Image.open("lab3 img/obraz1_1.jpg"))
plt.axis('off')
plt.subplot(3,4,2)
plt.imshow(Image.open("lab3 img/obraz1_1N.jpg"), "gray")
plt.axis('off')
plt.subplot(3,4,3)
plt.imshow(Image.open("lab3 img/obraz1_1.png"), "gray")
plt.axis('off')
plt.subplot(3,4,4)
plt.imshow(Image.open("lab3 img/obraz1_1N.png"), "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
#plt.show()


def wlasny(w,h,dokładnosc):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    tab += tab + 3
    for r in range(h):
        for c in range(r + 1):
            tab[r][c] = c % dokładnosc != 0
    tab = tab * 200
    return tab

T_im = Image.fromarray(wlasny(700,525,50))
im4 = Image.open('obraz.jpg')
r, g, b = im4.split()
im4_1 = Image.merge('RGB', (T_im, g, b))
im4_2 = Image.merge('RGB', (r, T_im, b))
im4_3 = Image.merge('RGB', (r, g, T_im))

plt.figure(figsize=(32, 16))
plt.subplot(1, 3, 1)
plt.imshow(im4_1)
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(im4_2)
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(im4_3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')
#plt.show()


def obraz(x, y):
    tab = np.zeros((300, 300), dtype=np.uint8)
    #tab += tab + 3
    for r in range(x):
        for c in range(y):
            tab[r][c] = c
    img = Image.fromarray(tab)
    return img


img1 = obraz(200, 200)
img2 = obraz(300, 175)
img3 = obraz(175, 300)


image1 = Image.merge('RGB', (img1, img2, img3))
image2 = Image.merge('RGB', (img1, img3, img2))
image3 = Image.merge('RGB', (img2, img1, img3))
image4 = Image.merge('RGB', (img2, img3, img1))
image5 = Image.merge('RGB', (img3, img1, img2))
image6 = Image.merge('RGB', (img3, img2, img1))
plt.figure(figsize=(32, 16))
plt.subplot(3, 2, 1)
plt.imshow(image1)
plt.axis('off')
plt.subplot(3, 2, 2)
plt.imshow(image2)
plt.axis('off')
plt.subplot(3, 2, 3)
plt.imshow(image3)
plt.axis('off')
plt.subplot(3, 2, 4)
plt.imshow(image4)
plt.axis('off')
plt.subplot(3, 2, 5)
plt.imshow(image5)
plt.axis('off')
plt.subplot(3, 2, 6)
plt.imshow(image6)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')
plt.show()

