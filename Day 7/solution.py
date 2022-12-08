with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()

# -------------------------- Generer et "non-binary tree" over mappestrukturen ---------------------------------

# klassen File skal representere en mappe eller fil. Hver mappe/fil har et navn og en peker til foreldre mappen.
# Mapper blir blir initialisert med størrelse lik 0 da størrelsen blir beregnet etter at treet er generert.
# Hver mappe har en liste over pekere til undermapper og filer. For filer er dennne listen tom.
# I tillegg har mappene funksjoner for å legge til undermapper/filer, returnere undermapper/filer og 
# beregne den samlede størrelsen på undermappene og filene
class File:
    def __init__(self, parentFile, name, size=0):
        self.Parent, self.Name, self.Size = parentFile, name, size
        self.Files = []
    def addFile(self, file):
        self.Files.append(file)
    def getChildFile(self, name):
        for file in self.Files:
            if file.Name == name:
                return file
    def calculateSize(self):
        if len(self.Files) != 0:
            self.Size = sum([file.Size for file in self.Files])

# Oppretter root-mappen
root = File(None, '/')
currentDir = root

# Bygger treet basert på linjene i input
for i in range(2, len(input)):
    if '$ cd' in input[i] and input[i] != '$ cd ..':
        currentDir = currentDir.getChildFile(input[i][5:])
    elif '$ cd ..'in input[i]:
        currentDir = currentDir.Parent
    elif 'dir' in input[i][0:4]:
        currentDir.addFile(File(currentDir,input[i][4:]))
    else:
        if '$ ls' not in input[i]:
            currentDir.addFile(File(currentDir,input[i],int(input[i].split(' ')[0])))

# Funksjon som beregner størrelsene på mappene i treet rekrusivt
def calculateDirSize(file):
    if len(file.Files) != 0:
        for dir in file.Files:
            calculateDirSize(dir)
        file.calculateSize()

calculateDirSize(root)

# Funksjon som finner og returnerer størrelsen på mapper større/mindre enn en gitt størrelse
def findDirBySize(dir, n, operator, listOfDirs):
    if len(dir.Files) != 0:
        for file in dir.Files:
            findDirBySize(file, n, operator, listOfDirs)
        if operator == '<=':
            if dir.Size <= n:
                listOfDirs.append(dir.Size)
        else:
            if dir.Size >= n:
                listOfDirs.append(dir.Size)
    return listOfDirs

# ---------------------------------------- Del 1 -------------------------------------------
# Finner summen av alle mappene som er mindre en n
print(sum(findDirBySize(root, 100000, '<=', [])))

# ---------------------------------------- Del 2 -------------------------------------------
# Finner den minste mappen som er større enn størrelsen på hele strukturen - 4 000 0000
print(min(findDirBySize(root,(root.Size-40000000),'>=', [])))