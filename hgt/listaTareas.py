from hgt.tarea import Tarea
class ListaTareas(Tarea):
    LIMITCHAR = "|&&|"
    def __init__(self) -> None:
        self.tareas = []




#Métodos CRUD
    
    def agregar(self, tarea:Tarea):
        self.tareas.append(tarea)


    def read(self):
        resultado = ""
        for tarea in self.tareas:
            resultado += tarea
            if tarea != self.tareas[-1]:
                resultado += self.LIMITCHAR

        return resultado


    def update(self, tarea:Tarea, Nombretarea:str, estado:bool, id:int):
        for i in self.tareas:
            if i == tarea:
                tarea.update(Nombretarea, estado, id)
                break


    def delete(self, tarea:Tarea):
        for i in self.tareas:
            if i == tarea:
                i.delete()
                break


    def load(self, data:str):
        tareas = data.split(self.LIMITCHAR)
        for tarea in tareas:
            self.tareas.append(tarea)

