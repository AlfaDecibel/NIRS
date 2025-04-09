import init
import random
import numpy as np
import polygon

def split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,main_ch):
    buf_main = init.init_chan(0,width,int(height)+1,0)
    cords = polygon.finding() #получаем координаты центральной области
    height_ch = int(height/2)
    width_ch = int(width/2)

    verif_pixels = [[100,80],[200,80],[100,160],[200,160]]

    x_ver = random.randint(0,255) #-3 for garanty location r g b pixels
    y_ver = random.randint(0,240) #verification pixels
    # x_ver = 0
    # y_ver = 0
    j_2 = 0
    i_2 = height_ch
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
            if((x>cords[0] and x<cords[2]) and (y>cords[1] and y<cords[3])): #если пиксель попадает в центральный квадрат
                if(j_2==320): #если строчка кончилась
                    i_2=i_2+1 #переходим на строчку ниже
                    j_2=0 #обнуляем счётчик столбцов
                channel_0[j_2][i_2] = frame[y][x] #резервируем пиксель в канале 0
                channel_1[j_2][i_2] = frame[y][x] #резервируем пиксель в канале 1
                channel_2[j_2][i_2] = frame[y][x] #резервируем пиксель в канале 2
                channel_3[j_2][i_2] = frame[y][x] #резервируем пиксель в канале 3
                j_2=j_2+1 #движемся дальше

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
    ret = (channel_0,channel_1,channel_2,channel_3,[x_ver,y_ver],cords)
    return ret

def noise_for_ch_0(channels,width,height,num):
    print("Noise in "+str(num)+"channel!")
    for x in range(int(width/2)):
        for y in range(int(height/2)):
            channels[num][x][y]=[0,0,255]
    return channels

def assemble_pic_0(frame,width,height,channels,main_ch,cords,priority):
    #There is check channels for noise
    x_ver=cords[0]
    y_ver=cords[1]
    ideal=[0,0,255,0,255,0,255,0,0]
    delta=0
    counter = 0
    not_noise=-1 #номер незашумлённого канала
    height_ch = int(height/2)
    width_ch = int(width/2)
    verif_zones = [0,0,0,0]
    for index in range(0,4):
        for zone in range(0,4):
            for pix_of_ver in range(0,3):
                for rgb in range(0,3):
                    if(channels[zone][x_ver+pix_of_ver][y_ver][rgb]>=ideal[pix_of_ver*3+rgb]-delta):
                        if(channels[zone][x_ver+pix_of_ver][y_ver][rgb]<=ideal[pix_of_ver*3+rgb]+delta):
                            counter+=1
            if(counter==9):
                print("In channel "+str(zone)+" NO noise")
                verif_zones[zone]=1 #номер незашумлённого канала
                not_noise=zone
                counter=0
                continue
            else:
                print("In channel "+str(zone)+" IS noise")
            counter=0
    print(verif_zones)
    j_2 = 0
    i_2 = height_ch
    verif =0
    for x in range(int(width)):
        for y in range(int(height)):
            if(x<(int(width/2))):
                if((y<int(height/2) and verif_zones[0]==1)):
                    frame[y][x]=channels[0][x][y]
                else:
                    if(y>int(height/2) and verif_zones[2]==1):
                    # frame[y][x]=channels[2][x][y-int(height/2)]
                        frame[y][x]=channels[2][x][y-int(height/2)]
            else:
                if(y<int(height/2) and verif_zones[1]):
                    # frame[y][x]=channels[1][x-int(width/2)][y]
                    frame[y][x]=channels[1][x-int(width/2)][y]
                else:
                    # frame[y][x]=channels[3][x-int(width/2)][y-int(height/2)]
                    # frame[y][x]=channels[3][x-int(width/2)][y-int(height/2)]
                    if(y>int(height/2) and verif_zones[3]):
                        frame[y][x]=channels[3][x-int(width/2)][y-int(height/2)]
            if((x>priority[0] and x<priority[2]) and (y>priority[1] and y<priority[3]) and not_noise!=-1): #если пиксель попадает в центральный квадрат
                if(j_2==320): #если строчка кончилась
                    i_2=i_2+1 #переходим на строчку ниже
                    j_2=0 #обнуляем счётчик столбцов
                frame[y][x]=channels[not_noise][j_2][i_2] #выводим пиксель из резерва
                j_2=j_2+1 #движемся дальше
    return frame
