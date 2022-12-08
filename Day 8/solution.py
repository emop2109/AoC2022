with open('.\input.txt', 'r'):
    input = input.read().splitlines()

input = [[int(x) for x in line] for line in input]
print(input)