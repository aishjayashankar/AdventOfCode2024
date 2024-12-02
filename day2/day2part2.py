import copy

def checkReportSafety(reportArr):
    isIncreasing = True if reportArr[0] < reportArr[1] else False
    isReportSafe = True
    errorIndex = -1

    for q in range(1, len(reportArr)):
        # Check if trend is maintained
        if ((reportArr[q] > reportArr[q-1] and not(isIncreasing)) or 
            (reportArr[q] < reportArr[q-1] and isIncreasing)):
            isReportSafe = False
            errorIndex = q
            break

        # Check if difference between levels is acceptable
        absDiffInLevels = abs(reportArr[q] - reportArr[q-1])
        if (absDiffInLevels < 1 or absDiffInLevels > 3):
            isReportSafe = False
            errorIndex = q
            break
    return isReportSafe, errorIndex

file1 = open('input.txt', 'r')
reports = file1.readlines()
safeReports = 0
for report in reports:
    reportArr = [int(x) for x in report.split()]
    isReportSafe, errorIndex = checkReportSafety(reportArr)
    if (isReportSafe):
        safeReports+=1
    else:
        leftPoppedReportArr = copy.deepcopy(reportArr)
        leftPoppedReportArr.pop(errorIndex-1)
        rightPoppedReportArr = copy.deepcopy(reportArr)
        rightPoppedReportArr.pop(errorIndex)
        firsPoppedReportArr = copy.deepcopy(reportArr)
        firsPoppedReportArr.pop(0)
        if (checkReportSafety(leftPoppedReportArr)[0] or 
            checkReportSafety(rightPoppedReportArr)[0] or
            checkReportSafety(firsPoppedReportArr)[0]):
            safeReports+=1    
print(safeReports)