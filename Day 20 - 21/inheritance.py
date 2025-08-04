class animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale , exhale.")
class fish(animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("DOING THIS WATER")
    def swim(self):
        print("Moving in water.")

nemo = fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
