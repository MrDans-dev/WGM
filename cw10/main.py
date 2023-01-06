from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageEnhance
from PIL import ImageStat as stat

im = Image.open("shrek.jpg")
w, h = im.size
s_w = 0.15
s_h = 0.27
resample_method =['NEAREST', 'LANCZOS', 'BILINEAR', 'BICUBIC', 'BOX', 'HAMMING']
im_N = im.resize((int(w*s_w), int(h*s_h)), 0)
plt.figure(figsize=(20, 16))
i=1
for t in range(6):
    file_name = "resample_"+ str(resample_method[t])
    im_r = im.resize((int(w*s_w), int(h*s_h)), t)
    print(file_name+str(im_r.size))
    plt.subplot(6, 2, i)
    plt.title(str(file_name))
    plt.imshow(im_r)
    plt.axis('off')
    i +=1
    diff=ImageChops.difference(im_N, im_r)
    s = stat.Stat(diff)
    plt.subplot(6, 2, i)
    plt.title('srednia' + str(np.round(s.mean, 2)))
    plt.imshow(diff)
    plt.axis('off')
    i +=1
plt.savefig("fig1.png")
plt.show()

im_rot_tab = []
im_title = ["a","b","c","d"]
im_rot_tab.append(im.rotate(60, expand=1, fillcolor=(255, 0, 0))) #1
im_rot_tab.append(im.rotate(60, expand=0, fillcolor=(255, 0, 0))) #2
im_rot_tab.append(im.rotate(300, expand=1, fillcolor=(0, 255, 0))) #3
im_rot_tab.append(im.rotate(300, expand=0, fillcolor=(0, 255, 0))) #4

for i in range(len(im_rot_tab)):
    plt.subplot(4, 1, i+1)
    plt.title(im_title[i])
    plt.imshow(im_rot_tab[i])
    plt.axis('off')
plt.savefig("fig4.png")
plt.show()

glowa = im.resize(size=im.size, box=(414, 61, 616, 292))
glowa = glowa.resize((glowa.size[0] * 2, glowa.size[1] * 3))
glowa.show()
glowa.save("glowa.jpg")

rozowy_45_not_center = im.rotate(45, fillcolor="pink")
rozowy_45_not_center.show()