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
        lista = []
        print("\nN total de proyectos: " + str(len(proyectos)))
        n = input("Elija el proyecto a usar (escriba un numero del 1 al N): ")
        n = int(n)
        if int(n) > 0 and int(n) <= len(proyectos):
            for i in range(len(proyectos[n-1].tareas)):
                for j in range(len(proyectos[n-1].tareas[i].subtareas)):
                    if proyectos[n-1].tareas[i].subtareas[j].condicion == "Completada":
                        lista.append(proyectos[n-1].tareas[i].subtareas[j].titulo)
            print("Lista:",lista)
            lista = funciones.shellsortalfabetico(lista)
            print("Lista Ordenada:",lista)
            print()
        else:
            print("Proyecto Inexistente")
            print()

    def opcion4(self):
        global proyectos
        lista = []
        for i in range(len(proyectos)):
            for j in range(len(proyectos[i].tareas)):
                temp = len(proyectos[i].tareas[j].subtareas)
                lista.append(temp)
        print("Lista:",lista)
        lista = funciones.merge_sort(lista)
        print("Lista ordenada: ",lista)
        print()

    def opcion5(self):
        global proyectos
        valor = int(input("Ingrese el valor especifico: "))
        lista = []
        for i in range(len(proyectos)):
            for j in range(len(proyectos[i].tareas)):
                if proyectos[i].tareas[j].avance < valor:
                    temp = proyectos[i].tareas[j].vencimiento.strftime("%y-%m-%d").split("-")
                    for k in range(len(temp)):
                        temp[k] = int(temp[k])
                    lista.append(temp)
        print("Lista: ",lista)
        lista = funciones1.heapsort(lista)
        print("Lista ordenada: ", lista)
        print()

    def opcion6(self):
        global proyectos
        lista = []
        print("\nN total de proyectos: " + str(len(proyectos)))
        n = input("Elija el proyecto a usar (escriba un numero del 1 al N): ")
        n = int(n)
        if int(n) > 0 and int(n) <= len(proyectos):
            HashTable = [[] for _ in range(len(proyectos[n-1].tareas))]
            for i in range(len(proyectos[n-1].tareas)):
                funciones.insert(HashTable,int(proyectos[n-1].tareas[i].inicio.strftime("%y-%m-%d").split("-")[0]),proyectos[n-1].tareas[i])
            funciones.display_hash(HashTable)

rep = Reporte()
band = True
while(band):
    rep.menu()
    bucle = input("Quieres seguir con el programa?(S/N): ")
    print()
    if bucle.upper() != "S":
        band = False