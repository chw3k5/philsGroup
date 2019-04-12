import numpy as np
from solidworks.solidWorksVariables import SolidWorksPart
from sys import platform
import getpass
import os

def numFormat(testNum, format_str="%2.1f"):
    try:
        return str(format_str % testNum)
    except:
        return testNum


"""
Measured Variables (in millimeters)
"""
user_name = getpass.getuser()
base_directory = "C:\\Users\\" + user_name + "\\Documents\\"
if user_name == "jemoor15":
    harness_name = "SAT 1"
else:
    harness_name = "ASU Test Harness"

electrical_plane_to_coax_tip = 2.794

bulkhead_sma_short_side_flange_bottom_to_electrical_plane = 14.224
bulkhead_sma_long_side_to_electrical_plane = 12.7
bulkhead_plus_40K_attenuator = 37.338 - 4.064
fortyK_plate_thickness = 8.0
sma_weld_to_electrical_plane = 8.382
amp_center_pin_to_40K_plate = 16.157

inner_distance_40K_to_300K_sma_relief = 111.7
inner_distance_4K_40K = 102.35

coax_electrical_length_forty_to_three_hundred = inner_distance_40K_to_300K_sma_relief - sma_weld_to_electrical_plane \
                                                - bulkhead_sma_long_side_to_electrical_plane + fortyK_plate_thickness
coax_electrical_length_four_to_forty_attenuator = inner_distance_4K_40K - bulkhead_plus_40K_attenuator \
                                                  - bulkhead_sma_short_side_flange_bottom_to_electrical_plane
coax_electrical_length_four_to_amp = inner_distance_4K_40K - amp_center_pin_to_40K_plate \
                                     - bulkhead_sma_short_side_flange_bottom_to_electrical_plane
# amplifier_center_pin_to_forty_coax_end = -5.969
port1_cable_diameter = 0.86
port2_cable_diameter = 2.19
port2_copper_diameter = 2.09


"""
Calculations (in millimeters)
"""
rad_to_deg = 180.0 / np.pi

# port 2 Copper cable from 40K amplifier to 40K bulkhead connector
# port2_copper_cable_amplifier_center_to_forty_kelvin = abs(amplifier_center_pin_to_forty_coax_end)


"""
These are the variable that you can change (in millimeters)
"""

parent_directory = base_directory + "GrabCAD\\SO\\" + \
            "Universal Readout Harness\\" + harness_name + "\\Coax Cables"
port_parent_directory = base_directory + "GrabCAD\\SO\\" + \
            "Universal Readout Harness\\" + harness_name + "\\Ports"
standard_helix_radius = 20.0
standard_helix_pitch = 10.0
strait_distance_to_amplifier = 5.0
port2_4to40_helix_start_offset = 10


port1_forty_to_four_right = {"name":"port1_forty_to_four_right", "helix_chirality":"left"}
port1_three_hundred_to_forty_right = {"name":"port1_three_hundred_to_forty_right", "helix_chirality":"right"}

port1_forty_to_four_left = {"name":"port1_forty_to_four_left", "helix_chirality":"left"}
port1_three_hundred_to_forty_left = {"name":"port1_three_hundred_to_forty_left", "helix_chirality":"left"}

port2_four_to_forty_right = {"name":"port2_four_to_forty_right", "helix_chirality":"right"}
port2_copper_right = {"name":"port2_copper_right"}
port2_forty_to_three_hundred_right = {"name":"port2_forty_to_three_hundred_right", "helix_chirality":"right"}

port2_four_to_forty_left = {"name":"port2_four_to_forty_left", "helix_chirality":"left"}
port2_forty_to_three_hundred_left = {"name":"port2_forty_to_three_hundred_left", "helix_chirality":"left"}

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
    dict["thermal_len"] = 0.0
    dict["numberToOrder"] = 8.0 #15.0
    dict["cableMaterial"] = "Cupronickel/PTFE/Cupronickel"

for dict in list_of_port1_cable_dictionaries:
    dict["cableDiameter"] = port1_cable_diameter
    dict["loss_dB_per_mm_1Ghz"] = 0.0077
    dict["loss_dB_per_mm_5Ghz"] = 0.0171
    dict["loss_dB_per_mm_10Ghz"] = 0.0243

    dict["coax_head_len"] = 14.0
    dict["coax_head_electrical_len"] = dict["coax_head_len"] - electrical_plane_to_coax_tip


for dict in list_of_port2_cable_dictionaries:
    dict["cableDiameter"] = port2_cable_diameter
    dict["loss_dB_per_mm_1Ghz"] = 0.0034
    dict["loss_dB_per_mm_5Ghz"] = 0.0076
    dict["loss_dB_per_mm_10Ghz"] = 0.0108

    dict["coax_head_len"] = 10.83
    dict["coax_head_electrical_len"] = dict["coax_head_len"] - electrical_plane_to_coax_tip

for dict in list_of_300K_to40K_cable_dictionaries:
    dict["helixRadius"] = 25.0

    dict["electrical_plane_overall_distance"] = coax_electrical_length_forty_to_three_hundred
    dict["visible_coax_overall_distance"] = dict["electrical_plane_overall_distance"] \
                                            - (2.0 * dict["coax_head_electrical_len"])
    dict["tip_to_tip_overall_distance"] = dict["electrical_plane_overall_distance"] \
                                          + (2.0 * electrical_plane_to_coax_tip)
    dict["firstRegionLength"] = dict["visible_coax_overall_distance"] / 2.0
    dict["secondRegionLength"] = dict["visible_coax_overall_distance"] / 2.0

for dict in list_of_4K_to_attenuator_cable_dictionaries:
    dict["electrical_plane_overall_distance"] = coax_electrical_length_four_to_forty_attenuator
    dict["visible_coax_overall_distance"] = dict["electrical_plane_overall_distance"] \
                                            - (2.0 * dict["coax_head_electrical_len"])
    dict["tip_to_tip_overall_distance"] = dict["electrical_plane_overall_distance"] \
                                          + (2.0 * electrical_plane_to_coax_tip)
    dict["firstRegionLength"] = dict["visible_coax_overall_distance"] / 2.0
    dict["secondRegionLength"] = dict["visible_coax_overall_distance"] / 2.0

port2_four_to_forty_right["arcRadius"] = 15.0
port2_four_to_forty_left["arcRadius"] = 9.525
for dict in list_of_4K_toAmplifier_cable_dictionaries:
    dict["electrical_plane_overall_distance"] = coax_electrical_length_four_to_amp
    dict["visible_coax_overall_distance"] = dict["electrical_plane_overall_distance"] - dict["coax_head_electrical_len"]
    dict["tip_to_tip_overall_distance"] = dict["electrical_plane_overall_distance"] + electrical_plane_to_coax_tip

    dict["firstRegionLength"] = (dict["visible_coax_overall_distance"] /
                                 2.0) - dict["arcRadius"] + port2_4to40_helix_start_offset
    dict["secondRegionLength"] = (dict["visible_coax_overall_distance"] /
                                  2.0) - port2_4to40_helix_start_offset
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
    # thermal length calculations
    dict["helix_len"] = ((2.0 * np.pi * dict["helixRadius"])**2.0 + (dict["pitch"])**2.0)**0.5
    dict["slopeArc_len"] = dict["slopeAngle_rad"] * dict["pitch"]
    dict["thermal_len"] += dict["firstRegionLength"] \
                           + (2.0 * dict["slopeArc_len"]) \
                           + dict["helix_len"] \
                           + dict["secondRegionLength"]

    if dict["arcRadius"] is not None:
        dict["totalLength"] = dict["totalLength"] + dict["arcRadius"]
        dict["thermal_len"] += ((dict["arcRadius"] * np.pi * 2.0) / 4.0) + dict["strait_distance_to_amplifier"]

    dict["surface_area"] = dict["thermal_len"] * dict["cableDiameter"] * np.pi


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
if platform == "win32":
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
if platform == "win32":
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
if platform == "win32":
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
if platform == "win32":
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
if platform == "win32":
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
if platform == "win32":
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
if platform == "win32":
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
if platform == "win32":
    port2_40Kto300K_left.writeFile()

""" The Assembly Files """
port1_assembly_angle = 42.535


port1_Assembly_left = SolidWorksPart("port1_assembly_left_Equations.txt", units="deg",
                                     parent_directory=port_parent_directory)
port1_Assembly_left.addVariableLine("D1@Angle1", port1_assembly_angle)
if platform == "win32":
    port1_Assembly_left.writeFile()

port1_Assembly_right = SolidWorksPart("port1_assembly_right_Equations.txt", units="deg",
                                      parent_directory=port_parent_directory)
port1_Assembly_right.addVariableLine("D1@Angle1", port1_assembly_angle)
if platform == "win32":
    port1_Assembly_right.writeFile()

port2_Assembly_left = SolidWorksPart("port2_assembly_left_Equations.txt", units="deg",
                                     parent_directory=port_parent_directory)
port2_Assembly_left.addVariableLine("D1@Angle1", port2_forty_to_three_hundred_left_angle)
if platform == "win32":
    port2_Assembly_left.writeFile()

port2_Assembly_right = SolidWorksPart("port2_assembly_right_Equations.txt", units="deg",
                                     parent_directory=port_parent_directory)
port2_Assembly_right.addVariableLine("D1@Angle1", port2_forty_to_three_hundred_right_angle)
if platform == "win32":
    port2_Assembly_right.writeFile()


"""
Print Calculations for total coax lengths and surface area. 
"""

for cable_dict in list_of_cable_dictionaries:
    cable_dict["electrical_len"] = cable_dict["thermal_len"] + (2.0 * cable_dict["coax_head_electrical_len"])
    cable_dict["cable_len"] = cable_dict["thermal_len"] + (2.0 * cable_dict["coax_head_len"])

    cable_dict["loss_at_1GHz"] = cable_dict["electrical_len"] * cable_dict["loss_dB_per_mm_1Ghz"]
    cable_dict["loss_at_5GHz"] = cable_dict["electrical_len"] * cable_dict["loss_dB_per_mm_5Ghz"]
    cable_dict["loss_at_10GHz"] = cable_dict["electrical_len"] * cable_dict["loss_dB_per_mm_10Ghz"]

# header_keys = ["name", "cable_len", "thermal_len", "surface_area", "loss_at_1GHz", "loss_at_5GHz", "loss_at_10GHz", "helixRadius"]
header_keys = ["name", "cable_len", "cableDiameter", "cableMaterial", "helixRadius", "helix_chirality", "numberToOrder"]
if user_name == "jemoor15":
    f = open(os.path.join(base_directory, "cable_properties.csv"), "w")
else:
    f = open("/Users/" + user_name + " /Documents/ASUpostdoc/SimonsObs/ASU Cryostat/cable_properties.csv", "w")
write_line = ""
for header_key in header_keys:
    if header_key in ["cable_len", "thermal_len", "cableDiameter", "helixRadius"]:
        write_line += header_key + " (mm),"
    elif header_key in ["surface_area"]:
        write_line += header_key + " (mm^2),"
    elif header_key in ["loss_at_1GHz", "loss_at_5GHz", "loss_at_10GHz"]:
        write_line += header_key + " (dB),"
    else:
        write_line += header_key + ","
write_line = write_line[:-1] + "\n"
f.write(write_line)

for cable_dict in list_of_cable_dictionaries:
    write_line = ""
    for header_key in header_keys:
        if header_key in ["cable_len", "thermal_len", "helixRadius"]:
            write_line += numFormat(cable_dict[header_key], "%3.1f") + ","
        elif header_key in ["surface_area"]:
            write_line += numFormat(cable_dict[header_key], "%4.0f") + ","
        elif header_key in ["loss_at_1GHz", "loss_at_5GHz", "loss_at_10GHz"]:
            write_line += numFormat(cable_dict[header_key], "%02.1f") + ","
        elif header_key in ["cableDiameter"]:
            write_line += numFormat(cable_dict[header_key], "%1.2f") + ","
        else:
            write_line += numFormat(cable_dict[header_key]) + ","
    write_line = write_line[:-1] + "\n"
    f.write(write_line)
f.close()
