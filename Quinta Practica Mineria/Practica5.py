#Alumno:Miguel Giovanny Vargas Cantú
#Matricula: 1954779
#Escuela: FCFM UANL
#Materia: Minería de Datos 035 Jueves de 7:00pm a 10:00pm
#Docente: Jose Anastacio Hernandez Saldaña

#IMPORTANTE

#Es necesario haber ejecutado la practica 1,2,3 y 4 dado que se hace referencia a dicho DataSet.
#IMPORTANTE


#Iniciamos importando pandas, para ello se necesita hacer un pip install pandas, teniendo pandas es la forma en la que podemos manipular los dataframes, existe
#tambien la libreria de CSV pero en este clase veremos al respecto sobre pandas
import pandas as pd

#Tenemos que importat statsmodels tambien, esto se realiza con pip install statsmodels, es de vital importancia realizar este paso dado que es lo que permitira realizar el ANOVA como tal
import statsmodels.api as sm
from statsmodels.formula.api import ols

#Primera función, esta función se encarga de hacer el anova practicamente, y regresara el anova si es que hay diferencias asi como un print indicando que hay diferencias
#de no haber diferencias solo imprimira un no hay diferencia
def ANOVA(df: pd.DataFrame, str_ols: str): #Se define el nombre de la función y se le pasa como parametro el dataframe y el string para la formula del modelo
    modl = ols(str_ols, data=df).fit() #Se ajusta primero un modelo de ANOVA
    anova_df = sm.stats.anova_lm(modl, typ=2) #Se aplica el anova_lm con el modelo que se le paso, es el enfoque mas comun utilizado para los ANOVA
    if anova_df["PR(>F)"][0] < 0.005: #Si el p value es menor que 0.005 entonces significa que hay diferencias significativas (esto es dado el alpha que le di en este caso)
        print("Hay diferencias significativas:")  #Se imprime el mensaje que hay diferencias significativas
        print(anova_df) #Se imprime el anova
    else: #Caso contrario del p value, significa que no hay diferencias
        print("No hay diferencias significativas.")#Se imprime el mensaje

#Segunda función, esta función se encarga de preparar todo para hacer el anova, con preparar me refiero simplemente a tener un dataframe auxiliar, con el cual nos basaremos para el 
#Anova, por cuestiones de que se vea mas organizado creo esta función
def GenerarANOVA(df: pd.DataFrame): #Se define el nombre de la función y se le pasa como parametro el dataframe
    df['Salario Promedio'] = (df['Salary Range From'] + df['Salary Range To']) / 2 #Se crea una nueva columna de Promedio Salario, dado que tengo 2 columnas
    #que indican el minimo y maximo de salario, con ellas genero un promedio de cuanto es del trabajo
    df_aux= df[['Job Category', 'Salario Promedio']] #Genero un dataframe auxiliar, que contendra las variables del ANOVA, en este caso sera Job Category y Salario Promedio que
    #Salario Promedio recordar que acabo de crearla en la linea anterior y como tal no viene en el dataframe original, el CSV vaya.
    #Como dato adicional, viendo que variables podia utilizar para realizar el ANOVA y demas, apenas me di cuenta de la existencia de Job Category como columna, dado que tengo un
    #Dataframe con bastantes columnas en principio me costo trabajo verlo, pero ahora que me di cuenta de esa columna, en este caso la utilizare
    #Basicamente este ANOVA vera si hay diferencias significativas en el Salario Promedio dado la categoria del trabajo, es decir Job Category, es mera cuestión de analizar con el ANOVA.
    #Que si bien podemos hacer este analisis mediante graficas y nosotros mismos darnos cuenta, lo interesante es que el ANOVA automatiza un poco este proceso, para que uno no tenga que
    #Andar viendo graficas como tal, si no que te dice si si hay diferencias significativas o no, claro todo esto en base a un alpha designado, que dependiendo el alpha cambia las respuestas
    df_aux.rename(columns={'Job Category': 'Job_Category', 'Salario Promedio': 'Promedio_Salario'}, inplace=True)
    #Mera cuestión de renombrar las columnas dado que vi que me estaba dando errores por los espacios en los nombres
    df_aux.reset_index(drop=True, inplace=True) #un simple reseto de indices, ya ha sido explicado en anteriores practicas y en clase inclusive.
    print(df_aux) #Se imprime el df_aux para que se vea con que se esta trabajando
    ANOVA(df_aux, "Promedio_Salario ~ Job_Category") #Se manda a hacer el anova, que en realidad pues ya viene todo explicado en la función anterior, es decir la numero 1.

#Tercera función, simplemente se encarga de ejecutar la función de GenerarANOVA que dicha función pues realiza todo dado que tiene la otra función de anova dentro de esa función.
def GenerarPruebasEstadisticas():#Se define el nombre de la función
    DataFrame = pd.read_csv('DataSet.csv') #Se almacena el dataframe en la variable DataFrame
    GenerarANOVA(DataFrame)#Se ejecuta la función que realiza el ANOVA

#Se ejecuta la función que realiza todo lo correspondiente a la practica #5 de Minería de Datos, Pruebas Estadisticas, en este caso ANOVA
GenerarPruebasEstadisticas()