from random import randint

def genericDie(faces):
    return randint(1, faces)

# This may look stupid programming-wise, but in the game different dice are refered as 'x'd'y', where
# 'x' is the amount of dice to be rolled
# 'y' is the amount of faces those dices have
# so if I write 3d12, I'm rolling 3 twelve-faced dice
# writing the code this way makes it so it is closer to the game.
def d2():
    return genericDie(2)

def d4():
    return genericDie(4)


def d6():
    return genericDie(6)


def d8():
    return genericDie(8)


def d10():
    return genericDie(10)


def d12():
    return genericDie(12)


def d20():
    return genericDie(20)


def d100():
    return genericDie(100)

