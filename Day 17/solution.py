import time
with open('.\input.txt', 'r') as file:
    input = file.read()

# Løsningen baserer seg på å finne et sykel i hvordan steinene beveger seg og faller
# Oppretter først et sett som skal inneholde steinenes posisjon i hulen. Inkluderer fra start
# settet for gulvet av hulen. Definerer så de ulike type steine som funskjon av høyden til 
# den høyeste steinen.
cave = set((col,0 ) for col in range(0,6))
objs = (lambda height: {(2, height+4), (3, height+4), (4, height+4), (5, height+4)},
        lambda height: {(3, height+6), (2, height+5), (3, height+5), (4, height+5), (3, height+4)},
        lambda height: {(2,height+4), (3, height+4), (4, height+4), (4, height+5), (4,height+6)},
        lambda height: {(2, height+4), (2, height+5), (2, height+6), (2, height+7)},
        lambda height: {(2, height+4), (3, height+4), (2, height+5), (3, height+5)})

# Funksjon som beveger en stein til venstre eller høyre. Dersom den nye posisjonen til steinen
# finnes i "hule"-settet vil det si at den nye posisjonen er ugyldig og den opprinnelige 
# posisjonen returneres. Ellers returneres den nye posisjonen
def moveRock(dir, rock):
    if dir == '<':
        position = {(xy[0]-1, xy[1]) for xy in rock}
        if any(xy[0] < 0 for xy in position) or position&cave:
            return rock
        return position
    else:
        position = {(xy[0]+1, xy[1]) for xy in rock}
        if any(xy[0] > 6 for xy in position) or position&cave:
            return rock
        return position

# Beveger en stein nedover. Samme som i funskjonen over; dersom den nye posisjonen finnes i 
# "hule"-settet returnes den gamle posisjonen som betyr at steinen har kollidert med en stein
# eller gulvet.
def moveDownward(rock):
    position = {(xy[0], xy[1]-1) for xy in rock}
    return rock if position&cave else position

# Funksjon som finner høyden på høyeste kolonnen basert på antall steiner som har falt.
# Hver kombinasjon av stein-type og indeks av inputen ("vinden") lagres i en dict. 
# Dersom kombinasjonen allerede finnes, sjekkes det om det er funnet en sykel.
# Dersom modulo av antall steiner falt og antall steiner siden forrige observasjon er lik
# modulo av antall steiner totalt og antall steiner siden forrige observasjon har man funnet en sykel.
# Det vil da si at høyden vil stige like mye for hver sykel og man kan finne høyden ved å summere
# høyden så langt og høyden per sykler ganget med antall sykler igjen.
def simulateFallingRocks(numberOfRocks, wind):
    cycles, rockType, j, height = {}, 0, 0, 0
    for rock in range(numberOfRocks):
        obj = objs[rockType](height)
        while True:
            if (rockType, j) in cycles:
                previousRock, previousHeight = cycles[(rockType, j)]
                cycle = rock - previousRock
                if rock % cycle == numberOfRocks % cycle:
                    cycleHeight = height-previousHeight
                    cyclesLeft = ((numberOfRocks - rock)//cycle)
                    return height + cycleHeight*cyclesLeft
            else:
                cycles[(rockType, j)] = (rock, height)

            # Beveger steinen enten til venstre eller høyre og nedover. Dersom
            # steinens posisjon er lik før den er forsøkt å flytte nedover har steinen
            # kollidert med en stein eller gulvet. Steinen legges da til "hule"-settet
            # og en ny høyde blir beregnet samt ny stein-type
            obj = moveRock(wind[j], obj)
            obj_ = moveDownward(obj)
            j = j+1 if j+1 < len(wind) else 0
            if obj == obj_:
                cave.update(obj)
                height = max(xy[1] for xy in cave)
                rockType = rockType + 1 if rockType < 4 else 0
                break
            obj = obj_
    
    return height
st = time.time()
print(simulateFallingRocks(2022, input)) 
end = time.time()
print(f'Elapsed runtime: {end-st} seconds')

st = time.time()
cave = set((col,0 ) for col in range(0,6))
print(simulateFallingRocks(1000000000000, input))
end = time.time()
print(f'Elapsed runtime: {end-st} seconds')