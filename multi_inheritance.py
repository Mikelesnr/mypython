#!/usr/bin/python3

class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with a power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.arrows = num_arrows

    def attack(self):
        print(f'attacking with {self.arrows} arrows')

    def check_arrows(self):
        print(f'{self.arrows} remaining')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard('mike', 80)
archer1 = Archer('jim', 100)

hb1 = HybridBorg("borgie", 80, 130)
print(hb1.check_arrows())
print(hb1.attack())
