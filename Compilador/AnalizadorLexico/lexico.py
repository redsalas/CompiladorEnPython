lexico = __name__
class Lexico:
    fuente = str
    ind = 0
    cadena = []
    token = str
    estado = str
    tipo = str
    continua = bool

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


    def CadenaToArray(self):
        for letra in self.fuente:
            self.cadena.append(letra)
        self.c = self.cadena[self.ind]

    def EstadoSig(self):
        self.token = self.c
        self.ind += 1
        self.Automata()

    def Sig(self):
        if self.cadena[self.ind] == '$':
            self.continua = False
        elif "\n" in self.c or "\t" in self.c:
            self.ind += 1
            self.c = self.cadena[self.ind]
            self.continua = True
        elif self.c.isalpha():
            self.estado = self.TipoCadena(0)
            self.continua = False
            self.EstadoSig()
        elif self.c.isdigit():
            self.estado = self.TipoCadena(1)
            self.continua = False
            self.EstadoSig()
        elif self.c == '"':
            self.estado = self.TipoCadena(3)
            self.continua = False
            self.EstadoSig()
        elif self.c == '+' or self.c == '-':
            self.estado = self.TipoCadena(5)
            self.continua = False
            self.EstadoSig()
        elif self.c == '*' or self.c == '/':
            self.estado = self.TipoCadena(6)
            self.continua = False
            self.EstadoSig()
        elif self.c == '=':
            self.estado = self.TipoCadena(7)
            self.continua = False
            self.EstadoSig()
        elif self.c == '|':
            self.estado = self.TipoCadena(8)
            self.continua = False
            self.EstadoSig()
        elif self.c == '&':
            self.estado = self.TipoCadena(9)
            self.continua = False
            self.EstadoSig()
        elif self.c == ';':
            self.estado = self.TipoCadena(12)
            self.continua = False
            self.EstadoSig()
        elif self.c == ',':
            self.estado = self.TipoCadena(13)
            self.continua = False
            self.EstadoSig()
        elif self.c == '(':
            self.estado = self.TipoCadena(14)
            self.continua = False
            self.EstadoSig()
        elif self.c == '{':
            self.estado = self.TipoCadena(16)
            self.continua = False
            self.EstadoSig()
        else:
            self.estado = self.TipoCadena(-1)
            self.continua = False
            print("Programa terminado, estado de Error")

    def Automata(self):
        sigue = True
        while sigue:
            self.c = self.cadena[self.ind]
            if self.estado == "IDENTIFICADOR":
                if self.c.isalpha() or self.c.isdigit():
                    self.token = self.token + self.c
                    self.ind += 1
                elif '\n' in self.c or '\t ' in self.c:
                    sigue = False
                else:
                    sigue = False
            elif self.estado == "ENTERO":
                if self.c.isdigit():
                    self.token = self.token + self.c
                    self.ind += 1
                elif self.c == '.':
                    self.estado = self.TipoCadena(2)
                    self.token = self.token + self.c
                    self.ind += 1
                else:
                    sigue = False
                    break
            elif self.estado == "REAL":
                if self.c.isdigit():
                    self.token = self.token + self.c
                    self.ind += 1
                elif '\n' in self.c or '\t ' in self.c:
                    self.ind += 1
                    sigue = False
                else:
                    sigue = False
        print(self.token, " es ", self.estado)
        self.token = ""
        self.continua = True

#Leer
f = open("entrada.txt","r")
cadena = f.read()
f.close()

#Iniciar Automata
lex = Lexico(cadena)
lex.CadenaToArray()

while lex.continua:
    lex.Sig()



