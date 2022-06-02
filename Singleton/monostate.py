from datetime import datetime

class SingletonMonostate(object):
    __state = {}

    def __new__(cls, *args, **kwargs):
        print(*args, **kwargs)
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state
        return obj

m1 = SingletonMonostate()
m2 = SingletonMonostate()
m3 = SingletonMonostate()

print(f'm1 id: {id(m1)}')
print(m1.__dict__)
print(f'm1 id: {id(m2)}')
print(m2.__dict__)
print(f'm1 id: {id(m3)}')
print(m3.__dict__)

m2.name = 'Geraldo'
m2.id = 34825932
m3.time = datetime.now()

print(f'm1 id: {id(m1)}')
print(m1.__dict__)
print(f'm1 id: {id(m2)}')
print(m2.__dict__)
print(f'm1 id: {id(m3)}')
print(m3.__dict__)