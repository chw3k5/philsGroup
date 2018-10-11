import numpy as np
from solidworks.swVariables import SolidWorksPart
"""
Measured Variables (in millimeters)
"""
coax_length_forty_to_three_hundred = 82.12
coax_length_four_to_forty = 34.278
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
standard_helix_radius = 20.0
standard_helix_pitch = 10.0
strait_distance_to_amplifier = 5.0
port2_4to40_helix_start_offset = 10



port2_four_to_forty_right = {}
port2_copper_right = {}
port2_forty_to_three_hundred_right = {}

port2_four_to_forty_left = {}
port2_forty_to_three_hundred_left = {}

list_of_cable_dictionaries = [port2_forty_to_three_hundred_right, port2_four_to_forty_right,
                              port2_four_to_forty_left, port2_forty_to_three_hundred_left]

list_of_port1_cable_dictionaries = []
list_of_port2_cable_dictionaries = [port2_forty_to_three_hundred_right, port2_four_to_forty_right,
                                    port2_four_to_forty_left, port2_forty_to_three_hundred_left]
list_of_300K_to40K_cable_dictionaries = [port2_forty_to_three_hundred_right, port2_forty_to_three_hundred_left]
list_of_40K_to_4K_cable_dictionaries = []
list_of_4K_toAmplifier_cable_dictionaries = [port2_four_to_forty_right, port2_four_to_forty_left]
list_of_Amplifier_to40K_cable_dictionaries = [port2_copper_right]


"""Standard dictionary assignments"""
for dict in list_of_cable_dictionaries:
    dict["pitch"] = standard_helix_pitch
    dict["helixRadius"] = standard_helix_radius

for dict in list_of_port1_cable_dictionaries:
    dict["cableDiameter"] = port1_cable_diameter

for dict in list_of_port2_cable_dictionaries:
    dict["cableDiameter"] = port2_cable_diameter

for dict in list_of_300K_to40K_cable_dictionaries:
    dict["firstRegionLength"] = coax_length_forty_to_three_hundred / 2.0
    dict["secondRegionLength"] = coax_length_forty_to_three_hundred / 2.0

for dict in list_of_40K_to_4K_cable_dictionaries:
    dict["firstRegionLength"] = coax_length_four_to_forty / 2.0
    dict["secondRegionLength"] = coax_length_four_to_forty / 2.0

port2_four_to_forty_right["arcRadius"] = 15.0
port2_four_to_forty_left["arcRadius"] = 9.525
for dict in list_of_4K_toAmplifier_cable_dictionaries:
    dict["firstRegionLength"] = (coax_length_four_to_amp / 2.0) - dict["arcRadius"] + port2_4to40_helix_start_offset
    dict["secondRegionLength"] = coax_length_four_to_amp / 2.0 - port2_4to40_helix_start_offset
    dict["strait_distance_to_amplifier"] = strait_distance_to_amplifier


"""Customized dimensions for specific cables (millimeters)"""
port2_four_to_forty_right["pitch"] = 8.0

port2_four_to_forty_left["pitch"] = 12.0
# port2_four_to_forty_left["strait_distance_to_amplifier"] = 2.0

port2_forty_to_three_hundred_right["pitch"] = 27.952
port2_forty_to_three_hundred_left["pitch"] = 9.838


"""
A second round of calculations 
"""
for dict in list_of_cable_dictionaries:
    dict["slopeAngle_rad"] = np.arctan(dict["pitch"] / (2.0 * np.pi * dict["helixRadius"]))
    dict["slopeAngle_deg"] = dict["slopeAngle_rad"] * rad_to_deg
    length_of_slope_offset = dict["helixRadius"] * np.sin(dict["slopeAngle_rad"])
    height_of_slope_offset = dict["helixRadius"] * (1.0 - np.cos(dict["slopeAngle_rad"]))
    dict["length_of_slope_offset"] = length_of_slope_offset
    dict["height_of_slope_offset"] = height_of_slope_offset
    dict["firstRegionLength"] = dict["firstRegionLength"] - length_of_slope_offset
    dict["secondRegionLength"] = dict["secondRegionLength"] - length_of_slope_offset
    dict["perpendicularOffset"] = dict["pitch"] + (2.0 * height_of_slope_offset)



"""
Scripts for writing Equations text files for SolidWorks.
"""
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
                                    port2_four_to_forty_right["helixRadius"])
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
                                      port2_forty_to_three_hundred_right["helixRadius"])
port2_40Kto300K_right.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                      port2_forty_to_three_hundred_right["slopeAngle_deg"], units="deg")
port2_40Kto300K_right.addVariableLine("D3@Slope-In going from 1st Strait Region to Helix",
                                      port2_forty_to_three_hundred_right["helixRadius"])
port2_40Kto300K_right.addVariableLine("D1@Reference Circle for Helix",
                                      port2_forty_to_three_hundred_right["helixRadius"])
# port2_40Kto300K_right.addVariableLine("D3@Reference Circle for Helix",
#                                       port2_forty_to_three_hundred_right["pitch"])
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
                                      port2_forty_to_three_hundred_left["helixRadius"])
port2_40Kto300K_left.addVariableLine("D2@Slope-In going from 1st Strait Region to Helix",
                                      port2_forty_to_three_hundred_left["slopeAngle_deg"], units="deg")
port2_40Kto300K_left.addVariableLine("D1@Reference Circle for Helix",
                                      port2_forty_to_three_hundred_left["helixRadius"])
# port2_40Kto300K_left.addVariableLine("D3@Reference Circle for Helix",
#                                       port2_forty_to_three_hundred_left["pitch"])
port2_40Kto300K_left.addVariableLine("D4@Helix/Spiral1",
                                      port2_forty_to_three_hundred_left["pitch"])

port2_40Kto300K_left.writeFile()

