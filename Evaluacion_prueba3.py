#Variable
lista_estudiantes=['|','NOMBRE',"|",'EDAD',"|",'CURSO',"|",'PROMEDIO','|']
matriz=[]


import time
#Ejecucion

#Lucas hizo esto
def agregar_estudiante():
    while True:
        try:
            nom=input("Ingrese el nombre del estudiante: ");
            edad=int(input("Ingrese la edad del estudiante: "));
            curso=input("Ingrese el curso del estudiante: ");
            promedio=input("Ingrese el promedio del estudiante: ");
        except:
            print ("Ingrese un valor adecuado porfavor..")
        else:
            fila=[F"|",nom,"|",edad,"|",curso,"|",promedio,"|"]
            matriz.append(fila)
            print("¿Desea repetir el registro? (ENTER para continuar) (SI para salir)")
            try:
                pregunta=input("").upper()
            except:
                print("Ingrese una oracion..")
            else:
                if pregunta=="SI":
                    print ("Saliendo..")
                    time.sleep(1);
                    break;

def ver_productos():
    print (lista_estudiantes);
    for x in matriz:
        print (x)
        
#Axel hizo esto
def modificar_producto():
    print("")

def eliminar_producto():
    print (lista_estudiantes)
    for x in matriz:
        print (x)
    try:
        fila_eliminar=int(input("Ingrese la fila que quiere eliminar: "))
    except:
        print ("Ingrese un numero!")
    else:
        matriz.pop(fila_eliminar-1)
        print (lista_estudiantes)
        for x in matriz:
            print (x)

#Matias hizo esto
def guardar_archivo():
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







