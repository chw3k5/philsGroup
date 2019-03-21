import sys
from solidworks.simonsASUTestCryostat.cryostatParams import PhysicalParams
from solidworks.solidWorksVariables import SolidWorksPart
from solidworks.simonsASUTestCryostat.jwSupports import ceiling_shield_hole_distance, \
    cryo_side_ceiling_base_hole_offset

params = PhysicalParams()
valuesDict = {}
# parentDir = params.base_directory + "GrabCAD\\SO\\" + \
#             "Universal Readout Harness\\ASU Test Harness\\ASU Test Cryostat\\40 K"
parentDir = params.base_directory + "Simon's Observartory\\Machine Shop Pack and Go\\SO Order2 - Full Cryostat\\40 K"
coldhead_edge_offset = 27.5 - params.shieldSpace_40K_300K

"""
middle flange at 40K
"""
middle_flange_40K = SolidWorksPart("middleFlange40K_v2.txt", units="mm", parent_directory=parentDir)
middle_flange_40K.addVariableLine("D1@Extrude-Thin1", params.baseFlangeThickness)
middle_flange_40K.addVariableLine("D5@Extrude-Thin1", params.shieldsFlangeWidth)

middle_flange_40K.addVariableLine("D5@sketch1", coldhead_edge_offset)
middle_flange_40K.addVariableLine("D6@sketch1", params.coldhead40K_flange_Z)
middle_flange_40K.addVariableLine("D7@sketch1", params.total40K_FlangeWidth)
middle_flange_40K.addVariableLine("D8@sketch1", params.millRadius, units="in")

middle_flange_40K.addVariableLine("D1@3Dsketch1", params.coldhead_flangeScrewInset)

middle_flange_40K.addVariableLine("D1@sketch6", params.leftBottomFlange_lengthX)

middle_flange_40K.addVariableLine("D2@sketch6", params.leftBottomFlange_widthZ)
middle_flange_40K.addVariableLine("D3@sketch6", params.rearBottomFlange_lengthX)

middle_flange_40K.addVariableLine("D1@fillet1", params.millRadius, units="in")

middle_flange_40K.addVariableLine("D1@sketch11", params.shieldsFlange_holeInset)
middle_flange_40K.addVariableLine("D1@sketch13", params.shieldsFlangeWidth)

middle_flange_40K.addVariableLine("D3@sketch14", ceiling_shield_hole_distance)
middle_flange_40K.addVariableLine("D4@sketch14", cryo_side_ceiling_base_hole_offset)

middle_flange_40K.writeFile(verbose=True)


"""
Assembly of middle flange at 40K with fasteners 
"""
assem8_32RivetsWithFasteners = SolidWorksPart("assem8_32RivetsWithFasteners.txt", units="mm", parent_directory=parentDir)
assem8_32RivetsWithFasteners.addVariableLine("D1@Distance1", params.HMS_bottomFlangeThickness)
assem8_32RivetsWithFasteners.writeFile(verbose=True)


"""
coldhead flange at 40K
"""
coldhead_flange_40K = SolidWorksPart("coldhead_flange_40K.txt", units="mm", parent_directory=parentDir)
coldhead_flange_40K.addVariableLine("D1@Boss-Extrude1", params.coldhead40K_flange_thickness)

coldhead_flange_40K.addVariableLine("D5@sketch1", coldhead_edge_offset)
coldhead_flange_40K.addVariableLine("D6@sketch1", params.coldhead40K_flange_Z)
coldhead_flange_40K.addVariableLine("D7@sketch1", params.total40K_FlangeWidth)

coldhead_flange_40K.addVariableLine("D1@fillet1", params.millRadius, units="in")

coldhead_flange_40K.addVariableLine("D1@sketch7", params.shield_clamp_spacing)


coldhead_flange_40K.writeFile(verbose=True)


"""
coldhead shield Wall
"""
coldhead_shieldwall_40K = SolidWorksPart("coldhead_shieldWall_40K.txt", units="mm", parent_directory=parentDir)
coldhead_shieldwall_40K.addVariableLine("D1@Extrude-Thin1", params.coldheadShieldWall_height)
coldhead_shieldwall_40K.addVariableLine("D5@Extrude-Thin1", params.shieldThickness_heatConduction)

coldhead_shieldwall_40K.addVariableLine("D5@sketch1", coldhead_edge_offset)
coldhead_shieldwall_40K.addVariableLine("D6@sketch1", params.coldhead40K_flange_Z)
coldhead_shieldwall_40K.addVariableLine("D7@sketch1", params.total40K_FlangeWidth)
coldhead_shieldwall_40K.addVariableLine("D8@sketch1", params.millRadius, units="in")
coldhead_shieldwall_40K.writeFile(verbose=True)


"""
coldhead_shield_clamps
"""
coldhead_shield_clamps_40K = SolidWorksPart("Heat strapping\\coldhead_shield_clamps_40K.txt",
                                            units="mm", parent_directory=parentDir)
coldhead_shield_clamps_40K.addVariableLine("D1@sketch1", params.coldhead40K_flange_Z
                                    - (4.0 * params.shieldThickness_heatConduction))

coldhead_shield_clamps_40K.addVariableLine("D1@sketch5", params.shield_clamp_spacing)
coldhead_shield_clamps_40K.addVariableLine("D3@LPattern1", params.shield_clamp_spacing)
coldhead_shield_clamps_40K.addVariableLine("D4@LPattern1", params.shield_clamp_spacing)

coldhead_shield_clamps_40K.writeFile(verbose=True)

"""
Harness main Shield - Bottom Weld Flange - 40K
"""
HMS_bottom_weld_flange_40K = SolidWorksPart("HMS_bottom_weld_flange_40K.txt", units="mm", parent_directory=parentDir)

HMS_bottom_weld_flange_40K.addVariableLine("D1@sketch2", params.total40K_FlangeWidth)
HMS_bottom_weld_flange_40K.addVariableLine("D2@sketch2", params.leftBottomFlange_lengthX)
HMS_bottom_weld_flange_40K.addVariableLine("D1@Boss-Extrude1", params.HMS_bottomFlangeThickness)

HMS_bottom_weld_flange_40K.addVariableLine("D1@Fillet1", params.millRadius, units="in")

HMS_bottom_weld_flange_40K.addVariableLine("D1@sketch3", params.shieldsFlangeWidth)

HMS_bottom_weld_flange_40K.addVariableLine("D1@sketch4", params.shieldsFlange_holeInset)

HMS_bottom_weld_flange_40K.addVariableLine("D1@sketch5", 12.0)

HMS_bottom_weld_flange_40K.writeFile(verbose=True)

"""
Harness main Shield - Walls - 40K
"""
HMS_wall_40K = SolidWorksPart("HMS_wall_40K.txt", units="mm", parent_directory=parentDir)

HMS_wall_40K.addVariableLine("D1@sketch2", params.total40K_FlangeWidth)
HMS_wall_40K.addVariableLine("D2@sketch2", params.leftBottomFlange_lengthX)
HMS_wall_40K.addVariableLine("D3@Sketch2", params.millRadius, units="in")
HMS_wall_40K.addVariableLine("D4@sketch2", params.shieldsFlangeWidth)

HMS_wall_40K.addVariableLine("D1@Extrude-Thin1", 340.2025 - params.shieldSpace_40K_300K)  # params.shield_40K_workingHeight)
HMS_wall_40K.addVariableLine("D5@Extrude-Thin1", params.shieldThickness)

HMS_wall_40K.writeFile(verbose=True)


"""
Harness main Shield - top Weld Flange - 40K
"""
HMS_top_weld_flange_40K = SolidWorksPart("HMS_top_weld_flange_40K.txt", units="mm", parent_directory=parentDir)

HMS_top_weld_flange_40K.addVariableLine("D1@sketch2", params.total40K_FlangeWidth)
HMS_top_weld_flange_40K.addVariableLine("D2@sketch2", params.leftBottomFlange_lengthX)
HMS_top_weld_flange_40K.addVariableLine("D1@Boss-Extrude1", params.HMS_topFlangeThickness)

HMS_top_weld_flange_40K.addVariableLine("D1@Fillet1", params.millRadius, units="in")

HMS_top_weld_flange_40K.addVariableLine("D1@sketch3", params.shieldsFlangeWidth)

HMS_top_weld_flange_40K.addVariableLine("D1@sketch4", params.shieldsFlange_holeInset)

HMS_top_weld_flange_40K.writeFile(verbose=True)

"""
Harness main Shield - Lid- 40K
"""
HMS_lid_40K = SolidWorksPart("HMS_lid_40K.txt", units="mm", parent_directory=parentDir)

HMS_lid_40K.addVariableLine("D1@sketch2", params.total40K_FlangeWidth)
HMS_lid_40K.addVariableLine("D2@sketch2", params.leftBottomFlange_lengthX)
HMS_lid_40K.addVariableLine("D1@Boss-Extrude1", params.lid_shieldThickness)

HMS_lid_40K.addVariableLine("D1@Fillet1", params.millRadius, units="in")

HMS_lid_40K.addVariableLine("D1@sketch3", params.shieldsFlangeWidth)

HMS_lid_40K.addVariableLine("D1@sketch4", params.shieldsFlange_holeInset)

HMS_lid_40K.writeFile(verbose=True)
