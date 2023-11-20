#Alumno:Miguel Giovanny Vargas Cantú
#Matricula: 1954779
#Escuela: FCFM UANL
#Materia: Minería de Datos 035 Jueves de 7:00pm a 10:00pm
#Docente: Jose Anastacio Hernandez Saldaña

#IMPORTANTE

#Es necesario haber ejecutado la practica 1,2 y 3, dado que se hace referencia a dicho DataSet.

#IMPORTANTE


#Iniciamos importando pandas, para ello se necesita hacer un pip install pandas, teniendo pandas es la forma en la que podemos manipular los dataframes, existe
#tambien la libreria de CSV pero en este clase veremos al respecto sobre pandas
import pandas as pd
#Tambien es necesario importar matplotlib.pyplot para las graficas, en este caso solo con el comando pip install matplotlib 
import matplotlib.pyplot as plt


#Primera función, esta función genera una grafica de boxplots, donde se tiene el departamento de trabajo y el promedio salario, es decir es un boxplot donde se ve en cada departamento el promedio salario
def create_boxplot_by_cat(df: pd.DataFrame, col1: str, col2: str): #Se define el nombre de la función, asi como los parametros, en este caso sera el parametro del dataframe
    #asi como el de las columnas que se desean hacer el boxplot
    df.boxplot(column=col2, by=col1, figsize=(27, 18)) #Se genera el boxplot con la función .boxplot, le pasamos las columnas asi como el tamaño de figura que tendra
    plt.xticks(rotation=90) #Roto el eje de las x en 90 grados, es decir, en vez de que se vea de manera horizontal las categorias las quiero de manera vertical, es mera cuestión
    #de que no se junten encima de otras las categorias y todo se pueda visualizar mejor
    plt.savefig(f"imagenes/boxplot_{col1}_{col2}.png") #Guardo el boxplot en la carpeta de imagenes, con un nombre en especifico
    plt.close() #Se cierra el plot
    print("Se creo un boxplot con formato png en la carpeta de imagenes de manera exitosa con el nombre de boxplot_"+col1+"_"+col2+".png") #Simple mensaje de confirmación que se creo el png

#Segunda función, esta función se encarga de generar una grafica de pastel, donde ahora quiero ver, okey, hay 1000 trabajos, y tenemos 64 departamentos, que porcentaje tiene cada
#departamento, es decir, cuantos trabajos en porcentajes son del departamento de transporte, construcción, etc. 
def create_pieplot_by_cat(df: pd.DataFrame): #Se define el nombre de la función y el parametro que recibe, en este caso es el dataframe
    num_dept = df['Agency'].value_counts() #Aca obtenemos el conteo de los departamentos (es agency en el dataset original)
    plt.figure(figsize=(40, 30)) #Se define el figsize de la figura
    plt.pie(num_dept, labels=num_dept.index, autopct='%1.1f%%') #Y aqui ya hacemos la grafica de pastel con .pie, que en este caso le pasamos num_dept como datos
    #num_dept.index son el nombre de las departamentos, autopct defini cuantos decimales quiero en este caso me guie por 1 decimal unicamente 
    plt.title('Proporción de Departamento de Trabajo') #Aqui simplemente le doy un titulo en la imagen a mero arriba para que sea mas explicativo el grafico
    plt.savefig(f"imagenes/PiePlot de Departamento de Trabajo.png") #Cuestión de guardar el pieplot
    plt.close() #Se cierra el plot
    print("Se creo un pieplot con formato png en la carpeta de imagenes de manera exitosa con el nombre de PiePlot de Departamento de Trabajo.png")#Simple mensaje de confirmación que se creo el png

#Tercera función, esta función genera una grafica de barras, en este caso se podra ver el promedio de salario en cada departamento
def create_barplot_promsalary_cat(df: pd.DataFrame): #Se define el nombre de la función y el parametro, en este caso el parametro es un dataframe
    plt.figure(figsize=(10, 6)) #Se establece el tamaño de la figura
    departamentos = df['Departamento de Trabajo'] #Obtengo los departamentos
    salarioprom = df['Promedio Salario'] #Obtengo sus salarios
    plt.bar(departamentos,salarioprom, color='skyblue', edgecolor='k') #Aqui hago la grafica de barras con .bar, en este caso le paso los nombres, valores, le asigno el color 
    plt.ylabel('Promedio Salario') #Le asigne al eje de las y la eitqueta promedio salario para que sea mas explicativa la grafica simplemente
    plt.grid(axis='y', linestyle='--', alpha=0.7) #Agrego una cuadricula horizontal para que se aprecie mejor la grafica
    plt.xticks(rotation=90) #Roto el eje de las x en 90 grados, es decir, en vez de que se vea de manera horizontal los departamentos los quiero de manera vertical, es mera cuestión
    #de que no se junten encima de otros departamentos los departamentos y todo se pueda visualizar mejor
    plt.tight_layout()#Ajusto el diseño de la grafica, mera cuestión de que se vea de una mejor forma tambien
    plt.savefig(f"imagenes/Grafica de Barras de Salario Total.png") #Simple guardado de archivo
    plt.close() #Se cierra el plot
    print("Se creo un barplot con formato png en la carpeta de imagenes de manera exitosa con el nombre de Grafica de Barras de Salario Total.png")#Simple mensaje de confirmación que se creo el png

#Cuarta función, esta función cumple el rol el cual es ejecutar las funciones anteriores
def GenerarVisualizacion(): #Se define el nombre de la función, no recibe parametros en este caso
    DataFrame = pd.read_csv('csv/Analyzed DataSet Departments.csv') #Se obtiene el dataframe de la practica 3 de los departamentos
    DataFrameConTrabajos = pd.read_csv('csv/DataSet.csv') #Se obtiene el DataSet con todos los trabajos para la función del pastel
    create_boxplot_by_cat(DataFrame, 'Departamento de Trabajo', 'Promedio Salario') #Se ejecuta la función para el boxplot, qeu le mando de parametro el dataframe asi como departamento de trabajo y promedio salario en strings
    create_pieplot_by_cat(DataFrameConTrabajos) #Se ejecuta la función para la grafica de pastel, simplemente le paso el dataframe
    create_barplot_promsalary_cat(DataFrame) #Se ejecuta la función para la grafica de barras, le paso el dataframe tambien unicamente

GenerarVisualizacion() #Ejecuto la sexta función que me genera la practica 4 que consta de la visualización

#NOTA: Se creo una carpeta manualmente de imagenes en el que se almaceno los plots, asi como dato queria comentarlo tambien por si las dudas