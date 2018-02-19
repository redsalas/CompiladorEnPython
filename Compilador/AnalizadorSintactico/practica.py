import clasePila
import lexico

g1 = [  [2,0,0,1],
        [0,0,-1,0],
        [0,3,0,0],
        [4,0,0,0],
        [0,0,-2,0]]

g2 = [  [2,0,0,1],
        [0,0,-1,0],
        [0,3,-3,0],
        [2,0,0,4],
        [0,0,-2,0]]

entrada = 'a+b$'
continua = True

lex = lexico.Lexico(entrada)
lex.CadenaToArray()
pila = clasePila.Pila()

pila.apila(pila.regla("$"))
pila.apila(0)

print('Regla E -> <id> + <id>\n')
while continua:
    pila.imprime()
    lex.Sig()
    accion = g1[pila.tope()][pila.regla(lex.estado)]
    print('Entrada: ',lex.estado)
    print('Accion: ',accion)
    if accion > 0:
        pila.apila(pila.regla(lex.estado))
        pila.apila(accion)
    elif accion < 0:
        if accion == -2:
            for x in range(0,6):  #Longitud de la regla = (3*2) = 6
                pila.desapila()
            regla = g1[pila.tope()][3]
            pila.apila(3)
            pila.apila(regla)
        elif accion == -1:
            print('Acceptacion\n')
            continua = False
    else:
        print('Error\n')
        continua = False


continua = True
print('Regla E -> <id> + E | <id>\n')
entrada = 'c$'

pila.vaciar()

lex.setNuevo(entrada)
lex.CadenaToArray()

idRegla = [1,2]
lnRegla = [3,1]

pila.apila(pila.regla("$"))
pila.apila(0)

while continua:
    pila.imprime()
    lex.Sig()
    accion = g2[pila.tope()][pila.regla(lex.estado)]
    print('Entrada: ',lex.estado)
    print('Accion: ',accion)
    if accion > 0:
        pila.apila(pila.regla(lex.estado))
        pila.apila(accion)
    elif accion < 0:
        if accion == -3:
            rango = idRegla[1]*lnRegla[1];
            for x in range(0,rango):
                pila.desapila()
            regla = g2[pila.tope()][3]
            pila.apila(3)
            pila.apila(regla)
        elif accion == -2:
            rango = (idRegla[0]*lnRegla[0])*2;
            for x in range(0,rango):
                pila.desapila()
            regla = g2[pila.tope()][3]
            pila.apila(3)
            pila.apila(regla)
        elif accion == -1:
            print('Acceptacion')
            continua = False
    else:
        print('Error')
        continua = False