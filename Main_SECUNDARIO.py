#mine

import Evaluacion_prueba3 as funcion
import time 
def menu():
    while True:
        print ("Menu de opciones")
        print ("")
        print ("1. Agregar un estudidante.")
        print ("2. Ver todos los estudiante.")
        print ("3. Modificar un estudiante.")
        print ("4. Eliminar un estudiante.")
        print ("5. Guardar archivo.")
        print ("6. Salir del programa.")
        try:
            opcion=int(input("Ingrese una opcion: "));
        except:
            print ("Ingrese un numero!")
        else:
            print ("")
            if opcion==1:
                print ("")
                print ("Agregar un estudiante.")
                print ("")
                funcion.agregar_estudiante()
                print ("")
                
            elif opcion==2:
                print ("")
                print ("Ver todos los estudianes.")
                print ("")
                funcion.ver_productos()
                print ("")
                
            elif opcion==3:
                print ("")
                print ("Modificar un estudiante.")
                print ("")
                funcion.modificar_producto()
                print ("")
                
            elif opcion==4:
                print ("")
                print ("Elminar un estudiante.")
                print ("")
                funcion.eliminar_producto()
                print ("")
                
            elif opcion==5:
                print ("")
                funcion.guardar_archivo()
                print ("")
                
            elif opcion==6:
                print ("")
                print ("Saliendo..")
                time.sleep(1)
                break;
                print ("")
