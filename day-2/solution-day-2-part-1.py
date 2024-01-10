import functools
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
filePath = scriptDir / "input.txt"

tresholds = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def transformGameMove(gameMove):
    gameMoveDetails = gameMove.removeprefix(' ').split(' ')
    return tresholds[gameMoveDetails[1]] >= int(gameMoveDetails[0])

def transformGameSet(gameSet):
    gameMoves = gameSet.split(',')
    return functools.reduce(lambda a, b: a and b, map(transformGameMove, gameMoves))

def transformGame(game):
    gameSets = game.split(':')[1].split(';')
    return functools.reduce(lambda a, b: a and b, map(transformGameSet, gameSets))

with open(filePath, "r") as file:

    sum = 0
    idx = 1

    for game in file:
        game = game.removesuffix('\n')

        if (transformGame(game)):
            sum += idx

        idx += 1

    print("Part One: {0}".format(sum))
