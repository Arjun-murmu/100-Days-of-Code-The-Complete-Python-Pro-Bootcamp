name = "Arjun Murmu"
regd_no = '22020410'

class Car:
    def __init__(self, num_of_seats, speed):
        self.num_of_seats = num_of_seats
        self.speed = speed

    def drive(self):
        return f"The car is driving at {self.speed} km/h."

    def brake(self):
        return "The car is braking."


