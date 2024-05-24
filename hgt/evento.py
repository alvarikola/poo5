from tarea import Tarea
class Evento(Tarea):
    def __init__(self, tarea, estado, id, fechaInicio:str, horaInicio:str, fechaFin:str, horaFin:str):
        super.__init__(tarea, estado, id)
        self.fechaInicio = fechaInicio
        self.horaInicio = horaInicio
        self.fechaFin = fechaFin
        self.horaFin = horaFin


    #Métodos CRUD
    
    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass