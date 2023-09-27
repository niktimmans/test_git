class Bird:


    type = 'Птица'

    def __init__(self, name):
        self.name = name
        self.age = 0
        print('Птица создана')

    def sing(self):
        print('Птица поет')

    def fly(self):
        pass

    def setAge(self, newAge):
        if(newAge >= 0):
            self.age = newAge
        else:
            print('Возраст не может быть отрицательным')

    def getAge(self):
        return self.age

class Penguin(Bird):

    def __init__(self, name):
        super().__init__(name)
        print('Пингвин создан')
        print('Имя пингвина ' + self.name)

    def sing(self):
        print('Пингвин по имени ' + self.name + ' поет')

    def swim(self):
        print('Пингвин по имени ' + self.name + ' плавает')

    def fly(self):
        print('Пингвин летать не умеет')

class Parrot(Bird):

    def __init__(self, name):
        super().__init__(name)

    def sing(self):
        print(self.name + ' поет ')

    def fly(self):
        print('Попугай по имени ' + self.name + ' летает')

def flying_test(bird):
    bird.fly()

kesha = Parrot('Кеша')
peggy = Penguin('Пегги')

print(kesha.name)
print(peggy.name)
print(kesha.type)
print(peggy.type)