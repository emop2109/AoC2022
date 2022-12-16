with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()

input = [[[int(v.split('=')[-1]) for v in x.split(',')] for x in line.split(':')] for line in input] 

# Klassen sensor representerer en sensor med posisjon til både sensoren og nærmeste beacon og 
# manhatten - distansen til sensoren. I tillegg har klassen en funskjon som returnere et set 
# med x-verdien som befinner seg langs y = i, og en funksjon som sjekker om et vilkårlig punkt
# er utenfor rekkevidden til sensoren.
class Sensor:
    def __init__(self, position, beacon):
        self.Position, self.Beacon = position, beacon
        self.Distance = self.dinstanceToBeacon()
    def dinstanceToBeacon(self):
        return abs(self.Position[0] - self.Beacon[0]) + abs(self.Position[1] - self.Beacon[1])
    def coverageOf(self, value):
        r = self.Distance - abs(self.Position[1] - value)
        return set(i for i in range(self.Position[0]-r, self.Position[0]+r+1))
    def coverage(self, p):
        d = abs(self.Position[0] - p[0]) + abs(self.Position[1] - p[1])
        if d <= self.Distance:
            return False
        else:
            return True

# Lagrer alle sensorene i en liste
sensors = []
for line in input:
    sensors.append(Sensor(line[0], line[1]))

# ---------------------------------------- Del 1 -------------------------------------------

# Funksjon som iterer gjennom alle sensorene og genererer et set med x-verdien er som befinner
# seg på y = value. Returner lengen på settet da set kun inneholder unike verdier minus antall 
# beacons som befinner seg på y = value
def checkLine(value):
    points, beacons = set({}), []
    for sen in sensors:
        points.update(sen.coverageOf(value))
        if sen.Beacon[1] == value and sen.Beacon not in beacons:
            beacons.append(sen.Beacon)
    return len(points) - len(beacons)

print(checkLine(2000000))

# ---------------------------------------- Del 2 -------------------------------------------

# Sjekker avstanden mellom hver sensor da ideen er at punktet man vil finne befinner seg mellom to par av sensorer
# med en avstand mellom seg lik summen av hver enkelts distanse til en beacon + 2. Dersom dette er tilfelle legges 
# disse sensorene i en egen liste.
sens = []
for i in range(0,len(sensors) - 1):
    for j in range(i, len(sensors)):
        d = abs(sensors[i].Position[0] - sensors[j].Position[0]) + abs(sensors[i].Position[1] - sensors[j].Position[1])
        if d == sensors[i].Distance + sensors[j].Distance + 2:
            sens.extend([sensors[i], sensors[j]])

# Sjekker et spefikt punkt p mot alle sensorene. Dersom punktet ikke er dekket av noen sensorer er dette punktet for 
# den gjemte beacon'n
def checkPoint(p, s):
    for sen in sensors:
        if sen != s:
            if sen.coverage(p) == False:
                return False
    return True

# Iterer over sensorene i sens og sjekker alle punkter som ligger rett utenfor rekkevidden til den aktuelle sensoren.
# Passer også på at x og y verdier under 0 eller over 4 000 000 ikke sjekkes.
def findBeacon():
    for s in sens:
        xl, xu = s.Position[0] - s.Distance - 1, s.Position[0] + s.Distance + 1
        xl, xu = 0 if xl < 0 else xl, 4000000 if xu > 4000000 else xu
        yl, yu = s.Position[1] - s.Distance - 1, s.Position[1] + s.Distance + 1
        yl, yu = 0 if yl < 0 else yl, 4000000 if yu > 4000000 else yu
        for i in range(xl, xu+1):
            r = abs(s.Distance - abs(i - s.Position[0] - 1))
            y = s.Position[1] - r
            if y >= 0:
                p = (i,y)
                if checkPoint(p, s):
                    return (i,y)
        for i in range(xu-1, xl, -1):
            r = abs(s.Distance - abs(i - s.Position[0] - 1))
            y = s.Position[1] + r
            if y <= 4000000:
                p = (i,y)  
                if checkPoint(p, s):
                    return (i,y)
x,y = findBeacon()
print(x*4000000+y)