from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt # MODULO
import random
imagen = Image.open('medi.png')
imagen1 = Image.open('blank.jpg')
imagen2 = Image.open('med1.png')
a = np.array(imagen)
a1 = np.array(imagen2)
a3 = np.array(imagen1)
ay = len(a)
ax = len(a[0])
i = 0
i_1 = 0
i_2 = 0
l_random = [1,2,3]
def map_grafo():
    global i, i_1, i_2,ax,ay,a,a1,a3
    for y in range(ay):
        #f =l_random[random.randint(0,2)]
        f = 3
        i_1 = i_1 + 1
        if i_1%f == 0:
            f = 2
            for x in range(ax):
                i = i + 1

                
                if i%f == 0:
                    ab = (a[y][x][0] + a[y][x][1] + a[y][x][2])/255
                    if ab > 0.4:
                        a3[y][x][0] = 255
                        a3[y][x][1] = 0
                        a3[y][x][2] = 0
                        i_2 = i_2 + 1
                if i%f == 0:
                    ab = (a[y][x][0] + a[y][x][1] + a[y][x][2])/255
                    if ab < 0.3:
                        a3[y][x][2] = 255 
                        a3[y][x][0] = 0
                        a3[y][x][1] = 0
                if i%(f*10) == 0 and i_1%(f*10)==0:
                    ab = (a[y][x][0] + a[y][x][1] + a[y][x][2])/255
                    if ab > 0.4:
                        a3[y][x][1] = 255
                        a3[y][x][2] = 0
                        a3[y][x][0] = 0
        else:
            f = 3
    plt.imshow(a3)
    plt.show()
    a3 = Image.fromarray(a3.astype(np.uint8))
    a3.save('med1.png')
    print(i_2)
def test():
    global i, i_1, i_2,ax,ay,a
    i = 0
    for y in range(ay):
        for x in range(ax):
            ar = a1[y][x][0]
            ag = a1[y][x][1]
            ab = a1[y][x][2]
            if ar == 255 and ag == 255 and ab == 0:
                i = i + 1
    print(i) 
map_grafo()