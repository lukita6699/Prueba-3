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
        promedio=int(input("Ingrese el promedio del estudiante: "));
        matriz.append(F"|",nom,"|",edad,"|",curso,"|",promedio,"|")
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






