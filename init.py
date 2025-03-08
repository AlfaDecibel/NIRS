#chan must be initialize like "channel_X = [0 ,0 ,0]"" in main
#num- number of channel

import numpy as np
import cv2

def init_chan(num,width,height,met_of_split):

    #  metod 0
    #  00000001111111
    #  00000001111111
    #  00000001111111
    #  22222223333333
    #  22222223333333
    #  22222223333333

    if(met_of_split==0):
        height_ch=int((height/2)*2)
        width_ch=int(width/2)
        image = np.zeros((height_ch, width_ch, 3), dtype=np.uint8)
        for i in range(height_ch):
            for j in range(width_ch):
                image[i][j] = [i + j, i, j]  # Пример градиента (B, G, R)
        return image

    #  metod 1
    #  000001111122222
    #  000001111122222
    #  333334444455555
    #  333334444455555
    #  666667777788888
    #  666667777788888
