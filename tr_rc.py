import init
import random
import numpy as np

def split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,main_ch):
    buf_main = init.init_chan(0,width,int(height)+1,0)

    height_ch = int(height/2)
    width_ch = int(width/2)

    # x_ver = random.randint(0,width_ch-3) #-3 for garanty location r g b pixels
    # y_ver = random.randint(0,height_ch)

    end_pixels = [[0,0,255],[0,255,0],[255,0,0],[0,255,0],[0,0,255]]

    x_ver = random.randint(0,255) #-3 for garanty location r g b pixels
    y_ver = random.randint(0,240)
    # x_ver = 0
    # y_ver = 0
    print("красный пиксель: x="+str(x_ver)+" y="+str(y_ver))
    for i in range(int(width)):
        for j in range(height):
            if(i<width_ch):
                if(j<height_ch):    #zero part
                    channel_0[j][i]=frame[j][i]
                    if(main_ch==0):
                        buf_main[j][i]=frame[j][i]
                else:                   #second part
                    channel_2[j-height_ch][i]=frame[j][i]
                    if(main_ch==2):
                        buf_main[j-height_ch][i]=frame[j][i]
            else:
                if(j<height_ch):    #first part
                    channel_1[j][i-width_ch]=frame[j][i]
                    if(main_ch==1):
                        buf_main[j][i-width_ch]=frame[j][i]
                else:                   #third part
                    channel_3[j-height_ch][i-width_ch]=frame[j][i]
                    if(main_ch==3):
                        buf_main[j-height_ch][i-width_ch]=frame[j][i]
    channel_0[y_ver][x_ver] = [0,0,255]
    channel_0[y_ver][x_ver+1] = [0,255,0]
    channel_0[y_ver][x_ver+2] = [255,0,0]

    channel_1[y_ver][x_ver] = [0,0,255]
    channel_1[y_ver][x_ver+1] = [0,255,0]
    channel_1[y_ver][x_ver+2] = [255,0,0]

    channel_2[y_ver][x_ver] = [0,0,255]
    channel_2[y_ver][x_ver+1] = [0,255,0]
    channel_2[y_ver][x_ver+2] = [255,0,0]

    channel_3[y_ver][x_ver] = [0,0,255]
    channel_3[y_ver][x_ver+1] = [0,255,0]
    channel_3[y_ver][x_ver+2] = [255,0,0]

    #channel_0=np.append(channel_0,end_pixels)
    # if(channel_0[y_ver][x_ver]==[255,0,0]):
    #     print("красный пиксель захвачен")
    # else:
    #     print("красный пиксель не захвачен")



    ret = (channel_0,channel_1,channel_2,channel_3)
    return ret

def noise_for_ch_0(channel,width,height):
    print("no noise")
    for i in range(int(width/2)):
        for j in range(int(height/2)):
            channel[j][i]=[0,0,255]
    return channel

def assemble_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,main_ch):
    for i in range(int(width)):
        for j in range(int(height)):
            if(i<(int(width/2))):
                if(j<int(height/2)):
                    frame[j][i]=channel_0[j][i]
                else:
                    frame[j][i]=channel_2[j-int(height/2)][i]
            else:
                if(j<int(height/2)):
                    frame[j][i]=channel_1[j][i-int(width/2)]
                else:
                    frame[j][i]=channel_3[j-int(height/2)][i-int(width/2)]
    return frame
