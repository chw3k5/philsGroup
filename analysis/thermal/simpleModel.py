import matplotlib.pyplot as plt
import numpy as np


thermal_conductivity_of_copper = 401.0 # Watts per m Kelvin


def heatTransfer(area, length, T1, T2, thermal_conductivity=thermal_conductivity_of_copper):
    # m Kg s units

    heating_W = thermal_conductivity * (area / length) * (T2 - T1)
    return heating_W

def areaOfHeatTransfer(heating_W, length_m, T1_K, T2_K, thermal_conductivity_W_mK=thermal_conductivity_of_copper):
    """
    :param heating_W: the amount of heating in Watts
    :param length_m: the length of the heat strapping in meters
    :param T1_K: The temperature in Kelvin of the coldhead or heat sink
    :param T2_K: The temperature in Kelvin of the thing being cooled or heated
    :param thermal_conductivity_W_mK: Thermal conductivity in Watt per (meter * Kelvin
    :return: area in units of meters squared
    Q = k * (A/L) * (T2 - T1)
    <==> Q = k * A * (T2 - T1) / L
    <==> Q = k * A * (T2 - T1) / L
    <==> Q * L / (k * (T2-T1)) = A

    """
    return heating_W * length_m / (thermal_conductivity_W_mK * np.abs(T2_K - T1_K))


if __name__ == "__main__":
    print("starting Tests")




