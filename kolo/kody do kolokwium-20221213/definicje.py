#szary1
def szary1(w, h):
    t = (w, h)
    tab = np.zeros(t, dtype=np.uint8)
    kolor = 255 - int(w / 2) + 1
    for k in range(int(w / 2)):
        for i in range(k, w - k):
            for j in range(k, h - k):
                tab[i, j] = kolor
        kolor = kolor + 30
    return tab

#szary2
def szary2(w, h):
    t = (w, h)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            tab[i, j] = (i * j)
    return tab

#szary3
def szary3(w, h):
    t = (w, h)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            tab[i, j] = (i**2 * j)
    return tab

#szary4
def szary4(w, h):
    t = (w, h)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            tab[i, j] = (i**2 +  j )
    return tab

#szary5
def szary5(w, h):
    t = (w, h)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            tab[i, j] = (i**2 +  j**2 )
    return tab
