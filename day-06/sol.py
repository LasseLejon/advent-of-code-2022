def getStartOfMessageMarker(input, n):
    for i in range(len(input)):
        sub = input[i:i+n]
        if len([x for x in set(sub) if sub.count(x) > 1]):
            continue
        else:
            return i+n


def p1(input):
    print(getStartOfMessageMarker(input, 4))


def p2(input):
    print(getStartOfMessageMarker(input, 14))


p1(open('input.txt').readline())
p2(open('input.txt').readline())
