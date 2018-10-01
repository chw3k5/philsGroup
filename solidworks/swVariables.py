"""
This script generates the txt files that SolidWorks can reference for global variables and equations within parts.
"""
import os, sys


def putInQuotes(var):
    return "\"" + var + "\""


def makeLine(varName, value, units):
    return putInQuotes(varName) + "=" + str(float(value)) + units + "\n"


def exctactInputVals(val_str, valuesDict):
    return val_str, valuesDict[val_str][0], valuesDict[val_str][1]


class equationsFile():
    def __init__(self, fullFilePath, fileName="equations"):
        self.saveName = os.path.join(fullFilePath, fileName + ".txt")
        self.fileContent = []

    def addVarLine(self, varName, value, units):
        self.fileContent.append(makeLine(varName, value, units))

    def listAddVarLine(self, stringList, valuesDict):
        for varString in stringList:
            varName, value, units = exctactInputVals(varString, valuesDict)
            self.addVarLine(varName, value, units)

    def addRefLine(self, ref, var):
        self.fileContent.append(putInQuotes(ref) + "=" + putInQuotes(var) + "\n")

    def writeFile(self, appendMode=False):
        if appendMode:
            f = open(self.saveName, "a")
        else:
            f = open(self.saveName, "w")
        for singleLine in self.fileContent:
            f.write(singleLine)
        f.close()
        print("Wrote file:\n", self.saveName, "\n")


if __name__ == "__main__":
    pass
