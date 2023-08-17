table = '''01–50 	A
51–60 	B
61–70 	C
71–90 	D
91–94 	E
95–98 	F
99 	G
00 	H'''

lines = table.split('\n')
table = []
for line in lines:
    weight, item = line.split(' \t')
    if '–' in weight:
        weight = weight.split('–')
    else:
        weight = [weight]
    table.append({'weight': weight, 'name': item})
print(table)