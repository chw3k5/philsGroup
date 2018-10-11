"""
These are classes used to generate text files that can be imported into SolidWorks to set values.
"""
import os
import sys


class SolidWorksPart:
    def __init__(self, file_name, units="in", parent_directory=None):
        if parent_directory is None:
            if sys.platform == "win32":
                parent_directory = "G:\\chwheele\\SolidWorks\\SimonsObs\\GrabCAD\\SO\\Universal Readout Harness\\ASU Test Cryostat\\supports"
            else:
                parent_directory = ""

        self.fullFileName = os.path.join(parent_directory, file_name)
        self.units = units
        self.fileContent = ""

    def addVariableLine(self, solidworks_variable, a_number, units=None):

        temporary_string = "\"" + solidworks_variable + "\"=" + str(a_number)
        if units is None:
            temporary_string += self.units + "\n"
        else:
            temporary_string += units + "\n"
        self.fileContent += temporary_string

    def writeFile(self):
        file_handle = open(self.fullFileName, "w")
        file_handle.write(self.fileContent)
        file_handle.close()


"""Legacy classed and definitions that are being phased out."""

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
