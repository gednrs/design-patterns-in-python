from abc import ABCMeta, abstractmethod


# Abstract Factory
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass

    @abstractmethod
    def criar_pizza(self):
        pass


#Concret Factory B
class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaCamarao()


#Concret Factory B
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocoli()

    def criar_pizza(self):
        return PizzaBolonha()


#Abstract Produto A
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, pizzaVeg):
        pass


#Abstract Produto B
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, pizzaVeg):
        pass


#Produto Concreto
class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')


#Produto Concreto
class PizzaCamarao(Pizza):

    def servir(self, pizzaveg):
        print(f'{type(self).__name__} é servida com camarao na {type(pizzaveg).__name__}')


#Produto Concreto
class PizzaBrocoli(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')


#Produto Concreto
class PizzaBolonha(Pizza):

    def servir(self, pizzaveg):
        print(f'{type(self).__name__} é servida com bolonha na {type(pizzaveg).__name__}')


# Cliente
class Pizzaria:
    
    def fazer_pizza(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg()
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)


pizzaria = Pizzaria()
pizzaria.fazer_pizza()
