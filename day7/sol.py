from collections import defaultdict


def p1():
    lines = map(str.split, open('input.txt').read().split('\n'))
    cwd = []
    d = defaultdict(int)
    print(d)
    current_directory = ''
    for line in lines:
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    cwd.pop()
                else:
                    current_directory = line[2]
                    cwd.append(current_directory)
        elif line[0] != 'dir':
            for i in range(len(cwd)):
                d[tuple(cwd[: i + 1])] += int(line[0])
    print(sum(size for size in d.values() if size <= 100000))
    fs_total = 70000000
    update = 30000000
    required_space = (update - (fs_total - d[('/',)]))
    print(min(size for size in d.values() if size >= required_space))


p1()
