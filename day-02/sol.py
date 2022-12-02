# A=rock B=paper C=scissors
# X=rock, Y=paper, Z=scissors
# 1       2        3
# Lost = 0, draw = 3, win = 6

# X=lose, Y=draw, Z=win

def getRoundOutcomeScore(outcome):
    score = 0
    if outcome == 'X':
        score = 0
    if outcome == 'Y':
        score = 3
    if outcome == 'Z':
        score = 6
    return score


def getMyMove(outcome, opp):
    moveToWinningMove = {'A': 'B', 'C': 'A', 'B': 'C'}
    moveToLoosingMove = {'B': 'A', 'A': 'C', 'C': 'B'}
    myMove = ""
    if outcome == 'Z':
        return moveToWinningMove[opp]
    if outcome == 'X':
        return moveToLoosingMove[opp]
    else:
        return opp


lines = open("input.txt").readlines()
totalScore = 0
moveToScore = {'A': 1, 'B': 2, 'C': 3}
for line in lines:
    opponentMove = line[:1]
    roundOutcome = line[2:3]
    totalScore += getRoundOutcomeScore(roundOutcome)
    totalScore += moveToScore[getMyMove(roundOutcome, opponentMove)]
print(totalScore)
