#Variable
lista_estudiantes=['|','NOMBRE',"|",'EDAD',"|",'CURSO',"|",'PROMEDIO','|']
matriz=[]
guardar_archivo=[]
matriz1=[]

import time
#Ejecucion

def agregar_estudiante():
    while True:
        nom=input("Ingrese el nombre del estudiante: ");
        edad=int(input("Ingrese la edad del estudiante: "));
        curso=input("Ingrese el curso del estudiante: ");
        promedio=input("Ingrese el promedio del estudiante: ");
        fila=["|",nom,"|",edad,"|",curso,"|",promedio,"|"]
        matriz.append(fila)
        print("¿Desea repetir el registro? (ENTER para continuar) (SI para salir)")
        pregunta=input("")
        if pregunta=="SI":
            print ("Saliendo..")
            time.sleep(1);
            break;

def ver_productos():
    print (lista_estudiantes);
    for x in matriz:
        print (x)




# guardar archivo
def guardararchivo():
 import csv

 with open('nuevo_archivolol.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    escritor_csv.writerow(lista_estudiantes)

    escritor_csv.writerows(matriz)
    print ("Se creo correctamente el archivo .csv"); 

 import csv
 with open('nuevo_archivolol.csv', 'r', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader (archivo_csv);
    for x in lector_csv:
        print (x) 






