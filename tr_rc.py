import init

def shift_xy(x,y,heigth,width):
    xy = [x,y]
    if(x<=width-1 and y<=heigth-1):
        if(x<width-2):
            xy[1]+=1
        else:
            xy[0]+=1
    return xy



def split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,main_ch):
    buf_main = init.init_chan(0,width,int(height/2)+1,0)
    # print("Ширина:"+str(int(width/2)))

    for i in range(int(width)):
        for j in range(int(height)):
            if(i<(int(width/2))):
                if(j<int(height/2)):
                    channel_0[j][i]=frame[j][i]
                    if(main_ch==0):
                        #print("Vivod:"+str(int(i)))
                        buf_main[j][i]=frame[j][i]
                else:
                    channel_2[j-int(height/2)][i]=frame[j][i]
                    if(main_ch==2):
                        buf_main[j-int(height/2)][i]=frame[j][i]
            else:
                if(j<int(height/2)):
                    channel_1[j][i-int(width/2)]=frame[j][i]
                    if(main_ch==1):
                        buf_main[j][i-int(width/2)]=frame[j][i]
                else:
                    channel_3[j-int(height/2)][i-int(width/2)]=frame[j][i]
                    if(main_ch==3):
                        buf_main[j-int(height/2)][i-int(width/2)]=frame[j][i]

    for i in range(int(height/2)):
        for j in range(int(width/2)):
            channel_0[i+int(height/2)][j] = buf_main[i][j]
            channel_1[i+int(height/2)][j] = buf_main[i][j]
            channel_2[i+int(height/2)][j] = buf_main[i][j]
            channel_3[i+int(height/2)][j] = buf_main[i][j]

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
                    if(main_ch==0):
                        frame[j][i]=channel_0[j+int(height/2)][i]
                        frame[j][i]=channel_1[j+int(height/2)][i]
                        frame[j][i]=channel_2[j+int(height/2)][i]
                        frame[j][i]=channel_3[j+int(height/2)][i]
                else:
                    frame[j][i]=channel_2[j-int(height/2)][i]
                    # if(main_ch==2):
                    #     frame[j][i]=channel_0[j][i+int(height/2)]
                    #     frame[j][i]=channel_1[j][i+int(height/2)]
                    #     frame[j][i]=channel_2[j][i+int(height/2)]
                    #     frame[j][i]=channel_3[j][i+int(height/2)]
            else:
                if(j<int(height/2)):
                    frame[j][i]=channel_1[j][i-int(width/2)]
                else:
                    frame[j][i]=channel_3[j-int(height/2)][i-int(width/2)]
    return frame
