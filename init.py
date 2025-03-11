#chan must be initialize like "channel_X = [0 ,0 ,0]"" in main
#num- number of channel

import numpy as np
import cv2

def init_chan(num,width,height,met_of_split): #new channel generate

    #  metod 0
    #  00000001111111
    #  00000001111111
    #  00000001111111
    #  22222223333333
    #  22222223333333
    #  22222223333333

    if(met_of_split==0):    #if method of splitting is 0 (for 4 polygons)
        height_ch=int((height/2)) #calculation of image height
        width_ch=int(width/2) #calculation of image width
        image = np.zeros(( width_ch,height_ch, 3), dtype=np.uint8) #filling image zeros
        for i in range(width_ch):
            for j in range(height_ch):
                image[i][j] = [i + j, i, j]  #filling image gradient
        return image
