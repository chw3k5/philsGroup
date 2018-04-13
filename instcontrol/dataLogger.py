import time, os, sys
from instcontrol.vacuumMonitor import getFormattedPressure
from instcontrol.lakeshore224 import readLS224
from instcontrol.lakeshore336 import readLS336

# this is the folder where you can keep the data
dataLogFolder = os.path.join("cryoLog")
dataFileName = "April_12_2018.csv"

# This an attempt at writing platform independent code.
if sys.platform == "win32":
    rootName = "C:\\"
else:
    rootName = "/"

# if the directory does not exist you can make it

if not os.path.exists(rootName + dataLogFolder):
    os.mkdir(rootName + dataLogFolder)

# the base file name
fullDataPath = os.path.join(rootName + dataLogFolder, dataFileName)
def logCryoData(verbose=False, logInterval=5.0, logTime=float("inf")):
    startTime = time.time()
    nowTime = startTime
    diffTime = nowTime - startTime
    loopCount = 0
    headerString = ""

    while diffTime < logTime:
        loopCount += 1
        pressureString = getFormattedPressure(verbose=verbose)
        temperatureDict_LS224 = readLS224(verbose=verbose)
        temperatureDict_LS336 = readLS336(verbose=verbose)

        # if this is a new file, write the header string
        if headerString == "":
            if os.path.exists(fullDataPath):
                # the file has been start on another run use append mode
                f = open(fullDataPath, 'a')
                headerString = "file exists, it is assumed the header is the same as that at the top of the file, " + \
                               "this variable will not be used."
            else:
                # this is a new, file write the header here.
                f = open(fullDataPath, 'w')
                headerString += "ctime_s,"
                headerString += "pressure_torr,"
                for key in temperatureDict_LS224.keys():
                    headerString += key + "_K,"
                for key in temperatureDict_LS336.keys():
                    headerString += key + "_K,"
                # get rid of the final ',' and at the newline character '\n'
                headerString = headerString[:-1] + "\n"
                f.write(headerString)
        else:
            # this file has already been opened by this script, use append mode to add dat to the file.
            f = open(fullDataPath, 'a')

        # write the data to the a line, that is appended to the file
        writeString = ""
        writeString += str(nowTime) + ","
        writeString += pressureString + ","
        for key in temperatureDict_LS224.keys():
            writeString += str(temperatureDict_LS224[key]) + ","
        for key in temperatureDict_LS336.keys():
            writeString += str(temperatureDict_LS336[key]) + ","
        # get rid of the final ',' and at the newline character '\n'
            writeString = writeString[:-1] + "\n"
        f.write(writeString)
        f.close()

        # sleep for the log interval time
        nowTime = time.time()
        diffTime = nowTime - startTime
        if verbose:
            print("data log loop count:", loopCount)
        while diffTime < (float(logInterval) * float(loopCount)):
            time.sleep(0.1)
            nowTime = time.time()
            diffTime = nowTime - startTime
        if verbose:
            print("  diff time in seconds:" + str("%6.1f" % diffTime) + "\n" +
                  "log trigger in seconds:" + str("%6.1f" % (logInterval * float(loopCount))) + "\n")

    return


if __name__ == "__main__":
    logCryoData(verbose=True, logInterval=5.0)