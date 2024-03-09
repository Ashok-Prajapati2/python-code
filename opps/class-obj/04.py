class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car started")
        self.engine.start()

my_car = Car()
my_car.start()
