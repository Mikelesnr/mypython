#!/usr/bin/python3

class PlayerCharacter: #class created
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

player1 = PlayerCharacter("Mike", 32) #instance of a class
player2 = PlayerCharacter("Tatenda", 23) #instance of a class

print(player1.name)
print(player2.age)