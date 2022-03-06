import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

##### Video
Nombre_carpeta = 'Imagenes'
Ubicacion_carpeta = 'C:/Users/PC/TrabajosPython' #Almacenado Data
Carpeta = Ubicacion_carpeta + '/' + Nombre_carpeta

if not os.path.exists(Carpeta):
	print('Carpeta creada: ',Carpeta)
	os.makedirs(Carpeta)


Nombre_carpeta1 = 'ImagenesProcesadas'
Ubicacion_carpeta1 = 'C:/Users/PC/TrabajosPython' #Almacenado Imagen Procesada
Carpeta1 = Ubicacion_carpeta1 + '/' + Nombre_carpeta1

if not os.path.exists(Carpeta1):
	print('Carpeta creada: ',Carpeta1)
	os.makedirs(Carpeta1)


cap = cv2.VideoCapture('prueba/0001-0250 (1).avi')
n_imagen= 0


total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) -1
lista= np.ones(total_frames)

while (cap.isOpened()):
    ret,frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret == False:
        break
    #cv2.imwrite(Carpeta +'frame' + str(n_imagen) + '.png', frame)
    cv2.imwrite(Carpeta + '/frame_{}.png'.format(n_imagen),frame)
    n_imagen = n_imagen +1


    ##### Pixeles
    n_blancos=0
    img=cv2.imread(Carpeta + '/frame_{}.png'.format(n_imagen),0)


    #print('frame_{}.png'.format(n_imagen))
    (x,y) = img.shape
    total_pixeles=img.size
    #print("altura: ", x)
    #print("base: ", y)

    for i in range(0,x):
        for j in range(0,y):
            if img.item(i,j)>=76:
                img.itemset((i,j),255)
                n_blancos=n_blancos+1
            else:
                img.itemset((i,j),0)
    cv2.imwrite(Carpeta1 + '/frameProcesado_{}.png'.format(n_imagen-1),img)

    #print("n_blancos: ",n_blancos)
    #print("Total de Pixeles", img.size)
    #print(img.dtype)
    Porcentaje_blancos=(n_blancos/total_pixeles) *100
    
    
    lista[n_imagen-1]=lista[n_imagen-1]*Porcentaje_blancos

    
      

    #print(lista)
    print(Porcentaje_blancos)
    #print("Porcentaje_blancos: {} %".format(Porcentaje_blancos))
    


    

    if n_imagen>=total_frames:
        break

print(lista)
plt.plot(lista)
plt.grid(True, linestyle=":")
plt.xlabel("Frames Number")
plt.ylabel("Brightness(%)")
plt.savefig("graficaFuncion.png", bbox_inches = "tight")
