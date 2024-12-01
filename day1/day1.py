file1 = open('input.txt', 'r')
lines = file1.readlines()
leftList = []
rightList = []
for line in lines:
    l, r = [int(x) for x in line.split('   ')]
    leftList.append(l)
    rightList.append(r)
leftList.sort()
rightList.sort()
sum = 0
for q in range(0, len(leftList)):
    sum += abs(leftList[q] - rightList[q])
print(sum)