
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os




def grafica():
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

grafica()


