
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
from sklearn.neighbors import NearestNeighbors




def graficakmeans():
    todos_los_datos = []
    datos_gestacion = []
    datos_fuma = []

    archivo = open(
        'C:/Users/maria/OneDrive/Escritorio/dataset/babies23.txt', 'r')

    for linea in archivo:
        linea1 = linea.split()
        todos_los_datos.append(linea1)

        dato_gestacion = linea1[4]
        dato_fuma = linea1[20]

        if( (dato_gestacion != "gestacion" and dato_fuma != "smoke") and (dato_gestacion != "999") and (dato_fuma!= "9")):
            dato_gestacion = int(linea1[4])
            dato_fuma = int(linea1[20])

            if dato_gestacion <=300:
                datos_gestacion.append(dato_gestacion)
                datos_fuma.append(dato_fuma)






    columna_gestacion = datos_gestacion  #Filtra por columna duracion gestacion
    columna_smoke = datos_fuma # Filtra por columna fumadora



    Data = {'gestacion' : columna_gestacion,
            'smoke' : columna_smoke}



    df = pd.DataFrame(Data, columns=['gestacion','smoke'])
    df = df.fillna(0)

    kmeans = KMeans(n_clusters=4).fit(df)
    centroids = kmeans.cluster_centers_


    # nuevoDato = np.array([[4400,25]])
    # prediccionNuevoDato = kmeans.predict(nuevoDato)

    plt.scatter(df['gestacion'], df['smoke'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    plt.show()

    # imagen = plt
    # rutaImagen = os.path.join(os.getcwd(), 'Universidad',  'prediccion')
    # imagen.savefig(rutaImagen)

def graficafiltrando():
    todos_los_datos = []
    datos_gestacion = []
    datos_fuma = []

    archivo = open(
        'C:/Users/maria/OneDrive/Escritorio/dataset/babies23.txt', 'r')
    contador_00 = 0
    contador_01 = 0
    contador_10 = 0
    contador_11 = 0

    var0 = 0
    var1 = 0
    var2 = 0
    var3=0

    for linea in archivo:
        linea1 = linea.split()
        todos_los_datos.append(linea1)

        dato_gestacion = linea1[4]
        dato_fuma = linea1[20]


        if( (dato_gestacion != "gestacion" and dato_fuma != "smoke") and (dato_gestacion != "999") and (dato_fuma!= "9")):
            dato_gestacion = int(linea1[4])
            dato_fuma = int(linea1[20])


            if dato_fuma ==0:
                var0 = var0+1
            elif dato_fuma ==1:
                var1=var1+1
            elif dato_fuma==2:
                var2=var2+1
            else:
                var3 = var3+1

            if dato_gestacion <=266 and dato_fuma !=0: # 11
                datos_gestacion.append(1)
                datos_fuma.append(1)
                contador_11 = contador_11 + 1
            elif dato_gestacion >266 and dato_fuma ==0: #00
                datos_gestacion.append(0)
                datos_fuma.append(0)
                contador_00 = contador_00 + 1
            elif dato_gestacion <=266 and dato_fuma==0: #01

                datos_gestacion.append(1)
                datos_fuma.append(0)
                contador_01 = contador_01 + 1
            else:

                datos_gestacion.append(0)
                datos_fuma.append(1)
                contador_10 = contador_10 + 1








    columna_gestacion = datos_gestacion  #Filtra por columna duracion gestacion
    columna_smoke = datos_fuma # Filtra por columna fumadora



    Data = {'gestacion' : columna_gestacion,
            'smoke' : columna_smoke}



    df = pd.DataFrame(Data, columns=['smoke','gestacion'])
    df = df.fillna(0)

    kmeans = KMeans(n_clusters=2).fit(df)
    centroids = kmeans.cluster_centers_


    nuevoDato = np.array([[1,0.5]])
    prediccionNuevoDato = kmeans.predict(nuevoDato)

    plt.scatter(df['smoke'], df['gestacion'], c=kmeans.labels_.astype(int), s=50, alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    plt.show()

    # imagen = plt
    # rutaImagen = os.path.join(os.getcwd(), 'Universidad',  'prediccion')
    # imagen.savefig(rutaImagen)

# graficakmeans()

graficafiltrando()



