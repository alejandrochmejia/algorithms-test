#Alejandro Chávez (32.278.392)
#José Santana()

class Proyecto:
    def __init__(self,id,titulo,detalles,inicio,vencimiento,condicion,organizacion,responsable,grupo):
        self.id = id
        self.titulo = titulo
        self.detalles = detalles
        self.inicio = inicio
        self.vencimiento = vencimiento
        self.condicion = condicion
        self.organizacion = organizacion
        self.responsable = responsable
        self.grupo = grupo
        self.tareas = []

    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)

class Tarea:
    def __init__(self,id,titulo,cliente,detalles,inicio,vencimiento,condicion,avance):
        self.id = id
        self.titulo = titulo
        self.cliente = cliente
        self.detalles = detalles
        self.inicio = inicio
        self.vencimiento = vencimiento
        self.condicion = condicion
        self.avance = avance
        self.subtareas = []
    
    def agregar_subtarea(self,subtarea):
        self.subtareas.append(subtarea)

class Subtarea:
    def __init__(self,id,titulo,detalles,condicion):
        self.id = id
        self.titulo = titulo
        self.detalles = detalles
        self.condicion = condicion