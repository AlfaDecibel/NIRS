import init
import random
import numpy as np

def finding():

    a=200 #сторона квадрата в центре
    height = 480 #габариты экрана
    width = 640
    x_0 = int(width)/2-int(a/2) #левый верхний угол центрального квадрата
    y_0 = int(height)/2-int(a/2)

    x_1 = int(width)/2+int(a/2) #правый нижний угол центрального квадрата
    y_1 = int(height)/2+int(a/2)

    res = (x_0,y_0,x_1,y_1) #упаковка результатов
    return res

def find_ver_pix(last_cords):
    verif_pixels = [[100,80],[200,80],[100,160],[200,160]]

    while(match_ver == 0):

        numb=numb-1
        if(numb==-1):
            numb=3
