def getStartingPositions(grid):
    d = {}
    for line in grid.split('\n'):
        sp = line.split(' ')
        i = 0
        pos = 1

        while i < len(sp):
            if sp[i] == '1':
                break
            if sp[i] == '':
                i += 4
            else:
                if str(pos) not in d:
                    d[str(pos)] = []
                d[str(pos)].insert(0, str(sp[i]))
                i += 1
            pos += 1
    return d


def p1(f):
    ans = ''
    crates, moves = f.split('\n\n')
    d = getStartingPositions(crates)
    for line in moves.split('\n'):
        sp = line.split(' ')
        if sp[0] == 'move':
            for i in range(int(sp[1])):
                toMove = d[sp[3]].pop()
                d[sp[5]].append(toMove)
    for i in range(1, len(d) + 1):
        ans += d[str(i)].pop()[1:2]
    print(ans)


p1(open('input.txt').read())
