# def add(*args):
#     # print(args)
#     # print(type(args))
#     # print([args])
#     print(args[2])
#     sum = 0
#     for n in args:
#         print(n)
#         sum += n
#     return sum
# # add(2,3,4,5)
# print(add(2,3,4,5))

# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
print(add(3, 5, 6, 2, 1, 7, 4, 3))
#
# def calculation(**keyword):
#     print(type(keyword))  #<class 'dict'>
#     print(keyword)  # {'add': 3, 'multiply': 5}
#     # for key,value in keyword.items():
#     #     print(key)
#     #     print(value)
#     print(keyword["add"])  # 3
#
# calculation(add=3,multiply=5)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]  #2+3 = 5
    n *= kwargs["multiply"] # 5*5 = 25
    print(n) # 25
calculate(2,add=3,multiply=5)

# class Car:
#     def __init__(self,**kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
# my_car = Car(make="Arjun",model="Suraj")
# # print(my_car) #<__main__.Car object at 0x000002FB66B56F90>
# print(my_car.make) #Arjun
# print(my_car.model)  #Suraj

# class Bike:
#     def __init__(self,**key):
#         self.model = key.get("model")
#         self.make = key.get("make")
#         self.investment = key.get("investment")
#
# my_bike = Bike(model="Arjun")
# print(my_bike.model) #Arjun
# print(my_bike.make) # None
#
# she_bike = Bike(make="B.R.H")
# print(she_bike.make) #B.R.H
# print(she_bike.model) # None

def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)