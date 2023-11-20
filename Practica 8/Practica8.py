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

#Quinta función, esta es la encarga de hacer el algoritmo de k  means para el clustering
def k_means(points: List[np.array], k: int): #Se define nombre de la función, le paso los puntos en points y el numero de grupos que habra (que encontrara el clustering) en el parametro k
    dimension = len(points[0]) #Se obitene la dimension de los puntos
    num_puntos = len(points) #El numero de puntos (como tal el numero de datos)
    num_grupos = k #Numero de grupos, este como mencione es los grupos que quiero que el clustering encuentre
    iterations = 15 #Numero de iteraciones

    x = np.array(points) #Almaceno la lista de puntos en x
    y = np.random.randint(0, num_grupos, num_puntos) #Le asignamos un grupo aleatorio a cada punto

    mean = np.zeros((num_grupos, dimension)) #Donde se almacena los centro de masa de los grupo
    for t in range(iterations):  #Inicio iteracion en base a las iteraciones asignadas desde un inicio
        for k in range(num_grupos): #Para cada grupo k 
            mean[k] = np.mean(x[y == k], axis=0) #se calcula un nuevo centro de masa, en base a la media de los puntos
        for i in range(num_puntos): #Para cada punto que tengo
            dist = np.sum((mean - x[i]) ** 2, axis=1) #Le calculo la distancia cuadrada 
            pred = np.argmin(dist) #Grupo cuyo centro de masa esta mas cerca del punto
            y[i] = pred #Actualizacion de grupo 

    for kl in range(num_grupos): #Inicio de iteración en base de los grupos
        xp = x[y == kl, 0] #Almacenamiento de las coordenadas X de los puntos que pertenecen al grupo actual
        yp = x[y == kl, 1] #Almacenamiento de las coordenadas Y de los puntos que pertenecen al grupo actual
        plt.scatter(xp, yp) #Se crea el grafico de dispersion, le paso las variables que se acaban de inicializar

    plt.savefig("imagenes/kmeans.png") #Guardado del plot en la carpeta imagenes con el nombre kmeans
    plt.close() #Se cierra el plot
    return mean #Se regresa los grupos

# Función, esta función se encarga de generar la practica numero 8 correspondiente a mineria de datos
def GenerarPractica():
    DataFrame = pd.read_csv("csv/DataSet.csv") #Leo el dataset y le asigno a la variable DataFrame
    DataFrame['Grupo'] = DataFrame.apply(creacion_grupos,axis=1) #Llamo a los grupos para crear la nueva columna en donde se tendra grupo 1,2 o 3
    scatter_group_by("imagenes/groups.png", DataFrame, "Salary Range From", "Salary Range To", "Grupo") #Llamado a la función para el grafico de dispersion, le paso el 
    #Salario minimo y el maximo, que es el range from y el range to
    list_t = [(np.array(row[['Salary Range From', 'Salary Range To']]), row['Grupo']) for index, row in DataFrame.iterrows()]
    #Dado que en la función de k nearest neighbors no se usa dataframe como parametro, debo de convertir mi dataframe a points y labels
    points = [point for point, _ in list_t]
    kMeans = k_means(points, 3) #Llamado de k means para el clustering
    print(kMeans) #imprimo los grupos obtenidos por el clustering

#Genero la Practica, simple ejecución de función
GenerarPractica()