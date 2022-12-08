with open('.\input.txt', 'r') as file:
    input = file.read().splitlines()


# ---------------------------------------- Del 1 -------------------------------------------

# Linje for linje blir hver bokstav som befinner seg i første halvdel av linjen
# sjekket om den finnes i den andre halvdelen
# benytter ord-funksjonen til å konvertere bokstaver til tall
res = []
for line in input:
    for item in line[:len(line)//2]:
        if item in line[len(line)//2:]:
            if ord(item) > 96:
                res.append(ord(item)-96)
                break
            else:
                res.append(ord(item)-38)
                break
print(sum(res))

# ---------------------------------------- Del 2 -------------------------------------------

# Hver bokstav i hver tredje linje blir sjekket om finnes i de to neste linjene
res = []
for i in range(0,len(input)-2,3):
    for item in input[i]:
        if item in input[i+1] and item in input[i+2]:
            if ord(item) > 96:
                res.append(ord(item)-96)
                break
            else:
                res.append(ord(item)-38)
                break
print(sum(res))