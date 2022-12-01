f = open('input.txt')
rows = f.readlines()
cur = 0
calories = []
for row in rows:
    if row == '\n':
        calories.append(cur)
        cur = 0
    else:
        cur += int(row)
three_highest = 0
for i in range(3):
    mx = max(calories)
    three_highest += mx
    print(three_highest)
    calories.remove(mx)
