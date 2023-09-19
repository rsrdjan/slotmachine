import random
from money import Money
from time import sleep
from stats import Stats

class Machine:
    def __init__(self, money):
        self.list = ['A','B','C','$']
        self.slotA = 0
        self.slotB = 0
        self.slotC = 0
        self.slotD = 0
        self.money = Money(money)
        self.doubleOrNothing = False
        self.decreaseStep = 5
        self.stats = Stats()
    
    def printStats(self):
        print("Statistics:\n")
        print("$$$$ - ",self.stats.straitDollars)
        print("AAAA - ",self.stats.straitAs)
        print("BBBB - ",self.stats.straitBs)
        print("CCCC - ",self.stats.straitCs)
        print("Three in a row: ", self.stats.threeInRows)
        print("Double or nothing times played: ",self.stats.doubleOrNots,end='\n\n')
        print("Thank you for playing.")

    def check(self, row):
        if row == ['$','$','$','$']:
            self.stats.incStrDols()
            winning = 200
            print("ALL $!")
            if self.doubleOrNothing == True:
                self.money.increase(winning*2)
                self.doubleOrNothing = False
            else:
                self.money.increase(winning)
        elif row == ['A','A','A','A']:
            self.stats.incStrAs()
            winning = 100
            print("ALL As!")
            if self.doubleOrNothing == True:
                self.money.increase(winning*2)
                self.doubleOrNothing = False
            else: 
                self.money.increase(winning)
        elif row == ['B','B','B','B']:
            self.stats.incStrBs()
            winning = 50
            print("ALL Bs!")
            if self.doubleOrNothing == True:
                self.money.increase(winning*2)
                self.doubleOrNothing = False
            else:
                self.money.increase(winning)
        elif row == ['C','C','C','C']:
            self.stats.incStrCs()
            winning = 30
            print("ALL Cs!")
            if self.doubleOrNothing == True:
                self.money.increase(winning*2)
                self.doubleOrNothing = False
            else:
                self.money.increase(winning)
        elif (row[0] == row[1] == row[2]) or (row[-1] == row[-2] == row[-3]):
            self.stats.incThreeInRows()
            winning = 15
            print("THREE IN A ROW!")
            if self.doubleOrNothing == True:
                self.money.increase(winning*2)
                self.doubleOrNothing = False
            else:
                self.money.increase(winning)
        else:
            self.money.decrease(self.decreaseStep)
            self.decreaseStep = 5
            self.doubleOrNothing = False

    def dOrNothing(self):
        num = random.random()
        if num > 0.95:
            print("\n[------------ DOUBLE OR NOTHING! ------------]\n")
            print("You have a chance to DOUBLE your winning, but if you miss you are loosing -", end='')
            print(self.decreaseStep*2,end='\n\n')
            print("Do you want to play (y/n)?", end='')
            play = input()
            if play == 'y':
                self.stats.incDoubleOrNots()
                self.doubleOrNothing = True
                self.decreaseStep = self.decreaseStep*2
                print("Playing double or nothing: \n")
            else:
                print("\n")
                pass

    def roll(self):
        if self.money.getMoney() > 0:
            print("Money: ", end='')
            print(self.money.getMoney(), end=' | ')
            print("Loss per missed step: -", end='')
            print(self.decreaseStep, end="\n\n")

            row = [random.choice(self.list), random.choice(self.list), random.choice(self.list), random.choice(self.list)]
            self.dOrNothing()
            for letter in row:
                sleep(0.5)
                print(letter, end='    ', flush=True)
            print("\n")
            self.check(row)