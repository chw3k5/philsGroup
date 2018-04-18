from getpass import getuser
from matplotlib import pyplot as plt
import numpy, os



def readAgilentData(fullPath):
    numberOfLineToSkip = 2
    columns = [0, 1]
    delimiter = ","

    # read the data
    with open(fullPath) as f:
        content = f.readlines()

    # get the column names from the header
    headerLine = content[numberOfLineToSkip].replace(" ", "").lower().split(delimiter)

    # initialize the dictionary that returns the data
    dataDict = {}
    for column in columns:
        dataDict[headerLine[column]] = []

    # put the data in the dictionary with the corresponding column name
    for dataLine in content[numberOfLineToSkip + 1:]:
        dataInTheLine = dataLine.split(delimiter)
        for column in columns:
            dataDict[headerLine[column]].append(float(dataInTheLine[column]))

    # make the data a numpy array to make math easier
    for column in columns:
        dataDict[headerLine[column]] = numpy.array(dataDict[headerLine[column]])

    return dataDict


def plotFunction(frequencyData, dBmData, fileName, plotFolder, showPlots, savePlots, useGHz, title='', color='black'):
    if useGHz:
        frequencyData = frequencyData / 1.0e9

    plt.plot(frequencyData, dBmData, color=color)

    if useGHz:
        plt.xlabel("Frequency (GHz)")
    else:
        plt.xlabel("Frequency (Hz)")

    plt.ylabel("dBm")
    plt.title(title)

    if showPlots:
        plt.show()

    if savePlots:
        plt.savefig(os.path.join(plotFolder, fileName.replace(".csv", ".png")))

    plt.clf()

    return


class AgilentData():
    def __init__(self, fileNames, parentFolder):
        self.parentFolder = parentFolder
        [self.S11_fileName, self.S12_fileName, self.S21_fileName, self.S22_fileName] = [None, None, None, None]
        [self.S11_dataDict, self.S12_dataDict, self.S21_dataDict, self.S22_dataDict] = [None, None, None, None]

        for fileName in fileNames:
            lowerFileName = fileName.lower()
            if "s11" in lowerFileName:
                self.S11_fileName = fileName
            elif "s12" in lowerFileName:
                self.S12_fileName = fileName
            elif "s21" in lowerFileName:
                self.S21_fileName = fileName
            elif "s22" in lowerFileName:
                self.S22_fileName = fileName

    def readData(self):
        if self.S11_fileName is not None:
            self.S11_dataDict = readAgilentData(os.path.join(self.parentFolder, self.S11_fileName))
        if self.S12_fileName is not None:
            self.S12_dataDict = readAgilentData(os.path.join(self.parentFolder, self.S12_fileName))
        if self.S21_fileName is not None:
            self.S21_dataDict = readAgilentData(os.path.join(self.parentFolder, self.S21_fileName))
        if self.S22_fileName is not None:
            self.S22_dataDict = readAgilentData(os.path.join(self.parentFolder, self.S22_fileName))

    def plotSparams(self, showPlots=True, savePlots=False, useGHz=True):
        # make the plot folder if there is not one already
        plotFolder = self.parentFolder + "plots"
        if savePlots:
            if not os.path.lexists(plotFolder):
                os.mkdir(plotFolder)

        if self.S11_dataDict is not None:
            plotFunction(self.S11_dataDict["frequency"],
                         self.S11_dataDict["formatteddata"],
                         self.S11_fileName,
                         plotFolder, showPlots, savePlots, useGHz,
                         title="S11 from " + self.S11_fileName,
                         color='firebrick')

        if self.S12_dataDict is not None:
            plotFunction(self.S12_dataDict["frequency"],
                         self.S12_dataDict["formatteddata"],
                         self.S12_fileName,
                         plotFolder, showPlots, savePlots, useGHz,
                         title="S12 from " + self.S12_fileName,
                         color='dodgerblue')

        if self.S21_dataDict is not None:
            plotFunction(self.S21_dataDict["frequency"],
                         self.S21_dataDict["formatteddata"],
                         self.S21_fileName,
                         plotFolder, showPlots, savePlots, useGHz,
                         title="S21 from " + self.S21_fileName,
                         color='darkorchid')

        if self.S22_dataDict is not None:
            plotFunction(self.S22_dataDict["frequency"],
                         self.S22_dataDict["formatteddata"],
                         self.S22_fileName,
                         plotFolder, showPlots, savePlots, useGHz,
                         title="S22 from " + self.S22_fileName,
                         color='DarkSalmon')



if getuser() == "chw3k5":
    parentFolder = os.path.join("/Users", "chw3k5", "Documents", "ASUpostdoc", "BabyBeluga", "Sparams")

    setsOfFileNames =[
        ["A3_S11_300K_2.10V.csv",
         "A3_S12_300K_2.10V.csv",
         "A3_S21_300K_2.10V.csv",
         "A3_S22_300K_2.10V.csv"],
        ["B3_S11_300K_1.54V.csv",
         "B3_S12_300K_1.54V.csv",
         "B3_S21_300K_1.54V.csv",
         "B3_S22_300K_1.54V.csv",],
        ["C2_S11_300K.csv",
         "C2_S12_300K.csv",
         "C2_S21_300K.csv",
         "C2_S22_300K.csv",],
        ["C3_S11_300K.csv",
         "C3_S12_300K.csv",
         "C3_S21_300K.csv",
         "C3_S22_300K.csv", ]
    ]
    for setOfFileNames in setsOfFileNames:
        paramGroup = AgilentData(setOfFileNames, parentFolder)
        paramGroup.readData()
        paramGroup.plotSparams(showPlots=False, savePlots=True)




if getuser() == "Heriberto":
    parentFolder = os.path.join("C:\\", "Users", "Heriberto", "Downloads")
    setsOfFileNames =[
        ["test_s21_SuperSpec.csv"]
    ]
    for setOfFileNames in setsOfFileNames:
        paramGroup = AgilentData(setOfFileNames, parentFolder)
        paramGroup.readData()
        paramGroup.plotSparams(showPlots=True, savePlots=False)
else:
    print("Your username is:", getuser())
    print("This program takes different actions based on the user.")
    print("The default action is these three print statements. ")