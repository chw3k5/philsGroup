import numpy


thermal_conductivity_of_copper = 401.0 # Watts per m Kelvin


def heatTransfer(area, length, T1, T2, thermal_conductivity=thermal_conductivity_of_copper):
    # m Kg s units
    # Q = k * (A/L) * (T1 - T2)
    heating_W = None



    return heating_W



if __name__ == "__main__":
    print("starting Tests")
    thermal_conductivity = thermal_conductivity_of_copper
    thickness = float(1) # in millimeters
    width = float(30) # in milimeters
    area =( thickness/1000.) * (width/1000.0) # m^2
    heatTransfer(area, length, T1, T2)