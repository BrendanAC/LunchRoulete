import random
class Roulette:
    totalUser=0p
    totalCoins=0

    def __init__(self):
     self.totalUsers+=1
     self.totalCoins+=self.getBaseCoins()
     self.BaseCoins=20
    def getBaseCoins(self):
        return self.BaseCoins
    def setBaseCoins(self,newVal):
        self.BaseCoins=newVal


class User(Roulette):
    def __init__(self):
        self.name=self.setName()
        self.coins=self.getBaseCoins()

    def setName(self):
        self.name=input('Please enter user name')

    def getName(self):
        return self.name


class gameManager(Roulette):
    def __init__(self):
        self.gameList=[self.totalUsers]
        self.index=0

    def start(self):
        winner=random.randint(0,self.getBaseCoins)
        self.index=0
        print(self.gameList[winner])

    def addToList(self,UserName):
        self.gameList.append(UserName)
        self.index+=1
