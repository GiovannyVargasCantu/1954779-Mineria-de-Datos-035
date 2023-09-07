#Alumno:Miguel Giovanny Vargas Cantú
#Matricula: 1954779
#Escuela: FCFM UANL
#Materia: Minería de Datos 035 Jueves de 7:00pm a 10:00pm
#Docente: Jose Anastacio Hernandez Saldaña

#Se importa requests, para ello es necesario hacer un pip install requests, de otra forma no se podra utilizar esta linea de codigo.
import requests

#El url es el url de descarga, este lo obtuve en la pagina de dat.gov llamado nyc jobs, de ahi hay un boton de descarga del .CSV, le di copiar dirección de enlace y este es el URL
url = 'https://data.cityofnewyork.us/api/views/kpav-sd4t/rows.csv?accessType=DOWNLOAD'

# Aqui se realiza un get para obtener el contenido
response = requests.get(url)

# Aca verificamos si nos da el codigo de estado 200 (Que sabemos que significa OK que no hubo problemas)
if response.status_code == 200: #Si es okey entonces se realiza lo siguiente
    #Se abre un archivo, que en este caso lo llamamos como DataSet.cv, y con write binary escribiremos en DataSet.csv lo que nos arrojo response
    with open('DataSet.csv', 'wb') as file:
        file.write(response.content) #Para ello accedemos con .content en response 
    print("El dataset ha sido descargado exitosamente.") #Se manda un mensaje donde se confirma que se realizo de manera exitosa la descarga
else:
    print("Se tuvo un error al descargar el dataset, el codigo obtenido es el siguiente: ", response.status_code)
    # Se manda un mensaje donde se niega que se realizo de manera exitosa la descarga, y te manda el codigo para información al respecto del error.

