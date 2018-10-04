import sys
from solidworks.swVariables import equationsFile
from solidworks.simonsASUTestCryostat.rectangleCryoShell import inch_str, mm_str, inch_to_mm,\
    workingLen, workingWidth, workingDepthBottom, workingDepthTop, millRadius

parentDir = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\" + \
            "Universal Readout Harness\\ASU Test Cryostat\\40 K"
valuesDict = {}
"""
controlled values
"""
sheildThickness = (1.0/8.0)  # inches
rearExtensionDistance = 40.0
leftExtensionDistance = rearExtensionDistance
rightExtensionDistance = rearExtensionDistance
frontExtensionDistance = 150.0
shellHeight = 2000.0


"""
measured values
"""
insert40K_X = 300.0
insert40K_Z = 400.0
expected_edgeOverLap = 15.0

refHole_to_edgeX = 10.935
refHole_to_edgeZ = 14.58

# 2 corner holes, 4 edge holes
refHole_to_smallSideNextHoleX = 53.721
refHole_to_smallSideNextHoleZ = 7.0485
smallSideHole_CenterToCenter = 56.896

# 2 corner holes, 6 edge holes
refHole_to_largeSideNextHoleX = 3.175
refHole_to_largeSideNextHoleZ = 47.9425
largeSideHole_CenterToCenter = 54.991

# Calculations for Left Bottom Flange
leftBottomFlangeCornerReferenceScrewInsetX = rearExtensionDistance + refHole_to_edgeX
leftBottomFlangeCornerReferenceScrewInsetZ = expected_edgeOverLap - refHole_to_edgeZ
leftBottomFlange_lengthX = rearExtensionDistance + insert40K_X + frontExtensionDistance
leftBottomFlange_widthZ = expected_edgeOverLap + leftExtensionDistance

"""
Left Bottom Flange
"""
# Left side (viewed from above and with the cold head at the "front") bottom flange at 40k
leftBottomFlangeCornerReferenceScrewInsetX_str = "leftBottomFlangeCornerReferenceScrewInsetX"
valuesDict[leftBottomFlangeCornerReferenceScrewInsetX_str] = (leftBottomFlangeCornerReferenceScrewInsetX, mm_str)
leftBottomFlangeCornerReferenceScrewInsetZ_str = "leftBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[leftBottomFlangeCornerReferenceScrewInsetZ_str] = (leftBottomFlangeCornerReferenceScrewInsetZ, mm_str)

leftBottomFlange_lengthX_str = "leftBottomFlange_lengthX"
valuesDict[leftBottomFlange_lengthX_str] = (leftBottomFlange_lengthX, mm_str)
leftBottomFlange_widthZ_str = "leftBottomFlange_widthZ"
valuesDict[leftBottomFlange_widthZ_str] = (leftBottomFlange_widthZ, mm_str)

leftBottomFlange_thickness_str = "leftBottomFlange_thickness"
valuesDict[leftBottomFlange_thickness_str] = (sheildThickness, inch_str)

refHole_to_smallSideNextHoleX_str = "refHole_to_smallSideNextHoleX"
valuesDict[refHole_to_smallSideNextHoleX_str] = (refHole_to_smallSideNextHoleX, mm_str)
refHole_to_smallSideNextHoleZ_str = "refHole_to_smallSideNextHoleZ"
valuesDict[refHole_to_smallSideNextHoleZ_str] = (refHole_to_smallSideNextHoleZ, mm_str)
smallSideHole_CenterToCenter_str = "smallSideHole_CenterToCenter"
valuesDict[smallSideHole_CenterToCenter_str] = (smallSideHole_CenterToCenter, mm_str)

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
rearBottomFlangeCornerReferenceScrewInsetX = rearExtensionDistance + refHole_to_edgeX
rearBottomFlangeCornerReferenceScrewInsetZ = abs(expected_edgeOverLap - refHole_to_edgeZ)
rearBottomFlange_lengthX = rearExtensionDistance + expected_edgeOverLap
rearBottomFlange_widthZ = insert40K_Z - (2.0 * expected_edgeOverLap)

# Rear side (viewed from above and with the cold head at the "front") bottom flange at 40k
rearBottomFlangeCornerReferenceScrewInsetX_str = "rearBottomFlangeCornerReferenceScrewInsetX"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetX_str] = (rearBottomFlangeCornerReferenceScrewInsetX, mm_str)
rearBottomFlangeCornerReferenceScrewInsetZ_str = "rearBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetZ_str] = (rearBottomFlangeCornerReferenceScrewInsetZ, mm_str)

rearBottomFlange_lengthX_str = "rearBottomFlange_lengthX"
valuesDict[rearBottomFlange_lengthX_str] = (rearBottomFlange_lengthX, mm_str)
rearBottomFlange_widthZ_str = "rearBottomFlange_widthZ"
valuesDict[rearBottomFlange_widthZ_str] = (rearBottomFlange_widthZ, mm_str)

rearBottomFlange_thickness_str = "rearBottomFlange_thickness"
valuesDict[rearBottomFlange_thickness_str] = (sheildThickness, inch_str)

refHole_to_largeSideNextHoleX_str = "refHole_to_largeSideNextHoleX"
valuesDict[refHole_to_largeSideNextHoleX_str] = (refHole_to_largeSideNextHoleX, mm_str)
refHole_to_largeSideNextHoleZ_str = "refHole_to_largeSideNextHoleZ"
valuesDict[refHole_to_largeSideNextHoleZ_str] = (refHole_to_largeSideNextHoleZ, mm_str)
largeSideHole_CenterToCenter_str = "largeSideHole_CenterToCenter"
valuesDict[largeSideHole_CenterToCenter_str] = (largeSideHole_CenterToCenter, mm_str)

bottomLefFlange_softCornerRadius_str = "bottomLefFlange_softCornerRadius"
valuesDict[bottomLefFlange_softCornerRadius_str] = (millRadius, inch_str)


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
valuesDict[leftWallLengthX_str] = (leftBottomFlange_lengthX, mm_str)
leftWallHalfWidthZ_str = "leftWallHalfWidthZ"
valuesDict[leftWallHalfWidthZ_str] = (leftBottomFlange_widthZ / 2.0, mm_str)
leftWallHeightY_str = "leftWallHeightY"
valuesDict[leftWallHeightY_str] = (shellHeight - (2.0 * sheildThickness), mm_str)

leftWallThickness_str = "leftWallThickness"
valuesDict[leftWallThickness_str] = (sheildThickness, inch_str)


bottomShellStringList = []

leftWall = equationsFile(fullFilePath=parentDir, fileName="rearBottomFlangeEquations")
leftWall.listAddVarLine(bottomShellStringList, valuesDict)
leftWall.addRefLine("D1@sketch1", rearBottomFlangeCornerReferenceScrewInsetX_str)

if sys.platform == "win32":
    leftWall.writeFile()
else:
    print(leftWall.fileContent)