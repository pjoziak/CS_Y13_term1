class Animal:
    def move(self):
        print('Move by 1 step')


class Cat(Animal):
    def move(self):
        print('Move by 3 step')


class Rodent(Animal):
    def move(self):
        print('Move by 2 step')


class Mouse(Rodent):
    pass


class Beaver(Rodent):
    def move(self):
        super(Rodent, self).move()


beaver = Beaver()
beaver.move()
















