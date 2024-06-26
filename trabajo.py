lista_estudiantes=['|','NOMBRE',"|",'EDAD',"|",'CURSO',"|",'PROMEDIO','|']
matriz=[]
guardar_archivo=[]
matriz1=[]
lista_modificados=[]
matriz2=[]
import time
#Ejecucion


while True:
        nom=input("Ingrese el nombre del estudiante: ");
        edad=int(input("Ingrese la edad del estudiante: "));
        curso=input("Ingrese el curso del estudiante: ");
        promedio=input("Ingrese el promedio del estudiante: ");
        fila=[nom,edad,curso,promedio]
        matriz.append(fila)
        print("¿Desea repetir el registro? (ENTER para continuar) (SI para salir)")
        pregunta=input("")
        if pregunta=="SI":
            print ("Saliendo..")
            time.sleep(1);
            break;
        for x in matriz:
            print (x)
 
        while True:
            print("1.-cambiar nombre")
            print("2.-cambiar edad")
            print("3.-cambiar curso")
            print("4.-cambiar promedio")
            print("5.-salir")
            opc=int(input("Ingrese Una opcion: "))
            if opc==1:
                 fila.remove(nom)
                 nom=input("ingrese el nombre: ")
                 fila.append(nom)
            elif opc==2:
                 fila.remove(edad)
                 nom=input("ingrese la edad: ")
                 fila.append(edad)
            elif opc==3:
                 fila.remove(nom)
                 nom=input("ingrese el curso: ")
                 fila.append(curso)
            elif opc==4:
                 fila.remove(nom)
                 nom=input("ingrese el promedio: ")
                 fila.append(promedio)
            elif opc==5:
                 break
                
