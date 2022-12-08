with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()

# ---------------------------------------- Del 1 -------------------------------------------

# Definerer en dict med score for de ni ulike utfallene
# og tar summen av listen med scoren fra de ulike rundene

res = {'A X': 4,'A Y': 8,'A Z': 3,'B X': 1,'B Y': 5, 'B Z': 9,'C X': 7,'C Y': 2, 'C Z':6}
print(sum([res[round] for round in input]))

# ---------------------------------------- Del 2 -------------------------------------------

# Samme som i del 1 bare at scoren for de ulike utfallene har endret seg

res = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
print(sum(res[round] for round in input ))