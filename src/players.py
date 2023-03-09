class Player:
    def __init__(self, name):
        self.name = name
    def answer(self, numOFMove, registry):
        if numOFMove == 1:
            return True

class Cheater(Player):

    def __init__(self):
        super().__init__('cheater')
    def answer(self, numOFMove, registry):
        return False

class Cooperator(Player):

    def __init__(self):
        super().__init__('cooperator')

    def answer(self, numOFMove, registry):
        return True

class Copycat(Player):

    def __init__(self):
        super().__init__('copycat')
        self.prevScore = 0
    def answer(self, numOFMove, registry):
        if numOFMove == 1:
            self.prevScore = registry[self.name]
            return True
        else:
            res = registry[self.name] - self.prevScore > 0
            self.prevScore = registry[self.name]
            return res

class Grudger(Player):

    def __init__(self):
        super().__init__('grudger')
        self.flagTrust = True
        self.prevScore = 0

    def answer(self, numOFMove, registry):
        if numOFMove == 1:
            self.flagTrust = True
            self.prevScore = registry[self.name]
            return True
        else:
            if self.flagTrust:
                res = registry[self.name] - self.prevScore >= 0
                self.prevScore = registry[self.name]
                if not res:
                    self.flagTrust = False
            return self.flagTrust


class Detective(Player):

    def __init__(self):
        super().__init__('detective')
        self.prevScore = 0
        self.IAmCopycat = False

    def answer(self, numOFMove, registry):

        if numOFMove == 1:
            self.IAmCopycat = False
        if numOFMove in [1, 3, 4]:
            if registry[self.name] - self.prevScore < 0:
                self.IAmCopycat = True
            res = True
        elif numOFMove == 2:
            res = False
        elif self.IAmCopycat:
            res = registry[self.name] - self.prevScore > 0
        else:
            return False
        self.prevScore = registry[self.name]
        return res

class MyBehaviorType(Player):
    def __init__(self):
        super().__init__('myBehaviorType')
        self.countLie = 0
        self.flagTrust = True
    def answer(self, numOFMove, registry):
        if numOFMove == 1:
            self.prevScore = 0
            self.countLie = 0
            self.flagTrust = True
            res =  True    
        else:
            if self.countLie > 0:
                res = registry[self.name] - self.prevScore > 0
                self.flagTrust = False
            else:
                if registry[self.name] - self.prevScore > 0:
                    self.countLie += 1
                res = True
        self.prevScore = registry[self.name]
        return res