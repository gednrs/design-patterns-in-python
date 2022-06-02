class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


s1 = Singleton()
s2 = Singleton()
s3 = Singleton()

print(id(s1))
print(id(s2))
print(id(s3))
