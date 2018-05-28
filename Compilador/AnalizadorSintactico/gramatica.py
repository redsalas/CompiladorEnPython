import pandas
import clasePila
import lexico
import Metodos

datos = pandas.read_csv('compilador.csv')

m = Metodos.Metodos()

gramatica = datos.iloc[:,1:47].values

for i in range(95):
    for j in range(46):
        gramatica[i][j] = str(gramatica[i][j])
        if gramatica[i][j] == 'nan':
            gramatica[i][j] = 0

entrada = 'int main()$'
continua = True

lex = lexico.Lexico(entrada)
lex.CadenaToArray()
p = clasePila.Pila()

p.apila('$')
p.apila(0)

i = 0

while continua:
    p.imprime()
    lex.Sig()
    if lex.tab == False:
        accion = gramatica[p.tope()][p.regla(lex.estado)]
        print('Entrada: ',lex.estado)
        print('Accion: ',accion)
        if accion != 0:
            d = m.Desplazamiento(accion)
        if d > 0:
            p.apila(p.regla(lex.estado))
            p.apila(d)
        i += 1
        if i > 3:
            continua = False
