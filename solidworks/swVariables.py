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
    valuesDict[wallThickness_str] = (0.375, inch_str)
    bottomShellStringList = [innerLength_str, innerWidth_str, innerDepth_str, wallThickness_str]

    # bottom Flange Parameters
    bottomFlangeInnerLength_str = "bottomFlangeInnerLength"
    valuesDict[bottomFlangeInnerLength_str] = (valuesDict[innerLength_str][0] + (2.0 * valuesDict[wallThickness_str][0]),
                                         inch_str)
    bottomFlangeInnerWidth_str = "bottomFlangeInnerWidth"
    valuesDict[bottomFlangeInnerWidth_str] = (valuesDict[innerWidth_str][0] + (2.0 * valuesDict[wallThickness_str][0]),
                                         inch_str)
    bottomFlangeWidth_str = "bottomFlangeWidth"
    valuesDict[bottomFlangeWidth_str] = (1.5, inch_str)
    bottomFlangeThickness_str = "bottomFlangeThickness"
    valuesDict[bottomFlangeThickness_str] = (0.5, inch_str)
    bottomFlangeHoleInsetDist_str = "bottomFlangeHoleInsetDist"
    valuesDict[bottomFlangeHoleInsetDist_str] = (0.3, inch_str)
    bottomFlangeStringList = [bottomFlangeInnerLength_str, bottomFlangeInnerWidth_str,
                              bottomFlangeWidth_str, bottomFlangeThickness_str,
                              bottomFlangeHoleInsetDist_str]

    # top Flange Parameters
    topFlangeInnerLength_str = "topFlangeInnerLength"
    valuesDict[topFlangeInnerLength_str] = (valuesDict[innerLength_str][0] + (2.0 * valuesDict[wallThickness_str][0]),
                                         inch_str)
    topFlangeInnerWidth_str = "topFlangeInnerWidth"
    valuesDict[topFlangeInnerWidth_str] = (valuesDict[innerWidth_str][0] + (2.0 * valuesDict[wallThickness_str][0]),
                                         inch_str)
    topFlangeWidth_str = "topFlangeWidth"
    valuesDict[topFlangeWidth_str] = (1.5, inch_str)
    topFlangeThickness_str = "topFlangeThickness"
    valuesDict[topFlangeThickness_str] = (0.5, inch_str)
    topFlangeHoleInsetDist_str = "topFlangeHoleInsetDist"
    valuesDict[topFlangeHoleInsetDist_str] = (0.3, inch_str)
    topFlangeStringList = [topFlangeInnerLength_str, topFlangeInnerWidth_str,
                           topFlangeWidth_str, topFlangeThickness_str,
                           topFlangeHoleInsetDist_str]

    """
    Start of the the script for making equation files
    """
    # bottom shell walls
    bottomShellWalls = equationsFile(fullFilePath=parentDir, fileName="bottomShellWallsEquations")
    bottomShellWalls.listAddVarLine(bottomShellStringList, valuesDict)
    bottomShellWalls.addRefLine("D1@sketch1", innerLength_str)
    bottomShellWalls.addRefLine("D2@sketch1", innerWidth_str)
    bottomShellWalls.addRefLine("D3@sketch1", wallThickness_str)
    bottomShellWalls.addRefLine("D1@Boss-Extrude2", innerDepth_str)
    if sys.platform == "win32":
        bottomShellWalls.writeFile()
    else:
        print(bottomShellWalls.fileContent)

    # bottom flange for walls
    bottomFlangeForWalls = equationsFile(fullFilePath=parentDir, fileName="bottomFlangeForWallsEquations")
    bottomFlangeForWalls.listAddVarLine(bottomFlangeStringList, valuesDict)
    bottomFlangeForWalls.addRefLine("D1@sketch1", bottomFlangeInnerLength_str)
    bottomFlangeForWalls.addRefLine("D2@sketch1", bottomFlangeInnerWidth_str)
    bottomFlangeForWalls.addRefLine("D3@sketch1", bottomFlangeWidth_str)
    bottomFlangeForWalls.addRefLine("D1@Boss-Extrude1", bottomFlangeThickness_str)
    bottomFlangeForWalls.addRefLine("D1@Sketch3", bottomFlangeHoleInsetDist_str)
    if sys.platform == "win32":
        bottomFlangeForWalls.writeFile()
    else:
        print(bottomFlangeForWalls.fileContent)

    # top flange for walls
    topFlangeForWalls = equationsFile(fullFilePath=parentDir, fileName="topFlangeForWallsEquations")
    topFlangeForWalls.listAddVarLine(topFlangeStringList, valuesDict)
    topFlangeForWalls.addRefLine("D1@sketch1", topFlangeInnerLength_str)
    topFlangeForWalls.addRefLine("D2@sketch1", topFlangeInnerWidth_str)
    topFlangeForWalls.addRefLine("D3@sketch1", topFlangeWidth_str)
    topFlangeForWalls.addRefLine("D1@Boss-Extrude1", topFlangeThickness_str)
    if sys.platform == "win32":
        topFlangeForWalls.writeFile()
    else:
        print(topFlangeForWalls.fileContent)