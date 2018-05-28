class Metodos:

    def __init__(self):
        print('Inicio')

    def Desplazamiento(self,tipo):
        n = ''
        negativo = False
        contador = 0;
        for char in tipo:
            if char == 'r':
                negativo = True
            if contador > 0:
                n = n + char
            contador += 1
        if negativo:
            return int(n)*-1
        return int(n)

    def Reduccion(self,r):
        switcher = {
            'r2':2,
            'r10':6
        }
        return switcher.get(r,-1)

    def Regla(self,regla):
        switcher = {
            'r2':'<DEFINICIONES>',
            'r10':'<PARAMETROS>'
        }
        return switcher.get(regla,'<ERROR>')