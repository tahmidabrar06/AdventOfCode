import sys
with open(sys.path[0]+r"\input.txt", "r") as file:
    puzzleInput = file.readlines()

def CheckError(levels):
    asc = True
    dsc = True
    for i in range(0, len(levels)-1):
        difference = abs(int(levels[i])-int(levels[i+1]))    
        if  difference not in range(1,4):
            return False
        if int(levels[i]) > int(levels[i+1]):
            asc = False
        if int(levels[i]) < int(levels[i+1]):
            dsc = False
    if asc or dsc:
        return True
safe = 0
for line in puzzleInput:
    levels = line.split()
    isSafe = CheckError(levels)
    if not isSafe:
        for i in range(len(levels)):
            dampLevel = levels[:i] + levels[i+1:]
            if CheckError(dampLevel):
                isSafe = True
                break
    if isSafe:
        safe += 1
        print(levels)

print(safe)