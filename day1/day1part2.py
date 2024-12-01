file1 = open('input.txt', 'r')
lines = file1.readlines()
leftList = []
rightList = []
for line in lines:
    l, r = [int(x) for x in line.split('   ')]
    leftList.append(l)
    rightList.append(r)
sum = 0
for q in range(0, len(leftList)):
    num = leftList[q]
    countNum = rightList.count(num)
    sum += num * countNum
print(sum)
