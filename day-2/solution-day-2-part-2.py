import functools
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
filePath = scriptDir / "input.txt"

def mergeGameSets(gameSetA, gameSetB):
    return {
        "green": max(gameSetA.get("green", 0), gameSetB.get("green", 0)),
        "blue": max(gameSetA.get("blue", 0), gameSetB.get("blue", 0)),
        "red": max(gameSetA.get("red", 0), gameSetB.get("red", 0))
    }

def transformGameMove(gameMove):
    gameMoveDetails = gameMove.removeprefix(' ').split(' ')
    return (gameMoveDetails[1], int(gameMoveDetails[0]))

def transformGameSet(gameSet):
    gameMoves = gameSet.split(',')
    result = dict(map(transformGameMove, gameMoves))
    return result

def transformGame(game):
    gameSets = game.split(':')[1].split(';')
    return list(functools.reduce(mergeGameSets, map(transformGameSet, gameSets)).values())

with open(filePath, "r") as file:
    sum = 0

    for game in file:
        game = game.removesuffix('\n')
        sum += functools.reduce(lambda a, b: a * b, transformGame(game))

    print("Part Two: {0}".format(sum))