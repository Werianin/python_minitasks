class SingletonMeta(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


c1 = SingletonClass("42")
c2 = SingletonClass("I Hate 42")
print(c1 is c2)  # True
print(c1.value)  # 42
print(c2.value)  # 42


if __name__ == "__main__":
    import doctest

    doctest.testmod()
