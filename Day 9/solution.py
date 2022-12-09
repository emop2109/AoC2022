import math

with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()
#####################################################################################
# Definerer en klasse som beskriver hvert segment av tauet. Hvert segment har en 
# peker mot segmentet foran seg og med en liste over alle posisjonene segmentet har 
# vært innom. Tauet er beveger seg i xy-koordinatsystem hvor alle segmenter har
# initialbetingelsen [0,0].
#####################################################################################

# Definerer en dict med retningsvektorer basert på avstanden mellom et
# segment og segmentet fremfor
vectors = {'2,0' : [1,0], '-2,0' : [-1,0], '0,2' : [0,1], '0,-2': [0,-1], '1,2': [1,1], '2,1': [1,1], '2,-1': [1,-1], '1,-2': [1,-1], '-1,-2': [-1,-1], '-2,-1': [-1,-1], '-1,2': [-1,1], '-2,1': [-1,1],
            '2,2': [1,1], '2,-2': [1,-1], '-2,-2': [-1,-1], '-2,2': [-1,1]}

# Definerer klassen RopeSegment som beskriver hvert segment i tauet. 
class RopeSegment:
    def __init__(self,parent = None, start = [0,0]):
        self.Parent = parent
        self.Position = [start]
        self.Segments = []
    
    # Dersom legnden på vektoren mellom det aktuelle segmentet og segmentet fremfor
    # er større enn sqrt(2) legger man til en ny posisjon basert på verdien til "vectors"
    def move(self):
        vector = self.getVectorToParent()
        if math.sqrt(vector[0]**2+vector[1]**2) > math.sqrt(2):
            moveVector = vectors['{},{}'.format(vector[0],vector[1])]
            self.Position.append([self.Position[-1][0] + moveVector[0], self.Position[-1][1] + moveVector[1]])
    def getVectorToParent(self):
        return [self.Parent.Position[-1][0]-self.Position[-1][0], self.Parent.Position[-1][1]-self.Position[-1][1]]

    # Funksjoner for å bevege "hode"-segmentet
    def moveLeft(self):
        self.Position.append([self.Position[-1][0]-1, self.Position[-1][1]]) 
    def moveRight(self):
        self.Position.append([self.Position[-1][0]+1, self.Position[-1][1]])
    def moveUp(self):
        self.Position.append([self.Position[-1][0], self.Position[-1][1]+1])
    def moveDown(self):
        self.Position.append([self.Position[-1][0], self.Position[-1][1]-1])

    # Iterer over alle segmenter i listen over segmenter til "hode"-segmentet og endrer deres posisjon  
    def moveChildSegments(self):
        for segments in self.Segments:
            segments.move()
    
    # Legger til et undersegment som har peker mot segmentet foran i tauet
    def addSegment(self):
        if len(self.Segments) == 0:
            self.Segments.append(RopeSegment(parent = self))
        else:
            self.Segments.append(RopeSegment(parent = self.Segments[-1]))

# Funksjonen beveger tauet etter instruksjonene i hver linje
def moveRope(input, rope):
    for line in input:
        dir, num = line.split(' ')[0], int(line.split(' ')[1])
        for i in range(0,num):
            if dir == 'L':
                rope.moveLeft()
            elif dir == 'R':
                rope.moveRight()
            elif dir == 'U':
                rope.moveUp()
            else:
                rope.moveDown()
            rope.moveChildSegments()
    return rope.Segments[-1].Position
# ---------------------------------------- Del 1 -------------------------------------------

# Definerer "hode"-segment og legger til et segment(halen)
Rope = RopeSegment()
Rope.addSegment()

# Henter ut, fjerner duplikater og printer lengden av listen over posisjoner for det siste segmentet til tauet
positionsOfTail = moveRope(input,Rope)
positionsOfTail = [i for n, i in enumerate(positionsOfTail) if i not in positionsOfTail[:n]]
print(len(positionsOfTail))

# ---------------------------------------- Del 2 -------------------------------------------

# Samme som del 1 men vi legger til 9 segmenter i tillegg til selve "hodet"
Rope = RopeSegment()
for i in range(0,9):
    Rope.addSegment()

positionsOfTail = moveRope(input,Rope)
positionsOfTail = [i for n, i in enumerate(positionsOfTail) if i not in positionsOfTail[:n]]
print(len(positionsOfTail))