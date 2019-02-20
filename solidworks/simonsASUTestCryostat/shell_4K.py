from solidworks.swVariables import equationsFile, SolidWorksPart
from solidworks.simonsASUTestCryostat.cryostatParams import PhysicalParams


params = PhysicalParams()
valuesDict = {}
parentDir = params.base_directory + "GrabCAD\\SO\\" + \
            "Universal Readout Harness\\ASU Test Harness\\ASU Test Cryostat\\4 K"


relief_cut_4k_shield_and_heat_strap = 260.0
relief_cut_corner_radius_4k_shield_and_heat_strap = 12.7

shieldOffset_4K = params.shieldsFlangeWidth + params.shieldSpace_4K_40K
total4K_flangeWidth = params.total40K_FlangeWidth - (2.0 * shieldOffset_4K)
total4K_flangeLength = params.leftBottomFlange_lengthX - (2.0 * shieldOffset_4K)

"""
4K Shield bottom flange. 
"""
bottom_flange_4K = SolidWorksPart("bottom_flange_4K.txt", units="mm", parent_directory=parentDir)
bottom_flange_4K.addVariableLine("D1@Boss-Extrude1", params.baseFlangeThickness)
bottom_flange_4K.addVariableLine("D5@sketch1", params.total4K_flangeWidth)
bottom_flange_4K.addVariableLine("D6@sketch1", params.total4K_flangeLength)
bottom_flange_4K.addVariableLine("D7@sketch1", params.shieldExtensionFromColdHeadCenter)

bottom_flange_4K.addVariableLine("D1@fillet1", params.millRadius, units="in")

bottom_flange_4K.addVariableLine("D1@sketch7", relief_cut_4k_shield_and_heat_strap)
bottom_flange_4K.addVariableLine("D2@sketch7", relief_cut_corner_radius_4k_shield_and_heat_strap)

bottom_flange_4K.addVariableLine("D1@fillet2", relief_cut_corner_radius_4k_shield_and_heat_strap)

bottom_flange_4K.writeFile(verbose=True)


"""
4 K Plate and Heat Strap
"""
pate_and_heat_strap_4K = SolidWorksPart("Heat Strapping\\pate_and_heat_strap_4K.txt", units="mm",
                                        parent_directory=parentDir)
pate_and_heat_strap_4K.addVariableLine("D1@Relief Cut for Shield", params.baseFlangeThickness)
pate_and_heat_strap_4K.addVariableLine("D1@sketch5", relief_cut_4k_shield_and_heat_strap)

pate_and_heat_strap_4K.addVariableLine("D1@Boss-Extrude1", params.fourK_plateHeight)

pate_and_heat_strap_4K.addVariableLine("D2@sketch5", relief_cut_corner_radius_4k_shield_and_heat_strap)

pate_and_heat_strap_4K.addVariableLine("D1@fillet1", relief_cut_corner_radius_4k_shield_and_heat_strap)

pate_and_heat_strap_4K.writeFile(verbose=True)


"""
Plate to cold head heat strap - 4K

The heat strapping as it attached to the top of the 40K cold head.
"""

plate_to_cold_head_strap_4K = SolidWorksPart("Heat Strapping\\plate_to_cold_head_strap_4K.txt", units="mm",
                                        parent_directory=parentDir)

plate_to_cold_head_strap_4K.addVariableLine("D1@sketch1", params.coldhead4K_boltCircle)
plate_to_cold_head_strap_4K.addVariableLine("D2@sketch1", params.coldhead4K_OD)
plate_to_cold_head_strap_4K.addVariableLine("D4@sketch1", params.coldhead4K_clearanceForID)
plate_to_cold_head_strap_4K.addVariableLine("D5@sketch1", params.heatStrappingHeight4K)
plate_to_cold_head_strap_4K.addVariableLine("D8@sketch1", params.heatStrap4K_OD)
plate_to_cold_head_strap_4K.addVariableLine("D1@Boss-Extrude1", params.heatStrappingHeight4K)

plate_to_cold_head_strap_4K.addVariableLine("D1@Boss-Extrude2", params.heatStrappingLowerExtensionDistance)

plate_to_cold_head_strap_4K.writeFile(verbose=True)


"""
4K Bottom Weld Flange
"""
bottom_weld_flange_4K = SolidWorksPart("bottom_weld_flange_4K.txt", units="mm", parent_directory=parentDir)

bottom_weld_flange_4K.addVariableLine("D1@sketch2", params.total4K_flangeWidth)
bottom_weld_flange_4K.addVariableLine("D2@sketch2", params.total4K_flangeLength)
bottom_weld_flange_4K.addVariableLine("D1@Boss-Extrude1", params.baseFlangeThickness)

bottom_weld_flange_4K.addVariableLine("D1@Fillet1", params.millRadius, units="in")

bottom_weld_flange_4K.addVariableLine("D1@sketch3", params.shieldsFlangeWidth_4K)

bottom_weld_flange_4K.addVariableLine("D1@sketch4", params.shieldsFlange_holeInset_4K)

bottom_weld_flange_4K.writeFile(verbose=True)

"""
Assembly of middle flange at 40K with fasteners 
"""
assem8_32RivetsWithFasteners = SolidWorksPart("assem8_32_0.45in_4K.txt", units="mm", parent_directory=parentDir)
assem8_32RivetsWithFasteners.addVariableLine("D1@Distance1", params.baseFlangeThickness)
assem8_32RivetsWithFasteners.writeFile(verbose=True)
"""

# """
# Left Bottom Flange
#
#
# The sections below have not benn updated!
# """
# # Left side (viewed from above and with the cold head at the "front") bottom flange at 40k
# leftBottomFlangeCornerReferenceScrewInsetZ_str = "leftBottomFlangeCornerReferenceScrewInsetZ"
# valuesDict[leftBottomFlangeCornerReferenceScrewInsetZ_str] = (params.leftBottomFlangeCornerReferenceScrewInsetZ_4K, params.mm_str)
#
# leftBottomFlange_lengthX_str = "leftBottomFlange_lengthX"
# valuesDict[leftBottomFlange_lengthX_str] = (params.leftBottomFlange_lengthX_4K, params.mm_str)
# leftBottomFlange_widthZ_str = "leftBottomFlange_widthZ"
# valuesDict[leftBottomFlange_widthZ_str] = (params.leftBottomFlange_widthZ_4K, params.mm_str)
#
# leftBottomFlange_thickness_str = "leftBottomFlange_thickness"
# valuesDict[leftBottomFlange_thickness_str] = (params.bottomFlangeThickness_4K, params.inch_str)
#
# smallSideHole_CenterToCenter_str = "smallSideHole_CenterToCenter"
# valuesDict[smallSideHole_CenterToCenter_str] = (params.smallSideHole_CenterToCenter_4K, params.mm_str)
#
# bottomShellStringList = [leftBottomFlangeCornerReferenceScrewInsetZ_str,
#                          leftBottomFlange_lengthX_str, leftBottomFlange_widthZ_str,
#                          leftBottomFlange_thickness_str, smallSideHole_CenterToCenter_str]
#
# leftBottomFlange = equationsFile(fullFilePath=parentDir, fileName="leftBottomFlangeEquations")
# leftBottomFlange.listAddVarLine(bottomShellStringList, valuesDict)
# leftBottomFlange.addRefLine("D2@sketch1", leftBottomFlangeCornerReferenceScrewInsetZ_str)
# leftBottomFlange.addRefLine("D4@sketch1", leftBottomFlange_lengthX_str)
# leftBottomFlange.addRefLine("D3@sketch1", leftBottomFlange_widthZ_str)
# leftBottomFlange.addRefLine("D1@Boss-Extrude1", leftBottomFlange_thickness_str)
# leftBottomFlange.addRefLine("D3@sketch2", smallSideHole_CenterToCenter_str)
#
# # leftBottomFlange.writeFile()
#
#
# """Rear Bottom Flange"""
# # Rear side (viewed from above and with the cold head at the "front") bottom flange at 40k
# rearBottomFlangeCornerReferenceScrewInsetX_str = "rearBottomFlangeCornerReferenceScrewInsetX"
# valuesDict[rearBottomFlangeCornerReferenceScrewInsetX_str] = (params.rearBottomFlangeCornerReferenceScrewInsetX_4K, params.mm_str)
# rearBottomFlangeCornerReferenceScrewInsetZ_str = "rearBottomFlangeCornerReferenceScrewInsetZ"
# valuesDict[rearBottomFlangeCornerReferenceScrewInsetZ_str] = (params.rearBottomFlangeCornerReferenceScrewInsetZ_4K, params.mm_str)
#
# rearBottomFlange_lengthX_str = "rearBottomFlange_lengthX"
# valuesDict[rearBottomFlange_lengthX_str] = (params.rearBottomFlange_lengthX_4K, params.mm_str)
# rearBottomFlange_widthZ_str = "rearBottomFlange_widthZ"
# valuesDict[rearBottomFlange_widthZ_str] = (params.rearBottomFlange_widthZ_4K, params.mm_str)
#
# rearBottomFlange_thickness_str = "rearBottomFlange_thickness"
# valuesDict[rearBottomFlange_thickness_str] = (params.bottomFlangeThickness_4K, params.inch_str)
#
# largeSideHole_CenterToCenter_str = "largeSideHole_CenterToCenter"
# valuesDict[largeSideHole_CenterToCenter_str] = (params.largeSideHole_CenterToCenter_4K, params.mm_str)
#
# bottomLefFlange_softCornerRadius_str = "bottomLefFlange_softCornerRadius"
# valuesDict[bottomLefFlange_softCornerRadius_str] = (params.millRadius, params.inch_str)
#
#
# bottomShellStringList = [rearBottomFlangeCornerReferenceScrewInsetX_str, rearBottomFlangeCornerReferenceScrewInsetZ_str,
#                          rearBottomFlange_lengthX_str, rearBottomFlange_widthZ_str,
#                          rearBottomFlange_thickness_str, largeSideHole_CenterToCenter_str,
#                          bottomLefFlange_softCornerRadius_str]
#
# rearBottomFlange = equationsFile(fullFilePath=parentDir, fileName="rearBottomFlangeEquations")
# rearBottomFlange.listAddVarLine(bottomShellStringList, valuesDict)
# rearBottomFlange.addRefLine("D1@sketch1", rearBottomFlangeCornerReferenceScrewInsetX_str)
# rearBottomFlange.addRefLine("D2@sketch1", rearBottomFlangeCornerReferenceScrewInsetZ_str)
# rearBottomFlange.addRefLine("D3@sketch1", rearBottomFlange_lengthX_str)
# rearBottomFlange.addRefLine("D4@sketch1", rearBottomFlange_widthZ_str)
# rearBottomFlange.addRefLine("D1@Boss-Extrude1", rearBottomFlange_thickness_str)
# rearBottomFlange.addRefLine("D3@sketch2", largeSideHole_CenterToCenter_str)
#
# # rearBottomFlange.writeFile()
#
#
# """Left Wall"""
# # Left side (viewed from above and with the cold head at the "front") wall at 40k
# leftWallLengthX_str = "leftWallLengthX"
# valuesDict[leftWallLengthX_str] = (params.leftBottomFlange_lengthX_4K, params.mm_str)
# leftWallHalfWidthZ_str = "leftWallHalfWidthZ"
# valuesDict[leftWallHalfWidthZ_str] = (params.Wall4K_halfWidthZ, params.mm_str)
# leftWallBendRadius_str = "leftWallBendRadius"
# valuesDict[leftWallBendRadius_str] = (params.millRadius, params.inch_str)
#
# leftWallHeightY_str = "leftWallHeightY"
# valuesDict[leftWallHeightY_str] = (params.shield_4K_workingHeight - (2.0 * params.shieldThickness_4K), params.mm_str)
#
# leftWallThickness_str = "leftWallThickness"
# valuesDict[leftWallThickness_str] = (params.shieldThickness_4K, params.inch_str)
# bottomShellStringList = [leftWallLengthX_str, leftWallHalfWidthZ_str,
#                          leftWallBendRadius_str,
#                          leftWallHeightY_str, leftWallThickness_str]
#
# leftWall = equationsFile(fullFilePath=parentDir, fileName="leftWallsEquations")
# leftWall.listAddVarLine(bottomShellStringList, valuesDict)
# leftWall.addRefLine("D1@sketch1", leftWallLengthX_str)
# leftWall.addRefLine("D2@sketch1", leftWallHalfWidthZ_str)
# leftWall.addRefLine("D3@sketch1", leftWallBendRadius_str)
# leftWall.addRefLine("D1@Extrude-Thin1", leftWallHeightY_str)
# leftWall.addRefLine("D5@Extrude-Thin1", leftWallThickness_str)
#
# # leftWall.writeFile()
#
#
# """Rear and Front Top Flange"""
# # Rear and Front (viewed from above and with the cold head at the "front") Flanges at 40k
# RearAndFrontTopFlangeLenX_str = "RearAndFrontTopFlangeLenX"
# valuesDict[RearAndFrontTopFlangeLenX_str] = (params.RearAndFrontTopFlangeLenX_4K, params.mm_str)
# RearAndFrontTopFlangeBendRadius_str = "RearAndFrontTopFlangeBendRadius"
# valuesDict[RearAndFrontTopFlangeBendRadius_str] = (params.RearAndFrontTopFlangeBendRadius_4K, params.inch_str)
# bottomShellStringList = [RearAndFrontTopFlangeLenX_str]
# RearAndFrontTopFlangeInPlaneWidth_str = "RearAndFrontTopFlangeInPlaneWidth"
# valuesDict[RearAndFrontTopFlangeInPlaneWidth_str] = (params.shieldsTopFlangeWidth_4K, params.mm_str)
# RearAndFrontTopFlangeThickness_str = "RearAndFrontTopFlangeThickness"
# valuesDict[RearAndFrontTopFlangeThickness_str] = (params.shieldsTopFlangeThickness_4K, params.inch_str)
#
# RearAndFrontTopFlangeStringList = [RearAndFrontTopFlangeLenX_str, RearAndFrontTopFlangeBendRadius_str,
#                                    RearAndFrontTopFlangeInPlaneWidth_str, RearAndFrontTopFlangeThickness_str]
#
# RearAndFrontTopFlange = equationsFile(fullFilePath=parentDir, fileName="RearAndFrontTopFlangeEquations")
# RearAndFrontTopFlange.listAddVarLine(RearAndFrontTopFlangeStringList, valuesDict)
# RearAndFrontTopFlange.addRefLine("D1@sketch1", RearAndFrontTopFlangeLenX_str)
# RearAndFrontTopFlange.addRefLine("D2@sketch1", RearAndFrontTopFlangeBendRadius_str)
# RearAndFrontTopFlange.addRefLine("D4@sketch1", RearAndFrontTopFlangeInPlaneWidth_str)
# RearAndFrontTopFlange.addRefLine("D5@Extrude-Thin1", RearAndFrontTopFlangeInPlaneWidth_str)
# RearAndFrontTopFlange.addRefLine("D1@Extrude-Thin1", RearAndFrontTopFlangeThickness_str)
#
# # RearAndFrontTopFlange.writeFile()
#
#
# """Left and Right Top Flange"""
# # Rear and Front (viewed from above and with the cold head at the "front") Flanges at 40k
# LeftAndRightTopFlangeLen_str = "LeftAndRightTopFlangeLen"
# valuesDict[LeftAndRightTopFlangeLen_str] = (params.LeftAndRightTopFlangeLen_4K, params.mm_str)
# bottomShellStringList = [LeftAndRightTopFlangeLen_str]
# LeftAndRightTopFlangeInPlaneWidth_str = "LeftAndRightTopFlangeInPlaneWidth"
# valuesDict[LeftAndRightTopFlangeInPlaneWidth_str] = (params.shieldsTopFlangeWidth_4K, params.mm_str)
# shieldsLeftAndRightTopFlangeScrewInsertDist_str = "shieldsLeftAndRightTopFlangeScrewInsertDist"
# valuesDict[shieldsLeftAndRightTopFlangeScrewInsertDist_str] = (params.shieldsLeftAndRightTopFlangeScrewInsertDist_4K,
#                                                                params.inch_str)
# LeftAndRightTopFlangeThickness_str = "LeftAndRightTopFlangeThickness"
# valuesDict[LeftAndRightTopFlangeThickness_str] = (params.shieldsTopFlangeThickness_4K, params.inch_str)
#
# LeftAndRightTopFlangeStringList = [LeftAndRightTopFlangeLen_str, LeftAndRightTopFlangeInPlaneWidth_str,
#                                    shieldsLeftAndRightTopFlangeScrewInsertDist_str, LeftAndRightTopFlangeThickness_str]
#
# LeftAndRightTopFlange = equationsFile(fullFilePath=parentDir, fileName="LeftAndRightTopFlangeEquations")
# LeftAndRightTopFlange.listAddVarLine(LeftAndRightTopFlangeStringList, valuesDict)
# LeftAndRightTopFlange.addRefLine("D1@sketch1", LeftAndRightTopFlangeLen_str)
# LeftAndRightTopFlange.addRefLine("D2@sketch1", LeftAndRightTopFlangeInPlaneWidth_str)
# LeftAndRightTopFlange.addRefLine("D3@Sketch1", shieldsLeftAndRightTopFlangeScrewInsertDist_str)
# LeftAndRightTopFlange.addRefLine("D1@Boss-Extrude1", LeftAndRightTopFlangeThickness_str)
#
# # LeftAndRightTopFlange.writeFile()
#
# # flange and walls assembly
# tolerance_str = "tolerance"
#
# # flange and walls assembly
# ShieldAssem40K = equationsFile(fullFilePath=parentDir, fileName="ShieldAssem4K")
# ShieldAssem40K.addVarLine(tolerance_str, params.tolerance, params.inch_str)
# ShieldAssem40K.addRefLine("D1@Distance4", tolerance_str)
# ShieldAssem40K.addRefLine("D1@Distance5", tolerance_str)
#
# # ShieldAssem40K.writeFile()
#
#
# """Lid"""
# # The Lid of the 40k shields
# LidLeftRightLen_str = "LidLeftRightLen"
# valuesDict[LidLeftRightLen_str] = (params.LidLeftRightLen_4K, params.mm_str)
# LidRearFrontLen_str = "LidRearFrontLen"
# valuesDict[LidRearFrontLen_str] = (params.LidRearFrontLen_4K, params.mm_str)
# LidMillRadius_str = "LidMillRadius"
# valuesDict[LidMillRadius_str] = (params.LidMillRadius_4K, params.mm_str)
# LidHoles_InsetDist_str = "LidHoles_HalfFlangeDist"
# valuesDict[LidHoles_InsetDist_str] = (params.LidHoles_InsetDist_4K, params.mm_str)
#
# LeftAndRightTopFlangeStringList = [LidLeftRightLen_str, LidRearFrontLen_str,
#                                    LidMillRadius_str, LidHoles_InsetDist_str,
#                                    shieldsLeftAndRightTopFlangeScrewInsertDist_str]
#
# Lid = equationsFile(fullFilePath=parentDir, fileName="4KLidEquations")
# Lid.listAddVarLine(LeftAndRightTopFlangeStringList, valuesDict)
# Lid.addRefLine("D1@sketch1", LidLeftRightLen_str)
# Lid.addRefLine("D2@sketch1", LidRearFrontLen_str)
# Lid.addRefLine("D3@Sketch1", LidMillRadius_str)
# Lid.addRefLine("D4@Sketch1", LidHoles_InsetDist_str)
# Lid.addRefLine("D5@Sketch1", LidHoles_InsetDist_str)
# Lid.addRefLine("D1@Sketch1", shieldsLeftAndRightTopFlangeScrewInsertDist_str)
#
# # Lid.writeFile()
#
