numerosT = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)    
    
]

class RomanError(Exception):
    pass

def valida_numero(n):
    if not isinstance(n, int):
        raise TypeError(f"{n} debe ser de tipo int")

    if n <= 0:
        raise ValueError(f"{n} debe ser un entero positivo")

def arabigo_a_romano(n):
    valida_numero(n)
    romano = ""
    resto = None
    if n > 3999:
        romano += "("
        romano += arabigo_a_romano(n//1000)
        n = n % 1000
        romano +=")"
    while resto != 0:
        for simbolo, valor in numerosT:
            if n >= valor:
                break
        cociente = n // valor
        resto = n % valor
        romano += cociente * simbolo
        n = resto    
    return romano


valores_romanos = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

simbolos_romanos = {
    "I"  : 1,
    "IV" : 4,
    "V"  : 5,
    "IX" : 9,
    "X"  : 10,
    "XL" : 40,
    "L"  : 50,
    "XC" : 90,
    "C"  : 100,
    "CD" : 400,
    "D"  : 500,
    "CM" : 900,
    "M"  : 1000
}

def valida_str(cadena):
    if not isinstance(cadena, str):
        raise TypeError(f"{cadena} debe ser de tipo str")
    if cadena != cadena.upper():
        raise RomanError(f"{cadena} debe escribirse en mayusculas")
    caracteres_validos = ["M","D","C","L","X","V","I"]
    for caracter in cadena:
        if caracter not in caracteres_validos:
            raise RomanError(f"{caracter} no es un caracter valido en los numeros romanos")

def listaValores(n):
    listaValores = []
    for caracter in n:
        for simbolo, valor in numerosT:
            if caracter == simbolo:
                caracter = valor
                listaValores.append(caracter)
                break
    return listaValores

def valida_repeticiones(cadena):
    caracter1 = "n"
    caracter2 = "n"
    caracter3 = "n"
    for caracter in cadena:
        if caracter == caracter1 and caracter == caracter2 and caracter == caracter3:
            raise RomanError(f"{cadena} no puede tener cuatro caracteres iguales consecutivos")
        if caracter in "VLD" and caracter == caracter1:
            raise RomanError(f"{caracter} no puede repetirse de forma consecutiva")
        caracter3 = caracter2
        caracter2 = caracter1
        caracter1 = caracter

def valida_resta(cadena):
    lista = listaValores(cadena)
    numeroPreanterior = 1002
    numeroAnterior = 1001
    for numero in lista:
        if numero > numeroAnterior and numeroAnterior in (5,50,500):
            raise RomanError("V, L, y D no pueden utilizarse para restar")
        if numero > numeroAnterior and numeroAnterior == numeroPreanterior:
            raise RomanError(f"{numeroAnterior} no puede repetirse restando")
        if numero > numeroAnterior and numeroAnterior in (1,10,100):
            if numeroAnterior == 1 and numero not in (5,10):
                raise RomanError("I solo puede restar a V y X")
            if numeroAnterior == 10 and numero not in (50,100):
                raise RomanError("X solo puede restar a L y C")
            if numeroAnterior == 100 and numero not in (500,1000):
                raise RomanError("C solo puede restar a D y M")
        numeroPreanterior = numeroAnterior
        numeroAnterior = numero

def romano_a_arabigo(cadena):
    valida_str(cadena)
    valida_repeticiones(cadena)
    valida_resta(cadena)
    arabigo = 0
    lista = listaValores(cadena)
    numeroAnterior = 1001
    for numero in lista:
        if numero <= numeroAnterior:
            arabigo += numero
        elif numero > numeroAnterior:
            arabigo -= numeroAnterior
            arabigo += (numero - numeroAnterior)
        numeroAnterior = numero
    return arabigo
    
def romano_a_arabigo2(cadena):
    valida_str(cadena)
    valida_repeticiones(cadena)
    valida_resta(cadena)
    resultado = 0

    for ix in range(len(cadena)-1):
        letra = cadena[ix]
        siguiente = cadena[ix + 1]
        if simbolos_romanos[letra] >= simbolos_romanos[siguiente]:
            resultado += simbolos_romanos[letra]
        else:
            resultado -= simbolos_romanos[letra]

    resultado += simbolos_romanos[cadena[-1]]
    return resultado

print("Romano a arabigo: ",romano_a_arabigo2("XIII"),"\nArabigo a romano: ",arabigo_a_romano(13),"\nArabigo a romano +4000: ",arabigo_a_romano(7789))