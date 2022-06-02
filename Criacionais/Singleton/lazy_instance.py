class SingletonLazy(object):
    _instance = None

    def __init__(self):
        if not SingletonLazy._instance:
            print('O método __init__ foi chamado')
        else:
            print(f'Instancia criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = SingletonLazy()
        return cls._instance

s1 = SingletonLazy()

print(f'Objeto criado agora: {SingletonLazy.get_instance()}')

s2 = SingletonLazy()

print(id(s1))
print(id(s2))