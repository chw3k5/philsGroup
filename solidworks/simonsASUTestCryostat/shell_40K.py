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



# Rear side (viewed from above and with the cold head at the "front") bottom flange at 40k
rearBottomFlangeCornerReferenceScrewInsetX_str = "rearBottomFlangeCornerReferenceScrewInsetX"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetX_str] = (params.rearBottomFlangeCornerReferenceScrewInsetX, params.mm_str)
rearBottomFlangeCornerReferenceScrewInsetZ_str = "rearBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetZ_str] = (params.rearBottomFlangeCornerReferenceScrewInsetZ, params.mm_str)

rearBottomFlange_lengthX_str = "rearBottomFlange_lengthX"
valuesDict[rearBottomFlange_lengthX_str] = (params.rearBottomFlange_lengthX, params.mm_str)
rearBottomFlange_widthZ_str = "rearBottomFlange_widthZ"
valuesDict[rearBottomFlange_widthZ_str] = (params.rearBottomFlange_widthZ, params.mm_str)

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
valuesDict[leftWallHalfWidthZ_str] = (params.Wall40K_halfWidthZ, params.mm_str)
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

"""Rear and Front Top Flange"""
# Rear and Front (viewed from above and with the cold head at the "front") Flanges at 40k
RearAndFrontTopFlangeLenX_str = "RearAndFrontTopFlangeLenX"
valuesDict[RearAndFrontTopFlangeLenX_str] = (params.RearAndFrontTopFlangeLenX, params.mm_str)
RearAndFrontTopFlangeBendRadius_str = "RearAndFrontTopFlangeBendRadius"
valuesDict[RearAndFrontTopFlangeBendRadius_str] = (params.RearAndFrontTopFlangeBendRadius, params.inch_str)
bottomShellStringList = [RearAndFrontTopFlangeLenX_str]
RearAndFrontTopFlangeInPlaneWidth_str = "RearAndFrontTopFlangeInPlaneWidth"
valuesDict[RearAndFrontTopFlangeInPlaneWidth_str] = (params.shieldsTopFlangeWidth, params.mm_str)
RearAndFrontTopFlangeThickness_str = "RearAndFrontTopFlangeThickness"
valuesDict[RearAndFrontTopFlangeThickness_str] = (params.shieldsTopFlangeThickness, params.inch_str)

RearAndFrontTopFlangeStringList = [RearAndFrontTopFlangeLenX_str, RearAndFrontTopFlangeBendRadius_str,
                                   RearAndFrontTopFlangeInPlaneWidth_str, RearAndFrontTopFlangeThickness_str]

RearAndFrontTopFlange = equationsFile(fullFilePath=parentDir, fileName="RearAndFrontTopFlangeEquations")
RearAndFrontTopFlange.listAddVarLine(RearAndFrontTopFlangeStringList, valuesDict)
RearAndFrontTopFlange.addRefLine("D1@sketch1", RearAndFrontTopFlangeLenX_str)
RearAndFrontTopFlange.addRefLine("D2@sketch1", RearAndFrontTopFlangeBendRadius_str)
RearAndFrontTopFlange.addRefLine("D4@sketch1", RearAndFrontTopFlangeInPlaneWidth_str)
RearAndFrontTopFlange.addRefLine("D5@Extrude-Thin1", RearAndFrontTopFlangeInPlaneWidth_str)
RearAndFrontTopFlange.addRefLine("D1@Extrude-Thin1", RearAndFrontTopFlangeThickness_str)

if sys.platform == "win32":
    RearAndFrontTopFlange.writeFile()
    print(RearAndFrontTopFlange.fileContent)
else:
    print(RearAndFrontTopFlange.fileContent)

"""Left and Right Top Flange"""
# Rear and Front (viewed from above and with the cold head at the "front") Flanges at 40k
LeftAndRightTopFlangeLen_str = "LeftAndRightTopFlangeLen"
valuesDict[LeftAndRightTopFlangeLen_str] = (params.LeftAndRightTopFlangeLen, params.mm_str)
bottomShellStringList = [LeftAndRightTopFlangeLen_str]
LeftAndRightTopFlangeInPlaneWidth_str = "LeftAndRightTopFlangeInPlaneWidth"
valuesDict[LeftAndRightTopFlangeInPlaneWidth_str] = (params.shieldsTopFlangeWidth, params.mm_str)
shieldsLeftAndRightTopFlangeScrewInsertDist_str = "shieldsLeftAndRightTopFlangeScrewInsertDist"
valuesDict[shieldsLeftAndRightTopFlangeScrewInsertDist_str] = (params.shieldsLeftAndRightTopFlangeScrewInsertDist,
                                                               params.inch_str)
LeftAndRightTopFlangeThickness_str = "LeftAndRightTopFlangeThickness"
valuesDict[LeftAndRightTopFlangeThickness_str] = (params.shieldsTopFlangeThickness, params.inch_str)

LeftAndRightTopFlangeStringList = [LeftAndRightTopFlangeLen_str, LeftAndRightTopFlangeInPlaneWidth_str,
                                   shieldsLeftAndRightTopFlangeScrewInsertDist_str, LeftAndRightTopFlangeThickness_str]

LeftAndRightTopFlange = equationsFile(fullFilePath=parentDir, fileName="LeftAndRightTopFlangeEquations")
LeftAndRightTopFlange.listAddVarLine(LeftAndRightTopFlangeStringList, valuesDict)
LeftAndRightTopFlange.addRefLine("D1@sketch1", LeftAndRightTopFlangeLen_str)
LeftAndRightTopFlange.addRefLine("D2@sketch1", LeftAndRightTopFlangeInPlaneWidth_str)
LeftAndRightTopFlange.addRefLine("D3@Sketch1", shieldsLeftAndRightTopFlangeScrewInsertDist_str)
LeftAndRightTopFlange.addRefLine("D1@Boss-Extrude1", LeftAndRightTopFlangeThickness_str)

if sys.platform == "win32":
    LeftAndRightTopFlange.writeFile()
    print(LeftAndRightTopFlange.fileContent)
else:
    print(LeftAndRightTopFlange.fileContent)

# flange and walls assembly
tolerance_str = "tolerance"

# flange and walls assembly
ShieldAssem40K = equationsFile(fullFilePath=parentDir, fileName="ShieldAssem40K")
ShieldAssem40K.addVarLine(tolerance_str, params.tolerance, params.inch_str)
ShieldAssem40K.addRefLine("D1@Distance1", tolerance_str)
ShieldAssem40K.addRefLine("D1@Distance2", tolerance_str)

if sys.platform == "win32":
    ShieldAssem40K.writeFile()
else:
    print(ShieldAssem40K.fileContent)

"""Lid"""
# The Lid of the 40k shields
LidLeftRightLen_str = "LidLeftRightLen"
valuesDict[LidLeftRightLen_str] = (params.LidLeftRightLen, params.mm_str)
LidRearFrontLen_str = "LidRearFrontLen"
valuesDict[LidRearFrontLen_str] = (params.LidRearFrontLen, params.mm_str)
LidMillRadius_str = "LidMillRadius"
valuesDict[LidMillRadius_str] = (params.LidMillRadius, params.mm_str)
LidHoles_InsetDist_str = "LidHoles_HalfFlangeDist"
valuesDict[LidHoles_InsetDist_str] = (params.LidHoles_InsetDist, params.mm_str)

LeftAndRightTopFlangeStringList = [LidLeftRightLen_str, LidRearFrontLen_str,
                                   LidMillRadius_str, LidHoles_InsetDist_str,
                                   shieldsLeftAndRightTopFlangeScrewInsertDist_str]

Lid = equationsFile(fullFilePath=parentDir, fileName="LidEquations")
Lid.listAddVarLine(LeftAndRightTopFlangeStringList, valuesDict)
Lid.addRefLine("D1@sketch1", LidLeftRightLen_str)
Lid.addRefLine("D2@sketch1", LidRearFrontLen_str)
Lid.addRefLine("D3@Sketch1", LidMillRadius_str)
Lid.addRefLine("D4@Sketch1", LidHoles_InsetDist_str)
Lid.addRefLine("D5@Sketch1", LidHoles_InsetDist_str)
Lid.addRefLine("D1@Sketch1", shieldsLeftAndRightTopFlangeScrewInsertDist_str)

if sys.platform == "win32":
    Lid.writeFile()
    print(Lid.fileContent)
else:
    print(Lid.fileContent)
