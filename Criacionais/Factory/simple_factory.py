from abc import ABCMeta, abstractmethod 

class Framework(metaclass=ABCMeta):
    @abstractmethod
    def linguagem(self):
        pass

class Django(Framework):
    def linguagem(self):
        print('Python')

class NodeJs(Framework):
    def linguagem(self):
        print('Javascript')

class Rails(Framework):
    def linguagem(self):
        print('Ruby')

#Factory
class Factory:
    def create_framework(self, tipo):
        return eval(tipo)().linguagem()


if __name__ == '__main__':
    factory = Factory()
    framework = input('Framework [Django, NodeJs, Rails]: ')
    factory.create_framework(framework)

