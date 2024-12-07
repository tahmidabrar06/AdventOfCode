import sys
import re

with open(sys.path[0]+"\\input.txt", "r") as file:
    inputFile = ""
    for line in file:
        inputFile+=line

result = 0
enablePattern = r"do\(\)"
disablePattern = r"don't\(\)"
instructionPattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

validInstructionRanges = []

start = 0
end = re.search(disablePattern, inputFile).end()
while True:
    matchDisablePattern = re.search(disablePattern, inputFile[start:])
    if matchDisablePattern:
        end = matchDisablePattern.end()+start
        validInstructionRanges.append([start,end])
    else:
        validInstructionRanges.append([start, len(inputFile)])
        break
    matchEnablePattern = re.search(enablePattern, inputFile[end:])
    if matchEnablePattern:
        start = matchEnablePattern.start()+end
    else:
        break

for validRanges in validInstructionRanges:
    validInstructions = re.findall(instructionPattern, inputFile[validRanges[0]:validRanges[1]])
    for validInstruction in validInstructions:
        num1 = validInstruction[0]
        num2 = validInstruction[1]
        result += int(num1) * int(num2)
print(result)
    