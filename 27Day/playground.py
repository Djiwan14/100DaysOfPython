def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


print(add(1, 8, 9, 2, 7, 3))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=4)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("red")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.make)

