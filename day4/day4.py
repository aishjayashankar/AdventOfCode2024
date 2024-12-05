file = open('input.txt', 'r')
rows = file.readlines()
needle = 'XMAS'
total = 0
columns = ["" for i in range(len(rows[0]))]

# Horizontal count
for row in rows:
    total += row.count(needle)
    total += row[::-1].count(needle)
    for q in range(len(row)):
        columns[q] += row[q]

# Vertical count
del columns[-1]
for column in columns:
    total += column.count(needle)
    total += column[::-1].count(needle)

# Right diagonal \
for rowNum in range(len(rows)):
    haystack = ""
    for x, y in zip(range(rowNum, len(rows)), range(len(columns))):
        haystack += rows[x][y]
    total += haystack.count(needle)
    total += haystack[::-1].count(needle)
    haystack = ""
    for x, y in zip(range(len(rows)), range(rowNum + 1, len(columns))):
        haystack += rows[x][y]
    total += haystack.count(needle)
    total += haystack[::-1].count(needle)

# Left diagonal /
for rowNum in range(len(rows)):
    haystack = ""
    for x, y in zip(range(rowNum, len(rows)), range(len(columns)-1, -1, -1)):
        haystack += rows[x][y]
    total += haystack.count(needle)
    total += haystack[::-1].count(needle)
    haystack = ""
    for x, y in zip(range(len(rows)), range(len(columns)- rowNum - 2, -1, -1)):
        haystack += rows[x][y]
    total += haystack.count(needle)
    total += haystack[::-1].count(needle)
print(total)