from tarea import Tarea
class Evento(Tarea):
    def __init__(self, tarea:str, estado:bool, id:int, fechaInicio:str, horaInicio:str, fechaFin:str, horaFin:str):
        super.__init__(tarea, estado, id)
        self.fechaInicio = fechaInicio
        self.horaInicio = horaInicio
        self.fechaFin = fechaFin
        self.horaFin = horaFin


    #Métodos CRUD
    
    def read(self):
        print(super.read() + self.fechaInicio + self.fechaFin + self.horaInicio + self.horaFin)

    def update(self):
        pass

    def delete(self):
        pass



a = Evento("tarea1", True, 1, "1-2-2024", "13:00", "1-2-2024", "14:00")
a.read()