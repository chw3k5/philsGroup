"""
This script generates the txt files that SolidWorks can reference for global variables and equations within parts.
"""
import os, sys


def putInQuotes(var):
    return "\"" + var + "\""


def makeLine(varName, value, units):
    return putInQuotes(varName) + "=" + str(float(value)) + units + "\n"


def exctactInputVals(val_str, valuesDict):
    return val_str, valuesDict[innerLength_str][0], valuesDict[innerLength_str][1]


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
    # variables for script
    parentDir = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\" +\
                "Universal Readout Harness\\ASU Test Cryostat\\EDM Shell"
    valuesDict = {}
    inch_str = "in"

    # bottom Walls for cryostat shell parameters
    innerLength_str = "innerLength"
    valuesDict[innerLength_str] = (30.0, inch_str)
    innerWidth_str = "innerWidth"
    valuesDict[innerWidth_str] = (20.0, inch_str)
    innerDepth_str = "innerDepth"
    valuesDict[innerDepth_str] = (10.0, inch_str)
    wallThickness_str = "wallThickness"
    valuesDict[wallThickness_str] = (0.25, inch_str)
    bottomShellStringList = [innerLength_str, innerWidth_str, innerDepth_str, wallThickness_str]

    # bottom Flange Parameters
    flangeInnerLength_str = "flangeInnerLength"
    valuesDict[flangeInnerLength_str] = (valuesDict[innerLength_str][0] + valuesDict[wallThickness_str][0],
                                         inch_str)
    flangeInnerWidth_str = "flangeInnerWidth"
    valuesDict[flangeInnerWidth_str] = (valuesDict[innerWidth_str][0] + valuesDict[wallThickness_str][0],
                                         inch_str)
    flangeWidth_str = "flangeWidth"
    valuesDict[flangeWidth_str] = (1.0, inch_str)
    flangeThickness_str = "flangeThickness"
    valuesDict[flangeWidth_str] = (0.375, inch_str)
    bottomFlangeStringList = [flangeInnerLength_str, flangeInnerWidth_str, flangeWidth_str, flangeThickness_str]

    """
    Start of the the script for making equation files
    """
    # bottom shell walls
    bottomShellWalls = equationsFile(fullFilePath=parentDir, fileName="bottomShellWallsEquations")
    bottomShellWalls.listAddVarLine(bottomShellStringList, valuesDict)
    bottomShellWalls.addRefLine("D1@sketch1", innerLength_str)
    bottomShellWalls.addRefLine("D2@sketch1", innerWidth_str)
    bottomShellWalls.addRefLine("D1@Boss-Extrude2", innerDepth_str)
    if sys.platform == "win32":
        bottomShellWalls.writeFile()
    else:
        print(bottomShellWalls.fileContent)

    # bottom flange for walls
    bottomFlangeForWalls = equationsFile(fullFilePath=parentDir, fileName="bottomFlangeForWallsEquations")
    bottomFlangeForWalls.listAddVarLine(bottomFlangeStringList, valuesDict)
    bottomFlangeForWalls.addRefLine("D1@sketch1", flangeInnerLength_str)
    bottomFlangeForWalls.addRefLine("D2@sketch1", flangeInnerWidth_str)
    bottomFlangeForWalls.addRefLine("D1@Boss-Extrude1", flangeThickness_str)
    if sys.platform == "win32":
        bottomFlangeForWalls.writeFile()
    else:
        print(bottomFlangeForWalls.fileContent)

