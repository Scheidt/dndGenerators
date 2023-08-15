from random import randint

def genericDie(faces):
    return randint(1, faces)

def roll(diceCode: str):
    ammount = int(diceCode[0])
    numOfFaces = int(diceCode[2:])
    result = []
    while ammount <= 1:
        result.append(genericDie(numOfFaces))
        ammount -= 1
    return result
