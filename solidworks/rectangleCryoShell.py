import sys
from solidworks.swVariables import equationsFile



# variables for script
parentDir = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\" + \
            "Universal Readout Harness\\ASU Test Cryostat\\EDM Shell"
valuesDict = {}
inch_str = "in"
(workingLen, workingWidth, workingDepthBottom, workingDepthTop) = (23.0, 20.0, 9.0, 9.0)
shellThickness = 0.375
bottomWallShellThickness = 0.5
lidThickness = 0.5
oringInsetDistance = 0.4
millRadius = 2.0
flangeWidth = 1.5
flangeThickness = 0.5
flangeHoleInset = 0.4
tolerance = 0.005

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

# bottom Flange Parameters
bottomFlangeInnerLength_str = "bottomFlangeInnerLength"
valuesDict[bottomFlangeInnerLength_str] = (workingLen + (2.0 * (tolerance + shellThickness)), inch_str)
bottomFlangeInnerWidth_str = "bottomFlangeInnerWidth"
valuesDict[bottomFlangeInnerWidth_str] = (workingWidth + (2.0 * (tolerance + shellThickness)), inch_str)
bottomFlangeWidth_str = "bottomFlangeWidth"
valuesDict[bottomFlangeWidth_str] = (flangeWidth, inch_str)
bottomFlangeThickness_str = "bottomFlangeThickness"
valuesDict[bottomFlangeThickness_str] = (flangeThickness, inch_str)
bottomFlangeHoleInsetDist_str = "bottomFlangeHoleInsetDist"
valuesDict[bottomFlangeHoleInsetDist_str] = (flangeHoleInset, inch_str)
bottomFlangeOringInsetDistance_str = "bottomFlangeOringInsetDistance"
valuesDict[bottomFlangeOringInsetDistance_str] = (oringInsetDistance, inch_str)
bottomFlangeMillRadius_str = "bottomFlangeMillRadius"
valuesDict[bottomFlangeMillRadius_str] = (millRadius, inch_str)
bottomFlangeStringList = [bottomFlangeInnerLength_str, bottomFlangeInnerWidth_str,
                          bottomFlangeWidth_str, bottomFlangeThickness_str,
                          bottomFlangeHoleInsetDist_str, bottomFlangeMillRadius_str]

# bottom flange for walls
bottomFlangeForWalls = equationsFile(fullFilePath=parentDir, fileName="bottomFlangeForWallsEquations")
bottomFlangeForWalls.listAddVarLine(bottomFlangeStringList, valuesDict)
bottomFlangeForWalls.addRefLine("D1@sketch1", bottomFlangeInnerLength_str)
bottomFlangeForWalls.addRefLine("D2@sketch1", bottomFlangeInnerWidth_str)
bottomFlangeForWalls.addRefLine("D3@sketch1", bottomFlangeWidth_str)
bottomFlangeForWalls.addRefLine("D1@sketch2", bottomFlangeOringInsetDistance_str)
bottomFlangeForWalls.addRefLine("D2@sketch2", bottomFlangeMillRadius_str)
bottomFlangeForWalls.addRefLine("D1@Boss-Extrude1", bottomFlangeThickness_str)
bottomFlangeForWalls.addRefLine("D1@Fillet1", bottomFlangeMillRadius_str)
bottomFlangeForWalls.addRefLine("D1@Sketch3", bottomFlangeHoleInsetDist_str)
bottomFlangeForWalls.addRefLine("D1@Fillet2", bottomFlangeHoleInsetDist_str)
if sys.platform == "win32":
    bottomFlangeForWalls.writeFile()
else:
    print(bottomFlangeForWalls.fileContent)

# top Flange Parameters
topFlangeInnerLength_str = "topFlangeInnerLength"
valuesDict[topFlangeInnerLength_str] = (workingLen + (2.0 * (tolerance + shellThickness)), inch_str)
topFlangeInnerWidth_str = "topFlangeInnerWidth"
valuesDict[topFlangeInnerWidth_str] = (workingWidth + (2.0 * (tolerance + shellThickness)), inch_str)
topFlangeWidth_str = "topFlangeWidth"
valuesDict[topFlangeWidth_str] = (flangeWidth, inch_str)
topFlangeThickness_str = "topFlangeThickness"
valuesDict[topFlangeThickness_str] = (flangeThickness, inch_str)
topFlangeHoleInsetDist_str = "topFlangeHoleInsetDist"
valuesDict[topFlangeHoleInsetDist_str] = (flangeHoleInset, inch_str)
topFlangeOringInsetDistance_str = "topFlangeOringInsetDistance"
valuesDict[topFlangeOringInsetDistance_str] = (oringInsetDistance, inch_str)
topFlangeMillRadius_str = "topFlangeMillRadius"
valuesDict[topFlangeMillRadius_str] = (millRadius, inch_str)
topFlangeStringList = [topFlangeInnerLength_str, topFlangeInnerWidth_str,
                       topFlangeWidth_str, topFlangeThickness_str,
                       topFlangeHoleInsetDist_str, topFlangeMillRadius_str]

# top flange for walls
topFlangeForWalls = equationsFile(fullFilePath=parentDir, fileName="topFlangeForWallsEquations")
topFlangeForWalls.listAddVarLine(topFlangeStringList, valuesDict)
topFlangeForWalls.addRefLine("D1@sketch1", topFlangeInnerLength_str)
topFlangeForWalls.addRefLine("D2@sketch1", topFlangeInnerWidth_str)
topFlangeForWalls.addRefLine("D3@sketch1", topFlangeWidth_str)
topFlangeForWalls.addRefLine("D1@sketch2", topFlangeOringInsetDistance_str)
topFlangeForWalls.addRefLine("D2@sketch2", topFlangeMillRadius_str)
topFlangeForWalls.addRefLine("D1@Boss-Extrude1", topFlangeThickness_str)
topFlangeForWalls.addRefLine("D1@Fillet1", topFlangeMillRadius_str)
topFlangeForWalls.addRefLine("D1@Sketch3", topFlangeHoleInsetDist_str)
topFlangeForWalls.addRefLine("D1@Fillet2", topFlangeHoleInsetDist_str)
if sys.platform == "win32":
    topFlangeForWalls.writeFile()
else:
    print(topFlangeForWalls.fileContent)

# flange and walls assembly
tolerance_str = "tolerance"

# flange and walls assembly
flangeAndWallsAssem = equationsFile(fullFilePath=parentDir, fileName="flangeAndWallsAssemEquations")
flangeAndWallsAssem.addVarLine(tolerance_str, tolerance, inch_str)
flangeAndWallsAssem.addRefLine("D1@Distance1", tolerance_str)
flangeAndWallsAssem.addRefLine("D1@Distance2", tolerance_str)
flangeAndWallsAssem.addRefLine("D1@Distance3", tolerance_str)
flangeAndWallsAssem.addRefLine("D1@Distance4", tolerance_str)
if sys.platform == "win32":
    flangeAndWallsAssem.writeFile()
else:
    print(flangeAndWallsAssem.fileContent)

# bottom wall (insert and coldhead)
bottomWallInnerLength_str = "bottomWallInnerLength"
valuesDict[bottomWallInnerLength_str] = (workingLen, inch_str)
bottomWallInnerWidth_str = "bottomWallInnerWidth"
valuesDict[bottomWallInnerWidth_str] = (workingWidth, inch_str)
bottomWallOuterLength_str = "bottomWallOuterLength"
valuesDict[bottomWallOuterLength_str] = ((2.0 * (flangeWidth + tolerance + shellThickness)) + workingLen, inch_str)
bottomWallOuterWidth_str = "bottomWallOuterWidth"
valuesDict[bottomWallOuterWidth_str] = ((2.0 * (flangeWidth + tolerance + shellThickness)) + workingWidth, inch_str)
bottomWallThickness_str = "bottomWallThickness"
valuesDict[bottomWallThickness_str] = (bottomWallShellThickness, inch_str)
bottomWallOringInsetDistance_str = "bottomWallOringInsetDistance"
valuesDict[bottomWallOringInsetDistance_str] = (oringInsetDistance, inch_str)
bottomWallMatingFlangeMillRadius_str = "bottomWallMatingFlangeMillRadius"
valuesDict[bottomWallMatingFlangeMillRadius_str] = (millRadius, inch_str)
bottomWallHoleInsetDist_str = "bottomWallFlangeHoleInsetDist"
valuesDict[bottomWallHoleInsetDist_str] = (flangeHoleInset, inch_str)

bottomWallStringList = [bottomWallInnerLength_str, bottomWallInnerWidth_str,
                        bottomWallOuterLength_str, bottomWallOuterWidth_str,
                        bottomWallThickness_str, bottomWallOringInsetDistance_str,
                        bottomWallMatingFlangeMillRadius_str, bottomWallHoleInsetDist_str]

# bottom wall (insert and coldhead)
bottomWallAndPorts = equationsFile(fullFilePath=parentDir, fileName="bottomWallAndPortsEquations")
bottomWallAndPorts.listAddVarLine(bottomWallStringList, valuesDict)
bottomWallAndPorts.addRefLine("D3@sketch1", bottomWallOuterLength_str)
bottomWallAndPorts.addRefLine("D4@sketch1", bottomWallOuterWidth_str)
bottomWallAndPorts.addRefLine("D1@sketch1", bottomWallInnerLength_str)
bottomWallAndPorts.addRefLine("D2@sketch1", bottomWallInnerWidth_str)
bottomWallAndPorts.addRefLine("D1@Bottom Plate", bottomWallThickness_str)
bottomWallAndPorts.addRefLine("D1@Sketch13", bottomWallOringInsetDistance_str)
bottomWallAndPorts.addRefLine("D2@Sketch13", bottomWallMatingFlangeMillRadius_str)
bottomWallAndPorts.addRefLine("D1@Fillet1", bottomWallHoleInsetDist_str)
bottomWallAndPorts.addRefLine("D1@Sketch14", bottomWallHoleInsetDist_str)

if sys.platform == "win32":
    bottomWallAndPorts.writeFile()
else:
    print(bottomWallAndPorts.fileContent)


# top wall (lid)
lidInnerLength_str = "lidInnerLength"
valuesDict[lidInnerLength_str] = (workingLen, inch_str)
lidInnerWidth_str = "lidInnerWidth"
valuesDict[lidInnerWidth_str] = (workingWidth, inch_str)
lidOuterLength_str = "lidOuterLength"
valuesDict[lidOuterLength_str] = ((2.0 * (flangeWidth + tolerance + shellThickness)) + workingLen, inch_str)
lidOuterWidth_str = "lidOuterWidth"
valuesDict[lidOuterWidth_str] = ((2.0 * (flangeWidth + tolerance + shellThickness)) + workingWidth, inch_str)
lidThickness_str = "lidThickness"
valuesDict[lidThickness_str] = (lidThickness, inch_str)
lidHoleInsetDist_str = "lidFlangeHoleInsetDist"
valuesDict[lidHoleInsetDist_str] = (flangeHoleInset, inch_str)

lidStringList = [lidInnerLength_str, lidInnerWidth_str,
                        lidOuterLength_str, lidOuterWidth_str,
                        lidThickness_str, lidHoleInsetDist_str]

# top wall (insert and coldhead)
lid = equationsFile(fullFilePath=parentDir, fileName="lidEquations")
lid.listAddVarLine(lidStringList, valuesDict)
lid.addRefLine("D1@sketch1", lidInnerLength_str)
lid.addRefLine("D2@sketch1", lidInnerWidth_str)
lid.addRefLine("D3@sketch1", lidOuterLength_str)
lid.addRefLine("D4@sketch1", lidOuterWidth_str)
lid.addRefLine("D1@Boss-Extrude1", lidThickness_str)
lid.addRefLine("D1@Fillet1", lidHoleInsetDist_str)
lid.addRefLine("D1@Sketch2", lidHoleInsetDist_str)

if sys.platform == "win32":
    lid.writeFile()
else:
    print(lid.fileContent)