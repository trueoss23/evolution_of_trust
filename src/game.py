from collections import Counter


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        if self.registry.get(player1.name) is None:
            self.registry[player1.name] = 0
        if self.registry.get(player2.name) is None:
            self.registry[player2.name] = 0
        i = 1
        while (i <= self.matches):
            one = player1.answer(i, self.registry)
            two = player2.answer(i, self.registry)
            if one and two:
                self.registry[player1.name] += 2
                self.registry[player2.name] += 2
            elif one and not two:
                self.registry[player1.name] -= 1
                self.registry[player2.name] += 3
            elif two and not one:
                self.registry[player1.name] += 3
                self.registry[player2.name] -= 1
            i += 1

    def top3(self):
        listValue = list(self.registry.values())
        listKey = list(self.registry.keys())
        for i in range(3):
            print(listKey[listValue.index(max(listValue))], max(listValue))
            listKey.remove(listKey[listValue.index(max(listValue))])
            listValue.remove(max(listValue))
