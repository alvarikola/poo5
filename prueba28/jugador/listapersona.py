from persona import Persona
class ListaPersona:
    LIMITCHAR = "|&&|"
    
    def __init__(self):
        self.personas = []


#Métodos CRUD
    
    def agregar(self, persona:Persona):
        self.personas.append(persona)


    def read(self):
        resultado = ""
        for persona in self.personas:
            resultado += persona
            if persona != self.personas[-1]:
                resultado += self.LIMITCHAR

        return resultado


    def update(self, persona:Persona, nombrePersona:str):
        for i in self.personas:
            if i == persona:
                persona.update(nombrePersona)
                break


    def delete(self, persona:Persona):
        for i in self.personas:
            if i == persona:
                i.delete(persona)
                break


    def load(self, data:str):
        personas = data.split(self.LIMITCHAR)
        for persona in personas:
            self.personas.append(persona)


    def __str__(self):
        return self.read()

    def __len__(self):
        return  self.personas.__len__()
    
    def __getitem__(self, index):
        return self.personas[index]
    
    def __setitem__(self, index, value):
        self.personas[index] = value

    def __delitem__(self, index):
        del self.personas[index]

    def __iter__(self):
        return self.personas.__iter__()
    
    def __next__(self):
        return self.personas.__next__()
    
    def __contains__(self, item):
        return item in self.personas
    
    def __eq__(self, other):
        return self.personas == other.personas
    
    def __ne__(self, other):
        return self.personas != other.personas

    
