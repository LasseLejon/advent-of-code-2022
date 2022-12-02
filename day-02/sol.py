# A=rock B=paper C=scissors
# X=rock, Y=paper, Z=scissors
# 1       2        3
# Lost = 0, draw = 3, win = 6

# X=lose, Y=draw, Z=win

lines = open("input.txt").readlines()
totalScore = 0
move_winning_condition = {"X": "C", "Y": "A", "Z": "B"}
mymove_to_opponent = {"X": "A", "Y": "B", "Z": "C"}
for line in lines:
    opponentMove = line[:1]
    myMove = line[2:3]
    if myMove == 'X':
        totalScore += 1
    if myMove == 'Y':
        totalScore += 2
    if myMove == 'Z':
        totalScore += 3
    if move_winning_condition[myMove] == opponentMove:
        totalScore += 6
    if mymove_to_opponent[myMove] == opponentMove:
        totalScore += 3
print(totalScore)
