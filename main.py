import random
import init
import tr_rc
import numpy as np
print("Hello World")
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print("Высота:"+str(frame.shape[0]))
print("Ширина:" + str(frame.shape[1]))
print("Количество каналов:" + str(frame.shape[2]))

height = 480
width = 640

count_pixels_per_ch = (640*480*2)/9

channel_0=init.init_chan(0,width,height,0)
channel_1=init.init_chan(1,width,height,0)
channel_2=init.init_chan(2,width,height,0)
channel_3=init.init_chan(3,width,height,0)
print("Высота c0:"+str(channel_0.shape[0]))
print("Ширина c0:" + str(channel_0.shape[1]))

main_ch = 0

channels=tr_rc.split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,0)

channel_0=channels[0]
channel_1=channels[1]
channel_2=channels[2]
channel_3=channels[3]

# tr_rc.noise_for_ch_0(channel_0,width,height)

# tr_rc.assemble_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,0)
# print(frame)
while True:
    # Считываем изображение с камеры
    ret,frame = cap.read()
    cv2.imshow('transmitter', frame)

    # Отображаем изображение в окне
    #tr_rc.split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,0)
    channels=tr_rc.split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,0)

    channel_0=channels[0]
    channel_1=channels[1]
    channel_2=channels[2]
    channel_3=channels[3]
    # channel_0=tr_rc.noise_for_ch_0(channel_0,width,height)
    # channel_1=tr_rc.noise_for_ch_0(channel_1,width,height)
    channel_2=tr_rc.noise_for_ch_0(channel_0,width,height)
    channel_2=tr_rc.noise_for_ch_0(channel_1,width,height)
    channel_2=tr_rc.noise_for_ch_0(channel_2,width,height)

    frame=tr_rc.assemble_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,0)
    cv2.imshow('channel_0', channel_0)
    cv2.imshow('channel_1', channel_1)
    cv2.imshow('channel_2', channel_2)
    cv2.imshow('channel_3', channel_3)

    cv2.imshow('Reciever', frame)
    # Закрыть окно можно на клавишу 'Esc'
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
