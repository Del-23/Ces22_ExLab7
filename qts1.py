class Pizza: #componente
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Massa(Pizza): #ComponenteConcreto
    cost = 0.0
    def getDescription(self):
        return 'Massa fina'
   
class Decorator(Pizza): #Decorador
    def __init__(self, pizza):
        self.component = pizza
    
    def getTotalCost(self):
        return self.component.getTotalCost() + Pizza.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + Pizza.getDescription(self)

class Mozzarela(Decorator): #DecoradorConcretoA
    cost = 10.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Catupiry(Decorator): #DecoradorConcretoB
    cost = 10.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Calabresa(Decorator): #DecoradorConcretoC
    cost = 20.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Frango(Decorator): #DecoradorConcretoD
    cost = 20.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Parmesao(Decorator): #DecoradorConcretoE
    cost = 10.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

FrangoComCatupiry = Catupiry(Frango(Massa()))
print(FrangoComCatupiry.getDescription() + ': $' + str(FrangoComCatupiry.getTotalCost()))
TresQueijos = Mozzarela(Catupiry(Parmesao(Massa())))
print(TresQueijos.getDescription() + ': $' + str(TresQueijos.getTotalCost()))
