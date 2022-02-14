from romanos import arabigo_a_romano, romano_a_arabigo

class RomanNumber:
    def __init__(self, entrada):
        if isinstance(entrada, str):
            self.arabigo = romano_a_arabigo(entrada)
            self.romano = entrada
        elif isinstance(valor,int):
            self.romano = arabigo_a_romano(valor)
            self.arabigo = entrada
        else:
            pass