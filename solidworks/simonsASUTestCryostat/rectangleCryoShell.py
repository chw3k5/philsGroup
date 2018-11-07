import sys
from solidworks.swVariables import equationsFile
from solidworks.simonsASUTestCryostat.cryostatParams import PhysicalParams

from solidworks.simonsASUTestCryostat.stainlessSupport import SolidWorksPart


# variables for script
parentDir = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\" + \
            "Universal Readout Harness\\ASU Test Harness\\ASU Test Cryostat\\EDM Shell"
valuesDict = {}
params = PhysicalParams()


# bottom Walls for cryostat shell parameters
bottomWallInnerLength_str = "bottomWallInnerLength"
valuesDict[bottomWallInnerLength_str] = (params.workingLen, params.inch_str)
bottomWallInnerWidth_str = "bottomWallInnerWidth"
valuesDict[bottomWallInnerWidth_str] = (params.workingWidth, params.inch_str)
bottomWallInnerDepth_str = "bottomWallInnerDepth"
valuesDict[bottomWallInnerDepth_str] = (params.workingDepthBottom, params.inch_str)
bottomWallThickness_str = "bottomWallThickness"
valuesDict[bottomWallThickness_str] = (params.shellThickness, params.inch_str)
bottomWallMillRadius_str = "bottomWallMillRadius"
valuesDict[bottomWallMillRadius_str] = (params.millRadius, params.inch_str)

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
valuesDict[topWallInnerLength_str] = (params.workingLen, params.inch_str)
topWallInnerWidth_str = "topWallInnerWidth"
valuesDict[topWallInnerWidth_str] = (params.workingWidth, params.inch_str)
topWallInnerDepth_str = "topWallInnerDepth"
valuesDict[topWallInnerDepth_str] = (params.workingDepthTop, params.inch_str)
topWallThickness_str = "topWallThickness"
valuesDict[topWallThickness_str] = (params.shellThickness, params.inch_str)
topWallMillRadius_str = "topWallMillRadius"
valuesDict[topWallMillRadius_str] = (params.millRadius, params.inch_str)
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
valuesDict[bottomFlangeInnerLength_str] = (params.workingLen + (2.0 * (params.tolerance + params.shellThickness)), params.inch_str)
bottomFlangeInnerWidth_str = "bottomFlangeInnerWidth"
valuesDict[bottomFlangeInnerWidth_str] = (params.workingWidth + (2.0 * (params.tolerance + params.shellThickness)), params.inch_str)
bottomFlangeWidth_str = "bottomFlangeWidth"
valuesDict[bottomFlangeWidth_str] = (params.flangeWidth, params.inch_str)
bottomFlangeThickness_str = "bottomFlangeThickness"
valuesDict[bottomFlangeThickness_str] = (params.flangeThickness, params.inch_str)
bottomFlangeHoleInsetDist_str = "bottomFlangeHoleInsetDist"
valuesDict[bottomFlangeHoleInsetDist_str] = (params.flangeHoleInset, params.inch_str)
bottomFlangeOringInsetDistance_str = "bottomFlangeOringInsetDistance"
valuesDict[bottomFlangeOringInsetDistance_str] = (params.oringInsetDistance, params.inch_str)
bottomFlangeMillRadius_str = "bottomFlangeMillRadius"
valuesDict[bottomFlangeMillRadius_str] = (params.millRadius, params.inch_str)
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
valuesDict[topFlangeInnerLength_str] = (params.workingLen + (2.0 * (params.tolerance + params.shellThickness)), params.inch_str)
topFlangeInnerWidth_str = "topFlangeInnerWidth"
valuesDict[topFlangeInnerWidth_str] = (params.workingWidth + (2.0 * (params.tolerance + params.shellThickness)), params.inch_str)
topFlangeWidth_str = "topFlangeWidth"
valuesDict[topFlangeWidth_str] = (params.flangeWidth, params.inch_str)
topFlangeThickness_str = "topFlangeThickness"
valuesDict[topFlangeThickness_str] = (params.flangeThickness, params.inch_str)
topFlangeHoleInsetDist_str = "topFlangeHoleInsetDist"
valuesDict[topFlangeHoleInsetDist_str] = (params.flangeHoleInset, params.inch_str)
topFlangeOringInsetDistance_str = "topFlangeOringInsetDistance"
valuesDict[topFlangeOringInsetDistance_str] = (params.oringInsetDistance, params.inch_str)
topFlangeMillRadius_str = "topFlangeMillRadius"
valuesDict[topFlangeMillRadius_str] = (params.millRadius, params.inch_str)
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
flangeAndWallsAssem.addVarLine(tolerance_str, params.tolerance, params.inch_str)
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
valuesDict[bottomWallInnerLength_str] = (params.workingLen, params.inch_str)
bottomWallInnerWidth_str = "bottomWallInnerWidth"
valuesDict[bottomWallInnerWidth_str] = (params.workingWidth, params.inch_str)
bottomWallOuterLength_str = "bottomWallOuterLength"
valuesDict[bottomWallOuterLength_str] = ((2.0 * (params.flangeWidth + params.tolerance + params.shellThickness)) + params.workingLen, params.inch_str)
bottomWallOuterWidth_str = "bottomWallOuterWidth"
valuesDict[bottomWallOuterWidth_str] = ((2.0 * (params.flangeWidth + params.tolerance + params.shellThickness)) + params.workingWidth, params.inch_str)
bottomWallThickness_str = "bottomWallThickness"
valuesDict[bottomWallThickness_str] = (params.bottomWallShellThickness, params.inch_str)
bottomWallOringInsetDistance_str = "bottomWallOringInsetDistance"
valuesDict[bottomWallOringInsetDistance_str] = (params.oringInsetDistance, params.inch_str)
bottomWallMatingFlangeMillRadius_str = "bottomWallMatingFlangeMillRadius"
valuesDict[bottomWallMatingFlangeMillRadius_str] = (params.millRadius, params.inch_str)
bottomWallHoleInsetDist_str = "bottomWallFlangeHoleInsetDist"
valuesDict[bottomWallHoleInsetDist_str] = (params.flangeHoleInset, params.inch_str)
bottomWallInsertDist_str = "BottomWallInsertDist"
valuesDict[bottomWallInsertDist_str] = (params.insertDist, params.mm_str)

bottomWallStringList = [bottomWallInnerLength_str, bottomWallInnerWidth_str,
                        bottomWallOuterLength_str, bottomWallOuterWidth_str,
                        bottomWallThickness_str, bottomWallOringInsetDistance_str,
                        bottomWallMatingFlangeMillRadius_str, bottomWallHoleInsetDist_str,
                        bottomWallInsertDist_str]

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
bottomWallAndPorts.addRefLine("D5@Sketch7", bottomWallInsertDist_str)

if sys.platform == "win32":
    bottomWallAndPorts.writeFile()
else:
    print(bottomWallAndPorts.fileContent)


# top wall (lid)
lidInnerLength_str = "lidInnerLength"
valuesDict[lidInnerLength_str] = (params.workingLen, params.inch_str)
lidInnerWidth_str = "lidInnerWidth"
valuesDict[lidInnerWidth_str] = (params.workingWidth, params.inch_str)
lidOuterLength_str = "lidOuterLength"
valuesDict[lidOuterLength_str] = ((2.0 * (params.flangeWidth + params.tolerance + params.shellThickness)) + params.workingLen, params.inch_str)
lidOuterWidth_str = "lidOuterWidth"
valuesDict[lidOuterWidth_str] = ((2.0 * (params.flangeWidth + params.tolerance + params.shellThickness)) + params.workingWidth, params.inch_str)
lidThickness_str = "lidThickness"
valuesDict[lidThickness_str] = (params.lidThickness, params.inch_str)
lidHoleInsetDist_str = "lidFlangeHoleInsetDist"
valuesDict[lidHoleInsetDist_str] = (params.flangeHoleInset, params.inch_str)

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

collar_ID_str = "collar_ID"
valuesDict[collar_ID_str] = (params.collar_ID, params.inch_str)
collar_boltCircleDiameter_str = "collar_boltCircleDiameter"
valuesDict[collar_boltCircleDiameter_str] = (params.collar_boltCircleDiameter, params.inch_str)
collar_OD_str = "collar_OD"
valuesDict[collar_OD_str] = (params.collar_OD, params.inch_str)
collar_oringID_str = "collar_oringID"
valuesDict[collar_oringID_str] = (params.collar_oringID, params.inch_str)
collar_oringWidth_str = "collar_oringWidth"
valuesDict[collar_oringWidth_str] = (params.collar_oringWidth, params.inch_str)
collar_oringDepth_str = "collar_oringDepth"
valuesDict[collar_oringDepth_str] = (params.collar_oringDepth, params.inch_str)
collar_height_str = "collar_height"
valuesDict[collar_height_str] = (params.collar_height, params.inch_str)
counterBoreDepth_str = "counterBoreDepth"
valuesDict[counterBoreDepth_str] = (((params.collar_height * params.inch_to_mm) - params.underHeadThruDistance), params.mm_str)


collarStringList = [collar_OD_str, collar_boltCircleDiameter_str,
                    collar_ID_str, collar_oringID_str,
                    collar_oringWidth_str, collar_oringDepth_str,
                    collar_height_str, counterBoreDepth_str]

# Collar Extension for Coldhead
collar = equationsFile(fullFilePath=parentDir, fileName="collarEquations")
collar.listAddVarLine(collarStringList, valuesDict)
collar.addRefLine("D1@sketch1", collar_ID_str)
collar.addRefLine("D2@sketch1", collar_OD_str)
collar.addRefLine("D4@sketch1", collar_boltCircleDiameter_str)
collar.addRefLine("D1@Boss-Extrude1", collar_height_str)
collar.addRefLine("C'Bore Depth@Sketch4", counterBoreDepth_str)
collar.addRefLine("D1@sketch7", collar_oringID_str)
collar.addRefLine("D1@Cut-Extrude-Thin1", collar_oringDepth_str)
collar.addRefLine("D5@Cut-Extrude-Thin1", collar_oringWidth_str)
collar.addRefLine("D1@sketch8", collar_oringID_str)
collar.addRefLine("D1@Cut-Extrude-Thin2", collar_oringDepth_str)
collar.addRefLine("D5@Cut-Extrude-Thin2", collar_oringWidth_str)

if sys.platform == "win32":
    collar.writeFile()
else:
    print(collar.fileContent)