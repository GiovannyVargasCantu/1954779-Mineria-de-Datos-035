#Alumno:Miguel Giovanny Vargas Cantú
#Matricula: 1954779
#Escuela: FCFM UANL
#Materia: Minería de Datos 035 Jueves de 7:00pm a 10:00pm
#Docente: Jose Anastacio Hernandez Saldaña


#Iniciamos importando pandas, para ello se necesita hacer un pip install pandas, teniendo pandas es la forma en la que podemos manipular los dataframes, existe
#tambien la libreria de CSV pero en este clase veremos al respecto sobre pandas
import pandas as pd

#Importamos matplotlib.pyplot para las graficas
import matplotlib.pyplot as plt

#Esto es para la regresion lineal
import statsmodels.api as sm

#Se usa para ver si un dato es numerico
import numbers

#Para obtener tablas de resumen de modelos
from statsmodels.stats.outliers_influence import summary_table

#Para los tipos de Tupla y Diccionario
from typing import Tuple, Dict

# Para ello se hace un pip install numpy aunque al menos conmigo, al instalar Python, Numpy ya venia instalado
#Pero eso depende de la versión de cada quien, por lo que especifico que de no tener instalado numpy, hay que hacer el pip install numpy
import numpy as np

#Primera función, esta función se encarga de transformar las variables, en mi caso manejo fechas, entonces volvera las fechas en una serie numerica como tal
def transform_variable(df: pd.DataFrame, x:str)->pd.Series: #Se define el nombre de la función, y el parametro qeu recibe, en este caso el dataframe y la variable, y regresa una serie de pandas
    if isinstance(df[x][df.index[0]], numbers.Number): #Se verifica si el primer valor es un numero
        return df[x] #Asume que toda la columna es numerica y regresa la columna como una serie
    else: #En caso de que no sea numerico
        return pd.Series([i for i in range(0, len(df[x]))]) #Se crea una serie numerica
    
#Segunda función, esta funcióno es la encargada de tener los trabajados publicados en cada dia donde se ve el año y mes
def create_serie_tiempo(df:pd.DataFrame): #Se define el nombre de la función, y el parametro que recibe, en este caso el dataframe
    df['Posting Date'] = pd.to_datetime(df['Posting Date']) #Conversión formato de fecha
    df['Year'] = df['Posting Date'].dt.year  #Columna de año
    df['Month'] = df['Posting Date'].dt.month #Columna de mes
    df['Day'] = df['Posting Date'].dt.day #Columa de día 
    df['Combined Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']]) #Se combinan las fechas para que salga todo junto, es decir año, mes y dia
    jobs_per_day = df.groupby('Combined Date').size().reset_index(name='Jobs Posted') #Agrupamiento por año,mes y dia de los trabajos publicados
    return jobs_per_day #Regresa el dataframe que contiene el mes, dia y los trabajos publicados

#Tercera función, esta función se encarga de hacer la regresión lineal correspondiente
def linear_regression(df: pd.DataFrame, x:str, y: str)->Dict[str, float]: #Se define el nombre de la función, asi como los parametros que se le pasan, que es el dataframe
    #la columna independiente y la dependiente, y regresa un diccionario con su string y float
    fixed_x = transform_variable(df, x) #Se transforma la variable independiente
    model= sm.OLS(list(df[y]),sm.add_constant(fixed_x)).fit() #Se crea el modelo de regresión lineal
    bands = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0] #Se extraen las bandas de confianza del modelo
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef'] #Se extrae los coeficientes del modelo
    r_2_t = pd.read_html(model.summary().tables[0].as_html(),header=None,index_col=None)[0] #Se extrae los valores de r2
    return { #Se regresa un diccionario con los siguientes valores
        'm': coef.values[1], #Pendiente
        'b': coef.values[0],  #Termino independiente de la regresión
        'r2': r_2_t.values[0][3], #Coeficiente de determinación r2
        'r2_adj': r_2_t.values[1][3], #R2 ajustado
        'low_band': bands['[0.025'][0], #Valor inferior del intervalo de confianza
        'hi_band': bands['0.975]'][0] #Valor superior del intervalo de confianza
        } 

#Cuarta función, es para graficar una regresión lineal juntoo con un intervalo de confianza alrededor de dicho alrededor de la linea de regresión
def plt_lr(df: pd.DataFrame, x:str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float, colors: Tuple[str,str]):
    #Definimos nombre de función, y los parametros que le pasamos que es:
    #Dataframe
    #Variable independiente, dependiente
    #Pendiente y termino independiente de la regresion lineal
    #Coeficiente de determinación r2 y ajustado
    #Valores inferiores y superiores del IC
    #Una tupla de colores para la regresion y el area sombreada
    fixed_x = transform_variable(df, x) #Se transforma la variable independiente
    plt.plot(df[x],[ m * x + b for _, x in fixed_x.items()], color=colors[0]) #Genera el grafico de la regresión lineal como tal
    plt.fill_between(df[x],[ m * x  + low_band for _, x in fixed_x.items()],[ m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])
    #Rellena el area de los limites del intervalo de confianza

#Quinta función, esta función esta diseñada a generar la practica numero 9 que esta relacionada con el forecasting
def GenerarForeCasting(): #Se define el nombre de la función
    DataFrameOriginal = pd.read_csv('csv/DataSet.csv') #Se lee el dataset original
    DataFrame = create_serie_tiempo(DataFrameOriginal) #Se hace el nuevo dataframe con la función, es lo de los trabajos publicados por dias
    DataFrameReducido = DataFrame.tail(100) #Se reduce la cantidad de fechas a las ultimas 100 
    x = "Combined Date" #Eje de las x son las fechas
    y= "Jobs Posted" #Eje de las y son los trabajos publicados
    plt.figure(figsize=(30, 20))  # Establecer el tamaño de la figura
    DataFrameReducido.plot(x=x,y=y, kind='scatter') #Se crea un grafico de dispersión utilizando los datos del dataframe
    a = linear_regression(DataFrameReducido, x,y) #Realiza regresión lineal
    plt_lr(df=DataFrameReducido, x=x, y=y, colors=('red', 'orange'), **a) #Se traza la regresión lineal creada
    a = linear_regression(DataFrameReducido.tail(15), x,y) #Realiza regresión lineal de los ultimos 15 elementos del DataFrame
    plt_lr(df=DataFrameReducido.tail(15), x=x, y=y, colors=('red', 'orange'), **a) #Se traza la regresión lineal creada
    a = linear_regression(DataFrameReducido.head(15), x,y) #Realiza la regresión lineal de los primeros 15 elementos del DAtaFrame
    plt_lr(DataFrameReducido.head(15), x=x, y=y, colors=('blue', 'blue'), **a) #Se traza la regresión lineal creada
    plt.xticks(rotation=90)#Rotamiento del eje x
    plt.savefig('imagenes/lr_TrabajosPublicados_Fecha.png') #Guardado
    plt.close() #Cierre de plot 
    dfs = [ 
        ('50 fechas', DataFrameReducido), #El DataFrame como tal (que son tail 100)
        ('10 Fechas', DataFrameReducido.tail(10)), #Ultimas 10 fechas
        ('5 Fechas', DataFrameReducido.tail(5)), #Ultimas 5 fechas
    ]
    lrs = [(title, linear_regression(_df,x=x,y=y), len(_df)) for title, _df in dfs] #Se realiza regreisones lineales y se almacenan sus resultados en lrs
    lrs_p = [(title, lr_dict["m"]*size  + lr_dict["b"], lr_dict) for title, lr_dict, size in lrs] #Se calcula el valor usando la regresión lineal para cada conjunto de los resultados de lrs
    #y se almacena en lrs_p
    print(lrs_p) #Se imprime lrs_p
    
#Ejecuta la función que genera la practica
GenerarForeCasting()