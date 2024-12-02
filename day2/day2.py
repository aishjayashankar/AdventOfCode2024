file1 = open('sample.txt', 'r')
reports = file1.readlines()
safeReports = 0
for report in reports:
    reportArr = [int(x) for x in report.split()]
    isIncreasing = True if reportArr[0] < reportArr[1] else False
    isReportSafe = True

    for q in range(1, len(reportArr)):
        # Check if trend is maintained
        if ((reportArr[q] > reportArr[q-1] and not(isIncreasing)) or 
            (reportArr[q] < reportArr[q-1] and isIncreasing)):
            isReportSafe = False
            break

        # Check if difference between levels is acceptable
        absDiffInLevels = abs(reportArr[q] - reportArr[q-1])
        if (absDiffInLevels < 1 or absDiffInLevels > 3):
            isReportSafe = False
            break

    if (isReportSafe == True):
        safeReports+=1
print(safeReports)