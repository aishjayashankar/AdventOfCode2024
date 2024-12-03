import re

file = open('input.txt', 'r')
input = file.readlines()
operationRegex = r"\d{1,3}\,\d{1,3}"
functionRegex = r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)"
total = 0
isEnabled = True
for line in input:
    foundFunctions = re.findall(functionRegex, line)
    for q in range(0, len(foundFunctions)):
        if (foundFunctions[q] == 'do()'):
            isEnabled = True
        elif (foundFunctions[q] == 'don\'t()'):
            isEnabled = False
        elif(isEnabled):
            operands = [int(x) for x in re.search(operationRegex, foundFunctions[q]).group().split(',')]
            total += (operands[0] * operands[1])
print(total)
        
