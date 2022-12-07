with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()
    input = [lines for lines in input]

# --------------------------------- Konvertering av input ----------------------------------
# Generere en liste over stacks med innholdet i hver kolonne
# Finner den første raden som ikke inneholder '[', j = høyden på den største kolonnen/stacken
for i in range(0,len(input[0])):
    if '[' not in input[i]:
        j = i
        break

# Generer en liste med like mange tomme lister som antall kolonner, hver kolonne inneholder
# fire tegn "[, X, ], 'whitespace'"
items = [[] for i in range(0,len(input[0])//4+1)]

# For hver stack legges inneholdet inn fra bunn og opp dersom innholdet ikke er et whitespace
for i in range(0,len(items)):
    for n in range(j-1,-1,-1):
        if(input[n][i*4+1] != ' '):
            items[i].append(input[n][i*4+1])

# Legger kommandoene inn i en egen liste
commands = [[int(lines.split(' ')[1]),int(lines.split(' ')[3]),int(lines.split(' ')[5])] for lines in input[j+2:]]

# Lager en kopi av listen med stacker da Del 1 og Del 2 skal ha samme utgangspunkt
items2 = items.copy()

# ---------------------------------------- Del 1 -------------------------------------------
# com-listen er på formen [x,y,z] hvor x er antall bokser, y er fra kolonne y og z er fra kolonne z
def moveItems(items, com):
    for i in range(0,com[0]):
        items[com[2]-1].append(items[com[1]-1].pop())

# listen med stackene blir kjørt gjennom moveItems for hver kommandolinje
for com in commands:
    moveItems(items, com)

print(f'Message: {[x[-1] for x in items]}')

# ---------------------------------------- Del 2 -------------------------------------------
def moveMultipleItems(items,com):
    items[com[2]-1].extend(items[com[1]-1][-com[0]:])
    items[com[1]-1] = items[com[1]-1][:-com[0]]

# listen med stackene blir kjørt gjennom moveMultipleItems for hver kommandolinje
for com in commands:
    moveMultipleItems(items2,com)

print(f'Message: {[x[-1] for x in items2]}')