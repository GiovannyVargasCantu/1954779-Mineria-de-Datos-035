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

#Es necesario importar wordcloud para la realización de esta practica
from wordcloud import WordCloud

#Primera función, esta función se encargara de volver el texto de una columna en un string gigantesco, este string servira para despues utilizar WordCloud y poner ese string
#Que seria basicamente como all_words en cuestión si lo relacionamos con lo que vimos en clase
def creacion_string(df: pd.DataFrame, col: str)->str:#Se define nombre de la función, asi como parametros, que sería el dataframe y el nombre de la columna, y se regresa un string
    allwords = ' '.join(df[col]) #Concateno la columna del dataframe en un solo string que lo llamo allwords que pues serian todas las palabras de la columna
    return allwords #Regreso el stringsote
#Segunda función, esta función se encarga de generar el wordcloud como tal
def creacion_nubetexto(CadenaDeTextoGigante : str)->WordCloud: #Se define el nombre de la función, asi como parametros, qeu en este caso solo pide el stringsote anterior, regresa un WordCloud
    wordcloud = WordCloud(background_color="white",min_font_size=5).generate(CadenaDeTextoGigante) #Uso de WordCloud para generar la nube de texto con la ayuda de la cadena de texto
    return wordcloud #Regreso wordcloud

#Tercera función, esta función se encarga de graficar el wordcloud
def graficar(NubeTexto:WordCloud): #Se define nombre de la función, asi como parametro, que pues unicmanete seria el wordcloud, que es lo que queremos graficar
    plt.figure(figsize=(5, 5), facecolor=None) #se crea una figura con el size de 5x5 y sin un color de fondo en especifico
    plt.imshow(NubeTexto) #Muestra el wordcloud en la figura que cree
    plt.axis("off") #Desactivo ejes
    plt.tight_layout(pad=0) #Ajustra diseñoo de grafica
    plt.savefig("imagenes/word_cloud.png") #Se guarda la figura
    plt.show() #Se muestra
    plt.close() #Se cierra plot

#Cuarta función, esta función se encarga de ser la main basicamente
def GenerarPracticaDiez(): #Se define nombre de la función
    DataFrame = pd.read_csv('csv/DataSet.csv') #Se obtiene el dataframe
    all_words = creacion_string(DataFrame,"Business Title") #Se ejecuta para obtener el string
    nubeTexto = creacion_nubetexto(all_words) #Con el string ejecutamos la nube de texto
    graficar(nubeTexto) #Se grafica para finalizar

GenerarPracticaDiez() #Ejecución de la función que genera la practica numero 10

