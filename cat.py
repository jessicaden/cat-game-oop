class Cat:
    # constructor
    # to create cat, need given name + given colour
    # self is cat we are creating
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour
        self.intelligence = 100
        self.energy = 75
        self.weight = 5
        self.age = 1

    def play(self):
        print(self.name,"is playing...")
        self.energy -= 5
        self.weight -= 0.5
        self.age += 0.1
    def train(self):
        print(self.name,"is training...")
        self.intelligence += 5
        self.energy -= 2
        self.weight -= 0.75
        self.age += 0.1
    def stats(self):
        print(self.name,"is showing stats...")
        print("cat's intelligence",self.intelligence)
        print(self.energy)
        print(self.weight)
        print(self.age)
    def feed(self):
        print(self.name,"is eating...")
        self.energy += 5
        self.weight += 1
        self.age += 0.1
    def sleep(self):
        print(self.name,"is sleeping...")
        self.energy += 7
        self.age += 0.1