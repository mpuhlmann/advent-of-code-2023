import re
from pathlib import Path

scriptDir = Path(__file__).resolve().parent
filePath = scriptDir / "input.txt"

def partOne():
    with open(filePath, "r") as file:
        sum = 0

        for line in file:
            numbersPerLine = re.findall(r'\d', line)
            first = numbersPerLine[0]
            last = numbersPerLine[-1]

            sum+= int(first+last)

        print("Part One: {0}".format(sum))

def specialConvert(line):
    line = line.replace("oneight", "oneeight")
    line = line.replace("threeight", "threeeight")
    line = line.replace("fiveight", "fiveeight")
    line = line.replace("nineight", "nineeight")
    line = line.replace("sevenine", "sevennine")
    line = line.replace("twone", "twoone")
    line = line.replace("eighthree", "eightthree")
    line = line.replace("eightwo", "eighttwo")
    return line

def convert(line):
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")
    return line

def partTwo():
    with open(filePath, "r") as file:
        sum = 0

        for line in file:
            numbersPerLine = re.findall(r'\d', convert(specialConvert(line)))

            first = numbersPerLine[0]
            last = numbersPerLine[-1]

            sum+= int(first+last)

        print("Part Two: {0}".format(sum))

partOne()
partTwo()
