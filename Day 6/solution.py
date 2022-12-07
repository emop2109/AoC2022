with open('.\input.txt', 'r') as file:
    input = file.read()

def findMarker(line, n):
    for i in range(0,len(line)-n):
        if len(set(line[i:i+n])) == len(line[i:i+n]):
            return i+n

# ---------------------------------------- Del 1 -------------------------------------------
print(findMarker(input, 4))

# ---------------------------------------- Del 2 -------------------------------------------
print(findMarker(input, 14))