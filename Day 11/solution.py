with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()

# Klassen Monkey skal representere en ape med deres unike operator, liste over gjenstander
# divident, teller for antall inspeksjoner, gcd for dividentene for alle apene og 
# pekere til apene apen kaster til.
class Monkey:
    def __init__(self, id, items, operator, d):
        self.Id, self.Items = id, items
        self.Operator, self.Divider = operator, d
        self.Monkey1, self.Monkey2 = None, None
        self.Inspections = 0
        self.gcd = 0
    def addItems(self, item):
        self.Items.append(item)
    def addMonkeys(self, Monkey1, Monkey2):
        self.Monkey1, self.Monkey2 = Monkey1, Monkey2
    def shenanigans(self):
        for i in range(0, len(self.Items)):
            old = self.Items[i]
            # Kommenter ut de tre neste linkene for del 1 og inkluder linjen uner med "..//3"
            # For del to settes verdien til gjenstanden til lik x mod (gcd) dersom verdien er høyere enn gcd
            if old > self.gcd:
                old = old%self.gcd
            self.Items[i] = eval(self.Operator)
            #self.Items[i] = eval(self.Operator)//3
            if self.Items[i]%self.Divider == 0:
                self.Monkey1.addItems(self.Items[i])
            else:
                self.Monkey2.addItems(self.Items[i])
            self.Inspections += 1
        self.Items = []
    def setGcd(self, gcd):
        self.gcd = gcd

# Iterer over input og oppretter liste med aper. Pekere og gcd må beregnes og settes etter at Monkey-objekten 
# er blitt opprettet
monkeys = []
for i in range(0, len(input), 7):
    id = int(input[i].split(' ')[-1].replace(':', ''))
    items = [int(x) for x in input[i+1].split(':')[1].split(',')]
    operation = input[i+2].split(' = ')[-1]
    divider = int(input[i+3].split(' ')[-1])
    monkeys.append(Monkey(id, items, operation, divider))
for i in range(0, len(monkeys)):
    Monkey1,Monkey2 = int(input[i*7+4].split(' ')[-1]), int(input[i*7+5].split(' ')[-1])
    monkeys[i].addMonkeys(monkeys[Monkey1], monkeys[Monkey2])
gcd = 1
for m in monkeys:
    gcd *= m.Divider
for m in monkeys:
    m.setGcd(gcd)
# ---------------------------------------- Del 1 -------------------------------------------
# Simulerer 20 runder hvor funksjonen "shenanigangs" blir kjørt for hver ape.
# Linjene må kommenteres ut for del 2 da det simuleres på samme liste over Monkey-objekter
# og reglene er forskjellige.

#for i in range(0,20):
    #for m in monkeys:
        #m.shenanigans()

# Arrangere og sorterer antall inspeksjoner for de ulike apene og multipliserer de to største
inspections = sorted([m.Inspections for m in monkeys])
print(inspections[-1]*inspections[-2])

# ---------------------------------------- Del 2 -------------------------------------------
# Samme som i del 1. Del 1 må være kommentert ut for å få riktig svar.
for i in range(0,10000):
    for m in monkeys:
        m.shenanigans()

inspections = sorted([m.Inspections for m in monkeys])
print(inspections[-1]*inspections[-2])