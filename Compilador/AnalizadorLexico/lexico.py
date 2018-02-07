lexico = __name__
class Lexico:
    fuente = str
    ind = 0
    cadena = []
    token = str
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


    def CadenaToArray(self):
        for letra in self.fuente:
            self.cadena.append(letra)
        self.c = self.cadena[self.ind]

    def Inicio(self):
        if self.c.isalpha():
            self.estado = self.TipoCadena(0)
        elif self.c.isdigit():
            self.estado = self.TipoCadena(1)
        elif self.c == '"':
            self.estado = self.TipoCadena(3)
        elif self.c == '+' or self.c == '-':
            self.estado = self.TipoCadena(5)
        elif self.c == '*' or self.c == '/':
            self.estado = self.TipoCadena(6)
        elif self.c == '=':
            self.estado = self.TipoCadena(7)
        elif self.c == '|':
            self.estado = self.TipoCadena(8)
        elif self.c == '&':
            self.estado = self.TipoCadena(9)
        elif self.c == ';':
            self.estado = self.TipoCadena(12)
        elif self.c == ',':
            self.estado = self.TipoCadena(13)
        elif self.c == '(':
            self.estado = self.TipoCadena(14)
        elif self.c == '{':
            self.estado = self.TipoCadena(16)
        elif "\n" in self.c:
            self.SaltoEspacio()
        else:
            self.estado = self.TipoCadena(-1)
        self.token = self.c
        self.ind += 1

    def SaltoEspacio(self):
        self.ind += 1
        self.c = self.cadena[self.ind]
        self.Sig()

    def Sig(self):
        if self.c.isalpha():
            self.estado = self.TipoCadena(0)
        elif self.c.isdigit():
            self.estado = self.TipoCadena(1)
        elif self.c == '"':
            self.estado = self.TipoCadena(3)
        elif self.c == '+' or self.c == '-':
            self.estado = self.TipoCadena(5)
        elif self.c == '*' or self.c == '/':
            self.estado = self.TipoCadena(6)
        elif self.c == '=':
            self.estado = self.TipoCadena(7)
        elif self.c == '|':
            self.estado = self.TipoCadena(8)
        elif self.c == '&':
            self.estado = self.TipoCadena(9)
        elif self.c == ';':
            self.estado = self.TipoCadena(12)
        elif self.c == ',':
            self.estado = self.TipoCadena(13)
        elif self.c == '(':
            self.estado = self.TipoCadena(14)
        elif self.c == '{':
            self.estado = self.TipoCadena(16)
        elif "\n" in self.c:
            self.SaltoEspacio()
        else:
            self.estado = self.TipoCadena(-1)
        self.token = self.c
        self.ind += 1
        while True:
            self.Automata()

    def Automata(self):
        self.c = self.cadena[self.ind]
        if self.estado == "IDENTIFICADOR":
            if self.c.isalpha() or self.c.isdigit():
                self.token = self.token + self.c
                self.ind += 1
            else:
                print(self.token," es ",self.estado)
                self.token = ""
                self.Sig()
        elif self.estado == "ENTERO":
            if self.c.isdigit():
                self.token = self.token + self.c
                self.ind += 1
            elif self.c == '.':
                self.estado = self.TipoCadena(2)
            else:
                print(self.token," es ",self.estado)
                self.token = ""
                self.Sig()
#Leer
f = open("entrada.txt","r")
cadena = f.read()
f.close()
#Iniciar Automata
lex = Lexico(cadena)
lex.CadenaToArray()
#lex.Inicio()

while lex.ind < len(lex.cadena):
    lex.Sig()



