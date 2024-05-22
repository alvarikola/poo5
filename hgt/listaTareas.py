from hgt.tarea import Tarea
class ListaTareas:
    LIMITCHAR = "|&&|"
    
    def __init__(self):
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
                i.delete(tarea)
                break


    def load(self, data:str):
        tareas = data.split(self.LIMITCHAR)
        for tarea in tareas:
            self.tareas.append(tarea)


    def __str__(self):
        return self.read()

    def __len__(self):
        return  self.tareas.__len__()
    
    def __getitem__(self, index):
        return self.tareas[index]
    
    def __setitem__(self, index, value):
        self.tareas[index] = value

    def __delitem__(self, index):
        del self.tareas[index]

    def __iter__(self):
        return self.tareas.__iter__()
    
    def __next__(self):
        return self.tareas.__next__()
    
    def __contains__(self, item):
        return item in self.tareas
    
    def __eq__(self, other):
        return self.tareas == other.tareas
    
    def __ne__(self, other):
        return self.tareas != other.tareas

    