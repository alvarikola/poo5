class Tarea:
    def __init__(self, tarea:str, estado:bool, id:int):
        self.tarea = tarea
        self.estado = estado
        self.id = id


    #Métodos CRUD
    
    def read(self):
        return f"Esta es la tarea: {self.tarea}, su estado es: {self.estado} y su id: {self.id}"


    def update(self, estadoNuevo:bool):
        self.id = estadoNuevo
        return estadoNuevo


    def delete(self):
        del self.tarea
        del self.id
        del self.estado