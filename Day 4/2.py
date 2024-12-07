import sys

inputFile = []
with open(sys.path[0]+"\\input.txt", "r") as file:
    for line in file:
        inputFile.append(line.strip())
xmasCount = 0
for vert in range(0, len(inputFile)):
    for hor in range(0, len(inputFile[0])):
        if inputFile[vert][hor] == "A":
            if vert-1 >= 0 and vert+1 < len(inputFile) and hor-1 >= 0 and hor+1 < len(inputFile[0]):
                vertRight = inputFile[vert-1][hor-1]+"A"+inputFile[vert+1][hor+1]
                vertLeft = inputFile[vert-1][hor+1]+"A"+inputFile[vert+1][hor-1]
                if (vertRight == "SAM" or vertRight == "MAS") and (vertLeft == "SAM" or vertLeft == "MAS"):
                    xmasCount += 1

print(xmasCount)