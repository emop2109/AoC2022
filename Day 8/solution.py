with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()
grid = [[int(x) for x in line] for line in input]

# ---------------------------------------- Del 1 -------------------------------------------
# Funksjon som sjekker om den aktuelle cellene er større en den minste max verdien i 
# de ulike retningene
def checkVisibility(grid, i, j):
    setLeft, setRight = grid[i][:j],grid[i][j+1:]
    setUp = [line[j] for line in grid[:i]]
    setDown = [line[j] for line in grid[i+1:]]
    if grid[i][j] > min([max(setLeft), max(setRight), max(setUp), max(setDown)]):
        return True
    else:
        return False
# Summerer treene ved kantene
cnt = 2*len(grid[0]) + 2*(len(grid)-2)
# Itererer over de indre cellene av griden
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if checkVisibility(grid, i, j):
            cnt += 1
print(cnt)

# ---------------------------------------- Del 2 -------------------------------------------
# Funksjonene finner synsrekkevidden i de ulike retningene returnerer produktet av disse
def calculateViewDistance(grid, i, j):
    viewLeft, viewRight, viewUp, viewDown = 0,0,0,0
    for n in range(j-1,-1,-1):
        if grid[i][j] <= grid[i][n]:
            viewLeft += 1
            break
        viewLeft += 1
    for n in range(j+1,len(grid[i])):
        if grid[i][j] <= grid[i][n]:
            viewRight += 1
            break
        viewRight += 1
    for n in range(i-1,-1,-1):
        if grid[i][j] <= grid[n][j]:
            viewUp += 1
            break
        viewUp += 1
    for n in range(i+1, len(grid)):
        if grid[i][j] <= grid[n][j]:
            viewDown += 1
            break
        viewDown += 1
    return viewLeft*viewRight*viewUp*viewDown

# Start max verdi settes til 0
cnt = 0

# Itererer over de indre cellene og setter ny max dersom nylig
# beregnet max sum er større en den forrige
# Antar at cellen med størst produkt av synsrekkevidde
# ikke befinner seg langs en kant
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        maxView = calculateViewDistance(grid, i, j)
        if maxView > cnt:
            cnt = maxView
print(cnt)