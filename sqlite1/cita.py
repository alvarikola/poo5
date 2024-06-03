class Cita:
    def __init__(self, cita) -> None:
        self.cita = cita

    def __str__(self) -> str:
        return self.cita
    

    def leer(self) -> str:
        return self.cita