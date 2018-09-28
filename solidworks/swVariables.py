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
    bottomWallInnerLength_str = "bottomWallInnerLength"
    valuesDict[bottomWallInnerLength_str] = (30.0, inch_str)
    bottomWallInnerWidth_str = "bottomWallInnerWidth"
    valuesDict[bottomWallInnerWidth_str] = (20.0, inch_str)
    bottomWallInnerDepth_str = "bottomWallInnerDepth"
    valuesDict[bottomWallInnerDepth_str] = (10.0, inch_str)
    bottomWallThickness_str = "bottomWallThickness"
    valuesDict[bottomWallThickness_str] = (0.375, inch_str)
    bottomShellStringList = [bottomWallInnerLength_str, bottomWallInnerWidth_str,
                             bottomWallInnerDepth_str, bottomWallThickness_str]


    # top Walls for cryostat shell parameters
    topWallInnerLength_str = "topWallInnerLength"
    valuesDict[topWallInnerLength_str] = (valuesDict[bottomWallInnerLength_str][0], inch_str)
    topWallInnerWidth_str = "topWallInnerWidth"
    valuesDict[topWallInnerWidth_str] = (valuesDict[bottomWallInnerWidth_str][0], inch_str)
    topWallInnerDepth_str = "topWallInnerDepth"
    valuesDict[topWallInnerDepth_str] = (8.0, inch_str)
    topWallThickness_str = "topWallThickness"
    valuesDict[topWallThickness_str] = (valuesDict[bottomWallThickness_str][0], inch_str)
    topShellStringList = [topWallInnerLength_str, topWallInnerWidth_str,
                             topWallInnerDepth_str, topWallThickness_str]


    # bottom Flange Parameters
    bottomFlangeInnerLength_str = "bottomFlangeInnerLength"
    valuesDict[bottomFlangeInnerLength_str] = (valuesDict[bottomWallInnerLength_str][0] +
                                               (2.0 * valuesDict[bottomWallThickness_str][0]), inch_str)
    bottomFlangeInnerWidth_str = "bottomFlangeInnerWidth"
    valuesDict[bottomFlangeInnerWidth_str] = (valuesDict[bottomWallInnerWidth_str][0] +
                                              (2.0 * valuesDict[bottomWallThickness_str][0]), inch_str)
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
    valuesDict[topFlangeInnerLength_str] = (valuesDict[bottomWallInnerLength_str][0] +
                                            (2.0 * valuesDict[bottomWallThickness_str][0]), inch_str)
    topFlangeInnerWidth_str = "topFlangeInnerWidth"
    valuesDict[topFlangeInnerWidth_str] = (valuesDict[bottomWallInnerLength_str][0] +
                                           (2.0 * valuesDict[bottomWallThickness_str][0]), inch_str)
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
    bottomShellWalls.addRefLine("D1@sketch1", bottomWallInnerLength_str)
    bottomShellWalls.addRefLine("D2@sketch1", bottomWallInnerWidth_str)
    bottomShellWalls.addRefLine("D3@sketch1", bottomWallThickness_str)
    bottomShellWalls.addRefLine("D1@Boss-Extrude2", bottomWallInnerDepth_str)
    if sys.platform == "win32":
        bottomShellWalls.writeFile()
    else:
        print(bottomShellWalls.fileContent)

    # top shell walls
    topShellWalls = equationsFile(fullFilePath=parentDir, fileName="topShellWallsEquations")
    topShellWalls.listAddVarLine(topShellStringList, valuesDict)
    topShellWalls.addRefLine("D1@sketch1", topWallInnerLength_str)
    topShellWalls.addRefLine("D2@sketch1", topWallInnerWidth_str)
    topShellWalls.addRefLine("D3@sketch1", topWallThickness_str)
    topShellWalls.addRefLine("D1@Boss-Extrude2", topWallInnerDepth_str)
    if sys.platform == "win32":
        topShellWalls.writeFile()
    else:
        print(topShellWalls.fileContent)

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