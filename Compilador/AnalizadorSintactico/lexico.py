lexico = __name__
class Lexico:
    reservadas = {"int",
                  "float",
                  "string",
                  "double",
                  "bool",
                  "void"}

    fuente = str
    ind = 0
    cadena = []
    token = str
    estado = str
    tipo = str
    continua = bool
    tab = False

    def __init__(self,codigo): #Entrada
        self.fuente = codigo
        self.ind = 0

    def setNuevo(self,codigo):
        self.fuente = codigo
        self.ind = 0
        self.cadena = []

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
            23: "$"
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

    def Reservadas(self,palabra):
        continuar = True
        id = -1
        for i in range(19,23):
            if palabra == self.TipoCadena(i):
                id = i
                continuar = False
                break
        if continuar:
            for type in self.reservadas:
                if palabra == type:
                    id = 4
                    continuar = False
                    break
        return id

    def Sig(self):
        print("LEYENDO ",self.c)
        if self.cadena[self.ind] == '$':
            self.estado = self.TipoCadena(23)
            self.continua = False
            self.tab = False
        elif '\n' in self.c or '\t' in self.c or self.c.isspace():
            self.ind += 1
            self.c = self.cadena[self.ind]
            self.continua = True
            self.tab = True
        elif self.c.isalpha():
            self.estado = self.TipoCadena(0)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c.isdigit():
            self.estado = self.TipoCadena(1)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == '"':
            if self.estado == self.TipoCadena(3):
                self.ind += 1
                self.c = self.cadena[self.ind]
                self.continua = True
                self.tab = False
            else:
                self.estado = self.TipoCadena(3)
                self.continua = False
                self.tab = False
                self.EstadoSig()
        elif self.c == '+' or self.c == '-':
            self.estado = self.TipoCadena(5)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == '*' or self.c == '/':
            self.estado = self.TipoCadena(6)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == '<' or self.c == '>':
            self.estado = self.TipoCadena(7)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == '|':
            self.estado = self.TipoCadena(8)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == '&':
            if self.estado == self.TipoCadena(9):
                self.ind += 1
                self.c = self.cadena[self.ind]
                self.continua = True
                self.tab = False
            else:
                self.estado = self.TipoCadena(9)
                self.continua = False
                self.tab = False
                self.EstadoSig()
        elif self.c == '!':
            self.estado = self.TipoCadena(10)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == '=':
            if self.estado == self.TipoCadena(11):
                self.ind += 1
                self.c = self.cadena[self.ind]
                self.continua = True
                self.tab = False
            else:
                self.estado = self.TipoCadena(11)
                self.continua = False
                self.tab = False
                self.EstadoSig()
        elif self.c == ';':
            self.estado = self.TipoCadena(12)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == ',':
            self.estado = self.TipoCadena(13)
            self.continua = False
            self.EstadoSig()
        elif self.c == '(':
            self.estado = self.TipoCadena(14)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == ')':
            self.estado = self.TipoCadena(15)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == '{':
            self.estado = self.TipoCadena(16)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        elif self.c == '}':
            self.estado = self.TipoCadena(17)
            self.continua = False
            self.tab = False
            self.EstadoSig()
        else:
            self.estado = self.TipoCadena(-1)
            self.continua = False
            self.tab = False
            print("Programa terminado, estado de Error")

    def Automata(self):
        sigue = True
        while sigue:
            self.c = self.cadena[self.ind]
            if self.estado == self.TipoCadena(0):    #Identificador
                if self.c.isalpha() or self.c.isdigit():
                    self.token = self.token + self.c
                    self.ind += 1
                elif '\n' in self.c or '\t' in self.c or self.c.isspace():
                    sigue = False
                else:
                    sigue = False
            elif self.estado == self.TipoCadena(1):  #Entero
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
            elif self.estado == self.TipoCadena(2):  #Real
                if self.c.isdigit():
                    self.token = self.token + self.c
                    self.ind += 1
                elif '\n' in self.c or '\t' in self.c or self.c.isspace():
                    sigue = False
                else:
                    sigue = False
            elif self.estado == self.TipoCadena(3):    #Cadena
                if self.c != '"':
                    self.token = self.token + self.c
                    self.ind += 1
                elif '\n' in self.c:
                    self.estado = self.TipoCadena(-1)
                    sigue = False
                else:
                    self.token = self.token + self.c
                    #self.ind += 1
                    sigue = False
            elif self.estado == self.TipoCadena(5):  #OP suma/resta
                sigue = False
            elif self.estado == self.TipoCadena(6):  #OP mul/dividir
                sigue = False
            elif self.estado == self.TipoCadena(7):   #OP Relacion
                if self.c == '=':
                    self.token = self.token + self.c
                    self.ind += 1
                    sigue = False
                else:
                    sigue = False
            elif self.estado == self.TipoCadena(8):   #OP or
                if self.c != '|':
                    self.estado = self.TipoCadena(-1)
                    self.ind += 1
                    sigue = False
                else:
                    self.token = self.token + self.c
                    self.ind += 1
                    sigue = False
            elif self.estado == self.TipoCadena(9):   #OP and
                if self.c != '&':
                    self.estado = self.TipoCadena(-1)
                    self.ind += 1
                    sigue = False
                else:
                    self.token = self.token + self.c
                    self.ind += 1
                    sigue = False
            elif self.estado == self.TipoCadena(10):   #OP not
                if self.c == '=':
                    self.estado = self.TipoCadena(11)
                else:
                    sigue = False
            elif self.estado == self.TipoCadena(11):   #OP igualdad
                if self.c == '=':
                    self.token = self.token + self.c
                    self.ind += 1
                    sigue = False
                else:
                    self.estado = self.TipoCadena(18)
            elif self.estado == self.TipoCadena(12):   #Punto y Coma
                sigue = False
            elif self.estado == self.TipoCadena(13):   #Coma
                sigue = False
            elif self.estado == self.TipoCadena(14):   #LParentesis
                sigue = False
            elif self.estado == self.TipoCadena(15):   #RParentesis
                sigue = False
            elif self.estado == self.TipoCadena(16):   #L Llave
                sigue = False
            elif self.estado == self.TipoCadena(17):   #R Llave
                sigue = False
            elif self.estado == self.TipoCadena(18):   #Igual
                sigue = False
        id = self.Reservadas(self.token)
        if self.token == 'E':
            self.estado = 'E'
            print(self.token, " \tes ", self.estado)
        elif id != -1:
            self.estado = self.TipoCadena(id)
            print(self.token, " \tes ",self.TipoCadena(id))
        else:
            print(self.token, " \tes ", self.estado)
        self.token = ""
        self.continua = True