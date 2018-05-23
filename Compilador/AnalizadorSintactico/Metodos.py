class Metodos:

    def __init__(self):
        print('Inicio')

    def Desplazamiento(self,tipo):
        n = ''
        contador = 0;
        for char in tipo:
            if contador > 0:
                n = n + char
            contador += 1
        return int(n)