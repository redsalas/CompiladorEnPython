ArbolSintactico = __name__
class node:
    def __init__(self,dato):
        self.izq = None
        self.der = None
        self.regla = dato

class Arbol:
    def __init__(self):
        self.root = None

    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.izq = self.insert(a.izq, dato)
            else:
                a.der = self.insert(a.der, dato)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.izq)
            print(a.dato)
            self.inorder(a.der)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.izq)
            self.preorder(a.der)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.izq)
            self.postorder(a.der)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.izq)
                else:
                    return self.buscar(dato, a.der)
