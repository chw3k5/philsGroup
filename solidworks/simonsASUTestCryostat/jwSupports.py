from solidworks.simonsASUTestCryostat.cryostatParams import PhysicalParams
from solidworks.swVariables import SolidWorksPart

params = PhysicalParams()
valuesDict = {}
parentDir = params.base_directory + "GrabCAD\\SO\\" + \
            "Universal Readout Harness\\ASU Test Harness\\ASU Test Cryostat\\supports"
"""
Universal Driving Values
"""
# Driving Values for both 4K and 40K
required_support_height = 100.65

base_and_ceiling_height = 15

x_leg_width = 15
x_leg_overshoot = 1.5

base_and_ceiling_hole_distance = 80


"""
40 K Supports
"""
# Driving Values -> 40 K supports
base_length_40K = 120.0
base_depth_40K_cryo_side = 27.0
base_mounting_holes_offset_from_center = 7.0

fiberglass_thickness_40K = (1. / 8.) * params.inch_to_mm
fiberglass_ground_clearance = 2.0

ceiling_depth_40K = 16.0
ceiling_shield_hole_distance = 60.0


# Calculations -> 40K supports
base_mounting_holes_offset_from_edge = (base_depth_40K_cryo_side / 2.0) + base_mounting_holes_offset_from_center

fiberglass_height_40K = required_support_height - (2.0 * fiberglass_ground_clearance)
x_leg_overshoot_radius = x_leg_overshoot + (x_leg_width / 2.0)

ceiling_length_40K = base_and_ceiling_hole_distance + (2.0 * x_leg_overshoot_radius)

base_to_ceiling_hole_height = required_support_height - base_and_ceiling_height

cryo_side_ceiling_base_hole_offset = ((base_depth_40K_cryo_side - ceiling_depth_40K) / 2.0) \
                                      + base_mounting_holes_offset_from_center

"""
Commands to write the SolidWorks text files. 
"""
# Equations file -> 40K - Base - Fiber Glass Supports - Cryostat Side
base_fiberglass_40K_cryo = SolidWorksPart("equations_40_base_fiberglass_cryoSide.txt",
                                          units="mm", parent_directory=parentDir)

base_fiberglass_40K_cryo.addVariableLine("D1@sketch1", base_length_40K)  # base length
base_fiberglass_40K_cryo.addVariableLine("D2@sketch1", base_depth_40K_cryo_side)  # base depth (short dimension)
base_fiberglass_40K_cryo.addVariableLine("D1@Boss-Extrude1", base_and_ceiling_height)  # base thickness

base_fiberglass_40K_cryo.addVariableLine("D2@sketch2", base_mounting_holes_offset_from_edge)

base_fiberglass_40K_cryo.addVariableLine("D1@sketch5", base_and_ceiling_hole_distance)

base_fiberglass_40K_cryo.writeFile(verbose=True)


# Equations file -> 40K - Base - Fiber Glass Supports - Far Side
base_fiberglass_40K_far = SolidWorksPart("equations_40_base_fiberglass_farSide.txt",
                                         units="mm", parent_directory=parentDir)

base_fiberglass_40K_far.addVariableLine("D1@sketch1", base_length_40K)  # base length
base_fiberglass_40K_far.addVariableLine("D2@sketch1", ceiling_depth_40K)  # base depth (short dimension)
base_fiberglass_40K_far.addVariableLine("D1@Boss-Extrude1", base_and_ceiling_height)  # base thickness

base_fiberglass_40K_far.addVariableLine("D2@sketch2", ceiling_depth_40K / 2.0)

base_fiberglass_40K_far.addVariableLine("D1@sketch5", base_and_ceiling_hole_distance)

base_fiberglass_40K_far.writeFile(verbose=True)

# Equations file -> 40K - G10 sheet - Fiber Glass Supports
fiberglass_sheet_40K = SolidWorksPart("equations_40_fiberglass_sheet.txt", units="mm", parent_directory=parentDir)

fiberglass_sheet_40K.addVariableLine("D1@sketch1", base_to_ceiling_hole_height)
fiberglass_sheet_40K.addVariableLine("D2@sketch1", base_and_ceiling_hole_distance)
fiberglass_sheet_40K.addVariableLine("D3@sketch1", x_leg_width)
fiberglass_sheet_40K.addVariableLine("D4@sketch1", fiberglass_height_40K)

fiberglass_sheet_40K.addVariableLine("D1@Boss-Extrude1", fiberglass_thickness_40K)

fiberglass_sheet_40K.addVariableLine("D1@sketch4", x_leg_overshoot_radius)

fiberglass_sheet_40K.writeFile(verbose=True)


# Equations file -> 40K - ceiling - Fiber Glass Supports
ceiling_fiberglass_40K = SolidWorksPart("equations_40_ceiling_fiberglass.txt", units="mm", parent_directory=parentDir)

ceiling_fiberglass_40K.addVariableLine("D1@sketch1", ceiling_length_40K)  # ceiling length
ceiling_fiberglass_40K.addVariableLine("D2@sketch1", ceiling_depth_40K)  # ceiling depth (short dimension)
ceiling_fiberglass_40K.addVariableLine("D1@Boss-Extrude1", base_and_ceiling_height)  # ceiling thickness

ceiling_fiberglass_40K.addVariableLine("D1@sketch3", base_and_ceiling_hole_distance)

ceiling_fiberglass_40K.addVariableLine("D1@sketch6", ceiling_shield_hole_distance)


ceiling_fiberglass_40K.writeFile(verbose=True)

