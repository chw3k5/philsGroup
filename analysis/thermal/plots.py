import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

from analysis.thermal.simpleModel import areaOfHeatTransfer



thermal_conductivity_of_copper = 11.61 # Watts per cm Kelvin

def area_A(length_M,heating,delta_T, thermal_conductivity=thermal_conductivity_of_copper):

    return (length_M/thermal_conductivity)*(heating/delta_T)

if __name__ == "__main__":
    print("starting Tests")

    thermal_conductivity = thermal_conductivity_of_copper
    length_M = np.arange(3, 11, 1) # cm
    delta_T = float(10) # in Kelvin
    heating = float(50) # in Watts
    area_A =(length_M/thermal_conductivity)*(heating/delta_T)

    delta_T2 = float(3)  # in Kelvin
    area_A2 = (length_M / thermal_conductivity) * (heating / delta_T2)

    delta_T3 = float(1)  # in Kelvin
    area_A3 = (length_M / thermal_conductivity) * (heating / delta_T3)

    delta_T4 = float(0.3)  # in Kelvin
    area_A4 = (length_M / thermal_conductivity) * (heating / delta_T4)

    delta_T5 = float(0.3)  # in Kelvin
    area_A5 = (length_M / thermal_conductivity) * (heating / delta_T5)

    delta_T6 = float(0.03)  # in Kelvin
    area_A6 = (length_M / thermal_conductivity) * (heating / delta_T6)

    delta_T7 = float(0.01)  # in Kelvin
    area_A7 = (length_M / thermal_conductivity) * (heating / delta_T7)


    plt.plot(length_M, area_A, label="\u0394T = 10 K")
    plt.plot(length_M,area_A2, label="\u0394T = 3 K")
    plt.plot(length_M,area_A3, label="\u0394T = 1 K")
    plt.plot(length_M,area_A4, label="\u0394T = 0.3 K")
    plt.plot(length_M,area_A5, label="\u0394T = 0.1 K")
    plt.plot(length_M,area_A6, label="\u0394T = 0.03 K")
    plt.plot(length_M,area_A7, label="\u0394T = 0.01 K")
    plt.yscale('log')
    plt.ylabel('Area [$cm^2$]')
   # plt.xscale('log')
    plt.xlabel('Length [cm]')
    plt.title('First Stage (P = 50 Watts) ')
    plt.legend()
    plt.show()


    """
    Begin Caleb Example
    """
    print("Starting Caleb plots")
    plt.clf()
    T2 = float(40) # Kelvin
    # Here we make a list of temperatures for a cryogenic device under test
    difference_list = [10.0, 3.0, 1.0, 0.3, 0.1, 0.03, 0.01] # Kelvin
    T1_list = [] # Kelvin
    for difference in difference_list:
        T1_list.append(T2 + difference)

    # Now we convert to the meter-kilogram-seconds unit system
    # length
    length_array_cm = length_M # lengths in centimeters
    length_array_m = length_array_cm / 100.0 # lengths in meters
    length_list_m = list(length_array_m) # lengths in meters
    # heating
    heating_W = heating # Watts
    # thermal_conductivity
    thermal_conductivity_of_copper_W_cmK = thermal_conductivity_of_copper
    thermal_conductivity_of_copper_W_mK = thermal_conductivity_of_copper_W_cmK * 100.0

    # make a blank dictionary to store area data as a function of temperature
    temperatureProfiles_dict = {}

    # loop over the values to create a dictionary of T1 temperatures, each with a list of conduction areas as
    # a function of conductor lengths (the length_list_m variable)
    for T1 in T1_list:
        # make a blank list to store the conduction areas as a function of
        # conductor lengths (the length_list_m variable)
        temporaryList = []
        # loop over the length_list_m
        for length_m in length_list_m:
            # Use the standard function defined in simpleModel.py
            temporary_area = areaOfHeatTransfer(heating_W=heating_W, length_m=length_m, T1_K=T1, T2_K=T2,
                                                thermal_conductivity_W_mK=thermal_conductivity_of_copper_W_mK)
            temporaryList.append(temporary_area)
        # save this list in the dictionary with the current T1, as the key to find this data
        temperatureProfiles_dict[T1] = temporaryList

    # now we will generate the plots
    for T1 in T1_list:
        area_list_m2 = temperatureProfiles_dict[T1]
        # convert back to cm
        area_array_m2 = np.array(area_list_m2)
        area_array_cm2 = area_array_m2 * 100.0 * 100.0
        # plot
        plt.plot(length_array_cm, area_array_cm2, label="\u0394 T = " + str("%2.2f" % (T2 - T1)))

    # now the stuff to make the plot look good
    plt.yscale('log')
    plt.ylabel('Area [$cm^2$]')
    # plt.xscale('log')
    plt.xlabel('Length [cm]')
    plt.title('First Stage (P = 50 Watts) ')
    plt.legend()
    plt.show()


    print("Tests finished")



