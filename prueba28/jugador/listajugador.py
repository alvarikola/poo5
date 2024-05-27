from jugador import Jugador
class ListaJugador:
    LIMITCHAR = "|&&|"
    
    def __init__(self):
        self.jugadores = []


#Métodos CRUD
    
    def agregar(self, jugador:Jugador):
        self.jugadores.append(jugador)


    def read(self):
        resultado = ""
        for jugador in self.jugadores:
            resultado += jugador
            if jugador != self.jugadores[-1]:
                resultado += self.LIMITCHAR

        return resultado


    def update(self, jugador:Jugador, nombreJugador:str, deporteJugador):
        for i in self.jugadores:
            if i == jugador:
                jugador.update(nombreJugador, deporteJugador)
                break


    def delete(self, jugador:Jugador):
        for i in self.jugadores:
            if i == jugador:
                i.delete(jugador)
                break


    def load(self, data:str):
        jugadores = data.split(self.LIMITCHAR)
        for jugador in jugadores:
            self.jugadores.append(jugador)


    def __str__(self):
        return self.read()

    def __len__(self):
        return  self.jugadores.__len__()
    
    def __getitem__(self, index):
        return self.jugadores[index]
    
    def __setitem__(self, index, value):
        self.jugadores[index] = value

    def __delitem__(self, index):
        del self.jugadores[index]

    def __iter__(self):
        return self.jugadores.__iter__()
    
    def __next__(self):
        return self.jugadores.__next__()
    
    def __contains__(self, item):
        return item in self.jugadores
    
    def __eq__(self, other):
        return self.jugadores == other.jugadores
    
    def __ne__(self, other):
        return self.jugadores != other.jugadores
