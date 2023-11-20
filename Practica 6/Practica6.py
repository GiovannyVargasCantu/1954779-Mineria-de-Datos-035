#Alumno:Miguel Giovanny Vargas Cantú
#Matricula: 1954779
#Escuela: FCFM UANL
#Materia: Minería de Datos 035 Jueves de 7:00pm a 10:00pm
#Docente: Jose Anastacio Hernandez Saldaña

#Tambien es necesario importar matplotlib.pyplot para las graficas, en este caso solo con el comando pip install matplotlib 
import matplotlib.pyplot as plt

#Tenemos que importat statsmodels tambien, esto se realiza con pip install statsmodels, es de vital importancia realizar este paso dado que es lo que permitira realizar el ANOVA como tal
import statsmodels.api as sm


#Iniciamos importando pandas, para ello se necesita hacer un pip install pandas, teniendo pandas es la forma en la que podemos manipular los dataframes, existe
#tambien la libreria de CSV pero en este clase veremos al respecto sobre pandas
import pandas as pd

#Primera función, esta función se encarga de hacer la regresión lineal como tal, en este caso hare la regresión lineal teniendo como variable independiente a salario minimo
#y a variable dependiente a salario maximo, asi de esta forma se puede analizar la relacion entre estas dos variables.
def linear_regression(df: pd.DataFrame, x: str, y: str): #Se define el nombre de la función y los parametros, que en este caso se pasa los parametros del dataframe, x string y y string que son las variables
    #que recordemos tienen que ser de orden, es por ello la razon que mas adelante utilizo otras distintas al ANOVA que realice de categorias en la practica pasada, dado que la variable
    #debe ser numerica, es decir no categorica, y de ser categorica podriamos transformarla, tal y como lo hizo el profe en una función de transformación, pero decidi optarme por
    #unos que ya eran numericos
    model = sm.OLS(df[y], sm.add_constant(df[x])).fit() #Crea un modelo de regresion lineal, agarra la columna de "y" y la de "x" se le agrega
    #una constante que es una practica comun y recomendada para los modelos de regresion lineal
    print(model.summary())  #Se imprime el resumen del modelo de regresión lineal
    coef = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]['coef'] #Se obtiene el coeficiente del resumen del modelo, este se tiene que obtener a traves de
    #pd.read_html y selecciona la columna coef
    df.plot(x=x, y=y, kind='scatter') #Se crea el grafico con el dataframe de scatter, que seria un grafico de dispersion
    plt.plot(df[x], [df[y].mean() for _ in range(len(df[x]))], color='green') #Aqui se traza una linea horizontal con la media de los valores de Salario Maximo para todos los Salarios Minimos
    plt.plot(df[x], [coef.values[1] * x + coef.values[0] for x in df[x]], color='red') #Esta linea traza la linea de regresion que se obutvo en el modelo de regresión lineal
    plt.savefig(f'imagenes/RegresionLineal_{y}_{x}.png') #Se guarda el plot en imagenes con el nombre de regresion lineal_variabley_variablex 
    plt.close() #Se cierra el plot

#Segunda función, simplemente se encarga de ejecutar linear_regression que pues esa función realiza toda la practica, dado que es todo lo de regresión lineal
def GenerarRegresionLineal(): #Se define nombre de función
    DataFrame = pd.read_csv("csv/DataSet.csv") #Se asigna a una variable dataframe el dataset que tengo
    df_SalMin_SalMax = DataFrame[['Salary Range From', 'Salary Range To']] #Creo un nuevo dataset que solamente contenga el salary range from y salary range to, por cuestiones de orden
    df_SalMin_SalMax.reset_index(inplace = True) #un simple reseto de indices, ya ha sido explicado en anteriores practicas y en clase inclusive.
    df_SalMin_SalMax = df_SalMin_SalMax.rename(columns={'Salary Range From': 'Salario Minimo', 'Salary Range To': 'Salario Maximo'}) #Renombro las columnas para que todo sea mas claro
    linear_regression(df_SalMin_SalMax, "Salario Minimo","Salario Maximo") #Aplico la función de linear_regression, le paso el dataframe, y las variables independientes y dependientes
    #Escogi salario minimo y maximo porque deben de tener relación de orden, que tambien pude aplicar transformacion a las columnas, tal y como lo hizo el profesor con su columna de fechas
    #que con una función los volvio numeros, pero en realidad me incline por esto dado que las dos variables ya son numericas.

#Se ejecuta la función que realiza todo lo correspondiente a la practica #6 de Minería de Datos, Regresión Lineal
GenerarRegresionLineal()

