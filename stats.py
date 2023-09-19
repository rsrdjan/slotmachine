class Stats:
    def __init__(self):
        self.straitDollars = 0
        self.straitAs = 0
        self.straitBs = 0
        self.straitCs = 0
        self.threeInRows = 0
        self.doubleOrNots = 0

    def incStrDols(self):
        self.straitDollars +=1
    
    def incStrAs(self):
        self.straitAs +=1
    
    def incStrBs(self):
        self.straitBs +=1
    
    def incStrCs(self):
        self.straitCs +=1
    
    def incThreeInRows(self):
        self.threeInRows +=1
    
    def incDoubleOrNots(self):
        self.doubleOrNots +=1