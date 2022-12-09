class Position:
    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def two_steps_apart(head_p, tail_p):
    if abs(head_p.x - tail_p.x) == 2:
        return True
    if abs(head_p.y - tail_p.y) == 2:
        return True
    if head_p.y != tail_p.y and head_p.x != tail_p.x and ():
        return True
    return False


def move_head(head_p, direction):
    if direction == 'R':
        head_p.x += 1
    elif direction == 'L':
        head_p.x -= 1
    elif direction == 'U':
        head_p.y += 1
    elif direction == 'D':
        head_p.y -= 1


def move_tail(head_p, tail_p, direction, prev_x, prev_y):
    if head_p.y != tail_p.y and head_p.x != tail_p.x:
        tail_p.x = prev_x
        tail_p.y = prev_y
    if abs(head_p.x - tail_p.x) == 2:
        if direction == 'R':
            tail_p.x += 1
        if direction == 'L':
            tail_p.x -= 1
    if abs(head_p.y - tail_p.y) == 2:
        if direction == 'U':
            tail_p.y += 1
        if direction == 'D':
            tail_p.y -= 1


def p1(lines):
    head_p = Position(0, 0)
    tail_p = Position(0, 0)
    visited = []
    visited.append((0, 0))
    for line in lines:
        direction = line[0]
        steps = line[1]
        for step in range(int(steps)):
            prev_x = head_p.x
            prev_y = head_p.y
            move_head(head_p, direction)
            if two_steps_apart(head_p, tail_p):
                move_tail(head_p, tail_p, direction, prev_x, prev_y)
                if (tail_p.x, tail_p.y) not in visited:
                    visited.append((tail_p.x, tail_p.y))
    print(len(visited))
    visualize(visited)


def visualize(visited):
    for y in range(4, -1, -1):
        s = f'{y}  '
        for x in range(6):
            if (x, y) in visited:
                s += '#'
            else:
                s += '0'
        print(s)
    print('   012345')


p1(map(str.split, open('input.txt').read().splitlines()))
