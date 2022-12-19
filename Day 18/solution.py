import time
with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()
st = time.time()
# ---------------------------------------- Del 1 -------------------------------------------
# Legger kubene i en dict hvor (x,y,z)-koordinatene er key og verdien er antall sider synlig.
# Antall sider synlig er satt til 6 da vi ikke har sjekket om kuben har en nærliggende kube
# Definerer også et sett med vektorer som forteller om to kuber er nærliggende eller ikke
cubes = {tuple(map(int, line.split(','))): 6 for line in input}
adjacent = {(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)}

# For hver kube sjekkes dens posisjon mot de andre kubene. Dersom vektoren mellom kubene
# er i settet "adjacent" ligger kubene inntil hverandre og vi trekker fra en for antall
# sider synlig.
for key in cubes:
    x,y,z = key
    for k in cubes:
        xx, yy, zz = k
        if key != k:
            if (x-xx,y-yy,z-zz) in adjacent:
                cubes[key] -= 1
area = sum([cubes[key] for key in cubes])
end = time.time()
print(area)
print(f'Elapsed runtime: {end-st} seconds')
# ---------------------------------------- Del 1 -------------------------------------------
# Finner først max-verdiene for x,y og z da det opprettes et sett med alle punktene i en 3d-grid
# som inneholder alle kubene.
st = time.time()
max_x, max_y, max_z = 0,0,0
for cube in cubes:
    x,y,z = cube
    max_x = x if x > max_x else max_x
    max_y = y if y > max_y else max_y
    max_z = z if z > max_z else max_z

# Funksjon som finner de nærliggende punktene for et gitt punkt
def adjacentOf(xyz):
    adjacentCubes = []
    x,y,z = xyz
    for vectors in adjacent:
        xx, yy, zz = vectors
        adjacentCubes.append((x+xx,y+yy,z+zz))
    return adjacentCubes

# BFS-algoritme som finner alle punktene som kan nåes fra (0,0,0). Det vil si at
# den vil finne alle punktene utennom de innestengte luftrommene
def breadthFirstSearch(start, visited):
    queue =[start]
    visited.add(start)
    while len(queue) != 0:
        x,y,z = queue.pop(0)
        if -1 < x < max_x+1 and -1 < y < max_y+1 and -1 < z < max_z+1:
            for cube in adjacentOf((x,y,z)):
                if cube not in visited:
                    visited.add(cube)
                    queue.append(cube)
    return visited
visited = set({})
for cube in cubes:
    visited.add(cube)
filled3dGrid = breadthFirstSearch((0,0,0), visited)
# Lager et sett for hele max_x x max_y x max_z griden
entireGrid = set({})
for i in range(0,max_x):
    for j in range(0, max_y):
        for n in range(0,max_z):
            entireGrid.add((i,j,n))
# Oppretter et sett med luftrom. Disse er punktene i hele gridden som ikke
# befinner seg i settet fra BFS-algoritmen. Antall eksponerte sider mot en 
# kube blir satt til null da vi ikke vet om luftrommet ligger inntil en kube.
air = {}
for sets in entireGrid:
    if sets not in filled3dGrid:
        air[sets] = 0
# Itererer gjennom alle punktene i luft-settet og sjekker om de ligger inntil en kube.
# Dersom det er tilfelle legges det til 1 for hver nærliggende kube.
for a in air:
    x,y,z = a
    for c in cubes:
        xx,yy,zz = c
        if (x-xx,y-yy,z-zz) in adjacent:
            air[a] += 1
# Svaret er da svaret fra del 1 minus antall sider for luftrom eksponert mot en kube
print(area-sum([air[key] for key in air]))
end = time.time()
print(f'Elapsed runtime: {end-st} seconds')