import matplotlib.pyplot as plt
import numpy as np


thermal_conductivity_of_copper = 401.0 # Watts per m Kelvin


def heatTransfer(area, length, T1, T2, thermal_conductivity=thermal_conductivity_of_copper):
    # m Kg s units
    # Q = k * (A/L) * (T2 - T1)
    heating_W = thermal_conductivity * (area / length) * (T2 - T1)
    return heating_W


if __name__ == "__main__":
    print("starting Tests")
    thermal_conductivity = thermal_conductivity_of_copper
    thickness = float(1) # in millimeters

    width = float(30) # in millimeters
    area =( thickness / 1000.) * (width / 1000.0) # m^2
    length = float(100) / 1000.0
    T1 = float(4) # in Kelvin
    T2 = float(41) # in Kelvin
    heating_W = heatTransfer(area, length, T1, T2)
    print(heating_W, "is the heating in Watts")
    print("Tests finished")

    width = float(30) # in millimeters
    area =(thickness/1000.) * (width/1000.0) # m^2
    heatTransfer(area, length, T1, T2)

