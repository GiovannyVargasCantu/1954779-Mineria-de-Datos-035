#Alumno:Miguel Giovanny Vargas Cantú
#Matricula: 1954779
#Escuela: FCFM UANL
#Materia: Minería de Datos 035 Jueves de 7:00pm a 10:00pm
#Docente: Jose Anastacio Hernandez Saldaña


#Iniciamos importando pandas, para ello se necesita hacer un pip install pandas, teniendo pandas es la forma en la que podemos manipular los dataframes, existe
#tambien la libreria de CSV pero en este clase veremos al respecto sobre pandas
import pandas as pd

#Tambien es necesario importar matplotlib.pyplot para las graficas, en este caso solo con el comando pip install matplotlib 
import matplotlib.pyplot as plt

# Para ello se hace un pip install numpy aunque al menos conmigo, al instalar Python, Numpy ya venia instalado
#Pero eso depende de la versión de cada quien, por lo que especifico que de no tener instalado numpy, hay que hacer el pip install numpy
import numpy as np
#Es necesario implementar las listas de typing
from typing import List


#Primera función, esta función se encarga de crear grupos, donde cada grupo significa algo con respecto al salario minimo y el maximo
def creacion_grupos(col): #Defino el nombre de función y el parametro, este caso es col, que seria pues la columna que se va checando, que luego le hare un apply
    #Y regresara un grupo en cada if o else
    if abs(col['Salary Range From'] - col['Salary Range To']) <= 10000: #Veo la diferencia absoluta, y si es menor de 10k lo considero grupo 1
        return 'Grupo 1' #Diferencia minima
    elif 10000 < abs(col['Salary Range From'] - col['Salary Range To']) <=25000: #Veo la diferencia absoluta si esta entre 10k y 25k lo considero grupo 2
        return 'Grupo 2' #Diferencia normal
    else: #Si no es ni grupo 1 ni 2, significa que hay mucha diferencia de salario, es decir mayor de 25k
        return 'Grupo 3' # Hay mucha diferencia de salario 

#Segunda función, esta función se encarga de dar la distancia euclidiana
def euclidean_distance(a: np.array, b: np.array): #Defino nombre de la función y los parametros, que en este caso seran dos np.array
    return np.sqrt(np.sum((b - a) ** 2)) #Regresa la distancia euclidiana

#Tercera función, para proporcionar un conjunto de colores predefinidos en un colormap, basicamente es para asignar colores a los grupos
def get_cmap(n, name="hsv"): #Defino el nombre de la función y los parametros, que paso el numero y el nombre del colormap, que en este caso viene hsv (Hue-Saturation-Value)
    return plt.cm.get_cmap(name, n) #Regresa un colormap con el numero de colores especificados

#Cuarta función, es la encargada de generar el grafico de scatter, el grafico de dispersion basicamente donde cada grupo tiene un color distinto.
def scatter_group_by(file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str): #Define nombre de la función y los parametros, el primer parametro seria
    #El lugar donde se guardara y el nombre el archivo, luego el dataframe, y sus respectivas columnas, asi como la columna de etiqueta
    fig, ax = plt.subplots() #Se crea una figura y un objeto de exes
    labels = pd.unique(df[label_column]) #Saca las etiquetas unicas en las columnas etiquetadas.
    cmap = get_cmap(len(labels) + 1) #Se hace uso de la función de get_cmap para obtener un mapa de colores y lo almaceno en la variable cmap
    for i, label in enumerate(labels): #Itero sobre las etiquetas unicas
        filter_df = df.query(f"{label_column} == '{label}'") #Filtrado de filas donde la columna de etiquetas es igual que la del bucle
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i)) #El agregado de puntos dispersos utilizando las coordenadas de X e Y del dataframe filtrado
        #Y se le asigna una etiqueta que corresponde a la etiqueta que es del grupo actual.
    ax.legend() #Se agrega una leyenda para mostrar la etiqueta de los grupos, es decir donde saldra grupo 1, grupo 2 y su respectivo color
    plt.savefig(file_path) #Guarda el plot
    plt.close() #Cierra el plot

#Quinta función, esta es la encarga de hacer el algoritmo de k vecinos mas cercanos
def k_nearest_neightbors(points: List[np.array], labels: np.array, input_data: List[np.array], k: int): #Defino el nombre de la función y los parametros que se le pasan
    #En este caso es points que es una lista de arrays de numpy, labels que es np.array, input data que es una lista de np.array  y k, que k representa los numeros de vecinos
    #mas cercanos a considerar al momento de hacer la predicción
    input_distances = [ #Se calcula las distancias euclidianas aqui, almacena estas distancias basicamente input_distances
        [euclidean_distance(input_point, point) for point in points] #Calculo de distancias
        for input_point in input_data
    ]
    points_k_nearest = [ #Se saca los indices de los k puntos mas cercanos para cada punto en "input_data" con np.argsort
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    
    def calculate_mode(indices): #Se calcula la moda en este caso con np.unique, dado que no me funciono el mode
        unique_labels, counts = np.unique([labels[index] for index in indices], return_counts=True)
        return unique_labels[np.argmax(counts)]
    
    return [calculate_mode(point_nearest) for point_nearest in points_k_nearest] #Se itera sobre la lista de points_k_nearest, y al final regresara una lista que contiene las etiquetas
    #para cada punto en input_data

# Función, esta función se encarga de generar la practica numero 7 correspondiente a mineria de datos
def GenerarPractica():
    DataFrame = pd.read_csv("csv/DataSet.csv") #Leo el dataset y le asigno a la variable DataFrame
    DataFrame['Grupo'] = DataFrame.apply(creacion_grupos,axis=1) #Llamo a los grupos para crear la nueva columna en donde se tendra grupo 1,2 o 3
    scatter_group_by("imagenes/groups.png", DataFrame, "Salary Range From", "Salary Range To", "Grupo") #Llamado a la función para el grafico de dispersion, le paso el 
    #Salario minimo y el maximo, que es el range from y el range to
    list_t = [(np.array(row[['Salary Range From', 'Salary Range To']]), row['Grupo']) for index, row in DataFrame.iterrows()]
    #Dado que en la función de k nearest neighbors no se usa dataframe como parametro, debo de convertir mi dataframe a points y labels
    points = [point for point, _ in list_t]
    labels = [label for _, label in list_t]
    kn = k_nearest_neightbors(points,labels, [np.array([1, 60000]), np.array([40000, 60000]), np.array([1, 250000]), np.array([80000, 40000])],5,) #Llamado de la función de k vecinos mas cercanos
    print(kn) #imprimo los vecinos mas cercanos

#Genero la Practica, simple ejecución de función
GenerarPractica()