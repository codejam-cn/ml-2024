class MyClass:
    def __init__(self, x):
        super().__init__()
        self.x = x

    def add(self, item):
        return self.x + item.x


myclass = MyClass(1)
myclass2 = MyClass(20)

c = myclass.add(myclass2)

print(c)
