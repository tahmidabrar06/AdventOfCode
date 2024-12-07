import sys

inputFile = []
with open(sys.path[0]+"\\input.txt", "r") as file:
    for line in file:
        inputFile.append(line.strip())
xmasCount = 0
for vert in range(0, len(inputFile)):
    for hor in range(0, len(inputFile[0])):
        if inputFile[vert][hor] == "X":
            rightMas = ""
            leftMas = ""
            downMas = ""
            upMas = ""
            downLeftMas = ""
            downRightMas = ""
            upLeftMas = ""
            upRightMas = ""
            for i in range(0, 4):
                if hor+i < len(inputFile[0]):
                    rightMas += inputFile[vert][hor+i]#Right
                if hor-i >= 0:
                    leftMas += inputFile[vert][hor-i]#Left
                if vert+i < len(inputFile):
                    downMas += inputFile[vert+i][hor]#Down
                if vert-i >= 0:
                    upMas += inputFile[vert-i][hor]#Up
                if vert+i < len(inputFile) and hor-i >= 0:
                    downLeftMas += inputFile[vert+i][hor-i]#Down-Left
                if vert+i < len(inputFile) and hor+i < len(inputFile[0]):
                    downRightMas += inputFile[vert+i][hor+i]#Down-Right
                if vert-i >= 0 and hor-i >= 0:
                    upLeftMas += inputFile[vert-i][hor-i]#Up-Left
                if vert-i >= 0 and hor+i < len(inputFile[0]):
                    upRightMas += inputFile[vert-i][hor+i]#Up-Right
            if rightMas == "XMAS":
                xmasCount += 1
            if leftMas == "XMAS":
                xmasCount += 1
            if downMas == "XMAS":
                xmasCount += 1
            if upMas == "XMAS":
                xmasCount += 1
            if downLeftMas == "XMAS":
                xmasCount += 1
            if downRightMas == "XMAS":
                xmasCount += 1
            if upLeftMas == "XMAS":
                xmasCount += 1        
            if upRightMas == "XMAS":
                xmasCount += 1

print(xmasCount)