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


wizard1 = Wizard('mike', 80)
archer1 = Archer('jim', 100)
wizard1.attack()
archer1.attack()
