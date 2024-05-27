DIGITOS = ["0","1","2","3","4","5","6","7","8","9"]
class UtilidadString:
    #Cuando solo vamos a usar un método estático no hace falta constructor
    #Función que devuelva el número de dígitos de un string
    @staticmethod
    def contarDigitos(cadena:str) ->int:
        resultado = 0
        for car in range(0, len(cadena)):
            if cadena[car] in DIGITOS:
                resultado += 1
        return f"Hay: {resultado} dígitos"
    





if __name__== "__main__":
    def main():
        print(UtilidadString.contarDigitos("estoesly esto 2"))


    main()
