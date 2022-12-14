with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()
input = [[[int(x) for x in xy.split(',')] for xy in line.split(' -> ')] for line in input]

# Generer en liste med startpunkter x,y og en retningsvektor vx, vy
# Finner også max verdiene i x og y retning
vectors, max_x, max_y = [], 0, 0
for i in range(0, len(input)):
    v = []
    for j in range(1, len(input[i])):
        vx, vy = input[i][j][0]-input[i][j-1][0], input[i][j][1]-input[i][j-1][1]
        v.append([input[i][j-1][0], input[i][j-1][1], vx, vy])
        max_x = input[i][j][0] if input[i][j][0] > max_x else max_x
        max_y = input[i][j][1] if input[i][j][1] > max_y else max_y
    vectors.append(v)
# Generer en grid 
grid = [['.' for i in range(0,max_x+1000)] for n in range(0,max_y+2)]

# Funksjonen tenger # basert på linjene i vektor listen
def drawRock(grid, v):
    if v[2] == 0:
        if v[3] < 0:
            for i in range(v[1], v[1]+v[3]-1,-1):
                grid[i][v[0]] = '#'
        else:
            for i in range(v[1], v[1]+v[3]+1):
                grid[i][v[0]] = '#'
    else:
        if v[2] < 0:
            for i in range(v[0], v[0]+v[2]-1,-1):
                grid[v[1]][i] = '#'
        else:
            for i in range(v[0], v[0]+v[2]+1):
                grid[v[1]][i] = '#'

# Tegner alle # som finnes i inputen
for vec in vectors:
    for v in vec:
        drawRock(grid, v)

# Funksjonen finner hvilestedet for hvert sandkorn rekursivt. arg=void er er for del 1 hvor
# sandkornet vil falle i evigheten.
def sandMove(grid, pos, arg='void'):
    if pos[1] + 1 == len(grid):
        if arg == 'void':
            return False
        else:
            grid[pos[1]][pos[0]] = 'o'
            return True
    else:
        if grid[pos[1] + 1][pos[0]] != 'o' and grid[pos[1] + 1][pos[0]] != '#':
            return sandMove(grid, [pos[0], pos[1] + 1], arg)
        elif grid[pos[1] + 1][pos[0] - 1] != 'o' and grid[pos[1] + 1][pos[0] - 1] != '#':
            return sandMove(grid, [pos[0] - 1, pos[1] + 1], arg)
        elif grid[pos[1] + 1][pos[0] + 1] != 'o' and grid[pos[1] + 1][pos[0] + 1] != '#':
            return sandMove(grid, [pos[0] + 1, pos[1] + 1], arg)
        else:
            grid[pos[1]][pos[0]] = 'o'
            return True
# ---------------------------------------- Del 1 -------------------------------------------
# Teller antall sandkorn som må til før neste sandkorn faller i evigheten
cnt = 0
while sandMove(grid, [500, 0]):
    cnt += 1
print(cnt)

# Funksjon som skriver en figur av sandkornenes bevegelse
msg = ''
grid[0][500] = '+'
for i in range(0, len(grid)):
    for j in range(450, 511):
        msg += grid[i][j]
    msg += '\n'
with open('.\output.txt', 'w') as file:
    file.write(msg)

# ---------------------------------------- Del 2 -------------------------------------------
# Teller antall sandkorn som må til før et sandkorn finner hvilestedet sitt i (500,0)
cnt = 0
while grid[0][500] != 'o':
    sandMove(grid, [500, 0], arg='NoVoid')
    cnt += 1
print(cnt)


