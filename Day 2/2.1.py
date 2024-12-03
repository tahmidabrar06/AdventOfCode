import sys
with open(sys.path[0]+r"\input.txt", "r") as file:
    puzzleInput = file.readlines()

safe = 0
for line in puzzleInput:
    levels = line.split()
    asc = False
    if int(levels[0]) < int(levels[1]):
        asc = True
    isSafe = True
    for i in range(0, len(levels)-1):
        if asc:
            difference = int(levels[i+1])-int(levels[i])
        else:
            difference = int(levels[i])-int(levels[i+1])
            
        if  difference not in range(1,4):
            isSafe = False
    if isSafe:
        safe += 1

print(safe)