import os, sys

class SolidWorksPart:
    def __init__(self, fileName, units="in"):
        if sys.platform == "win32":
            parentDirectory = "G:\\chwheele\\SolidWorks\\SimonsObs\\GrabCAD\\SO\\Universal Readout Harness\\ASU Test Cryostat\\supports"
        else:
            parentDirectory = ""

        self.fullFileName = os.path.join(parentDirectory, fileName)
        self.units = units
        self.fileContent = ""

    def addVariableLine(self, solidworks_variable, a_number, units=None):

        temporary_string = "\"" + solidworks_variable + "\"=" + str(a_number)
        if units is None:
            temporary_string += self.units + "\n"
        else:
            temporary_string += units + "\n"
        self.fileContent += temporary_string

    def writeFile(self):
        file_handle = open(self.fullFileName, "w")
        file_handle.write(self.fileContent)
        file_handle.close()

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

