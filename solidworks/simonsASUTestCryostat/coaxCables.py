import numpy as np
from solidworks.swVariables import SolidWorksPart
"""
Measured Variables (in millimeters)
"""
coax_length_forty_to_three_hundred = 82.12
coax_length_four_to_forty = 34.278
coax_length_four_to_forty_attenuator = 34.276
coax_length_four_to_amp = 63.353
amplifier_center_pin_to_forty_coax_end = -5.969
port1_cable_diameter = 0.89
port2_cable_diameter = 2.19
port2_copper_diameter = 2.09


"""
Calculations (in millimeters)
"""
rad_to_deg = 180.0 / np.pi

# port 2 Copper cable from 40K amplifier to 40K bulkhead connector
port2_copper_cable_amplifier_center_to_forty_kelvin = abs(amplifier_center_pin_to_forty_coax_end)


"""
These are the variable that you can change (in millimeters)
"""
parent_directory = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\Universal Readout Harness\\Coax Cables"
port_parent_directory = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\Universal Readout Harness\\Ports"
standard_helix_radius = 20.0
standard_helix_pitch = 10.0
strait_distance_to_amplifier = 5.0
port2_4to40_helix_start_offset = 10


port1_forty_to_four_right = {}
port1_three_hundred_to_forty_right = {}

port1_forty_to_four_left = {}
port1_three_hundred_to_forty_left = {}

port2_four_to_forty_right = {}
port2_copper_right = {}
port2_forty_to_three_hundred_right = {}

port2_four_to_forty_left = {}
port2_forty_to_three_hundred_left = {}

list_of_cable_dictionaries = [port1_forty_to_four_right, port1_three_hundred_to_forty_right,
                              port1_forty_to_four_left, port1_three_hundred_to_forty_left,
                              port2_forty_to_three_hundred_right, port2_four_to_forty_right,
                              port2_four_to_forty_left, port2_forty_to_three_hundred_left]

list_of_port1_cable_dictionaries = [port1_forty_to_four_right, port1_three_hundred_to_forty_right,
                                    port1_forty_to_four_left, port1_three_hundred_to_forty_left]
list_of_port2_cable_dictionaries = [port2_forty_to_three_hundred_right, port2_four_to_forty_right,
                                    port2_four_to_forty_left, port2_forty_to_three_hundred_left]
list_of_300K_to40K_cable_dictionaries = [port2_forty_to_three_hundred_right, port2_forty_to_three_hundred_left,
                                         port1_three_hundred_to_forty_right, port1_three_hundred_to_forty_left]
list_of_4K_toAmplifier_cable_dictionaries = [port2_four_to_forty_right, port2_four_to_forty_left]
list_of_4K_to_attenuator_cable_dictionaries = [port1_forty_to_four_right, port1_forty_to_four_left]
list_of_Amplifier_to40K_cable_dictionaries = [port2_copper_right]


"""Standard dictionary assignments"""
for dict in list_of_cable_dictionaries:
    dict["arcRadius"] = None
    dict["setPerpendicularOffset"] = None
    dict["pitch"] = standard_helix_pitch
    dict["helixRadius"] = standard_helix_radius

for dict in list_of_port1_cable_dictionaries:
    dict["cableDiameter"] = port1_cable_diameter

for dict in list_of_port2_cable_dictionaries:
    dict["cableDiameter"] = port2_cable_diameter

for dict in list_of_300K_to40K_cable_dictionaries:
    dict["helixRadius"] = 25.0
    dict["firstRegionLength"] = coax_length_forty_to_three_hundred / 2.0
    dict["secondRegionLength"] = coax_length_forty_to_three_hundred / 2.0

for dict in list_of_4K_to_attenuator_cable_dictionaries:
    dict["firstRegionLength"] = coax_length_four_to_forty_attenuator / 2.0
    dict["secondRegionLength"] = coax_length_four_to_forty_attenuator / 2.0

port2_four_to_forty_right["arcRadius"] = 15.0
port2_four_to_forty_left["arcRadius"] = 9.525
for dict in list_of_4K_toAmplifier_cable_dictionaries:
    dict["firstRegionLength"] = (coax_length_four_to_amp / 2.0) - dict["arcRadius"] + port2_4to40_helix_start_offset
    dict["secondRegionLength"] = coax_length_four_to_amp / 2.0 - port2_4to40_helix_start_offset
    dict["strait_distance_to_amplifier"] = strait_distance_to_amplifier


"""Customized dimensions for specific cables (millimeters)"""
port1_three_hundred_to_forty_right["pitch"] = 30.
port1_three_hundred_to_forty_left["pitch"] = port1_three_hundred_to_forty_right["pitch"]

port2_four_to_forty_right["pitch"] = 8.0

port2_four_to_forty_left["pitch"] = 12.0
port2_four_to_forty_left["helixRadius"] = 18.0
# port2_four_to_forty_left["strait_distance_to_amplifier"] = 2.0

dx_offset = 0.0
port2_forty_to_three_hundred_left_dx = 21.971617 + dx_offset
port2_forty_to_three_hundred_left_dz = 12.889
port2_forty_to_three_hundred_left_angle = \
    np.arctan(port2_forty_to_three_hundred_left_dx / port2_forty_to_three_hundred_left_dz) * 180.0 / np.pi
port2_forty_to_three_hundred_left["setPerpendicularOffset"] = \
    ((port2_forty_to_three_hundred_left_dx**2.0) + (port2_forty_to_three_hundred_left_dz**2.0))**(0.5)

port2_forty_to_three_hundred_right_dx = 19.460732 + dx_offset
port2_forty_to_three_hundred_right_dz = 24.856722
port2_forty_to_three_hundred_right_angle = \
    np.arctan(port2_forty_to_three_hundred_right_dx / port2_forty_to_three_hundred_right_dz) * 180.0 / np.pi
port2_forty_to_three_hundred_right["setPerpendicularOffset"] = \
    ((port2_forty_to_three_hundred_right_dx**2.0) + (port2_forty_to_three_hundred_right_dz**2.0))**(0.5)

"""
A second round of calculations 
"""
for dict in list_of_cable_dictionaries:
    if dict["setPerpendicularOffset"] is not None:
        newPitch = dict["setPerpendicularOffset"]
        accuracy = float("inf")
        requiredAccuracy = 0.001
        while requiredAccuracy < accuracy:
            pitch = newPitch
            slopeAngle_rad = np.arctan(pitch / (2.0 * np.pi * dict["helixRadius"]))
            height_of_slope_offset = pitch * (1.0 - np.cos(slopeAngle_rad))
            perpendicular_Offset = pitch + (2.0 * height_of_slope_offset)
            difference = dict["setPerpendicularOffset"] - perpendicular_Offset
            accuracy = np.abs(difference)
            newPitch += difference
        dict["pitch"] = pitch
    dict["slopeAngle_rad"] = np.arctan(dict["pitch"] / (2.0 * np.pi * dict["helixRadius"]))
    dict["slopeAngle_deg"] = dict["slopeAngle_rad"] * rad_to_deg
    length_of_slope_offset = dict["pitch"] * np.sin(dict["slopeAngle_rad"])
    height_of_slope_offset = dict["pitch"] * (1.0 - np.cos(dict["slopeAngle_rad"]))
    dict["length_of_slope_offset"] = length_of_slope_offset
    dict["height_of_slope_offset"] = height_of_slope_offset
    dict["firstRegionLength"] = dict["firstRegionLength"] - length_of_slope_offset
    dict["secondRegionLength"] = dict["secondRegionLength"] - length_of_slope_offset
    dict["perpendicularOffset"] = dict["pitch"] + (2.0 * height_of_slope_offset)
    dict["totalLength"] = dict["firstRegionLength"] + (2.0 * length_of_slope_offset) + dict["secondRegionLength"]
    if dict["arcRadius"] is not None:
        dict["totalLength"] = dict["totalLength"] + dict["arcRadius"]


"""
Scripts for writing Equations text files for SolidWorks.
"""
# port1 right
port1_40Kto4K_right = SolidWorksPart("port1_40Kto4K_right_Equations.txt", units="mm", parent_directory=parent_directory)
port1_40Kto4K_right.addVariableLine("D1@1st Strait Region",
                                    port1_forty_to_four_right["firstRegionLength"])

port1_40Kto4K_right.addVariableLine("D1@Slope-In going from 1st Strait Region to Helix",
                                    port1_forty_to_four_right["pitch"])
port1_40Kto4K_right.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                    port1_forty_to_four_right["slopeAngle_deg"], units="deg")

port1_40Kto4K_right.addVariableLine("D1@Reference Circle for Helix",
                                    port1_forty_to_four_right["helixRadius"])

port1_40Kto4K_right.addVariableLine("D3@Helix/Spiral1",
                                    port1_forty_to_four_right["pitch"])
port1_40Kto4K_right.addVariableLine("D4@Helix/Spiral1",
                                    port1_forty_to_four_right["pitch"])

port1_40Kto4K_right.addVariableLine("D1@Slope out of Helix and 2nd Strait Region",
                                    port1_forty_to_four_right["secondRegionLength"])
port1_40Kto4K_right.writeFile()


port1_300Kto40K_right = SolidWorksPart("port1_300Kto40K_right_Equations.txt", units="mm", parent_directory=parent_directory)
port1_300Kto40K_right.addVariableLine("D1@1st Strait Region",
                                      port1_three_hundred_to_forty_right["firstRegionLength"])

port1_300Kto40K_right.addVariableLine("D1@Slope-In going from 1st Strait Region to Helix",
                                      port1_three_hundred_to_forty_right["pitch"])
port1_300Kto40K_right.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                      port1_three_hundred_to_forty_right["slopeAngle_deg"], units="deg")

port1_300Kto40K_right.addVariableLine("D1@Reference Circle for Helix",
                                      port1_three_hundred_to_forty_right["helixRadius"])

port1_300Kto40K_right.addVariableLine("D3@Helix/Spiral1",
                                      port1_three_hundred_to_forty_right["pitch"])
port1_300Kto40K_right.addVariableLine("D4@Helix/Spiral1",
                                      port1_three_hundred_to_forty_right["pitch"])

port1_300Kto40K_right.addVariableLine("D1@Slope out of Helix and 2nd Strait Region",
                                      port1_three_hundred_to_forty_right["secondRegionLength"])
port1_300Kto40K_right.addVariableLine("D2@Slope out of Helix and 2nd Strait Region",
                                      port1_three_hundred_to_forty_right["pitch"])

port1_300Kto40K_right.addVariableLine("D1@Coax profile diameter for sweep",
                                      port1_three_hundred_to_forty_right["cableDiameter"])

port1_300Kto40K_right.writeFile()



# port1 Left
port1_40Kto4K_left = SolidWorksPart("port1_40Kto4K_Equations.txt", units="mm", parent_directory=parent_directory)
port1_40Kto4K_left.addVariableLine("D1@1st Strait Region",
                                   port1_forty_to_four_left["firstRegionLength"])

port1_40Kto4K_left.addVariableLine("D1@Slope-In going from 1st Strait Region to Helix",
                                   port1_forty_to_four_left["pitch"])
port1_40Kto4K_left.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                   port1_forty_to_four_left["slopeAngle_deg"], units="deg")

port1_40Kto4K_left.addVariableLine("D1@Reference Circle for Helix",
                                   port1_forty_to_four_left["helixRadius"])

port1_40Kto4K_left.addVariableLine("D3@Helix/Spiral1",
                                   port1_forty_to_four_left["pitch"])
port1_40Kto4K_left.addVariableLine("D4@Helix/Spiral1",
                                   port1_forty_to_four_left["pitch"])

port1_40Kto4K_left.addVariableLine("D1@Slope out of Helix and 2nd Strait Region",
                                   port1_forty_to_four_left["secondRegionLength"])
port1_40Kto4K_left.addVariableLine("D3@Slope out of Helix and 2nd Strait Region",
                                   port1_forty_to_four_left["pitch"])
port1_40Kto4K_left.writeFile()


port1_300Kto40K_left = SolidWorksPart("port1_300Kto40K_left_Equations.txt", units="mm", parent_directory=parent_directory)
port1_300Kto40K_left.addVariableLine("D1@1st Strait Region",
                                     port1_three_hundred_to_forty_left["firstRegionLength"])

port1_300Kto40K_left.addVariableLine("D1@Slope-In going from 1st Strait Region to Helix",
                                     port1_three_hundred_to_forty_left["pitch"])
port1_300Kto40K_left.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                     port1_three_hundred_to_forty_left["slopeAngle_deg"], units="deg")

port1_300Kto40K_left.addVariableLine("D1@Reference Circle for Helix",
                                     port1_three_hundred_to_forty_left["helixRadius"])

port1_300Kto40K_left.addVariableLine("D3@Helix/Spiral1",
                                     port1_three_hundred_to_forty_left["pitch"])
port1_300Kto40K_left.addVariableLine("D4@Helix/Spiral1",
                                     port1_three_hundred_to_forty_left["pitch"])

port1_300Kto40K_left.addVariableLine("D1@Slope out of Helix and 2nd Strait Region",
                                     port1_three_hundred_to_forty_left["secondRegionLength"])

port1_300Kto40K_left.addVariableLine("D1@Coax profile diameter for sweep",
                                     port1_three_hundred_to_forty_left["cableDiameter"])

port1_300Kto40K_left.writeFile()



# port2 Right
port2_4Kto40K_right = SolidWorksPart("port2_4Kto40K_right_Equations.txt", units="mm", parent_directory=parent_directory)
port2_4Kto40K_right.addVariableLine("D1@Sketch1",
                                    port2_four_to_forty_right["arcRadius"])
port2_4Kto40K_right.addVariableLine("D2@Sketch1",
                                    port2_four_to_forty_right["strait_distance_to_amplifier"])

port2_4Kto40K_right.addVariableLine("D1@1st Strait Region",
                                    port2_four_to_forty_right["firstRegionLength"])
port2_4Kto40K_right.addVariableLine("D1@Slope out of Helix and 2nd Strait Region",
                                    port2_four_to_forty_right["secondRegionLength"])
port2_4Kto40K_right.addVariableLine("D3@Slope-In going from 1st Strait Region to Helix",
                                    port2_four_to_forty_right["pitch"])
port2_4Kto40K_right.addVariableLine("D4@Slope-In going from 1st Strait Region to Helix",
                                    port2_four_to_forty_right["slopeAngle_deg"], units="deg")
port2_4Kto40K_right.addVariableLine("D1@Reference Circle for Helix",
                                    port2_four_to_forty_right["helixRadius"])
port2_4Kto40K_right.addVariableLine("D4@Helix/Spiral1",
                                    port2_four_to_forty_right["pitch"])

port2_4Kto40K_right.writeFile()


port2_40Kto300K_right = SolidWorksPart("port2_40Kto300K_right_Equations.txt", units="mm", parent_directory=parent_directory)
port2_40Kto300K_right.addVariableLine("D1@1st strait region",
                                      port2_forty_to_three_hundred_right["firstRegionLength"])
port2_40Kto300K_right.addVariableLine("D1@Slope out of Helix and 2nd Strait Region",
                                      port2_forty_to_three_hundred_right["secondRegionLength"])
port2_40Kto300K_right.addVariableLine("D1@Slope-In going from 1st Strait Region to Helix",
                                      port2_forty_to_three_hundred_right["pitch"])
port2_40Kto300K_right.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                      port2_forty_to_three_hundred_right["slopeAngle_deg"], units="deg")
port2_40Kto300K_right.addVariableLine("D3@Slope-In going from 1st Strait Region to Helix",
                                      port2_forty_to_three_hundred_right["pitch"])
port2_40Kto300K_right.addVariableLine("D1@Reference Circle for Helix",
                                      port2_forty_to_three_hundred_right["helixRadius"])
port2_40Kto300K_right.addVariableLine("D3@Helix/Spiral1",
                                      port2_forty_to_three_hundred_right["pitch"])
port2_40Kto300K_right.addVariableLine("D4@Helix/Spiral1",
                                      port2_forty_to_three_hundred_right["pitch"])

port2_40Kto300K_right.writeFile()


# port2 Left
port2_4Kto40K_left = SolidWorksPart("port2_4Kto40K_left_Equations.txt", units="mm", parent_directory=parent_directory)

port2_4Kto40K_left.addVariableLine("D1@Slope out of Helix and 2nd Strait Region",
                                   port2_four_to_forty_left["secondRegionLength"])
port2_4Kto40K_left.addVariableLine("D2@Slope out of Helix and 2nd Strait Region",
                                   port2_four_to_forty_left["strait_distance_to_amplifier"])
port2_4Kto40K_left.addVariableLine("D3@Slope out of Helix and 2nd Strait Region",
                                   port2_four_to_forty_left["arcRadius"])

port2_4Kto40K_left.addVariableLine("D1@1st Strait Region",
                                   port2_four_to_forty_left["firstRegionLength"])
port2_4Kto40K_left.addVariableLine("D1@Slope-In going from 1st Strait Region to Helix",
                                    port2_four_to_forty_left["pitch"])
port2_4Kto40K_left.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                   port2_four_to_forty_left["slopeAngle_deg"], units="deg")

port2_4Kto40K_left.addVariableLine("D1@Reference Circle for Helix",
                                   port2_four_to_forty_left["helixRadius"])
port2_4Kto40K_left.addVariableLine("D3@Helix/Spiral1",
                                   port2_four_to_forty_left["pitch"])
port2_4Kto40K_left.addVariableLine("D4@Helix/Spiral1",
                                   port2_four_to_forty_left["pitch"])

port2_4Kto40K_left.writeFile()


port2_40Kto300K_left = SolidWorksPart("port2_40Kto300K_left_Equations.txt", units="mm", parent_directory=parent_directory)
port2_40Kto300K_left.addVariableLine("D1@1st strait region",
                                     port2_forty_to_three_hundred_left["firstRegionLength"])
port2_40Kto300K_left.addVariableLine("D1@Slope out of Helix and 2nd Strait Region",
                                     port2_forty_to_three_hundred_left["secondRegionLength"])
port2_40Kto300K_left.addVariableLine("D1@Slope-In going from 1st Strait Region to Helix",
                                     port2_forty_to_three_hundred_left["pitch"])
port2_40Kto300K_left.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                     port2_forty_to_three_hundred_left["slopeAngle_deg"], units="deg")
port2_40Kto300K_left.addVariableLine("D1@Reference Circle for Helix",
                                     port2_forty_to_three_hundred_left["helixRadius"])
port2_40Kto300K_left.addVariableLine("D3@Helix/Spiral1",
                                     port2_forty_to_three_hundred_left["pitch"])
port2_40Kto300K_left.addVariableLine("D4@Helix/Spiral1",
                                     port2_forty_to_three_hundred_left["pitch"])

port2_40Kto300K_left.writeFile()

""" The Assembly Files """
port1_assembly_angle = 42.535


port1_Assembly_left = SolidWorksPart("port1_assembly_left_Equations.txt", units="deg",
                                     parent_directory=port_parent_directory)
port1_Assembly_left.addVariableLine("D1@Angle1", port1_assembly_angle)
port1_Assembly_left.writeFile()

port1_Assembly_right = SolidWorksPart("port1_assembly_right_Equations.txt", units="deg",
                                      parent_directory=port_parent_directory)
port1_Assembly_right.addVariableLine("D1@Angle1", port1_assembly_angle)
port1_Assembly_right.writeFile()

port2_Assembly_left = SolidWorksPart("port2_assembly_left_Equations.txt", units="deg",
                                     parent_directory=port_parent_directory)
port2_Assembly_left.addVariableLine("D1@Angle1", port2_forty_to_three_hundred_left_angle)
port2_Assembly_left.writeFile()

port2_Assembly_right = SolidWorksPart("port2_assembly_right_Equations.txt", units="deg",
                                     parent_directory=port_parent_directory)
port2_Assembly_right.addVariableLine("D1@Angle1", port2_forty_to_three_hundred_right_angle)
port2_Assembly_right.writeFile()
