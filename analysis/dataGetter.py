import numpy, os, sys, getpass
from matplotlib import pyplot as plt


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


def read_csv_file(filename, verbose=False):
    """
    This is made to read in comma separated value (csv) files with a simple header,
    and return them in a dictionary that uses the headers (column names) as keys.
    """
    # tell the user what file is being read
    if verbose:
        print("Opening the file", filename, " to read in.")
    # open the file to be read
    f = open(filename, 'r')
    # get the header from the first line
    headerLine = f.readline()
    # strip the newline charater and split the header names that are seporated by a comma
    headerNames = headerLine.replace("\n", "").split(",")
    ## initalize the dictionary that the file data will be read into
    # make a empty dictionary
    dataDictonary = {}
    # iterate over the the header names
    for key in headerNames:
        # each "key" is assigned an empty list
        dataDictonary[key] = []
    # append data in the file's lines to dataDictionary
    while True:
        # read one line of data
        dataline = f.readline()
        # when you get to end of the data file you break from the infinite loop
        if dataline == "":
            # this is the exit the loop command
            break
        # taking the data line, removing the newline ("\n") character, then separating the terms
        list_of_data = dataline.replace("\n", "").split(",")
        # tying the data to the correct header key
        for (index, key) in enumerate(headerNames):
            # check it the data is a number, if so turning it into a float
            datum = isNum(list_of_data[index])
            # add the datum to the end of the dictionary
            dataDictonary[key].append(datum)
    # close the file that was being read
    f.close()
    return dataDictonary

# The code below only executes if the this is the top level program that is called as "python dataGetter.py"
if __name__ == "__main__":
    # get the current users username
    username = getpass.getuser()
    # prints the current user's user name
    print("Your username is", username)

    # determine the current operating system
    if sys.platform == "win32":
        # root folder in windows
        rootfolder = "C:\\"
    else:
        # root folder in mac and unix
        rootfolder = "/Users/" + username + "/"
    # looking for file on my own computer
    if username == "meganmoore":
        filename = os.path.join(rootfolder, "Downloads", "April_12_2018.csv")
    elif username == "Rebop":
        filename = os.path.join(rootfolder, "Users", "Rebop", "Documents", "CryoStuff", "April_12_2018.csv")
        # platform independent way of joining folders together with the filename
    else:
        filename = os.path.join(rootfolder, "cryolog",  "April_12_2018.csv")
    # read the file using the definition in this file
    dataDictonary = read_csv_file(filename=filename)
    # make a simple test plot
    plt.plot(dataDictonary["ctime_s"], dataDictonary["UltraHead_K"])
    # show the plot
    plt.show()



