from PIL import Image  # Python Imaging Library
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
# ---------- wczytywanie obrazu zapisanego w różnych formatach .bmp, .jpg, .png oraz pobieranie informacji o obrazie  -------------------
obrazek = Image.open("inicialy.bmp")  # wczytywanie obrazu
obrazek.show()
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

# ---------- wczytywanie obrazu do tablicy oraz pobieranie informacji o tablicach ------------------------------
dane_obrazka = np.asarray(obrazek)
print("---------------- informqcje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)  # typ danych przechowywanych w tablicy
print("rozmiar tablicy:", dane_obrazka.shape)# rozmiar tablicy - warto porównac z rozmiarami obrazka
print("format obrazu", obrazek.format)
print("liczba elementow:", dane_obrazka.size)  # liczba elementów tablicy
print("wymiar tablicy:", dane_obrazka.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)  # pokazuje ile współrzednych trzeba do opisania wyrazu tablicy (piksela)
print("pierwszy wyraz:", dane_obrazka[0][0])
print("drugi wyraz:", dane_obrazka[1][0])
print("***************************************")
#print(dane_obrazka)  # mozna odkomentować, zeby zobaczyć tablicę
print("(50, 30): ", dane_obrazka[30][50])
print("(90, 40): ", dane_obrazka[40][90])
print("(99,0): ", dane_obrazka[0][99])
#np.savetxt("inicialy.txt", dane_obrazka, fmt='%.1d', delimiter=',')
txt = open('inicialy.txt', 'w')
for rows in dane_obrazka*1:
      for item in rows:
            txt.write(str(item) + ' ')
      txt.write('\n')
txt.close()
print("***************************************")

txt_bool = np.loadtxt("inicialy.txt", dtype=np.bool_)
print("typ txt:", txt_bool.dtype)
print("typ bmp:", dane_obrazka.dtype)
print("rozmiar txt:", txt_bool.shape)
print("rozmiar bmp:", dane_obrazka.shape)
print("liczba txt:", txt_bool.size)
print("liczba bmp:", dane_obrazka.size)
print("wymiar txt:", txt_bool.ndim)
print("wymiar bmp:", dane_obrazka.ndim)
print("rozmiar wyrazu txt:", txt_bool.itemsize)
print("rozmiar wyrazu bmp:", dane_obrazka.itemsize)
print((txt_bool == dane_obrazka).all())

print("***************************************")
txt_int = np.loadtxt("inicialy.txt", dtype=np.int_)
print("typ txt:", txt_int.dtype)
print("typ bmp:", dane_obrazka.dtype)
print("rozmiar txt:", txt_int.shape)
print("rozmiar bmp:", dane_obrazka.shape)
print("liczba txt:", txt_int.size)
print("liczba bmp:", dane_obrazka.size)
print("wymiar txt:", txt_int.ndim)
print("wymiar bmp:", dane_obrazka.ndim)
print("rozmiar wyrazu txt:", txt_int.itemsize)
print("rozmiar wyrazu bmp:", dane_obrazka.itemsize)
print((txt_int == dane_obrazka).all())
ob_d1 = Image.fromarray(txt_bool)
ob_d1.show()
