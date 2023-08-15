from random import randint

def genericDie(faces):
    return randint(1, faces)

def roll(diceCode: str):
    ammount, numOfFaces = map(int, diceCode.split('d'))
    result = []
    while ammount >= 1:
        result.append(genericDie(numOfFaces))
        ammount -= 1
    return result
