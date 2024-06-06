#Alejandro Chávez (32.278.392)
#José Santana()

import carga
import funciones
from datetime import datetime
proyectos = carga.cargar_datos_desde_json('datos_prueba.json')

class Reporte:
    def menu(self):
        print(" Menu de opciones")
        print("1. Ejercicio a")
        print("2. Ejercicio b")
        print("3. Ejercicio c")
        print("4. Ejercicio d")
        print("5. Ejercicio e")
        print("6. Ejercicio f")
        print("...")
        self.operacion(input("Elija una opción (1,2,3,4,5,6): "))
    
    def operacion(self,opcion):
        if opcion == "1":
            self.opcion1()
        if opcion == "2":
            self.opcion2()
        if opcion == "3":
            self.opcion3()
        if opcion == "4":
            self.opcion4()
        if opcion == "5":
            self.opcion5()
        if opcion == "6":
            self.opcion6()

    def opcion1(self):
        global proyectos
        lista = []
        condicion = input("Ingrese una condicion especica (Completada, Pendiente, En progreso): ")
        for i in range(len(proyectos)):
            for j in range(len(proyectos[i].tareas)):
                if proyectos[i].tareas[j].condicion == condicion:
                    lista.append(int(proyectos[i].tareas[j].avance))
        print("Lista: ",lista)
        lista = funciones.quicksort_descendente(lista)
        print("Lista ordenada: ",lista)
        print()
    
    def opcion2(self):
        global proyectos
        lista = []
        palabra = input("Ingrese la palabra especifica: ")
        for i in range(len(proyectos)):
            if palabra in proyectos[i].titulo:
                temp = proyectos[i].inicio.strftime("%y-%m-%d").split("-")
                for j in range(len(temp)):
                    temp[j] = int(temp[j])
                lista.append(temp)
        print("Lista: ",lista)
        lista = funciones.mergesortlistas(lista)
        print("Lista ordenada: ",lista)
        print()

    def opcion3(self):
        global proyectos
        pass

    def opcion4(self):
        global proyectos
        pass

    def opcion5(self):
        global proyectos
        pass

    def opcion6(self):
        global proyectos
        pass

rep = Reporte()
band = True
while(band):
    rep.menu()
    bucle = input("Quieres seguir con el programa?(S/N): ")
    print()
    if bucle.upper() != "S":
        band = False