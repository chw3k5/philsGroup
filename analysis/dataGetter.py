import string
import numpy

def isNum(testNum):
    try:
        return float(testNum)
    except:
        return testNum




def getTableData(filename, skiprows=1, delimiter=',', senseUnits=True):
    f = open(filename, 'r')
    # the first line is the header information naming the columns of data
    firstLine = f.readline()
    columnNames = firstLine.strip().split(delimiter)


    if senseUnits:
        unitFactorsList = []
        secondLine = f.readline()
        columnUnits = secondLine.strip().split(delimiter)
        for unit in columnUnits:
            unit = unit.replace( ')', '').replace( '(', '')
            unit = unit.replace(']', '').replace('[', '')
            if unit.lower() in ['v', 'a', 'm', 'kg, w', 's']:
                unitFactorsList.append(float(1))
            elif unit.lower() in ['mv', 'ma', 'mm', 'g', 'mw', 'ms']:
                unitFactorsList.append(float(1e-3))
            elif unit.lower() in ['uv', 'ua', 'um', 'mg', 'uw', 'us']:
                unitFactorsList.append(float(1e-6))
            elif unit.lower() in ['nv', 'na', 'nm', 'ng', 'nw', 'ns']:
                unitFactorsList.append(float(1e-9))
            else:
                unitFactorsList.append(float(1))


    f.close()
    tableData = numpy.loadtxt(filename, skiprows=skiprows, delimiter=delimiter)
    tableDict = {}
    for (n, columnName) in list(enumerate(columnNames)):
        if senseUnits:
            tableDict[columnName] = tableData[:,n] * unitFactorsList[n]
        else:
            tableDict[columnName] = tableData[:,n]
    return tableDict


def getTableRowData(filename, delimiter=','):
    tableDict = {}
    f = open(filename, 'r')
    for line in f:
        rowInfo = line.split(delimiter)
        rowHeader = rowInfo[0].strip()
        rowDataList = [isNum(datum) for datum in rowInfo[1:]]
        dataSize = len(rowDataList)
        if dataSize > 1:
            tableDict[rowHeader] = rowDataList
        elif dataSize == 1:
            tableDict[rowHeader] = rowDataList[0]
        else:
            tableDict[rowHeader] = None
    f.close()
    return tableDict

