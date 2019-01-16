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

base_slash_ceiling_height = 10

long_side_of_slot_to_part_edge = 2.0
slot_depth = 5.0  # 3.0 * fiberglass_thickness_40K

"""
40 K Supports
"""
# Driving Values -> 40 K supports
fiberglass_width_40K = 70.0  # millimeters
base_length_40K = 120

fiberglass_thickness_40K = (1. / 16.) * params.inch_to_mm
slot_clearance_for_fiberglass_40K = 0.015 * params.inch_to_mm

ceiling_depth_40K = 30
ceiling_slot_offset_fraction_40K = 0.8  # 1 is all the way to the top, 0.5 is in the middle, 0 is on the bottom

# Calculations -> 40K supports
slot_width_40K = fiberglass_thickness_40K + (2.0 * slot_clearance_for_fiberglass_40K)



fiberglass_height_40K = required_support_height - (2.0 * (base_slash_ceiling_height - slot_depth))

ceiling_slot_offset_40K = (slot_width_40K / 2.0) + (ceiling_depth_40K * ceiling_slot_offset_fraction_40K)

### Equations file -> 40K - Base - Fiber Glass Supports
base_fiberglass_40K = SolidWorksPart("equations_40_base_fiberglass.txt", units="mm", parent_directory=parentDir)

base_fiberglass_40K.addVariableLine("D1@sketch1", base_length_40K)  # base length
base_fiberglass_40K.addVariableLine("D2@sketch1", 30)  # base depth (short dimension)
base_fiberglass_40K.addVariableLine("D1@Boss-Extrude1", base_slash_ceiling_height)  # base thickness

base_fiberglass_40K.addVariableLine("D2@Sketch2", 10)  # 1/4-20 core bore screw center to part edge distance

base_fiberglass_40K.addVariableLine("D1@Sketch4", 2)  # short-side-of-slot min distance slot radius to edge of part
base_fiberglass_40K.addVariableLine("D2@Sketch4", slot_width_40K)  # Slot width
base_fiberglass_40K.addVariableLine("D3@Sketch4", 3)  # long-side-of-slot edge of slot to edge of part base
base_fiberglass_40K.addVariableLine("D1@Cut-Extrude1", slot_depth)

base_fiberglass_40K.writeFile(verbose=True)


### Equations file -> 40K - G10 sheet - Fiber Glass Supports
fiberglass_sheet_40K = SolidWorksPart("equations_40_fiberglass_sheet.txt", units="mm", parent_directory=parentDir)

fiberglass_sheet_40K.addVariableLine("D1@sketch1", fiberglass_width_40K)
fiberglass_sheet_40K.addVariableLine("D2@sketch1", fiberglass_height_40K)
fiberglass_sheet_40K.addVariableLine("D1@Boss-Extrude1", fiberglass_thickness_40K)

fiberglass_sheet_40K.writeFile(verbose=True)

### Equations file -> 40K - ceiling - Fiber Glass Supports
ceiling_fiberglass_40K = SolidWorksPart("equations_40_ceiling_fiberglass.txt", units="mm", parent_directory=parentDir)

ceiling_fiberglass_40K.addVariableLine("D1@sketch1", max(base_length_40K, 3.0 * params.inch_to_mm))  # ceiling length
ceiling_fiberglass_40K.addVariableLine("D2@sketch1", ceiling_depth_40K)  # ceiling depth (short dimension)
ceiling_fiberglass_40K.addVariableLine("D1@Boss-Extrude1", base_slash_ceiling_height)  # ceiling thickness

ceiling_fiberglass_40K.addVariableLine("D1@Sketch2", 2)  # short-side-of-slot min distance slot radius to edge of part
ceiling_fiberglass_40K.addVariableLine("D2@Sketch2", slot_width_40K)  # Slot width
ceiling_fiberglass_40K.addVariableLine("D3@Sketch2", ceiling_slot_offset_40K)  # long-side-of-slot edge of slot to edge of part base
ceiling_fiberglass_40K.addVariableLine("D1@Cut-Extrude1", slot_depth)

ceiling_fiberglass_40K.writeFile(verbose=True)

### Equations file -> 40K - Assembly - Fiber Glass Supports
assembly_fiberglass_40K = SolidWorksPart("equations_40_assemblyFiberglass.txt", units="mm", parent_directory=parentDir)

assembly_fiberglass_40K.addVariableLine("D1@Distance1", slot_clearance_for_fiberglass_40K)
assembly_fiberglass_40K.addVariableLine("D1@Distance2", slot_clearance_for_fiberglass_40K)

assembly_fiberglass_40K.writeFile(verbose=True)
