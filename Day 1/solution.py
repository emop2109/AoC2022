with open('.\input.txt', 'r') as file:
    input_ = file.read().splitlines()

# Konverterer inputen til en liste med list av kalorier for hver enkelt alv    
input, dummy = [],[]
for line in input_:
    if line != '':
        dummy.append(int(line))
    else:
        input.append(dummy)
        dummy = []
input.append(dummy)

# Del 1
print(max([sum(elf) for elf in input]))

# Del 2
# Summerer kaloriene for hver enkelt alv og sorterer disse. sorted sorterer summene fra lavest til høyest.
# Tar til slutt summen av de tre høyeste(siste) i den sorterte listen av totalt antall kalorier per alv
print(sum(sorted([sum(elf) for elf in input])[:-3]))
