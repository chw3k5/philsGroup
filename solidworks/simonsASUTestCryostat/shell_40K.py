import sys
from solidworks.swVariables import equationsFile
from solidworks.simonsASUTestCryostat.cryostatParams import PhysicalParams

parentDir = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\" + \
            "Universal Readout Harness\\ASU Test Cryostat\\40 K"
params = PhysicalParams()
valuesDict = {}




"""
Left Bottom Flange
"""
# Left side (viewed from above and with the cold head at the "front") bottom flange at 40k
leftBottomFlangeCornerReferenceScrewInsetX_str = "leftBottomFlangeCornerReferenceScrewInsetX"
valuesDict[leftBottomFlangeCornerReferenceScrewInsetX_str] = (params.leftBottomFlangeCornerReferenceScrewInsetX, params.mm_str)
leftBottomFlangeCornerReferenceScrewInsetZ_str = "leftBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[leftBottomFlangeCornerReferenceScrewInsetZ_str] = (params.leftBottomFlangeCornerReferenceScrewInsetZ, params.mm_str)

leftBottomFlange_lengthX_str = "leftBottomFlange_lengthX"
valuesDict[leftBottomFlange_lengthX_str] = (params.leftBottomFlange_lengthX, params.mm_str)
leftBottomFlange_widthZ_str = "leftBottomFlange_widthZ"
valuesDict[leftBottomFlange_widthZ_str] = (params.leftBottomFlange_widthZ, params.mm_str)

leftBottomFlange_thickness_str = "leftBottomFlange_thickness"
valuesDict[leftBottomFlange_thickness_str] = (params.bottomFlangeThickness, params.inch_str)

refHole_to_smallSideNextHoleX_str = "refHole_to_smallSideNextHoleX"
valuesDict[refHole_to_smallSideNextHoleX_str] = (params.refHole_to_smallSideNextHoleX, params.mm_str)
refHole_to_smallSideNextHoleZ_str = "refHole_to_smallSideNextHoleZ"
valuesDict[refHole_to_smallSideNextHoleZ_str] = (params.refHole_to_smallSideNextHoleZ, params.mm_str)
smallSideHole_CenterToCenter_str = "smallSideHole_CenterToCenter"
valuesDict[smallSideHole_CenterToCenter_str] = (params.smallSideHole_CenterToCenter, params.mm_str)

bottomShellStringList = [leftBottomFlangeCornerReferenceScrewInsetX_str, leftBottomFlangeCornerReferenceScrewInsetZ_str,
                         leftBottomFlange_lengthX_str, leftBottomFlange_widthZ_str,
                         leftBottomFlange_thickness_str, refHole_to_smallSideNextHoleX_str,
                         refHole_to_smallSideNextHoleZ_str, smallSideHole_CenterToCenter_str]

leftBottomFlange = equationsFile(fullFilePath=parentDir, fileName="leftBottomFlangeEquations")
leftBottomFlange.listAddVarLine(bottomShellStringList, valuesDict)
leftBottomFlange.addRefLine("D5@sketch1", leftBottomFlangeCornerReferenceScrewInsetX_str)
leftBottomFlange.addRefLine("D2@sketch1", leftBottomFlangeCornerReferenceScrewInsetZ_str)
leftBottomFlange.addRefLine("D4@sketch1", leftBottomFlange_lengthX_str)
leftBottomFlange.addRefLine("D3@sketch1", leftBottomFlange_widthZ_str)
leftBottomFlange.addRefLine("D1@Boss-Extrude1", leftBottomFlange_thickness_str)
leftBottomFlange.addRefLine("D1@sketch2", refHole_to_smallSideNextHoleX_str)
leftBottomFlange.addRefLine("D2@sketch2", refHole_to_smallSideNextHoleZ_str)
leftBottomFlange.addRefLine("D3@sketch2", smallSideHole_CenterToCenter_str)

if sys.platform == "win32":
    leftBottomFlange.writeFile()
else:
    print(leftBottomFlange.fileContent)

"""Rear Bottom Flange"""

# Calculations for Rear Bottom Flange
rearBottomFlangeCornerReferenceScrewInsetX = params.rearExtensionDistance + params.refHole_to_edgeX
rearBottomFlangeCornerReferenceScrewInsetZ = abs(params.expected_edgeOverLap - params.refHole_to_edgeZ)
rearBottomFlange_lengthX = params.rearExtensionDistance + params.expected_edgeOverLap
rearBottomFlange_widthZ = params.insert40K_Z - (2.0 * params.expected_edgeOverLap)

# Rear side (viewed from above and with the cold head at the "front") bottom flange at 40k
rearBottomFlangeCornerReferenceScrewInsetX_str = "rearBottomFlangeCornerReferenceScrewInsetX"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetX_str] = (rearBottomFlangeCornerReferenceScrewInsetX, params.mm_str)
rearBottomFlangeCornerReferenceScrewInsetZ_str = "rearBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetZ_str] = (rearBottomFlangeCornerReferenceScrewInsetZ, params.mm_str)

rearBottomFlange_lengthX_str = "rearBottomFlange_lengthX"
valuesDict[rearBottomFlange_lengthX_str] = (rearBottomFlange_lengthX, params.mm_str)
rearBottomFlange_widthZ_str = "rearBottomFlange_widthZ"
valuesDict[rearBottomFlange_widthZ_str] = (rearBottomFlange_widthZ, params.mm_str)

rearBottomFlange_thickness_str = "rearBottomFlange_thickness"
valuesDict[rearBottomFlange_thickness_str] = (params.bottomFlangeThickness, params.inch_str)

refHole_to_largeSideNextHoleX_str = "refHole_to_largeSideNextHoleX"
valuesDict[refHole_to_largeSideNextHoleX_str] = (params.refHole_to_largeSideNextHoleX, params.mm_str)
refHole_to_largeSideNextHoleZ_str = "refHole_to_largeSideNextHoleZ"
valuesDict[refHole_to_largeSideNextHoleZ_str] = (params.refHole_to_largeSideNextHoleZ, params.mm_str)
largeSideHole_CenterToCenter_str = "largeSideHole_CenterToCenter"
valuesDict[largeSideHole_CenterToCenter_str] = (params.largeSideHole_CenterToCenter, params.mm_str)

bottomLefFlange_softCornerRadius_str = "bottomLefFlange_softCornerRadius"
valuesDict[bottomLefFlange_softCornerRadius_str] = (params.millRadius, params.inch_str)


bottomShellStringList = [rearBottomFlangeCornerReferenceScrewInsetX_str, rearBottomFlangeCornerReferenceScrewInsetZ_str,
                         rearBottomFlange_lengthX_str, rearBottomFlange_widthZ_str,
                         rearBottomFlange_thickness_str, refHole_to_largeSideNextHoleX_str,
                         refHole_to_largeSideNextHoleZ_str, largeSideHole_CenterToCenter_str,
                         bottomLefFlange_softCornerRadius_str]

rearBottomFlange = equationsFile(fullFilePath=parentDir, fileName="rearBottomFlangeEquations")
rearBottomFlange.listAddVarLine(bottomShellStringList, valuesDict)
rearBottomFlange.addRefLine("D1@sketch1", rearBottomFlangeCornerReferenceScrewInsetX_str)
rearBottomFlange.addRefLine("D2@sketch1", rearBottomFlangeCornerReferenceScrewInsetZ_str)
rearBottomFlange.addRefLine("D3@sketch1", rearBottomFlange_lengthX_str)
rearBottomFlange.addRefLine("D4@sketch1", rearBottomFlange_widthZ_str)
rearBottomFlange.addRefLine("D1@Boss-Extrude1", rearBottomFlange_thickness_str)
rearBottomFlange.addRefLine("D1@sketch2", refHole_to_largeSideNextHoleX_str)
rearBottomFlange.addRefLine("D2@sketch2", refHole_to_largeSideNextHoleZ_str)
rearBottomFlange.addRefLine("D3@sketch2", largeSideHole_CenterToCenter_str)
rearBottomFlange.addRefLine("D1@Fillet1", bottomLefFlange_softCornerRadius_str)

if sys.platform == "win32":
    rearBottomFlange.writeFile()
else:
    print(rearBottomFlange.fileContent)


"""Left Wall"""
# Left side (viewed from above and with the cold head at the "front") wall at 40k
leftWallLengthX_str = "leftWallLengthX"
valuesDict[leftWallLengthX_str] = (params.leftBottomFlange_lengthX, params.mm_str)
leftWallHalfWidthZ_str = "leftWallHalfWidthZ"
valuesDict[leftWallHalfWidthZ_str] = ((rearBottomFlange_widthZ / 2.0) + params.leftBottomFlange_widthZ, params.mm_str)
leftWallBendRadius_str = "leftWallBendRadius"
valuesDict[leftWallBendRadius_str] = (params.millRadius, params.inch_str)

leftWallHeightY_str = "leftWallHeightY"
valuesDict[leftWallHeightY_str] = (params.shield_40K_workingHeight - (2.0 * params.shieldThickness), params.mm_str)

leftWallThickness_str = "leftWallThickness"
valuesDict[leftWallThickness_str] = (params.shieldThickness, params.inch_str)
bottomShellStringList = [leftWallLengthX_str, leftWallHalfWidthZ_str,
                         leftWallBendRadius_str,
                         leftWallHeightY_str, leftWallThickness_str]

leftWall = equationsFile(fullFilePath=parentDir, fileName="leftWallsEquations")
leftWall.listAddVarLine(bottomShellStringList, valuesDict)
leftWall.addRefLine("D1@sketch1", leftWallLengthX_str)
leftWall.addRefLine("D2@sketch1", leftWallHalfWidthZ_str)
leftWall.addRefLine("D3@sketch1", leftWallBendRadius_str)
leftWall.addRefLine("D1@Extrude-Thin1", leftWallHeightY_str)
leftWall.addRefLine("D5@Extrude-Thin1", leftWallThickness_str)

if sys.platform == "win32":
    leftWall.writeFile()
    print(leftWall.fileContent)
else:
    print(leftWall.fileContent)
