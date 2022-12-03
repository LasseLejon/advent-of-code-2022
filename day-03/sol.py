PRIO = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def p1(lines):
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


def p2(lines):
    totalSum = 0
    for i in range(len(lines)):
        if i % 3 == 0:
            a, b, c = lines[i][:len(lines[i])-1], lines[i+1], lines[i+2]
            c = set(a) & set(b) & set(c)
            totalSum += PRIO.index(next(iter(c)))
    print(totalSum)


p2(open("input.txt").readlines())
