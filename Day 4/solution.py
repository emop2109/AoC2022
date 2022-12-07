with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()

# Konverterer inputen til en liste hvor hver linje er en liste på formen [x1,y1,x2,y2]
input = [[int(n) for n in line.replace(',','-').split('-')] for line in input]

# Del 1

# Definerer en funksjon som returnerer 1 dersom linjen inneholder et fullstendig overlappet intervall
def fullyContained(line):
    if (line[0] >= line[2] and line[1] <= line[3]) or (line[2] >= line[0] and line[3] <= line[1]):
        return 1
    else:
        return 0
# Summerer listen med resultat fra fullyContained for hver linje i input
print(sum([fullyContained(line) for line in input]))

# Del 2

# Samme som over, men sjekker kun om det finnes tall i det første intervall som også finnes i det andre
def partlyContained(line):
    set1, set2 = range(line[0],line[1]+1), range(line[2],line[3]+1)
    if any(True if x in set2 else False for x in set1):
        return 1
    else:
        return 0
# Summerer listen med resultat fra partlyContained for hver linje i input
print(sum([partlyContained(line) for line in input]))