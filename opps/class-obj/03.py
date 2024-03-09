class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} is being destroyed")

obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

del obj1
print(obj2.name)

print(obj1.name)

