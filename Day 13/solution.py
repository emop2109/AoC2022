import json, bisect
with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()

# ---------------------------------------- Del 1 -------------------------------------------
# Funksjonen sammenligner to-enkeltelmenter mot hverandre i samsvar med instruksjonene i 
# oppgavebeskrivelsen. Dersom det ene eller begge elementene er en liste konverteres elementet 
# til en liste om nødvendig og det itereres over listen og sammenligningen skjer rekursivt
def checkOrderElement(s1,s2):
    if type(s1) == int and type(s2) == int:
        if s1 < s2:
            return True
        elif s1 > s2:
            return False
        else:
            return None
    s1 = [s1] if type(s1) == int else s1
    s2 = [s2] if type(s2) == int else s2
    for i in range(0,len(s1)):
        if i == len(s2):
            return False
        q = checkOrderElement(s1[i],s2[i])
        if q is not None:
            return q
    return True if len(s1) < len(s2) else None

# Tar i mot listene for de ulike linjene og sammenligner element for element
def checkOrderList(s1,s2):
    for i in range(0,len(s1)):
        if i == len(s2):
            return False
        q = checkOrderElement(s1[i],s2[i])
        if q is not None:
            return q
    return True

# Benytter json.loads for å parse hver linje. Dersom checkOrderList returnerer
# True legger vi til par-indeksen i listen cnt. Printer så summen av listen cnt
cnt = []
for i in range(0,len(input), 3):
    s1,s2 = json.loads(input[i]), json.loads(input[i+1])
    if checkOrderList(s1,s2):
        cnt.append((i+3)//3)
print(sum(cnt))

# ---------------------------------------- Del 2 -------------------------------------------
# Generer en liste med alle de parsete linjene i input. Legger også til "[2]" og "[6]" 
# i listen.
lines = []
for i in range(0,len(input),3):
    s1,s2 = json.loads(input[i]), json.loads(input[i+1])
    lines.append(s1)
    lines.append(s2)
lines.append([2])
lines.append([6])

# Bruker en merg-sort algoritme med løsningen fra del 1 som betingelse for sorteringen
# for å sortere listen over linjer
def merge(left, right):
    results, i, n = [], 0, 0
    while len(left) and len(right):
        if checkOrderList(left[0], right[0]):
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    while len(left):
        results.append(left.pop(0))
    while len(right):
        results.append(right.pop(0))
    return results

def merge_sort(l):
    if len(l) == 1:
        return l
    left, right = l[:len(l)//2], l[len(l)//2:]
    left, right = merge_sort(left), merge_sort(right)

    return merge(left,right)

sortedList = merge_sort(lines)

# Itererer over den sorterte listen og legger til indeksene i listen som
# inneholder [2] eller [6] og printer produktet av disse.
cnt = []
for i in range(0,len(sortedList)):
    if sortedList[i] == [2] or sortedList[i] == [6]:
        cnt.append(i+1)
print(cnt[0]*cnt[1])