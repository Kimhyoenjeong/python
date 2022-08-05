from random import randrange

class FunnyDice:
    def __init__(self, n=6):
        self.n = int(n)
        self.numbers = list(range(1, n+1))
        self.index = randrange(0, self.n)
        self.val = self.numbers[self.index]

    def throw(self):
        self.index = randrange(0, self.n)
        self.val = self.numbers[self.index]

    def getval(self):
        return self.val

    def setval(self, val):
        if val <= self.n:
            self.val = val
        else:
            msg = "dice has not number. dice has 1 to {0}".format(self.n)
            raise ValueError(msg)
def get_inputs():
    n=int(input("input dice number"))
    return n

def main():
    n = get_inputs()
    mydice = FunnyDice(n)
    mydice.throw()
    print("행운의 숫자는?{}".format(mydice.getval()))


main()
    
