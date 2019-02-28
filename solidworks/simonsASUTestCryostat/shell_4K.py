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

bottom_flange_4K.addVariableLine("D1@sketch7", params.width_for_heat_plate_at_fullDepth)
bottom_flange_4K.addVariableLine("D2@sketch7", relief_cut_corner_radius_4k_shield_and_heat_strap)

bottom_flange_4K.addVariableLine("D1@fillet2", relief_cut_corner_radius_4k_shield_and_heat_strap)

bottom_flange_4K.addVariableLine("D1@sketch15", params.shieldsFlange_holeInset_4K)
bottom_flange_4K.addVariableLine("D3@sketch15", params.shield_connection_holes_large_spacing_4K)

bottom_flange_4K.writeFile(verbose=True)


"""
4 K Plate and Heat Strap
"""
pate_and_heat_strap_4K = SolidWorksPart("Heat Strapping\\pate_and_heat_strap_4K.txt", units="mm",
                                        parent_directory=parentDir)
pate_and_heat_strap_4K.addVariableLine("D5@Sketch1", params.heat_strapping_from_coldHead_center)
pate_and_heat_strap_4K.addVariableLine("D6@Sketch1", params.heat_plate_4K_width)
pate_and_heat_strap_4K.addVariableLine("D8@Sketch1", params.heat_plate_4K_corner_radius)

pate_and_heat_strap_4K.addVariableLine("D1@Relief Cut for Shield", params.baseFlangeThickness)
pate_and_heat_strap_4K.addVariableLine("D1@sketch5", params.width_for_heat_plate_at_fullDepth)

pate_and_heat_strap_4K.addVariableLine("D1@Boss-Extrude1", params.fourK_plateHeight)

# pate_and_heat_strap_4K.addVariableLine("D2@sketch5", relief_cut_corner_radius_4k_shield_and_heat_strap)

# pate_and_heat_strap_4K.addVariableLine("D1@fillet1", relief_cut_corner_radius_4k_shield_and_heat_strap)

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

plate_to_cold_head_strap_4K.addVariableLine("D1@Sketch7", params.heat_strapping_from_coldHead_center)
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
bottom_weld_flange_4K.addVariableLine("D2@sketch4", params.shield_connection_holes_large_spacing_4K)

bottom_weld_flange_4K.writeFile(verbose=True)

"""
Assembly of middle flange at 40K with fasteners 
"""
assem8_32RivetsWithFasteners = SolidWorksPart("assem8_32_0.45in_4K.txt", units="mm", parent_directory=parentDir)
assem8_32RivetsWithFasteners.addVariableLine("D1@Distance1", params.baseFlangeThickness)
assem8_32RivetsWithFasteners.writeFile(verbose=True)


"""
4K wall
"""
wall_4K = SolidWorksPart("wall_4K.txt", units="mm", parent_directory=parentDir)

wall_4K.addVariableLine("D1@sketch1", params.total4K_flangeWidth)
wall_4K.addVariableLine("D2@sketch1", params.total4K_flangeLength)
wall_4K.addVariableLine("D3@Sketch1", params.millRadius, units="in")

wall_4K.addVariableLine("D1@Extrude-Thin1", 219.38 - params.shieldSpace_4K_40K)  # params.shield_40K_workingHeight)
wall_4K.addVariableLine("D5@Extrude-Thin1", params.shieldThickness)

wall_4K.writeFile(verbose=True)


"""
top Weld Flange - 4K
"""
top_weld_flange_4K = SolidWorksPart("top_weld_flange_4K.txt", units="mm", parent_directory=parentDir)

top_weld_flange_4K.addVariableLine("D1@sketch2", params.total4K_flangeWidth)
top_weld_flange_4K.addVariableLine("D2@sketch2", params.total4K_flangeLength)
top_weld_flange_4K.addVariableLine("D1@Boss-Extrude1", params.HMS_topFlangeThickness)

top_weld_flange_4K.addVariableLine("D1@Fillet1", params.millRadius, units="in")

top_weld_flange_4K.addVariableLine("D1@sketch3", params.shieldsFlangeWidth)

top_weld_flange_4K.addVariableLine("D1@sketch4", params.shieldsFlangeWidth - params.shieldsFlange_holeInset)

top_weld_flange_4K.writeFile(verbose=True)


"""
Lid - 4K
"""
lid_4K = SolidWorksPart("lid_4K.txt", units="mm", parent_directory=parentDir)

lid_4K.addVariableLine("D1@sketch2", params.total4K_flangeWidth)
lid_4K.addVariableLine("D2@sketch2", params.total4K_flangeLength)
lid_4K.addVariableLine("D1@Boss-Extrude1", params.lid_shieldThickness)

lid_4K.addVariableLine("D1@Fillet1", params.millRadius, units="in")

lid_4K.addVariableLine("D1@sketch3", params.shieldsFlangeWidth)

lid_4K.addVariableLine("D1@sketch4", params.shieldsFlangeWidth - params.shieldsFlange_holeInset)

lid_4K.writeFile(verbose=True)


