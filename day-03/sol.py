PRIO = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def p1():
    lines = open("input.txt").readlines()
    totalSum = 0
    matches = []
    for line in lines:
        mid = len(line)//2
        a, b = line[:mid], line[mid:]
        for i in range(len(a)):
            if a[i] in b:
                matches.append(a[i])
                break
    for match in matches:
        totalSum += PRIO.index(match)
    print(totalSum)


p1()
