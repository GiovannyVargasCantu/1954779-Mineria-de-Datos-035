#Alumno:Miguel Giovanny Vargas Cantú
#Matricula: 1954779
#Escuela: FCFM UANL
#Materia: Minería de Datos 035 Jueves de 7:00pm a 10:00pm
#Docente: Jose Anastacio Hernandez Saldaña

#IMPORTANTE

#Es necesario haber ejecutado la practica 1 y  2 (en realidad con la 1 es mas que suficiente dado que no utilizo columnas modificadas del dataset original, pero la 3 es continuación de la 2),
#es decir, tener descargado el DataSet.csv, de lo contrario no funcionara este codigo, dado que se hace referencia a dicho DataSet.

#IMPORTANTE

#Iniciamos importando pandas, para ello se necesita hacer un pip install pandas, teniendo pandas es la forma en la que podemos manipular los dataframes, existe
#tambien la libreria de CSV pero en este clase veremos al respecto sobre pandas
import pandas as pd


#Primera función, esta función se encarga de crear un nuevo dataframe con el que se muestre el departamento, salario total, cantidad de sueldos, promedio salario, salario maximo
#es decir, explorare las funciones de agregación vistas en clase, en este caso en el apartado de departamentos, de esta forma podre saber información relevante
#como por ejemplo al saber la cantidad de sueldos de no se, el departamento de transportación, con esa cantidad se cuantas ofertas de trabajo existentes hay, dado que el dataset
#es con respecto a ofertas de trabajos en NYC, asi mismo podre saber en promedio cual es el que mas gana, dado la columna promedio salario, y tambien sacar distintos tipos de
#conclusiones con respecto a estas funciones de agregación que son sum, count, mean, max

def show_data_by_department(df: pd.DataFrame)-> pd.DataFrame: #Defino el nombre de la función, asi como el parametro que recibira que es un dataframe, esta pensando en que le daremos
    #el dataframe original y de ahi el dataframe nuevo se basara en el, y pues por lo mismo se espera que regrese un pd.DataFrame esta función
    df['Salario Promedio'] = (df['Salary Range From'] + df['Salary Range To']) / 2 #Aqui mi dataframe tiene dos columnas relacionadas a salarios
    #es una columna de salary range from, y salary range to, entonces es como un rango como tal de salarios, para hacer esto un poco mas preciso, decidi hacer un promedio
    #entre los dos salarios que nos proveen las ofertas de trabajo, simplemente obtuve las columnas y las dividi entre el numero de totales que pues son 2 y asi saque el promedio
    #y tengo este Salario Promedio ahora
    df_new= df.groupby("Agency").agg({'Salario Promedio': ['sum', 'count', 'mean', 'max']}) #Aqui hago un groupby de Agency, que Agency es como el departamento si es que prestas
    #atención al DataSet original, dado que tiene multiples registros de departamentos, en si tambien son como "areas", trabajos de bombero por ejemplo hay un monton, es decir
    #distintos trabajos en el departamento de bomberos, pero pues al final todos son de ese departamento, asi es genial que haga yo este analisis
    #dado que a lo mejor el departamento de bombero, ser bombero fcomo tal pagan poco, pero en promedio el departamento de bombero paga bien, y puede ser por otros puestos que existan
    #o demas, en general me parecio una buena idea tomar este enfoque de "Agency", intente tomar el enfoque de pues los trabajos como tal que sería Business Title, pero no se, me termino
    #convenciendo mas tomar esta idea de Agency
    df_new.reset_index(inplace = True) #un simple reseto de indices, ya ha sido explicado en anteriores practicas y en clase inclusive.
    df_new.columns = ['Departamento de Trabajo', 'Salario Total', 'Cantidad de Sueldos', 'Promedio Salario', 'Salario Maximo'] #Aqui establezco el nombre de las columnas que se mostraran
    #Tengo la columna de departamento de trabajo, que ya mencione tipo los registros que aparecen ahi, por lo que me parecio conveniente darle ese nombre, luego sigue lo siguiente:
    #Salario Total: Aqui pues cada departamento tiene sus ofertas de trabajo con su salario, aqui pues se sumaron todos esos salarios, entonces es como el salario que estan proponiendo
    #en total, por eso el nombre de Salario Total, 
    #Cantidad de sueldos: Aqui cada oferta de trabajo las contamos, es decir, da igual ahora si pagan 1 millon o 1 centavo, lo que interesa aca en esta columna y de lo que trata es
    #cuantos sueldos hay, es decir hay 20,30,40, 1 o 2, y esta columna te muestra eso, de esta forma te das cuenta por ejemplo como la cantidad de ofertas de trabajo que hay en un
    #departamento en especifico
    #Promedio salario: Este nombre es bastante intuitivo, y es el promedio de salario de un departamento de trabajo, cuanto ganan en promedio la gente que trabaja en tal departamento
    #Salario Maximo: Este nombre igual es bastante intuitivo, es simplemente el salario Maximo de los trabajos en cada departamento
    return df_new #Se regresa el dataframe que genere nuevo despues de realizarle todo lo anterior

#Segunda función, en realidad solo es para ejecutar pues la función anterior, pero me gusta tener como todo mas ordenado por lo mismo cree otra función

def GenerarFuncionAgregacion(): #Se define el nombre de la función
    DataFrame = pd.read_csv('DataSet.csv') #Lee el archivo DataSet.csv, recuerden qeu si somos de practica 2, este seria el archivo ya limpio y ordenado
    DataFrame = show_data_by_department(DataFrame) #Se aplica la función en el dataframe DataSet.csv
    DataFrame.to_csv('Analyzed DataSet Deparments.csv', index=False) #Aqui es para pasar el dataframe que acabamos de definir a un nuevo archivo csv llamado Analyzed DataSet Departments
    #Este nombre pues porque es un poco el analisis de los departamentos del dataset como tal
    print("Se ha creado un nuevo archivo csv con las funciones de agregacion ") #Simple mensaje que al llegar al final te dice que ya se creo el archivo nuevo con formato csv 

GenerarFuncionAgregacion() #Se ejecuta la función que genera la Practica3


