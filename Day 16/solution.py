with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()
inp = {}
for line in input:
    key, flow = line.split(';')[0].split(' ')[1], int(line.split(';')[0].split('=')[-1])
    tunnels = tuple([x for x in line.split(';')[1].replace(',','').split(' ')[5:]])
    inp[key] = (flow, tunnels)

# Definerer en graf som representerer avstanden mellom de ulike ventilene.
# Del 2 tar fryktelig lang tid å beregne. Mulige forbedringer kan være å fjerne
# alle ventiler som "flow"-rate lik 0 etter at grafen er opprettet for å redusere
# antall stier DFS-algoritmene må søke igjennom. I tillegg bør mennesket og elefanten
# i del 2 operere på to ulike sett av ventiler. Da kan man kanskje kjøre DFS-algoritmen 
# for del 1 og returnere alle sett som har lengde lik halvparten av antall ventiler +-1
# og se hvilke par av ulike sett som gir høyest score.
class Graph:
    def __init__(self):
        self.graph, self.flows = {}, {}
    def addEdge(self, parent, childs):
        try:
            self.graph[parent][childs[0]] = childs[1]
        except:
            self.graph[parent] = {childs[0]: childs[1]}
    def addFlow(self, dict):
        self.flows = dict
    def updateEdgesToAll(self):
        temp = {}
        for key in self.graph:
            temp[key] = {}
            for k in self.graph:
                if k != key:
                    temp[key][k]= self.shorestPath(key, k)
        for key in temp:
            for k in temp[key]:
                self.addEdge(key, (k, temp[key][k]))
    def shorestPath(self, start, end):
        queue, visited, steps = [start], [start], 1
        path = {}
        while len(queue) != 0:
            vertex = queue.pop(0)
            if vertex == end:
                backtracker = end
                while path[backtracker] != start:
                    backtracker = path[backtracker]
                    steps += 1
                return steps
            for vertices in self.graph[vertex]:
                if vertices not in visited:
                    visited.append(vertices)
                    queue.append(vertices)
                    path[vertices] = vertex
        return 0
# Oppretter grafen og legger til en egen dict for de ulike
# "flow"-ratene for ventilene. I tillegg legges det til kanter mellom
# alle ventilene
G = Graph()   
flow = {}
for keys in inp:
    flow[keys] = inp[keys][0]
    for c in inp[keys][1]:
        G.addEdge(keys, (c, 1))
G.addFlow(flow)
G.updateEdgesToAll()

# ---------------------------------------- Del 1 -------------------------------------------
# DFS-algoritme som søker seg igjennom grafen og finner optimal score("pressure release")
# Fungerer relativt greit for del 1
def findOptimalPressure(g, start, score, i, visited):
    if i <= 0:
        return score
    maxS = score
    for valve in g.graph[start]:
        if valve not in visited and g.flows[valve] != 0:
            q = i - g.graph[start][valve] - 1
            if q >= 0:
                s = q*g.flows[valve] + score
                visitedExtended = [val for val in visited]
                visitedExtended.append(valve)
                ss = findOptimalPressure(g, valve, s, q, visitedExtended)
                if ss > maxS:
                    maxS = ss
    return maxS

print(findOptimalPressure(G, 'AA', 0, 30, []))

# ---------------------------------------- Del 2 -------------------------------------------
# En modifisert versjon av DFS-algoritmen over. For hver ventil enten mennesket eller elefanten
# åpner sjekkes samtlige stier som den motsatte "spilleren" kan ta. Funksjonen gir riktig svar 
# men bruker forferdelig lang tid på å beregne scoren, type ~ 30 min...

def findOptimalPressureV2(g, start, score, i, visited):
    if i[0] <= 0 and i[1] <= 0 or len(visited) == len(g.graph):
        return score
    maxS = score
    for valve in g.graph[start[0]]:
        if valve not in visited:
            q1 = i[0] - g.graph[start[0]][valve] - 1
            if q1 >= 0:
                s1 = q1*g.flows[valve] + score
                visitedExtended = [val for val in visited]
                visitedExtended.append(valve)
                for vals in g.graph[start[1]]:
                    if vals not in visitedExtended:
                        q2 = i[1] - g.graph[start[1]][vals] - 1
                        if q2 >= 0:
                            s2 = q2*g.flows[vals] + s1
                            visitedExt = [val for val in visitedExtended]
                            visitedExt.append(vals)
                            ss = findOptimalPressureV2(g, [valve, vals], s2, [q1, q2], visitedExt)
                            if ss > maxS:
                                maxS = ss
    return maxS
visited = []
for key in G.flows:
    if G.flows[key] == 0:
        visited.append(key)
print(findOptimalPressureV2(G, ['AA', 'AA'], 0, [26, 26], visited))