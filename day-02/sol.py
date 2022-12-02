# A=rock B=paper C=scissors
# X=rock, Y=paper, Z=scissors
# 1       2        3
# Lost = 0, draw = 3, win = 6

# X=lose, Y=draw, Z=win

def getMyMove(outcome, opp):
    moveToWinningMove = {'A': 'B', 'C': 'A', 'B': 'C'}
    moveToLoosingMove = {'B': 'A', 'A': 'C', 'C': 'B'}
    if outcome == 'Z':
        return moveToWinningMove[opp]
    if outcome == 'X':
        return moveToLoosingMove[opp]
    else:
        return opp


lines = open("input.txt").readlines()
totalScore = 0
moveToScore = {'A': 1, 'B': 2, 'C': 3}
roundOutcomeToScore = {'X': 0, 'Y': 3, 'Z': 6}
for line in lines:
    opponentMove = line[:1]
    roundOutcome = line[2:3]
    totalScore += roundOutcomeToScore[roundOutcome]
    totalScore += moveToScore[getMyMove(roundOutcome, opponentMove)]
print(totalScore)
