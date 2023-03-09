from game import Game 
from players import *

game1 = Game()

cheater = Cheater()
cooperator = Cooperator()
copycat = Copycat()
grudger = Grudger()
detective = Detective()
myBehaviorType = MyBehaviorType()

bufListOne = [cheater, cooperator, copycat,\
            grudger, detective]
for i, value in enumerate(bufListOne):
    j = 0
    while j < len(bufListOne) - 1 and bufListOne[i].name != bufListOne[j + 1].name:
        game1.play(bufListOne[i], bufListOne[j + 1])
        j += 1
game1.top3()
print()

game2 = Game()

bufListTwo = [cooperator, myBehaviorType, copycat,\
            grudger, detective]
for i, value in enumerate(bufListTwo):
    j = 0
    while j < len(bufListTwo) - 1 and bufListTwo[i].name != bufListTwo[j + 1].name:
        game2.play(bufListTwo[i], bufListTwo[j + 1])
        j += 1
game2.top3()
print()

game3 = Game()

bufListTwo = [cheater, myBehaviorType, copycat,\
            grudger, detective]
for i, value in enumerate(bufListTwo):
    j = 0
    while j < len(bufListTwo) - 1 and bufListTwo[i].name != bufListTwo[j + 1].name:
        game3.play(bufListTwo[i], bufListTwo[j + 1])
        j += 1
game3.top3()