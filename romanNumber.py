from romanos import RomanError, arabigo_a_romano, romano_a_arabigo

class RomanNumber:
    def __init__(self, entrada):
        if isinstance(entrada, str):
            self.arabigo = romano_a_arabigo(entrada)
            self.romano = entrada
        elif isinstance(entrada,int):
            self.romano = arabigo_a_romano(entrada)
            self.arabigo = entrada
        else:
            raise TypeError("La entrada tiene que ser entero o cadena")
    
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self.romano

    def __eq__(self,entrada): #Igual Que
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return self.arabigo == entrada.arabigo
    
    def __ne__(self,entrada): #Distinto Que
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return self.arabigo != entrada.arabigo
    
    def __gt__(self,entrada): #Mayor Que
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return self.arabigo > entrada.arabigo
    
    def __ge__(self, entrada): #Mayor o Igual
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return self.arabigo >= entrada.arabigo

    def __lt__(self, entrada): #Menor Que
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return self.arabigo < entrada.arabigo

    def __le__(self, entrada): #Menor o Igual
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return self.arabigo <= entrada.arabigo

    def __sub__(self, entrada): #Resta
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        elif (self.arabigo - entrada.arabigo) < 0:
            return RomanError("No se aceptan resultados negativos")
        else:
            return RomanNumber(self.arabigo - entrada.arabigo)

    def __add__(self, entrada): #Suma
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return RomanNumber(self.arabigo + entrada.arabigo)

    def __floordiv__(self, entrada): #Division
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return RomanNumber(self.arabigo // entrada.arabigo)

    def __mul__(self, entrada): #Multiplicacion
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return RomanNumber(self.arabigo * entrada.arabigo)

    def __pow__(self, entrada): #Exponencial
        if not isinstance(entrada, RomanNumber):
            raise TypeError("entrada tiene que ser romano")
        return RomanNumber(self.arabigo ** entrada.arabigo)