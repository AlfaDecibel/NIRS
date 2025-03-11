import init
import random
import numpy as np


def split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,main_ch):
    buf_main = init.init_chan(0,width,int(height)+1,0)

    height_ch = int(height/2)
    width_ch = int(width/2)

    end_pixels = [[0,0,255],[0,255,0],[255,0,0],[0,255,0],[0,0,255]]

    x_ver = random.randint(0,255) #-3 for garanty location r g b pixels
    y_ver = random.randint(0,240)
    # x_ver = 0
    # y_ver = 0
    print("красный пиксель: x="+str(x_ver)+" y="+str(y_ver))
    for x in range(int(width)):
        for y in range(int(height)):
            if(x<width_ch):
                if(y<height_ch):    #zero part
                    channel_0[x][y]=frame[y][x]
                else:                   #second part
                    channel_2[x][y-height_ch]=frame[y][x]
            else:
                if(y<height_ch):    #first part
                    channel_1[x-width_ch][y]=frame[y][x]
                else:                   #third part
                    channel_3[x-width_ch][y-height_ch]=frame[y][x]
    # gp = [0,0,255,0,255,0,255,0,0]
    # for i in range(0,3):



    channel_0[x_ver][y_ver] = [0,0,255]
    channel_0[x_ver+1][y_ver] = [0,255,0]
    channel_0[x_ver+2][y_ver] = [255,0,0]

    channel_1[x_ver][y_ver] = [0,0,255]
    channel_1[x_ver+1][y_ver] = [0,255,0]
    channel_1[x_ver+2][y_ver] = [255,0,0]

    channel_2[x_ver][y_ver] = [0,0,255]
    channel_2[x_ver+1][y_ver] = [0,255,0]
    channel_2[x_ver+2][y_ver] = [255,0,0]

    channel_3[x_ver][y_ver] = [0,0,255]
    channel_3[x_ver+1][y_ver] = [0,255,0]
    channel_3[x_ver+2][y_ver] = [255,0,0]
    ret = (channel_0,channel_1,channel_2,channel_3,[x_ver,y_ver])
    return ret

def noise_for_ch_0(channels,width,height,num):
    print("Noise in "+str(num)+"channel!")
    for x in range(int(width/2)):
        for y in range(int(height/2)):
            channels[num][x][y]=[0,0,255]
    return channels

def assemble_pic_0(frame,width,height,channels,main_ch,cords):
    #There is check channels for noise
    x_ver=cords[0]
    y_ver=cords[1]
    ideal=[0,0,255,0,255,0,255,0,0]
    delta=0
    counter = 0
    for z in range(0,4):
        for i in range(0,3):
            for j in range(0,3):
                if(channels[z][x_ver+i][y_ver][j]>=ideal[i*3+j]-delta and channels[z][x_ver+i][y_ver][j]<=ideal[i*3+j]+delta):
                    counter+=1
        if(counter==9):
            print("In channel "+str(z)+" NO noise")
            # print("   No noise in channel "+str(z))
        else:
            print("In channel "+str(z)+" IS noise")
        counter=0

    for x in range(int(width)):
        for y in range(int(height)):
            if(x<(int(width/2))):
                if(y<int(height/2)):
                    # frame[y][x]=channels[0][x][y]
                    frame[y][x]=channels[0][x][y]
                else:
                    # frame[y][x]=channels[2][x][y-int(height/2)]
                    frame[y][x]=channels[2][x][y-int(height/2)]
            else:
                if(y<int(height/2)):
                    # frame[y][x]=channels[1][x-int(width/2)][y]
                    frame[y][x]=channels[1][x-int(width/2)][y]
                else:
                    # frame[y][x]=channels[3][x-int(width/2)][y-int(height/2)]
                    # frame[y][x]=channels[3][x-int(width/2)][y-int(height/2)]
                    frame[y][x]=channels[3][x-int(width/2)][y-int(height/2)]
    return frame
