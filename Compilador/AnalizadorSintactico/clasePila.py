clasePila = __name__
class Pila:
    value = int

    def __init__(self):
        self.items = []

    def apila(self,x):
        self.items.append(x)

    def desapila(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")

    def tope(self):
        self.value = int(self.items[-1])
        return (self.value)

    def isEmpty(self):
        return self.items == []

    def vaciar(self):
        while not self.isEmpty():
            self.desapila()

    def imprime(self):
        print("Elementos en la Pila")
        for elemento in self.items:
            print(elemento,end='->')
        print("")

    def regla(self,tipo):
        switcher = {
            "IDENTIFICADOR":0,
            "ENTERO":1,
            "REAL":2,
            "CADENA":3,
            "TIPO":4,
            "OPSUMA":5,
            "OPMUL":6,
            "OPRELAC":7,
            "OPOR":8,
            "OPAND":9,
            "OPNOT":10,
            "OPIGUALDAD":11,
            ";":12,
            ",":13,
            "(":14,
            ")":15,
            "{":16,
            "}":17,
            "=":18,
            "if":19,
            "while":20,
            "return":21,
            "else":22,
            "$":23,
            "PROGRAMA":24,
            "DEFINICIONES":25,
            "DEFINICION":26,
            "DEFVAR":27,
            "LISTAVAR":28,
            "DEFFUNC":29,
            "PARAMETROS":30,
            "LISTAPARAM":31,
            "BLOQFUNC":32,
            "DEFLOCALES":33,
            "DEFLOCAL":34,
            "SENTENCIAS":35,
            "SENTENCIA":36,
            "OTRO":37,
            "BLOQUE":38,
            "VALORREGRESA":39,
            "ARGUMENTOS":40,
            "LISTAARGUMENTOS":41,
            "TERMINO":42,
            "LLAMADAFUNC":43,
            "SENTENCIABLOQUE":44,
            "EXPRESION":45
        }
        return switcher.get(tipo,"-1")