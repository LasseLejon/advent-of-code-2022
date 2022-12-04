def p1(lines):
    ans = 0
    for line in lines:
        sp = line.split(',')
        a, b = sp[0].split('-'), sp[1].split('-')
        a[0], a[1], b[0], b[1] = int(a[0]), int(a[1]), int(b[0]), int(b[1])
        if a[0] <= b[0] and a[1] >= b[1] or b[0] <= a[0] and b[1] >= a[1]:
            ans += 1
    print(ans)


def p2(lines):
    ans = 0
    for line in lines:
        sp = line.split(',')
        a, b = sp[0].split('-'), sp[1].split('-')
        r1, r2 = range(int(a[0]), int(a[1])+1), range(int(b[0]), int(b[1])+1)
        for i in r1:
            if i in r2:
                ans += 1
                break
    print(ans)


p2(open("input.txt").read().split('\n'))
