with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()
input = [[[int(n) for n in x.split(',')]for x in line.split(' -> ')] for line in input]
vectors, max_x, max_y = [], 0, 0
for i in range(0,len(input)):
    v = []
    for j in range(1,len(input[i])):
        v.append([input[i][j-1][0], input[i][j-1][1],input[i][j][0]-input[i][j-1][0], input[i][j][1]-input[i][j-1][1]])
    vectors.append(v)
for i in range(0,len(input)):
    for j in range(0,len(input[i])):
        max_x = input[i][j][0] if input[i][j][0] > max_x else max_x
        max_y = input[i][j][1] if input[i][j][1] > max_y else max_y

grid = [['.' for i in range(0,max_x+1)] for n in range(0,max_y+3)]

def drawRock(grid, xy, v):
    if v[0] == 0:
        if v[1] < 0:
            for i in range(xy[1], xy[1]-abs(v[1])-1, -1):
                grid[i][xy[0]] = '#'
        else:
            for i in range(xy[1], xy[1]+abs(v[1])):
                grid[i][xy[0]] = '#'
    else:
        if v[0] < 0:
            for i in range(xy[0], xy[0]-abs(v[0])-1, -1):
                grid[xy[1]][i] = '#'
        else:
            for i in range(xy[0], xy[0]+abs(v[0])):
                grid[xy[1]][i] = '#'

def sandMove(grid, pos):
    if pos[1]+1 == len(grid):
        return [pos[0], pos[1]+1]

    if grid[pos[1]+1][pos[0]] == '.':
        return [pos[0],pos[1]+1]
    elif grid[pos[1]+1][pos[0]-1] == '.':
        return [pos[0]-1,pos[1]+1]
    elif grid[pos[1]+1][pos[0]+1] == '.':
        return [pos[0]+1,pos[1]+1]
    else:
        return None
def drawSand(grid):
    position = [500,0]
    while sandMove(grid, position) is not None:
        position = sandMove(grid, position)
    try:
        grid[position[1]][position[0]] = 'o'
        return True
    except:
        return False

for line in vectors:
    for v in line:
        drawRock(grid, [v[0],v[1]], [v[2],v[3]])

for i in range(0,25):
    drawSand(grid) 

msg = ''
for i in range(0, len(grid)):
    for j in range(490, 504):
        msg += grid[i][j]
    msg += '\n'
print(msg)