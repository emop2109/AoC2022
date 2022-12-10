with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()

# ---------------------------------------- Del 1 -------------------------------------------

# Lager en liste med verdien til X for hver endt sykel. Første verdi er initialverdien til X
cycleVal = [1]
for line in input:
    if line == 'noop':
        cycleVal.append(cycleVal[-1])
    else:
        cycleVal.append(cycleVal[-1])
        cycleVal.append(cycleVal[-1]+int(line.split(' ')[1]))

print(sum([(i+1)*cycleVal[i] for i in range(19,220, 40)]))

# ---------------------------------------- Del 2 -------------------------------------------

# Iterer over hver pixel i hver linje av CRT'n og benytter listen over X verdiene beregnet i 
# del 1
msg = ''
for i in range(0,6):
    for n in range(0,40):
        if cycleVal[i*40+n] in [n-1, n, n+1]:
            msg += '#'
        else:
            msg += '.'
    msg += '\n'

print(msg)