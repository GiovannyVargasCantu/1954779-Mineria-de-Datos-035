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

#Primera función, esta función se encarga simplemente de crear una columna nueva que le pone tipo a cada departamento, me di cuenta que la cantidad de departamentos es 
#bastante, siendo asi que son 64, por lo que cree 20 categorias para que se haga un analisis por categoria mas bien.
def categorizar_dept(df: pd.DataFrame): #Defino el nombre de la función y el parametro, que en este caso es un dataframe el que recibe como parametro
    #Defino un diccionario en el que le coloco una categoria a cada departamento
    categorias = {
    "ADMIN FOR CHILDRENS SVCS": 'Servicios Sociales',
    "ADMIN TRIALS AND HEARINGS": 'Administracion',
    "BOARD OF CORRECTION": 'Administracion',
    "BOROUGH PRESIDENT-BRONX": 'Administracion',
    "BRONX COMMUNITY BOARD #1": 'Administracion',
    "BRONX COMMUNITY BOARD #7": 'Administracion',
    "BRONX COMMUNITY BOARD #8": 'Administracion',
    "BRONX DISTRICT ATTORNEY": 'Justicia',
    "BUSINESS INTEGRITY COMMISSION": 'Regulacion y Cumplimiento',
    "CAMPAIGN FINANCE BOARD": 'Regulacion y Cumplimiento',
    "CIVILIAN COMPLAINT REVIEW BD": 'Justicia',
    "CONFLICTS OF INTEREST BOARD": 'Regulacion y Cumplimiento',
    "CONSUMER AND WORKER PROTECTION": 'Regulacion y Cumplimiento',
    "CULTURAL AFFAIRS": 'Cultura y Arte',
    "DEPARTMENT FOR THE AGING": 'Servicios Sociales',
    "DEPARTMENT OF BUILDINGS": 'Construccion',
    "DEPARTMENT OF BUSINESS SERV.": 'Servicios Empresariales',
    "DEPARTMENT OF CITY PLANNING": 'Planificacion Urbana',
    "DEPARTMENT OF CORRECTION": 'Seguridad Publica',
    "DEPARTMENT OF FINANCE": 'Finanzas',
    "DEPARTMENT OF INVESTIGATION": 'Justicia',
    "DEPARTMENT OF PROBATION": 'Seguridad Publica',
    "DEPARTMENT OF SANITATION": 'Servicios Publicos',
    "DEPARTMENT OF TRANSPORTATION": 'Transporte',
    "DEPT OF CITYWIDE ADMIN SVCS": 'Administracion',
    "DEPT OF DESIGN & CONSTRUCTION": 'Construccion',
    "DEPT OF ENVIRONMENT PROTECTION": 'Medio Ambiente',
    "DEPT OF HEALTH/MENTAL HYGIENE": 'Salud',
    "DEPT OF PARKS & RECREATION": 'Parques y Recreacion',
    "DEPT OF YOUTH & COMM DEV SRVS": 'Servicios Comunitarios',
    "DEPT. OF HOMELESS SERVICES": 'Servicios Sociales',
    "DISTRICT ATTORNEY KINGS COUNTY": 'Justicia',
    "DISTRICT ATTORNEY RICHMOND COU": 'Justicia',
    "EQUAL EMPLOY PRACTICES COMM": 'Recursos Humanos',
    "FINANCIAL INFO SVCS AGENCY": 'Finanzas',
    "FIRE DEPARTMENT": 'Seguridad Publica',
    "HOUSING PRESERVATION & DVLPMNT": 'Vivienda',
    "HRA/DEPT OF SOCIAL SERVICES": 'Servicios Sociales',
    "HUMAN RIGHTS COMMISSION": 'Recursos Humanos',
    "LANDMARKS PRESERVATION COMM": 'Cultura y Arte',
    "LAW DEPARTMENT": 'Justicia',
    "MANHATTAN COMMUNITY BOARD #1": 'Administracion',
    "MANHATTAN COMMUNITY BOARD #10": 'Administracion',
    "MAYORS OFFICE OF CONTRACT SVCS": 'Administracion',
    "MUNICIPAL WATER FIN AUTHORITY": 'Finanzas',
    "NYC DEPT OF VETERANS' SERVICES": 'Servicios Sociales',
    "NYC EMPLOYEES RETIREMENT SYS": 'Recursos Humanos',
    "NYC FIRE PENSION FUND": 'Recursos Humanos',
    "NYC HOUSING AUTHORITY": 'Vivienda',
    "NYC POLICE PENSION FUND": 'Recursos Humanos',
    "OFF OF PAYROLL ADMINISTRATION": 'Administracion',
    "OFFICE OF CRIMINAL JUSTICE": 'Justicia',
    "OFFICE OF EMERGENCY MANAGEMENT": 'Seguridad Publica',
    "OFFICE OF LABOR RELATIONS": 'Recursos Humanos',
    "OFFICE OF MANAGEMENT & BUDGET": 'Administracion',
    "OFFICE OF THE ACTUARY": 'Recursos Humanos',
    "OFFICE OF THE COMPTROLLER": 'Administracion',
    "POLICE DEPARTMENT": 'Seguridad Publica',
    "PRESIDENT BOROUGH OF MANHATTAN": 'Administracion',
    "PUBLIC ADMINISTRATOR-NEW YORK": 'Administracion',
    "TAX COMMISSION": 'Impuestos',
    "TAXI & LIMOUSINE COMMISSION": 'Transporte',
    "TEACHERS RETIREMENT SYSTEM": 'Recursos Humanos',
    "TECHNOLOGY & INNOVATION": 'Tecnologia e Innovacion',
    }
    df['Categoria'] = df['Departamento de Trabajo'].map(categorias)  #Se tiene la columna cateogira en el que utilizo map con el diccionario que defini anterirmente
    return df #Se regresa el dataframe ya con la columna agregada de manera correcta

#Segunda función, esta función va de la mano de la función 1 y es meramente crear un csv con la nueva columna que se creo en la función 1, asi de simple es esta función honestamente
#eso si se crea un nuevo archivo, no remplazo el de Analyzed DataSet Deparments
def CrearCSVconDepartamentoCategorizado():
    DataFrame = pd.read_csv('Analyzed DataSet Deparments.csv') #Se lee el dataset que se habia creado en la practica 3, que de hecho una disculpa que apenas me di cuenta realizando
    #la practica 4 que escribi de manera erronea departamento en ingles
    DataFrame = categorizar_dept(DataFrame) #Se aplica la función #1 que agrega la columna con su categoria en cada departamento
    DataFrame.to_csv('Categorized Departments.csv', index=False) #Se guarda el dataframe ya con esa columna agregada  en este caso el nombre es Categorized Departments
    print("Se creo un nuevo archivo csv, con el nombre de Categorized Departments") #Simple mensaje de confirmación de que se creo el csv

#Tercera función, esta función genera una grafica de boxplots, donde se tiene la categoría y el promedio salario, es decir es un boxplot donde se ve en cada categoria el promedio salario
def create_boxplot_by_cat(df: pd.DataFrame, col1: str, col2: str): #Se define el nombre de la función, asi como los parametros, en este caso sera el parametro del dataframe
    #asi como el de las columnas que se desean hacer el boxplot
    df.boxplot(column=col2, by=col1, figsize=(27, 18)) #Se genera el boxplot con la función .boxplot, le pasamos las columnas asi como el tamaño de figura que tendra
    plt.xticks(rotation=90) #Roto el eje de las x en 90 grados, es decir, en vez de que se vea de manera horizontal las categorias las quiero de manera vertical, es mera cuestión
    #de que no se junten encima de otras las categorias y todo se pueda visualizar mejor
    plt.savefig(f"imagenes/boxplot_{col1}_{col2}.png") #Guardo el boxplot en la carpeta de imagenes, con un nombre en especifico
    plt.close() #Se cierra el plot
    print("Se creo un boxplot con formato png en la carpeta de imagenes de manera exitosa con el nombre de boxplot_"+col1+"_"+col2+".png") #Simple mensaje de confirmación que se creo el png

#Cuarta función, esta función se encarga de generar una grafica de pastel, donde ahora quiero ver, okey, hay 20 categorias, y tenemos 64 departamentos, que porcentaje tiene cada
#categoria, es decir, cuantos departamentos en porcentajes son de finanzas, administración, etc. 
def create_pieplot_by_cat(df: pd.DataFrame): #Se define el nombre de la función y el parametro que recibe, en este caso es el dataframe
    num_cat = df['Categoria'].value_counts() #Aca obtenemos el conteo de las categorias
    plt.figure(figsize=(16, 9)) #Se define el figsize de la figura
    plt.pie(num_cat, labels=num_cat.index, autopct='%1.1f%%') #Y aqui ya hacemos la grafica de pastel con .pie, que en este caso le pasamos num_cat como datos
    #num_cat.index son el nombre de las cateogrias, autopct defini cuantos decimales quiero en este caso me guie por 1 decimal unicamente 
    plt.title('Proporción de Categorías') #Aqui simplemente le doy un titulo en la imagen a mero arriba para que sea mas explicativo el grafico
    plt.savefig(f"imagenes/PiePlot de Categorias.png") #Cuestión de guardar el pieplot
    plt.close() #Se cierra el plot
    print("Se creo un pieplot con formato png en la carpeta de imagenes de manera exitosa con el nombre de PiePlot de Categorias.png")#Simple mensaje de confirmación que se creo el png

#Quinta función, esta función genera una grafica de barras, en este caso se podra ver el promedio de salario en cada categoria, por ejemplo si en cultura y arte solo son dos
#bueno se podra ver el promedio de esos 2 en una barra en comparación a las otras tambien
def create_barplot_promsalary_cat(df: pd.DataFrame): #Se define el nombre de la función y el parametro, en este caso el parametro es un dataframe
    plt.figure(figsize=(10, 6)) #Se establece el tamaño de la figura
    prom_salario_categoria = df.groupby('Categoria')['Promedio Salario'].mean() #Se obtiene el promedio de las categorias, para ello tuve que hacer un groupby de categoria y promedio salario
    #Maneje a promedio salario como si fuese el salario que reciben, pues al final de cuentas es el promedio vaya, pero no me sirve solo asi, necesito hacer el groupby para que se reuna
    #todo los salarios promedios de las categorias, y luego aplico el .mean para obtener pues el promedio, de esta forma por asi decirlo, ya tengo el salario promedio de Administración
    nombre_cat = prom_salario_categoria.index #Obtengo el nombre de las categorias
    valores = prom_salario_categoria.values #Obtengo los valores, es decir, el promedio de cada categoria
    plt.bar(nombre_cat,valores, color='skyblue', edgecolor='k') #Aqui hago la grafica de barras con .bar, en este caso le paso los nombres, valores, le asigno el color 
    plt.ylabel('Promedio Salario') #Le asigne al eje de las y la eitqueta promedio salario para que sea mas explicativa la grafica simplemente
    plt.grid(axis='y', linestyle='--', alpha=0.7) #Agrego una cuadricula horizontal para que se aprecie mejor la grafica
    plt.xticks(rotation=90) #Roto el eje de las x en 90 grados, es decir, en vez de que se vea de manera horizontal las categorias las quiero de manera vertical, es mera cuestión
    #de que no se junten encima de otras las categorias y todo se pueda visualizar mejor
    plt.tight_layout()#Ajusto el diseño de la grafica, mera cuestión de que se vea de una mejor forma tambien
    plt.savefig(f"imagenes/Grafica de Barras de Salario Total.png") #Simple guardado de archivo
    plt.close() #Se cierra el plot
    print("Se creo un barplot con formato png en la carpeta de imagenes de manera exitosa con el nombre de Grafica de Barras de Salario Total.png")#Simple mensaje de confirmación que se creo el png

#Sexta función, esta función cumple el rol el cual es ejecutar las funciones anteriores
def GenerarVisualizacion(): #Se define el nombre de la función, no recibe parametros en este caso
    CrearCSVconDepartamentoCategorizado() #Ejecuto para crear el nuevo csv, que con dicho csv es necesario para realizar las sisguientes funciones
    DataFrame = pd.read_csv('Categorized Departments.csv') #Se tiene la variable dataframe que tiene el csv nuevo que se creo en la anterior linea de codigo
    create_boxplot_by_cat(DataFrame, 'Categoria', 'Promedio Salario') #Se ejecuta la función para el boxplot, qeu le mando de parametro el dataframe asi como categoria ypromedio salario en strings
    create_pieplot_by_cat(DataFrame) #Se ejecuta la función para la grafica de pastel, simplemente le paso el dataframe
    create_barplot_promsalary_cat(DataFrame) #Se ejecuta la función para la grafica de barras, le paso el dataframe tambien unicamente

GenerarVisualizacion() #Ejecuto la sexta función que me genera la practica 4 que consta de la visualización

#NOTA: Se creo una carpeta manualmente de imagenes en el que se almaceno los plots, asi como dato queria comentarlo tambien por si las dudas