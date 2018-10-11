import os, sys

from solidworks.swVariables import SolidWorksPart
"""
These are the variable that you can change
"""
tolerance = 0.005
outer_width = 3.2
bottom_height = 0.5
top_height = 2.6
total_height = 12.0
pipe_thickness = 1/8.


"""
Calculations
"""
inner_width = outer_width - 2. * pipe_thickness
cylinder_height = total_height - 2. * bottom_height
inch_str = "in\n"




supportBase = SolidWorksPart("supportBaseEquations.txt", units="in")
supportBase.addVariableLine("D2@Sketch1", outer_width)
supportBase.addVariableLine("D1@Sketch1", inner_width)
supportBase.addVariableLine("D1@Boss-Extrude1", bottom_height)
supportBase.addVariableLine("D1@Boss-Extrude2", top_height)
supportBase.writeFile()


supportBase = SolidWorksPart("cylinderEquations.txt", units="in")
supportBase.addVariableLine("D2@Sketch1", outer_width)
supportBase.addVariableLine("D1@Sketch1", inner_width + tolerance)
supportBase.addVariableLine("D1@Boss-Extrude1", cylinder_height)
supportBase.writeFile()

