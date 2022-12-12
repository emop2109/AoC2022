with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()

# Klassen Vertex representere en node i en graph. Hver node har en høyde og en peker til 
# noden bak i "stien". 
class Vertex:
    def __init__(self,height = 100):
        self.Height = height
        self.Parent = None

# Definerer en (x+2)x(y+2) grid med Vertex-objekter. Vertex-objekter i den ytre rammen
# er ikke en del av den "faktiske"-griden, men er lagt til for å unngå out-of-bounds
# når en skal sjekke nabo-nodene i de fire ulike retningene.
grid = [[Vertex() for i in range(0, len(input[0])+2)] for n in range(0,len(input)+2)]

# Setter høyde verdiene til de ulike nodene og finner start(S) og slutt(E) noden.
startVertex, stopVertex = None, None
for i in range(1,len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if ord(input[i-1][j-1]) - 96 == -13:
            grid[i][j].Height = 1
            startVertex = grid[i][j]
        elif ord(input[i-1][j-1]) - 96 == -27:
            grid[i][j].Height = 26
            stopVertex = grid[i][j]
        else:
            grid[i][j].Height = ord(input[i-1][j-1])-96

# Oppretter en graf med uvektede kanter over den indre griden basert på reglene for hvordan
# man traverserer griden
graph = dict()
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        edges = []
        if grid[i][j].Height == grid[i-1][j].Height or grid[i-1][j].Height-grid[i][j].Height == 1 or grid[i][j].Height > grid[i-1][j].Height:
            edges.append(grid[i-1][j])
        if grid[i][j].Height == grid[i+1][j].Height or grid[i+1][j].Height-grid[i][j].Height == 1 or grid[i][j].Height > grid[i+1][j].Height:
            edges.append(grid[i+1][j])
        if grid[i][j].Height == grid[i][j-1].Height or grid[i][j-1].Height-grid[i][j].Height == 1 or grid[i][j].Height > grid[i][j-1].Height:
            edges.append(grid[i][j-1])
        if grid[i][j].Height == grid[i][j+1].Height or grid[i][j+1].Height-grid[i][j].Height == 1 or grid[i][j].Height > grid[i][j+1].Height:
            edges.append(grid[i][j+1])
        graph[grid[i][j]] = edges

# BFS - algoritme som finner korteste vei fra root til end-node. Setter pekeren til foreldre noden
# til noden man kom fra
def findShortestPath(G, root, end):
    queue, visited = [root], [root]
    while len(queue) != 0:
        vertex = queue.pop(0)
        if vertex == end:
            return 'Found shortest path'
        for vertices in G[vertex]:
            if vertices not in visited:
                visited.append(vertices)
                vertices.Parent = vertex
                queue.append(vertices)
    return 'Did not find shortes path'

# ---------------------------------------- Del 1 -------------------------------------------
# Finner den korteste stien og teller antall steg fra slutt noden og tilbake
findShortestPath(graph, startVertex, stopVertex)
node, cnt = stopVertex, 0
while node.Parent != None:
    node = node.Parent
    cnt += 1
print(cnt)

# ---------------------------------------- Del 2 -------------------------------------------
# Samme som over, men vi stopper i det øyeblikket vi treffer en node med høyde lik 1(a)
node, cnt = stopVertex, 0
while node.Height != 1:
    node = node.Parent
    cnt += 1
print(cnt)