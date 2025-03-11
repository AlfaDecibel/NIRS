import random
import init
import tr_rc
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print("Высота:"+str(frame.shape[0]))
print("Ширина:" + str(frame.shape[1]))
print("Количество каналов:" + str(frame.shape[2]))

height = 480
width = 640

# Инициализация каналов
# Initialization of channels
channel_0=init.init_chan(0,width,height,0)
channel_1=init.init_chan(1,width,height,0)
channel_2=init.init_chan(2,width,height,0)
channel_3=init.init_chan(3,width,height,0)

channels=tr_rc.split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,0)

channel_0=channels[0]
channel_1=channels[1]
channel_2=channels[2]
channel_3=channels[3]

cords=[0,0]

while True:
    # Считываем изображение с камеры
    ret,frame = cap.read()
    cv2.imshow('transmitter', frame)

    channels=tr_rc.split_pic_0(frame,width,height,channel_0,channel_1,channel_2,channel_3,0)

    cords=channels[4]

    frame=tr_rc.assemble_pic_0(frame,width,height,channels,0,cords)
    cv2.imshow('channel_0', channels[0])
    cv2.imshow('channel_1', channels[1])
    cv2.imshow('channel_2', channels[2])
    cv2.imshow('channel_3', channels[3])

    cv2.imshow('Reciever', frame)
    # Закрыть окно можно на клавишу 'Esc'
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
