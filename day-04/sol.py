def p1(lines):
    ans = 0
    for line in lines:
        sp = line.split(',')
        a, b = sp[0].split('-'), sp[1].split('-')
        if int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1]) or int(b[0]) <= int(a[0]) and int(b[1]) >= int(a[1]):
            ans += 1
    print(ans)


p1(open("input.txt").read().split('\n'))
