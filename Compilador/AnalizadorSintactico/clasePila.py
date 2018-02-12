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

    def imprime(self):
        print("Elementos en la Pila")
        for elemento in self.items:
            print(elemento,end='')
        print("")