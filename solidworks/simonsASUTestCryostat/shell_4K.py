import sys
from solidworks.swVariables import equationsFile
from solidworks.simonsASUTestCryostat.cryostatParams import PhysicalParams

parentDir = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\" + \
            "Universal Readout Harness\\ASU Test Harness\\ASU Test Cryostat\\4 K"
params = PhysicalParams()
valuesDict = {}

"""
Left Bottom Flange
"""
# Left side (viewed from above and with the cold head at the "front") bottom flange at 40k
leftBottomFlangeCornerReferenceScrewInsetZ_str = "leftBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[leftBottomFlangeCornerReferenceScrewInsetZ_str] = (params.leftBottomFlangeCornerReferenceScrewInsetZ_4K, params.mm_str)

leftBottomFlange_lengthX_str = "leftBottomFlange_lengthX"
valuesDict[leftBottomFlange_lengthX_str] = (params.leftBottomFlange_lengthX_4K, params.mm_str)
leftBottomFlange_widthZ_str = "leftBottomFlange_widthZ"
valuesDict[leftBottomFlange_widthZ_str] = (params.leftBottomFlange_widthZ_4K, params.mm_str)

leftBottomFlange_thickness_str = "leftBottomFlange_thickness"
valuesDict[leftBottomFlange_thickness_str] = (params.bottomFlangeThickness_4K, params.inch_str)

smallSideHole_CenterToCenter_str = "smallSideHole_CenterToCenter"
valuesDict[smallSideHole_CenterToCenter_str] = (params.smallSideHole_CenterToCenter_4K, params.mm_str)

bottomShellStringList = [leftBottomFlangeCornerReferenceScrewInsetZ_str,
                         leftBottomFlange_lengthX_str, leftBottomFlange_widthZ_str,
                         leftBottomFlange_thickness_str, smallSideHole_CenterToCenter_str]

leftBottomFlange = equationsFile(fullFilePath=parentDir, fileName="leftBottomFlangeEquations")
leftBottomFlange.listAddVarLine(bottomShellStringList, valuesDict)
leftBottomFlange.addRefLine("D2@sketch1", leftBottomFlangeCornerReferenceScrewInsetZ_str)
leftBottomFlange.addRefLine("D4@sketch1", leftBottomFlange_lengthX_str)
leftBottomFlange.addRefLine("D3@sketch1", leftBottomFlange_widthZ_str)
leftBottomFlange.addRefLine("D1@Boss-Extrude1", leftBottomFlange_thickness_str)
leftBottomFlange.addRefLine("D3@sketch2", smallSideHole_CenterToCenter_str)


if sys.platform == "win32":
    leftBottomFlange.writeFile()
    print(leftBottomFlange.fileContent)
else:
    print(leftBottomFlange.fileContent)

"""Rear Bottom Flange"""
# Rear side (viewed from above and with the cold head at the "front") bottom flange at 40k
rearBottomFlangeCornerReferenceScrewInsetX_str = "rearBottomFlangeCornerReferenceScrewInsetX"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetX_str] = (params.rearBottomFlangeCornerReferenceScrewInsetX_4K, params.mm_str)
rearBottomFlangeCornerReferenceScrewInsetZ_str = "rearBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetZ_str] = (params.rearBottomFlangeCornerReferenceScrewInsetZ_4K, params.mm_str)

rearBottomFlange_lengthX_str = "rearBottomFlange_lengthX"
valuesDict[rearBottomFlange_lengthX_str] = (params.rearBottomFlange_lengthX_4K, params.mm_str)
rearBottomFlange_widthZ_str = "rearBottomFlange_widthZ"
valuesDict[rearBottomFlange_widthZ_str] = (params.rearBottomFlange_widthZ_4K, params.mm_str)

rearBottomFlange_thickness_str = "rearBottomFlange_thickness"
valuesDict[rearBottomFlange_thickness_str] = (params.bottomFlangeThickness_4K, params.inch_str)

largeSideHole_CenterToCenter_str = "largeSideHole_CenterToCenter"
valuesDict[largeSideHole_CenterToCenter_str] = (params.largeSideHole_CenterToCenter_4K, params.mm_str)

bottomLefFlange_softCornerRadius_str = "bottomLefFlange_softCornerRadius"
valuesDict[bottomLefFlange_softCornerRadius_str] = (params.millRadius, params.inch_str)


bottomShellStringList = [rearBottomFlangeCornerReferenceScrewInsetX_str, rearBottomFlangeCornerReferenceScrewInsetZ_str,
                         rearBottomFlange_lengthX_str, rearBottomFlange_widthZ_str,
                         rearBottomFlange_thickness_str, largeSideHole_CenterToCenter_str,
                         bottomLefFlange_softCornerRadius_str]

rearBottomFlange = equationsFile(fullFilePath=parentDir, fileName="rearBottomFlangeEquations")
rearBottomFlange.listAddVarLine(bottomShellStringList, valuesDict)
rearBottomFlange.addRefLine("D1@sketch1", rearBottomFlangeCornerReferenceScrewInsetX_str)
rearBottomFlange.addRefLine("D2@sketch1", rearBottomFlangeCornerReferenceScrewInsetZ_str)
rearBottomFlange.addRefLine("D3@sketch1", rearBottomFlange_lengthX_str)
rearBottomFlange.addRefLine("D4@sketch1", rearBottomFlange_widthZ_str)
rearBottomFlange.addRefLine("D1@Boss-Extrude1", rearBottomFlange_thickness_str)
rearBottomFlange.addRefLine("D3@sketch2", largeSideHole_CenterToCenter_str)


if sys.platform == "win32":
    rearBottomFlange.writeFile()
else:
    print(rearBottomFlange.fileContent)


"""Left Wall"""
# Left side (viewed from above and with the cold head at the "front") wall at 40k
leftWallLengthX_str = "leftWallLengthX"
valuesDict[leftWallLengthX_str] = (params.leftBottomFlange_lengthX_4K, params.mm_str)
leftWallHalfWidthZ_str = "leftWallHalfWidthZ"
valuesDict[leftWallHalfWidthZ_str] = (params.Wall4K_halfWidthZ, params.mm_str)
leftWallBendRadius_str = "leftWallBendRadius"
valuesDict[leftWallBendRadius_str] = (params.millRadius, params.inch_str)

leftWallHeightY_str = "leftWallHeightY"
valuesDict[leftWallHeightY_str] = (params.shield_4K_workingHeight - (2.0 * params.shieldThickness_4K), params.mm_str)

leftWallThickness_str = "leftWallThickness"
valuesDict[leftWallThickness_str] = (params.shieldThickness_4K, params.inch_str)
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
valuesDict[RearAndFrontTopFlangeLenX_str] = (params.RearAndFrontTopFlangeLenX_4K, params.mm_str)
RearAndFrontTopFlangeBendRadius_str = "RearAndFrontTopFlangeBendRadius"
valuesDict[RearAndFrontTopFlangeBendRadius_str] = (params.RearAndFrontTopFlangeBendRadius_4K, params.inch_str)
bottomShellStringList = [RearAndFrontTopFlangeLenX_str]
RearAndFrontTopFlangeInPlaneWidth_str = "RearAndFrontTopFlangeInPlaneWidth"
valuesDict[RearAndFrontTopFlangeInPlaneWidth_str] = (params.shieldsTopFlangeWidth_4K, params.mm_str)
RearAndFrontTopFlangeThickness_str = "RearAndFrontTopFlangeThickness"
valuesDict[RearAndFrontTopFlangeThickness_str] = (params.shieldsTopFlangeThickness_4K, params.inch_str)

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
valuesDict[LeftAndRightTopFlangeLen_str] = (params.LeftAndRightTopFlangeLen_4K, params.mm_str)
bottomShellStringList = [LeftAndRightTopFlangeLen_str]
LeftAndRightTopFlangeInPlaneWidth_str = "LeftAndRightTopFlangeInPlaneWidth"
valuesDict[LeftAndRightTopFlangeInPlaneWidth_str] = (params.shieldsTopFlangeWidth_4K, params.mm_str)
shieldsLeftAndRightTopFlangeScrewInsertDist_str = "shieldsLeftAndRightTopFlangeScrewInsertDist"
valuesDict[shieldsLeftAndRightTopFlangeScrewInsertDist_str] = (params.shieldsLeftAndRightTopFlangeScrewInsertDist_4K,
                                                               params.inch_str)
LeftAndRightTopFlangeThickness_str = "LeftAndRightTopFlangeThickness"
valuesDict[LeftAndRightTopFlangeThickness_str] = (params.shieldsTopFlangeThickness_4K, params.inch_str)

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
ShieldAssem40K = equationsFile(fullFilePath=parentDir, fileName="ShieldAssem4K")
ShieldAssem40K.addVarLine(tolerance_str, params.tolerance, params.inch_str)
ShieldAssem40K.addRefLine("D1@Distance4", tolerance_str)
ShieldAssem40K.addRefLine("D1@Distance5", tolerance_str)


if sys.platform == "win32":
    ShieldAssem40K.writeFile()
else:
    print(ShieldAssem40K.fileContent)

"""Lid"""
# The Lid of the 40k shields
LidLeftRightLen_str = "LidLeftRightLen"
valuesDict[LidLeftRightLen_str] = (params.LidLeftRightLen_4K, params.mm_str)
LidRearFrontLen_str = "LidRearFrontLen"
valuesDict[LidRearFrontLen_str] = (params.LidRearFrontLen_4K, params.mm_str)
LidMillRadius_str = "LidMillRadius"
valuesDict[LidMillRadius_str] = (params.LidMillRadius_4K, params.mm_str)
LidHoles_InsetDist_str = "LidHoles_HalfFlangeDist"
valuesDict[LidHoles_InsetDist_str] = (params.LidHoles_InsetDist_4K, params.mm_str)

LeftAndRightTopFlangeStringList = [LidLeftRightLen_str, LidRearFrontLen_str,
                                   LidMillRadius_str, LidHoles_InsetDist_str,
                                   shieldsLeftAndRightTopFlangeScrewInsertDist_str]

Lid = equationsFile(fullFilePath=parentDir, fileName="4KLidEquations")
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

"""4K heat strap (fourK_heatStrap)"""
# The heat strapping as it attached to the topp of the 40K cold head.
coldhead4K_boltCircle_str = "coldhead4K_boltCircle"
valuesDict[coldhead4K_boltCircle_str] = (params.coldhead4K_boltCircle, params.mm_str)
coldhead4K_OD_str = "fortyK_heatPlate_OD"
valuesDict[coldhead4K_OD_str] = (params.coldhead4K_OD, params.mm_str)
coldhead4K_clearanceForID_str = "coldhead4K_clearanceForID"
valuesDict[coldhead4K_clearanceForID_str] = (params.coldhead4K_clearanceForID, params.mm_str)
heatStrap4K_OD_str = "heatStrap4K_OD"
valuesDict[heatStrap4K_OD_str] = (params.heatStrap4K_OD, params.mm_str)
heatStrappingHeight4K_str = "heatStrappingHeight4K"
valuesDict[heatStrappingHeight4K_str] = (params.heatStrappingHeight4K, params.mm_str)
heatStrappingLowerExtensionDistance_str = "heatStrappingLowerExtensionDistance"
valuesDict[heatStrappingLowerExtensionDistance_str] = (params.heatStrappingLowerExtensionDistance, params.mm_str)

fourK_heatStrapStringList = [coldhead4K_boltCircle_str, coldhead4K_OD_str,
                             coldhead4K_clearanceForID_str, heatStrap4K_OD_str,
                             heatStrappingHeight4K_str,
                             heatStrappingLowerExtensionDistance_str]

fourK_heatStrap = equationsFile(fullFilePath=parentDir, fileName="Heat Strapping\\4K_heatPStrapEquations")
fourK_heatStrap.listAddVarLine(fourK_heatStrapStringList, valuesDict)
fourK_heatStrap.addRefLine("D1@sketch1", coldhead4K_boltCircle_str)
fourK_heatStrap.addRefLine("D2@sketch1", coldhead4K_OD_str)
fourK_heatStrap.addRefLine("D4@sketch1", coldhead4K_clearanceForID_str)
fourK_heatStrap.addRefLine("D5@sketch1", heatStrappingHeight4K_str)
fourK_heatStrap.addRefLine("D8@sketch1", heatStrap4K_OD_str)
fourK_heatStrap.addRefLine("D1@Boss-Extrude1", heatStrappingHeight4K_str)
fourK_heatStrap.addRefLine("D1@Boss-Extrude2", heatStrappingLowerExtensionDistance_str)

if sys.platform == "win32":
    fourK_heatStrap.writeFile()
    print(fourK_heatStrap.fileContent)
else:
    print(fourK_heatStrap.fileContent)


"""4K heat plate (fourK_heatPlate)"""
fourK_heatPlate_refScrewX_str = "fourK_heatPlate_refScrewX"
valuesDict[fourK_heatPlate_refScrewX_str] = (params.fourK_heatPlate_refScrewX, params.mm_str)
rearBottomFlangeCornerReferenceScrewInsetZ_str = "rearBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[rearBottomFlangeCornerReferenceScrewInsetZ_str] = (params.rearBottomFlangeCornerReferenceScrewInsetZ_4K, params.mm_str)

fourK_heatPlate_lengthX_str = "fourK_heatPlate_lengthX"
valuesDict[fourK_heatPlate_lengthX_str] = (params.fourK_heatPlate_lengthX, params.mm_str)
rearBottomFlange_widthZ_str = "rearBottomFlange_widthZ"
valuesDict[rearBottomFlange_widthZ_str] = (params.rearBottomFlange_widthZ_4K, params.mm_str)

rearBottomFlange_thickness_str = "rearBottomFlange_thickness"
valuesDict[rearBottomFlange_thickness_str] = (params.bottomFlangeThickness_4K, params.inch_str)

largeSideHole_CenterToCenter_str = "largeSideHole_CenterToCenter"
valuesDict[largeSideHole_CenterToCenter_str] = (params.largeSideHole_CenterToCenter_4K, params.mm_str)

heatPlate_leftOffsetFromRefScrew_str = "heatPlate_leftOffsetFromRefScrew"
valuesDict[heatPlate_leftOffsetFromRefScrew_str] = (params.heatPlate_leftOffsetFromRefScrew, params.mm_str)
heatPlate_rightOffsetFromRefScrew_str = "heatPlate_rightOffsetFromRefScrew"
valuesDict[heatPlate_rightOffsetFromRefScrew_str] = (params.heatPlate_rightOffsetFromRefScrew, params.mm_str)
fourK_heatConductionExtensionDistance_str = "fourK_heatConductionExtensionDistance"
valuesDict[fourK_heatConductionExtensionDistance_str] = (params.fourK_heatConductionExtensionDistance, params.mm_str)
fourK_plateHeight_str = "fourK_plateHeight"
valuesDict[fourK_plateHeight_str] = (params.fourK_plateHeight, params.mm_str)


fourK_heatPlateStringList = [fourK_heatPlate_refScrewX_str, rearBottomFlangeCornerReferenceScrewInsetZ_str,
                             fourK_heatPlate_lengthX_str, rearBottomFlange_widthZ_str,
                             rearBottomFlange_thickness_str, largeSideHole_CenterToCenter_str,
                             heatPlate_leftOffsetFromRefScrew_str, heatPlate_rightOffsetFromRefScrew_str,
                             fourK_heatConductionExtensionDistance_str, fourK_plateHeight_str]

fourK_heatPlate = equationsFile(fullFilePath=parentDir, fileName="Heat Strapping\\4K_HeatPlateEquations")
fourK_heatPlate.listAddVarLine(fourK_heatPlateStringList, valuesDict)
fourK_heatPlate.addRefLine("D1@sketch1", fourK_heatPlate_refScrewX_str)
fourK_heatPlate.addRefLine("D2@sketch1", rearBottomFlangeCornerReferenceScrewInsetZ_str)
fourK_heatPlate.addRefLine("D3@sketch1", fourK_heatPlate_lengthX_str)
fourK_heatPlate.addRefLine("D4@sketch1", rearBottomFlange_widthZ_str)
fourK_heatPlate.addRefLine("D1@Boss-Extrude1", fourK_plateHeight_str)
fourK_heatPlate.addRefLine("D3@sketch2", largeSideHole_CenterToCenter_str)

fourK_heatPlate.addRefLine("D1@sketch6", heatPlate_leftOffsetFromRefScrew_str)
fourK_heatPlate.addRefLine("D2@sketch6", heatPlate_rightOffsetFromRefScrew_str)
fourK_heatPlate.addRefLine("D3@sketch6", fourK_heatConductionExtensionDistance_str)


if sys.platform == "win32":
    fourK_heatPlate.writeFile()
    print(fourK_heatPlate.fileContent)
else:
    print(fourK_heatPlate.fileContent)
