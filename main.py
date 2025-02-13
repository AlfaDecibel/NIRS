import random

print("Hello World")
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print("Высота:"+str(frame.shape[0]))
print("Ширина:" + str(frame.shape[1]))
print("Количество каналов:" + str(frame.shape[2]))

channel_1=frame
channel_2=frame
channel_3=frame
channel_4=frame
channel_5=frame
channel_6=frame
channel_7=frame
channel_8=frame
channel_9=frame

def transmit(frame):
    for i in range(0,480):
        if i<=160:
            for j in range(0,640):
                if j<=210:
                    #frame[i,j][0]=0     #zone 1
                    channel_1[i,j]=frame[i,j]
                if j>210 and j<430:
                    #frame[i,j][1]=127   #zone 2
                    channel_2[i,j]=frame[i,j]
                if j>=430:
                    #frame[i,j][2]=255   #zone 3
                    channel_3[i,j]=frame[i,j]
        if i>160 and i<320:
            for j in range(0,640):
                if j<=210:
                    #frame[i,j][0]=255     #zone 4
                    channel_4[i,j]=frame[i,j]
                if j>210 and j<430:
                    #frame[i,j][1]=0   #zone 5
                    channel_5[i,j]=frame[i,j]
                if j>=430:
                    #frame[i,j][2]=127   #zone 6
                    channel_6[i,j]=frame[i,j]
        if i>=320:
            for j in range(0,640):
                if j<=210:
                    #frame[i,j][0]=127     #zone 7
                    channel_7[i,j]=frame[i,j]
                if j>210 and j<430:
                    #frame[i,j][1]=255   #zone 8
                    channel_8[i,j]=frame[i,j]
                if j>=430:
                    #frame[i,j][2]=0   #zone 9
                    channel_9[i,j]=frame[i,j]

def efir(koefficent):
    for i in range(0,480):
        if i<=160:
            for j in range(0,640):
                if j<=210:
                    channel_1[i,j][0]+=koefficent*random.randint(0,100)
                    channel_1[i,j][1]+=koefficent*random.randint(0,100)
                    channel_1[i,j][2]+=koefficent*random.randint(0,100)
                if j>210 and j<430:
                    channel_2[i,j][1]+=koefficent*random.randint(0,100)
                if j>=430:
                    channel_3[i,j][2]+=koefficent*random.randint(0,100)
        if i>160 and i<320:
            for j in range(0,640):
                if j<=210:
                    channel_4[i,j][0]+=koefficent*random.randint(0,100)
                if j>210 and j<430:
                    channel_5[i,j][0]+=koefficent*random.randint(0,100)
                if j>=430:
                    channel_6[i,j][0]+=koefficent*random.randint(0,100)
        if i>=320:
            for j in range(0,640):
                if j<=210:
                    channel_7[i,j][0]+=koefficent*random.randint(0,100)
                if j>210 and j<430:
                    channel_8[i,j][0]+=koefficent*random.randint(0,100)
                if j>=430:
                    channel_9[i,j][0]+=koefficent*random.randint(0,100)

def recieve(frame):
    for i in range(0,480):
        if i<=160:
            for j in range(0,640):
                if j<=210:
                    frame[i,j]=channel_1[i,j]
                if j>210 and j<430:
                    frame[i,j]=channel_2[i,j]
                if j>=430:
                    frame[i,j]=channel_3[i,j]
        if i>160 and i<320:
            for j in range(0,640):
                if j<=210:
                    frame[i,j]=channel_4[i,j]
                if j>210 and j<430:
                    frame[i,j]=channel_5[i,j]
                if j>=430:
                    frame[i,j]=channel_6[i,j]
        if i>=320:
            for j in range(0,640):
                if j<=210:
                    frame[i,j]=channel_7[i,j]
                if j>210 and j<430:
                    frame[i,j]=channel_8[i,j]
                if j>=430:
                    frame[i,j]=channel_9[i,j]

while True:
    # Считываем изображение с камеры
    ret,frame = cap.read()
    cv2.imshow('transmitter', frame)
    transmit(frame)
    efir(0.5)
    recieve(frame)
    # Отображаем изображение в окне


    cv2.imshow('Reciever', frame)
    # Закрыть окно можно на клавишу 'Esc'
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
