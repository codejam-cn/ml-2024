class MyClass:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y


myclass = MyClass(1, 2)

c = myclass.add()

print(c)
