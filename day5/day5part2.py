file = open('input.txt', 'r')
consolidatedRules = {}
rule = file.readline().strip().split('|')
while (rule[0] != ''):
    if (rule[0] in consolidatedRules):
        consolidatedRules[rule[0]].append(rule[1])
    else:
        consolidatedRules[rule[0]] = [rule[1]]
    rule = file.readline().strip().split('|')

def findMidForPage(pageAsList):
    targetCount = int(len(pageAsList)/2)
    for q in range(len(pageAsList)):
        currentCount = 0
        for w in range(0, len(pageAsList)):
            if (q == w):
                continue
            if (pageAsList[q] not in consolidatedRules):
                break
            if (pageAsList[w] in consolidatedRules[pageAsList[q]]):
                currentCount += 1
        if (currentCount == targetCount):
            return int(pageAsList[q])

pages = file.readlines()
total = 0
for page in pages:
    pageAsList = [x.strip() for x in page.split(',')]
    isValid = True
    for q in range(len(pageAsList)):        
        for w in range(q+1, len(pageAsList)):
            if (pageAsList[q] not in consolidatedRules or
                pageAsList[w] not in consolidatedRules[pageAsList[q]]):
                isValid = False
                break
        if (not isValid):
            break
    if (not isValid):
        total += findMidForPage(pageAsList)
print(total)