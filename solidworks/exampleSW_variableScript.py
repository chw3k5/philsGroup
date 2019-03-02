from solidworks.solidWorksVariables import SolidWorksPart
import getpass
import os

"""
User specific Variables:
parent_dir is the location on you computer where the equations files will be generated.
"""
user_name = getpass.getuser()
parent_dir = os.path.join("C:\\Users", user_name,
                          "Documents\\GrabCAD\\SO\\Universal Readout Harness\\ASU Test Harness\\ASU Test Cryostat\\4 K")

"""
Example Script for Generating a text file that can be imported into SolidWorks: 
The example parts name is '4K - Bottom Shield flange.SLDPRT
The generated equation file is named 'bottom_flange_4K.txt"

The SolidWorks variables values are explicitly writen here for clarity. 
However, in most applications it may be more convenient to have a
dictionary or class that stores the all the variables across many different parts.
In practice may parts will share the same variables. 
"""
bottom_flange_4K = SolidWorksPart("bottom_flange_4K.txt", units="mm", parent_directory=parent_dir)
bottom_flange_4K.addVariableLine("D1@Boss-Extrude1", 3.175)
bottom_flange_4K.addVariableLine("D5@sketch1", 422.0)
bottom_flange_4K.addVariableLine("D6@sketch1", 499.95)
bottom_flange_4K.addVariableLine("D7@sketch1", 46.0)

bottom_flange_4K.addVariableLine("D1@fillet1", 2.0, units="in")

bottom_flange_4K.addVariableLine("D1@sketch7", 329.88)
bottom_flange_4K.addVariableLine("D2@sketch7", 12.7)

bottom_flange_4K.addVariableLine("D1@fillet2", 12.7)

bottom_flange_4K.addVariableLine("D1@sketch15", 8.06)
bottom_flange_4K.addVariableLine("D3@sketch15", 130.0)

bottom_flange_4K.writeFile(verbose=True)
