file = open('input.txt', 'r')
rows = file.readlines()

def isXMAS(x, y):
    if (rows[x-1][y-1] == 'M' and rows[x-1][y+1] == 'M' and rows[x+1][y-1] == 'S' and rows[x+1][y+1] == 'S'):
        return True
    if (rows[x-1][y-1] == 'M' and rows[x-1][y+1] == 'S' and rows[x+1][y-1] == 'M' and rows[x+1][y+1] == 'S'):
        return True
    if (rows[x-1][y-1] == 'S' and rows[x-1][y+1] == 'M' and rows[x+1][y-1] == 'S' and rows[x+1][y+1] == 'M'):
        return True
    if (rows[x-1][y-1] == 'S' and rows[x-1][y+1] == 'S' and rows[x+1][y-1] == 'M' and rows[x+1][y+1] == 'M'):
        return True
    return False

total = 0
for x in range(1, len(rows)-1):
    for y in range(1, len(rows)-1):
        if (rows[x][y] == 'A' and isXMAS(x, y)):
            total += 1
print(total)    