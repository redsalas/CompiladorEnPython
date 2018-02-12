import lexico

#Leer
f = open("entrada.txt","r")
cadena = f.read()
f.close()

#Iniciar Automata
lex = lexico.Lexico(cadena)
lex.CadenaToArray()
print(lex.cadena)

while lex.continua:
    lex.Sig()