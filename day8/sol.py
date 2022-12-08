lines = open('input.txt').read().split('\n')


def invisible_in_col(current_height, r, c, max_cols) -> bool:
    left, right = False, False
    for i in range(c-1, -1, -1):
        if lines[r][i] >= current_height:
            left = True
            break
    for i in range(c+1, max_cols):
        if lines[r][i] >= current_height:
            right = True
    return left and right


def invisible_in_row(current_height, r, c, max_rows) -> bool:
    up, down = False, False
    for i in range(r-1, -1, -1):
        if lines[i][c] >= current_height:
            up = True
            break
    for i in range(r+1, max_rows, +1):
        if lines[i][c] >= current_height:
            down = True
            break
    return up and down


def p1():
    max_rows = len(lines)
    max_cols = len(lines[0])
    invisible = 0
    for r in range(1, max_rows - 1):
        for c in range(1, max_cols - 1):
            if invisible_in_col(lines[r][c], r, c, max_cols):
                if invisible_in_row(lines[r][c], r, c, max_cols):
                    invisible += 1
    print(max_rows * max_cols - invisible)


def get_distance_col(current_height, r, c, max_cols) -> (int):
    left, right = 0, 0
    for i in range(c-1, -1, -1):
        left += 1
        if lines[r][i] >= current_height:
            break
    for i in range(c+1, max_cols):
        right += 1
        if lines[r][i] >= current_height:
            break
    return (left, right)


def get_distance_row(current_height, r, c, max_rows) -> (int):
    up, down = 0, 0
    for i in range(r-1, -1, -1):
        up += 1
        if lines[i][c] >= current_height:
            break
    for i in range(r+1, max_rows, +1):
        down += 1
        if lines[i][c] >= current_height:
            break
    return (up, down)


def p2():
    max_rows = len(lines)
    max_cols = len(lines[0])
    scenic_score = 0
    for r in range(1, max_rows - 1):
        for c in range(1, max_cols - 1):
            col = get_distance_col(lines[r][c], r, c, max_cols)
            row = get_distance_row(lines[r][c], r, c, max_rows)
            scenic_score = max(scenic_score, col[0] * col[1] * row[0] * row[1])
    print(scenic_score)


p2()
