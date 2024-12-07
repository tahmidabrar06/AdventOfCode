import sys
import re

with open(sys.path[0]+"\\input.txt", "r") as file:
    inputFile = ""
    for line in file:
        inputFile+=line

instructionPattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

validInstructions = re.findall(instructionPattern, inputFile)
result = 0
for validInstruction in validInstructions:
    num1 = validInstruction[0]
    num2 = validInstruction[1]
    result += int(num1) * int(num2)
print(result)
    