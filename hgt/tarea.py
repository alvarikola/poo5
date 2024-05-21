class Tarea:
    def __init__(self, tarea:str, estado:bool, id:int):
        self.tarea = tarea
        self.estado = estado
        self.id = id


    #Métodos CRUD
    
    def read(self):
        return f"{self.tarea} {self.estado} {self.id}"


    def update(self, tareaNueva, estadoNuevo, idNuevo):
        self.tarea = tareaNueva
        self.estado = estadoNuevo
        self.id = idNuevo   


    def delete(self):
        self.tarea = None
        self.id = None
        self.estado = None