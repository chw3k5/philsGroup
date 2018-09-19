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


class Shapes():
    def __init__(self, type, dimensions_m):
        self.type = type
        self.dimensions_m = np.array(dimensions_m, dtype=float)
        self.length_m = None
        self.area_m2 = None


    def getLengthAndArea(self):
        if self.type.lower() == "rectangularprism":
            self.length_m, self.width_m, self.depth_m = self.dimensions_m
            self.area_m2 = self.width_m * self.depth_m
        elif self.type.lower() == "cylinder":
            self.length_m, self.diameter_m = self.dimensions_m
            self.area_m2 = ((self.diameter_m / 2.0)**2 ) * np.pi()
        elif self.type.lower() == "cylinder":
            self.length_m, self.outerDiameter_m, self.innerDiameter_m = self.dimensions_m
            self.area_m2 = (((self.outerDiameter_m / 2.0)**2 ) * np.pi()) \
                            - (((self.innerDiameter_m / 2.0)**2 ) * np.pi())
        else:
            print("!Type:", self.type, "is not recognized!")


class HeatConductionStudy():
    def __init__(self, heating_W, T2_K, temperatureDifferenceList_K, testLengthList_m, thermalConductivity_W_mK):
        self.heating_W = float(heating_W) # Watts
        self.T2 = float(T2_K) # Kelvin
        self.temperatureDifferenceList_K = temperatureDifferenceList_K # Kevin
        self.testLengthList_m = testLengthList_m # meters
        self.T1_list_K = []  # Kelvin
        for difference in difference_list:
            self.T1_list_K.append(T2 + float(difference))

        # make a blank dictionary to store area data as a function of temperature
        self.areaProfiles_dict = {}

        # loop over the values to create a dictionary of T1 temperatures, each with a list of conduction areas as
        # a function of conductor lengths (the testLengthList_m variable)
        for T1 in self.T1_list_K:
            # make a blank list to store the conduction areas as a function of
            # conductor lengths (the testLengthList_m variable)
            temporaryList = []
            # loop over the testLengthList_m
            for length_m in self.testLengthList_m:
                # Use the standard function defined in simpleModel.py
                temporary_area = areaOfHeatTransfer(heating_W=heating_W, length_m=length_m, T1_K=T1, T2_K=T2,
                                                    thermal_conductivity_W_mK=thermalConductivity_W_mK)
                temporaryList.append(temporary_area)
            # save this list in the dictionary with the current T1, as the key to find this data
            self.areaProfiles_dict[T1] = temporaryList


    def generatePlots(self, showPlot=True, savePlot=False, doPNG=True,
                      units="m", xLogPlot=False, yLogPlot=True):
        plt.clf()
        # now we will generate the plots
        for T1 in self.T1_list_K:
            area_list_m2 = self.areaProfiles_dict[T1]
            if units == "cm":
                # convert to cm
                lengthArray = np.array(self.testLengthList_m) / 100.0
                area_array_m2 = np.array(area_list_m2)
                areaArray = area_array_m2 * 100.0 * 100.0
                # plot
            elif units == "mm":
                lengthArray = np.array(self.testLengthList_m) / 1000.0
                area_array_m2 = np.array(area_list_m2)
                areaArray = area_array_m2 * 1000.0 * 1000.0
            else:
                lengthArray = np.array(self.testLengthList_m)
                areaArray = np.array(area_list_m2)
            # Plot the Area profiles
            plt.plot(lengthArray, areaArray, label="\u0394 T = " + str("%2.2f" % (T2 - T1)))

        # now the stuff to make the plot look good
        if yLogPlot:
            plt.yscale('log')

        if xLogPlot:
            plt.xscale('log')
        if units == "cm":
            plt.ylabel('Conduction Cross Section ($cm^2$)')
            plt.xlabel('Conduction Length (cm)')
        plotTitleString = "" + str("%1.2f" % self.heating_W) + "W at " + str("%1.2f" %self.T2) + "K"
        plt.title(plotTitleString)
        plt.legend()
        if showPlot:
            plt.show()
        if savePlot:
            plt.draw()
            plotFileName = plotTitleString.replace(" ", "")
            if doPNG:
                plotFileName += '.png'
            else:
                plotFileName += '.eps'
                print("saving file:", plotFileName)
            plt.savefig(plotFileName)



if __name__ == "__main__":
    print("starting Tests")
    heating_W = 50.0 # Watts
    T2 = 40.0 # Kelvin
    # Here we make a list of temperatures for a cryogenic device under test
    difference_list = list(10.0**np.arange(-2, 1.5, 0.5, dtype=float)) # Kelvin

    Study1 = HeatConductionStudy(heating_W=heating_W, T2_K=T2,
                                 temperatureDifferenceList_K=difference_list,
                                 testLengthList_m=np.arange(5.0, 15.0, 0.1, dtype=float),
                                 thermalConductivity_W_mK = 1161.0)
    Study1.generatePlots(units='cm')

    print("Testing Complete")




