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

def arabigo_a_romano(n):

    if n <= 0:
        raise ValueError(f"{n} debe ser un entero positivo")
    
    romano = ""
    resto = 1
    
    while resto != 0:
        for simbolo, valor in numerosT:
            if n >= valor:
                
                break
            
        cociente = n // valor
        resto = n % valor
                
        romano += cociente * simbolo
        n = resto
        
        
        
    return romano

arabigo_a_romano(90)

def romano_a_arabigo(n):
    arabigo = ""
    pass