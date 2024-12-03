import re

file = open('input.txt', 'r')
input = file.readlines()
operationRegex = r"\d{1,3}\,\d{1,3}"
functionRegex = r"mul\(\d{1,3}\,\d{1,3}\)"
total = 0
for line in input:
    foundFunctions = re.findall(functionRegex, line)
    for function in foundFunctions:
        operands = [int(x) for x in re.search(operationRegex, function).group().split(',')]
        total += (operands[0] * operands[1])
print(total)
        
