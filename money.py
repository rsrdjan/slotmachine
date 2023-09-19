class Money:
    def __init__(self, money):
        self.money = int(money)
    
    def increase(self, inc):
        self.money = self.money + inc
    
    def decrease(self, step):
        self.money = self.money - step
    
    def getMoney(self):
        return int(self.money)
    
    def setMoney(self, money):
        self.money = money