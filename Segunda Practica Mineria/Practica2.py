#Alumno:Miguel Giovanny Vargas Cantú
#Matricula: 1954779
#Escuela: FCFM UANL
#Materia: Minería de Datos 035 Jueves de 7:00pm a 10:00pm
#Docente: Jose Anastacio Hernandez Saldaña

#IMPORTANTE

#Es necesario haber ejecutado la practica 1, es decir, tener descargado el DataSet.csv, de lo contrario no funcionara este codigo, dado que se hace referencia a dicho DataSet.

#IMPORTANTE

#Iniciamos importando pandas, para ello se necesita hacer un pip install pandas, teniendo pandas es la forma en la que podemos manipular los dataframes, existe
#tambien la libreria de CSV pero en este clase veremos al respecto sobre pandas
import pandas as pd

#Para ciertas funciones de limpieza/ordenamiento utilize Numpy, en si como tal no era 100% necesario utilizar Numpy, dado que se uso para los NaN y panda tiene ya sobre eso
#Pero quiero empezar a utilizar numpy, dado que se menciono en clase que seria una de las librerias con las que trabajemos durante estas practicas, asi que no esta demas
#Para ello se hace un pip install numpy aunque al menos conmigo, al instalar Python, Numpy ya venia instalado
#Pero eso depende de la versión de cada quien, por lo que especifico que de no tener instalado numpy, hay que hacer el pip install numpy
import numpy as np

#Es necesario esta libreria para algunas de las funciones utilizadas en esta practica
from datetime import date

#Se realizaran multiples funciones de data cleaning en esta segunda practica, en cada función explicare su función, por que la considere necesaria y demas, algunas funciones
#tienen como parametros columnas, pero como menciono al inicio de cada función, las cree por una razón, como por ejemplo la primera por Job ID y que el orden no me gusto, es decir,
# las intente hacer reutilizables pero en realidad las cree por cierta razon, igual y cada función tiene su explicación al inicio.

#Primera funcion es Ordenar los trabajos existentes por Job ID, esto simplemente no me gusto la organización dado que el dataset no estaba ordenado por nada en realidad
# asi que decidi inclinarme por lo mas simple que es el jobID, tambien se reinicia el Indice esto para que carguen con un nuevo indice, dado que si no realizo esa función 
# podria tener por dar un ejemplo que el JobID 6600 tiene el index de 3, y el JobID 4600 tiene el index de 4000, entonces como que no concuerdan, simplemente
# es para que se mantenga este orden del Job ID, por eso el reinicio

def Ordenar_Por_Valor_Ascendente(raw_df: pd.DataFrame, Columna: str)->pd.DataFrame: #Se define el nombre de la función, se mencionae en el parametro que recibe un dataframe y una columna, y regresa un dataframe
    raw_df = raw_df.sort_values(by=Columna) #El DataFrame crudo, es el dataframe como se recibe (el del parametro), aqui utilizo la función sortvalues y el by para indicar 
    #Cual es la medida por la cual se estan sorteando los valores, es decir en este caso es por la columna que se recibio como parametro (que lo pensamos para Job ID pero eso lo vemos al final)
    raw_df.reset_index(drop=True, inplace=True)
    #Esto es lo que mencione al inicio, sobre el reseteo de indices, es para que sean consecutivos y se lleve un orden y sea mas limpio todo en general.
    return raw_df #Regresa el dataframe sobre el que estuvimos trabajando toda la función


#Segunda función, esta función se encarga de validar que todas las filas tengan el valor de tiempo completo/medio en el trabajo, esto es de total relevancia dado que a la hora de 
#ver las estadisticas de quien paga mas y menos, podemos ver lo de tiempo completo y medio tiempo, por lo que las filas que no tengan esta columna son desechables dado que
# es una columna con muchisima importancia, caso contrario a la columna de Post Until, donde tampoco es la gran cosa que algunas no tengan nada
# Sin mencionar que hay muchisimos mas que no tienen nada en la parte de Post Until, que probablemente baje a menos de 5000 registros, que el docente especifico que buscaba 5000.
#En este caso al utilizar esta función pasamos de 6507 a 6229, por lo que sigo en el margen

def Eliminar_Filas_ConColumnaEspecificaVacia(raw_df: pd.DataFrame, Columna: str)->pd.DataFrame: #Se define la función, es identico que la anterior función, solo cambia el nombre de la función
    raw_df[Columna].replace('', np.nan, inplace=True)  #Aqui debo de remplazar todos los valores vacios con np.nan , investigando
    #me di cuenta que cambio mucho la sintaxis, y tuve que descubrir por mi cuenta que np.nan era lo que buscaba, ahora, la pregunta es porque tuve que hacer esto?
    #Cuando la siguiente linea (ya la explicare) quita los NaN, y es que, me di cuenta a traves de prueba y error que Panda los strings vacios tiene problemas al reconocerlo
    # Eso y tambien investigación en foros que hablaban al respecto, por lo que fue necesario buscar los  '' y remplazarlos con NaN y ya con eso podemos avanzar a la sig linea
    raw_df.dropna(subset=[Columna], inplace=True) #En esta linea tenemos un metodo que tienen los DataFrame de panda, y es el de .dropna, este metodo
    #Te ayuda a eliminar los que tienen NaN, en un principio si lo llamas sin parametros te eliminara las filas que estan solas, pero lo que yo quiero
    #es que me elimine las filas que tienen una columna vacia en especifico, entonces tengo que poner el subset que lleva la columna de parametro, que en este caso es lo de 
    #Full-Time/Part-Time indicator
    return raw_df#Regresa el dataframe sobre el que estuvimos trabajando toda la función

#Tercera función, esta función en vez de borrar rows (filas) como la segunda función dado que tienen una columna en blanco, esta se encargara de rellenar esa columna en blanco con un
#valor concreto, en este caso de la columna de la que hablo es la columna de Post Until, este columna tiene muchos NaN y a su vez tambien tiene fechas, por lo que
#para que se vea mas ordenado todo, y aparte para que no surgan problemas, rellenare las fechas con valores maximos, es decir, si no se tiene un Post Until, se asume que sera
#hasta que se quite esa oferta de trabajo (obviamente ya no nos interesa, porque tenemos el dataset), por lo que seria como que no tiene limite, por ello
#colocare la fecha de 12/31/2099, solo para indicar que es un tiempo muy largo hasta que se quite esta oferta, dado que no tiene limite, no coloco un string, por que luego si quiero
#hacer comparaciones y demas con todos estos ambitos de las fechas, puede que surgan problemas o que el codigo se complique de mas, asi que una solución, a mi parecer, adecuada
#seria ese como "placeholder" de una fecha maxima, dado que no se tiene limite, en si es para que todo se mantenga de un mismo tipo de dato, que seria Date

def Fillear_FechasFaltantes(raw_df: pd.DataFrame)->pd.DataFrame:#Se define la función que como parametro tiene dataframe y regresa un dataframe tambien
    raw_df['Post Until'].fillna('12/31/2099', inplace=True) #Aqui se utiliza el metodo de .fillna, que rellena los espacios en blanco en este caso con 12/31/2099
    return raw_df #Regresa el dataframe ya con los espacios en blancos rellenados

#Dado que la anterior función es muy especifica no le añadi el parametro de columna

#Cuarta función , en este caso llamare solo cuarta función a pesar de que sean dos funciones, dado que una se complementa con la otra, es decir, al final el objetivo de
#esta cuarta función, es ponerle un correcto formato a Post Until, y es que me di cuenta que los registros que ya tenia, es decir, no los que rellene en la función
#Anterior, esos registros venian en el formato de %d-%b-%Y, es decir venia 27-DEC-2023 y yo al final lo que deseo es que venga como %m/%d/%Y es decir
#que venga en el formato de MM/DD/YY, con sus barras diagonale en vez de guiones, entonces tengo una función, la primera realiza esa conversión, que dada una fecha 
#lo que te hara sera convertirla al formato correcto, en dado caso que ya tenga el formato (ValueError) es ahi donde te regresa la misma fecha, daod que
#esa misma fecha significa que ya esta en el formato correcto, solo es cuestión de regresarla, luego tengo la segunda función, que utiliza el apply en la columna de Post Until
#para aplicarles Formato_FechaIndividual, es decir la primera función, el apply hace que le pase como parametro 1 por 1 cada fecha, es decir, se le aplica a todas las fechas
# esa función (digo fechas, pero pues es todos los registros de esa columna vaya, si cambiase de columna dejaria de ser fechas, suponiendo que cambio a una que no sea fechas)

def Formato_FechaIndividual_DBY_a_MDY(fecha: date): #Se define nombre función, con su parametro que recibira que en este caso es fecha que es tipo date
    try:
        return pd.to_datetime(fecha, format='%d-%b-%Y').strftime('%m/%d/%Y') #Se toma un formato de %d-%b-%Y y se pasa al %m/%d/%Y y se regresa esa fecha cambiada de formato
    except ValueError: #En dado caso que no se matche el formato de "%d-%b-%Y" significa que ya se tiene el correcto, por lo que regresamos como esta
        return fecha #Regresamos la fecha

def Formato_Fechas_DBY_a_MDY(raw_df: pd.DataFrame, Columna:str)->pd.DataFrame: #se define nombre función, con su parametro que recibira que en este caso es un dataframe y la columna
    raw_df[Columna] = raw_df[Columna].apply(Formato_FechaIndividual_DBY_a_MDY) #Se le aplica la función anterior explicada a cada fecha de la columna Post Until del dataframe
    return raw_df #Se regresa el dataframe ya cambiado

 #Quinta función, analizando el dataframe me di cuenta que la columna de Recruitment Contact estaba vacia,  obviamente solo que yo vea, es decir, mi observación, no es suificiente
 #dado que existe el error humano siempre, en cuestión de que se me pase uno y demas, entonces decidi hacer codigo para verificar si en verdad estaba vacia la columna, al estar vacia
 #la columna decidi que es mejor eliminar la columna como tal, dado que es absolutamente inutil, que si bien, es una columna relevante, es decir, es el contacto y es importante,
 # al venir el dataset con esa columna vacia esa columna s evuelve inutil, y al final de cuenta me encargo del analisis de datos, y la mineria, etc, es decir no me encargo yo
 # de poner los contactos y esas cosas, por lo que, no hay manera de rellenar estos contactos con numeros falsos como "place holders" si no que lo mejor es borrar

def columna_esta_vacia(raw_df:pd.DataFrame, Columna: str)->pd.DataFrame:#se define nombre función, con su parametro que recibira que en este caso es un dataframe y la columna
    return raw_df[Columna].isna().all() #Regresa un valor booleano, te dice si es verdad o falso, y la función .isna indica si es NaN, y con all() se aplica a todos.

def Eliminar_Columna(raw_df: pd.DataFrame, Columna: str)->pd.DataFrame:#se define nombre función, con su parametro que recibira que en este caso es un dataframe y la columna
    raw_df = raw_df.drop(columns=Columna) #Se utiliza el metodo drop para eliminar en este caso la columna del parametro, que como se menciono en el inicio del texto
    #sobre la quinta función, fue pensada para Recruitment Contract, pero aun asi la mantengo como con parametros para que se pueda llegar a usar en un futuro
    #es mera cuestión de reutilización.
    return raw_df #Regresa el dataframe con la columna ya eliminada

#Sexta función, me di cuenta que despues de los Salary Frequency creo que lo mas idoneo seria que estuviera Hours/Shift dado qeu estan bastante relacionados, por lo que
#hare una función que cambie el orden de las columnas, dada una columna que deberia estar despues, y una columna que se movera, simplemente se hara un pop de la columna
#que se desea mover y luego se insertara la columna, claro teniendo en cuenta la posicion de donde se pondra
#por ello es de vital importancia saber la columna despues, dado que esta columna es la que nos da la posición

def OrdenarDataFrameHorasTurno(raw_df: pd.DataFrame, ColumMover: str, ColumDespues:str)->pd.DataFrame: #Aqui se define la función en este caso hay 3 parametros, el dataframe, y las 
    #columnas, que seria la que vamos a mover (a cambiar su orden) y la columna que queremos que este despues de la columna que moveremos, o si lo quieren ver de esta forma
    #la columna que moveremos ira antes de esta ColumDespues, es simplemente como una columna de referencia vaya
    ColumnaQuitada = raw_df.pop(ColumMover) #Aqui obtenemos los valores de la Columna que moveremos, por ejemplo yo lo pense para Hours/Shift, entonces aqui se tendria
    #Pues no se, 35 horas Lunes a Viernes por dar un ejemplo, es decir, sacamos los registros de la columna, no confundir con ColumMover que es un string simplemente
    #Para ello utilizo el metodo de pop en el dataframe y especifico cual columna se le aplicara el pop mediante ColumMover
    PosicionAPoner = raw_df.columns.get_loc(ColumDespues) #Aqui obtenemos la posición como mencione al inicio de la función, aca es bastante simple, simplemente uso
    #get loc para obtener la posicion de la ColumDespues que es la que nos interesa, dado que antes de ColumDespues ira la ColumMover (Columna que estamos ordenando)
    raw_df.insert(PosicionAPoner,ColumMover,ColumnaQuitada) #Y aca es bastante simple, es cuestión de insertar con insert, primero se coloca la posición donde se insertara
    #Acto seguido el nombre de la columna que tendra que es ColumMover, y por ultimo los valores que tendra esa columna que recordemos los obtuvimos en la primer linea de codigo de
    #esta función despues de definirla, lo de ColumnaQuitada
    return raw_df #Ya regresamos el dataframe modificado

#Esta función basicamente es la compilación de todas las funciones anteriores con los parametros adecuados y me genera al final la modificacion del dataset donde no esta ordenado
def DataFrame_Clean():
    DataFrame = pd.read_csv('DataSet.csv') #Se declara el dataframe, que lo lee de DataSet.csv, que sería el dataset que se descargo en la practica 1
    DataFrame = Ordenar_Por_Valor_Ascendente(DataFrame,'Job ID') #Se aplica la función con la columna de Job ID y el DataFrame
    DataFrame = Eliminar_Filas_ConColumnaEspecificaVacia(DataFrame,'Full-Time/Part-Time indicator') #Se aplica la función con la columna de Full-Time/Part-Time indicator y el DataFrame
    DataFrame = Fillear_FechasFaltantes(DataFrame) #Se aplica la función con el DataFrame
    DataFrame = Formato_Fechas_DBY_a_MDY(DataFrame,'Post Until') #Se aplica la función con el DataFrame y la columna de Post-Until
    if(columna_esta_vacia(DataFrame, 'Recruitment Contact')): #Se verifica si la columna esta vacia en este caso la de Recruitment Contact
        DataFrame = Eliminar_Columna (DataFrame, 'Recruitment Contact') #En caso de estarlo elimina la columna, por lo cual se llama la función con el parametro de la columna
        #Recruitment Contact
    DataFrame = OrdenarDataFrameHorasTurno(DataFrame,'Hours/Shift','Work Location') #Ordenamos para que Horas/Turno este antes de Localización Trabajo, asi tiene un poco mas de 
    #coherencia como es que tienen secuencia los datos, es mera cuestión de organización aca
    DataFrame.to_csv('DataSet.csv', index=False) #Se actualiza el dataset, se pone el mismo nombre que el original para que lo reemplaze y solo se haya como actualizado, es decir
    #no se cree un archivo nuevo con otro nombre o algo por el estilo, solamente lo actualiza el dataset.
    print("El dataset ha sido actualizado")

#IMPORTANTE

#Dado que remplazo el DataSet.csv que se tenia originalmente, es de vital importancia que no se tenga abierto el DataSet.csv (Es decir el que se descarga con la practica 1)
#Dado que al correr el programa windows le negara permisos, por que pues esta abierto
#Solamente es cuestión de no tener nada abierto para que se pueda ejecutar este script, y ahora si que ya este remplazado podemos consultar abriendo el nuevo DataSet.csv
#En si no se creara un nuevo archivo con otro nombre, si no que se tendra el mismo archivo DataSet.csv, pero pues ya no sera el mismo de la practica 1
#si no que sera el nuevo con las modificaciones especificadas.

#IMPORTANTE

#Corro la ultima función para que se tenga el DataSet.csv con las limpieza/ordenamiento ya hecho
DataFrame_Clean()

