"""
This is a class used to generate text files that can be imported into SolidWorks to set values.
"""
import os
import sys


class SolidWorksPart:
    def __init__(self, file_name, units="in", parent_directory=None):
        if parent_directory is None:
            if sys.platform == "win32":
                parent_directory = "C:\\Users\\chw3k5\\Documents\\GrabCAD\\SO\\Universal Readout Harness\\ASU Test Harness\\ASU Test Cryostat\\supports"
            else:
                parent_directory = ""

        self.fullFileName = os.path.join(parent_directory, file_name)
        self.units = units
        self.fileContent = ""

    def addVariableLine(self, solidworks_variable, a_number, units=None):

        temporary_string = "\"" + solidworks_variable + "\"=" + str(a_number)
        if units is None:
            temporary_string += self.units + "\n"
        else:
            temporary_string += units + "\n"
        self.fileContent += temporary_string

    def writeFile(self, verbose=False):
        file_handle = open(self.fullFileName, "w")
        file_handle.write(self.fileContent)
        file_handle.close()
        if verbose:
            print("Wrote file:\n ", self.fullFileName, "\n")
