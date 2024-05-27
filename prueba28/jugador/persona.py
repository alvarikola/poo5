class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


    def read(self) ->str:
        return self.nombre

    def update(self, nombreNuevo):
        self.nombre = nombreNuevo


    def delete(self):
        self.nombre = None