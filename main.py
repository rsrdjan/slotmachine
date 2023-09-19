from machine import Machine
from os import system

def printRules():
    print("RULES:")
    print("-------------------------------------------------------------")
    print("$ $ $ $ - +200\t\tC C C C - +30")
    print("A A A A - +100\t\tTHREE IN A ROW - +15")
    print("B B B B - +50\t\tDOUBLE OR NOTHING - Every winning is doubled")
    print("-------------------------------------------------------------\n")
    

system('cls')
print("SLOT MACHINE v0.1 by Srdjan Rajcevic\n")
printRules()
print("How much money you want to invest? ", end='')
money = input()
print("Let's start the game! \n(Hit ENTER)")
input()
mach = Machine(money)

while mach.money.getMoney() > 0:
    system('cls')
    mach.roll()
    print("\n\nHit me again")
    input()

system('cls')
mach.printStats()
input()
