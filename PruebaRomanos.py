from romanos import romano_a_arabigo2, arabigo_a_romano, RomanError

eleccion = input("romano o arabigo: ")

numero = input("¿Que numero quieres transformar? ")

if eleccion == "romano":
    resultado = romano_a_arabigo2(numero)
    print(numero, "en numeros arabigos es", resultado)
if eleccion == "arabigo":
    num = int(numero)
    resultado = arabigo_a_romano(num)
    print(numero, "en numeros romanos es", resultado)