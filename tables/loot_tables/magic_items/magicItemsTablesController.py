import json
from ....dice import *

tables = {'A': 'magic_items/tableA.json',
          'B': 'magic_items/tableB.json',
          'C': 'magic_items/tableC.json',
          'D': 'magic_items/tableD.json',
          'E': 'magic_items/tableE.json',
          'F': 'magic_items/tableF.json',
          'G': 'magic_items/tableG.json',
          'H': 'magic_items/tableH.json',
          'I': 'magic_items/tableJ.json'}

def roll_on_magic_table(letter: str):
    letter = letter.upper()
    table = tables[letter]
    with open(table, "r") as file:
        table = json.load(file)
    maxroll = str(table[-1]['weight'][-1])
    print(maxroll)
    result = roll('1d' + maxroll)
    print(result)
    for item in table:
        if len(item['weight']) == 2:
            if item['weight'][0] <= result <= item['weight'][1]:
                return result['name']
        else:
            if item['weight'][0] == result:
                return result['name']
    else:
        raise 'OutOfBoundError'

print(roll_on_magic_table('A'))