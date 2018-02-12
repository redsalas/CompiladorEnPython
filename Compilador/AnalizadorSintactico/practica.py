import clasePila

s = [[0 for x in range(4)] for y in range(5)]
s[0][0] = 'd2'
s[0][1] = 'null'
s[0][2] = 'null'
s[0][3] = '1'

s[1][0] = 'null'
s[1][1] = 'null'
s[1][2] = 'r0'
s[1][3] = 'null'

s[2][0] = 'null'
s[2][1] = 'd3'
s[2][2] = 'null'
s[2][3] = 'null'

s[3][0] = 'd4'
s[3][1] = 'null'
s[3][2] = 'null'
s[3][3] = 'null'

s[4][0] = 'null'
s[4][1] = 'null'
s[4][2] = 'r1'
s[4][3] = 'null'

p = clasePila.Pila()
p.apila(2)
p.apila(0)
entrada = '0102'

#Leer entradas
for leer in entrada:
    p.imprime()
    print("Entrada, analizando: ",leer)
    estado = s[p.tope()][int(leer)]
    print("Salida: ",estado)
    if estado == 'd2':
        p.apila(int(leer))
        p.apila(2)
    elif estado == 'd3':
        p.apila(int(leer))
        p.apila(3)
    elif estado == 'd4':
        p.apila(int(leer))
        p.apila(4)
    elif estado == 'r1':
        print("E->ind+ind  Haciendo POP")
        for x in range(0,6):
            print("Se desapilo: ",p.desapila())
        estado = s[p.tope()][3]
        p.apila(3)
        p.apila(estado)
    elif estado == 'r0':
        print("Aceptacion")
        break
    else:
        print("pss nada")

#Fin de la cadena, leer de nuevo ultimo elemento de entrada
p.imprime()
print("Entrada, analizando: ",leer)
estado = s[p.tope()][int(leer)]
print("Salida: ",estado)
if estado == 'd2':
    p.apila(int(leer))
    p.apila(2)
elif estado == 'd3':
    p.apila(int(leer))
    p.apila(3)
elif estado == 'd4':
    p.apila(int(leer))
    p.apila(4)
elif estado == 'r1':
    for x in range(0,6):
        p.desapila()
    estado = s[p.tope()][3]
    p.apila(3)
    p.apila(estado)
elif estado == 'r0':
    print("Aceptacion")
else:
    print("pss nada")