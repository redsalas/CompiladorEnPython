class Lexico:
    fuente = str
    ind = int
    continua = bool
    cadena = []
    c = str
    estado = str
    tipo = str

    def __init__(self,codigo): #Entrada
        self.fuente = codigo
        self.ind = 0

    def TipoCadena(self,tipo):
        switcher = {
            0: "IDENTIFICADOR",
            1: "ENTERO",
            2: "REAL",
            3: "CADENA",
            4: "TIPO",
            5: "OPSUMA",
            6: "OPMUL",
            7: "OPRELAC",
            8: "OPOR",
            9: "OPAND",
            10: "OPNOT",
            11: "OPIGUALDAD",
            12: ";",
            13: ",",
            14: "(",
            15: ")",
            16: "{",
            17: "}",
            18: "=",
            19: "if",
            20: "while",
            21: "return",
            22: "else",
            23: "$",
        }
        return switcher.get(tipo,"Error")

    def Leer(self):
        self.c = self.cadena[self.ind]
        self.Evaluar(self.c)

    def Evaluar(self,c):
        if c.isalpha():
            self.estado = self.TipoCadena(0)
        elif c.isdigit():
            self.estado = self.TipoCadena(1)
        elif c == "+" or c == "-":
            self.estado = self.TipoCadena(5)
        elif c == "*" or c == "/":
            self.estado = self.TipoCadena(6)
        elif c == "<" or c == ">":
            self.estado = self.TipoCadena(7)
        elif c == "|":
            self.estado = self.TipoCadena(8)
        elif c == "&":
            self.estado = self.TipoCadena(9)
        elif c == "!":


    def CadenaToArray(self):
        for letra in self.fuente:
            self.cadena.append(letra)


    def Automata(self):
        if self.estado == "IDENTIFICADOR":
            if self.cadena





f = open("entrada.txt","r")
cadena = f.read()
f.close()
lex = Lexico(cadena)

