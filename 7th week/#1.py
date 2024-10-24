#1

class Garden:
    def __init__(self, species, age):
        self.age = age
        self.species=species
    def how_old(self):
        print(f'This {self.species} is {self.age} years old.')
        

class Harvestable_Garden(Garden):
    def __init__ (self, species, age, harvest):
        super().__init__ (species, age)
        self.harvest=harvest
    def reap(self):
        print(f'{self.harvest} fetuses were harvested from this {self.species}.')
    def what_is_it(self):
        print(f'This is {self.species}.')

birch = Garden('birch', 30)
apple = Harvestable_Garden('apple tree', 50, 100)
melon = Harvestable_Garden('melon', 1, 1)
apple.reap()
melon.what_is_it()
birch.how_old()
