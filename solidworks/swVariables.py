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
    (workingLen, workingWidth, workingDepthBottom, workingDepthTop) = (30.0, 20.0, 10.0, 11.0)
    shellThickness = 0.375
    millRadius = 2.0
    flangeWidth = 1.5
    flangeThickness = 0.5
    flangeHoleInset = 0.3


    # bottom Walls for cryostat shell parameters
    bottomWallInnerLength_str = "bottomWallInnerLength"
    valuesDict[bottomWallInnerLength_str] = (workingLen, inch_str)
    bottomWallInnerWidth_str = "bottomWallInnerWidth"
    valuesDict[bottomWallInnerWidth_str] = (workingWidth, inch_str)
    bottomWallInnerDepth_str = "bottomWallInnerDepth"
    valuesDict[bottomWallInnerDepth_str] = (workingDepthBottom, inch_str)
    bottomWallThickness_str = "bottomWallThickness"
    valuesDict[bottomWallThickness_str] = (shellThickness, inch_str)
    bottomWallMillRadius_str = "bottomWallMillRadius"
    valuesDict[bottomWallMillRadius_str] = (millRadius, inch_str)
    bottomShellStringList = [bottomWallInnerLength_str, bottomWallInnerWidth_str,
                             bottomWallInnerDepth_str, bottomWallThickness_str,
                             bottomWallMillRadius_str]


    # top Walls for cryostat shell parameters
    topWallInnerLength_str = "topWallInnerLength"
    valuesDict[topWallInnerLength_str] = (workingLen, inch_str)
    topWallInnerWidth_str = "topWallInnerWidth"
    valuesDict[topWallInnerWidth_str] = (workingWidth, inch_str)
    topWallInnerDepth_str = "topWallInnerDepth"
    valuesDict[topWallInnerDepth_str] = (workingDepthTop, inch_str)
    topWallThickness_str = "topWallThickness"
    valuesDict[topWallThickness_str] = (shellThickness, inch_str)
    topWallMillRadius_str = "topWallMillRadius"
    valuesDict[topWallMillRadius_str] = (millRadius, inch_str)
    topShellStringList = [topWallInnerLength_str, topWallInnerWidth_str,
                          topWallInnerDepth_str, topWallThickness_str,
                          topWallMillRadius_str]


    # bottom Flange Parameters
    bottomFlangeInnerLength_str = "bottomFlangeInnerLength"
    valuesDict[bottomFlangeInnerLength_str] = (workingLen + (2.0 * shellThickness), inch_str)
    bottomFlangeInnerWidth_str = "bottomFlangeInnerWidth"
    valuesDict[bottomFlangeInnerWidth_str] = (workingWidth + (2.0 * shellThickness), inch_str)
    bottomFlangeWidth_str = "bottomFlangeWidth"
    valuesDict[bottomFlangeWidth_str] = (flangeWidth, inch_str)
    bottomFlangeThickness_str = "bottomFlangeThickness"
    valuesDict[bottomFlangeThickness_str] = (flangeThickness, inch_str)
    bottomFlangeHoleInsetDist_str = "bottomFlangeHoleInsetDist"
    valuesDict[bottomFlangeHoleInsetDist_str] = (flangeHoleInset, inch_str)
    bottomFlangeMillRadius_str = "bottomFlangeMillRadius"
    valuesDict[bottomFlangeMillRadius_str] = (millRadius, inch_str)
    bottomFlangeStringList = [bottomFlangeInnerLength_str, bottomFlangeInnerWidth_str,
                              bottomFlangeWidth_str, bottomFlangeThickness_str,
                              bottomFlangeHoleInsetDist_str, bottomFlangeMillRadius_str]

    # top Flange Parameters
    topFlangeInnerLength_str = "topFlangeInnerLength"
    valuesDict[topFlangeInnerLength_str] = (workingLen + (2.0 * shellThickness), inch_str)
    topFlangeInnerWidth_str = "topFlangeInnerWidth"
    valuesDict[topFlangeInnerWidth_str] = (workingWidth + (2.0 * shellThickness), inch_str)
    topFlangeWidth_str = "topFlangeWidth"
    valuesDict[topFlangeWidth_str] = (flangeWidth, inch_str)
    topFlangeThickness_str = "topFlangeThickness"
    valuesDict[topFlangeThickness_str] = (flangeThickness, inch_str)
    topFlangeHoleInsetDist_str = "topFlangeHoleInsetDist"
    valuesDict[topFlangeHoleInsetDist_str] = (flangeHoleInset, inch_str)
    topFlangeMillRadius_str = "topFlangeMillRadius"
    valuesDict[topFlangeMillRadius_str] = (millRadius, inch_str)
    topFlangeStringList = [topFlangeInnerLength_str, topFlangeInnerWidth_str,
                           topFlangeWidth_str, topFlangeThickness_str,
                           topFlangeHoleInsetDist_str, topFlangeMillRadius_str]

    """
    Start of the the script for making equation files
    """
    # bottom shell walls
    bottomShellWalls = equationsFile(fullFilePath=parentDir, fileName="bottomShellWallsEquations")
    bottomShellWalls.listAddVarLine(bottomShellStringList, valuesDict)
    bottomShellWalls.addRefLine("D1@sketch1", bottomWallInnerLength_str)
    bottomShellWalls.addRefLine("D2@sketch1", bottomWallInnerWidth_str)
    bottomShellWalls.addRefLine("D3@sketch1", bottomWallThickness_str)
    bottomShellWalls.addRefLine("D1@Fillet1", bottomWallMillRadius_str)
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
    topShellWalls.addRefLine("D1@Fillet1", topWallMillRadius_str)
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
    bottomFlangeForWalls.addRefLine("D2@sketch2", bottomFlangeMillRadius_str)
    bottomFlangeForWalls.addRefLine("D1@Boss-Extrude1", bottomFlangeThickness_str)
    bottomFlangeForWalls.addRefLine("D1@Fillet1", bottomFlangeMillRadius_str)
    bottomFlangeForWalls.addRefLine("D1@Sketch3", bottomFlangeHoleInsetDist_str)
    bottomFlangeForWalls.addRefLine("D1@Fillet2", bottomFlangeHoleInsetDist_str)
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
    topFlangeForWalls.addRefLine("D2@sketch2", topFlangeMillRadius_str)
    topFlangeForWalls.addRefLine("D1@Boss-Extrude1", topFlangeThickness_str)
    topFlangeForWalls.addRefLine("D1@Fillet1", topFlangeMillRadius_str)
    topFlangeForWalls.addRefLine("D1@Sketch3", topFlangeHoleInsetDist_str)
    topFlangeForWalls.addRefLine("D1@Fillet2", topFlangeHoleInsetDist_str)
    if sys.platform == "win32":
        topFlangeForWalls.writeFile()
    else:
        print(topFlangeForWalls.fileContent)