from getpass import getuser
from matplotlib import pyplot as plt
import numpy, os
from analysis.plotting.quickPlots import quickPlotter

colors = ["firebrick", "dodgerblue", "darkorchid", "DarkSeaGreen", "GoldenRod"]


def readGeneralData(fullPath, numberOfLineToSkip, columns, delimiter=','):
    # read the data
    with open(fullPath) as f:
        content = f.readlines()

    # get the column names from the header
    headerLine = content[numberOfLineToSkip].replace(" ", "").lower().strip().split(delimiter)

    # initialize the dictionary that returns the data
    dataDict = {}
    for column in columns:
        dataDict[headerLine[column]] = []

    # put the data in the dictionary with the corresponding column name
    for dataLine in content[numberOfLineToSkip + 1:]:
        dataInTheLine = dataLine.split(delimiter)
        for column in columns:
            dataDict[headerLine[column]].append(float(dataInTheLine[column]))

    # make the data a numpy array to make math easier
    for column in columns:
        dataDict[headerLine[column]] = numpy.array(dataDict[headerLine[column]])

    return dataDict


def readAgilentData(fullPath):
    numberOfLineToSkip = 2
    columns = [0, 1]
    delimiter = ","
    return readGeneralData(fullPath, numberOfLineToSkip, columns, delimiter=delimiter)


def convertRandS_toAgilent(dataPath, RandS_fileName, convertedBaseName):

    RandS_Dict = readGeneralData(fullPath=os.path.join(dataPath, RandS_fileName),
                               numberOfLineToSkip=2,
                               columns=range(5),
                               delimiter=",")

    for filetype in ["S11_", "S12_", "S21_", "S22_"]:
        search_str = filetype.lower().replace("_", "")
        for key in RandS_Dict.keys():
            if search_str in key.lower():
                break

        fullname = os.path.join(dataPath, filetype + convertedBaseName)
        f = open(fullname, "w")
        f.write("# Channel -1\n")
        f.write("# Trace -1\n")
        f.write("Frequency,Formatted Data\n")

        for index in range(len(RandS_Dict[key])):
            freq = RandS_Dict["freq[hz]"][index]
            value = RandS_Dict[key][index]
            f.write(str(freq) + "," + str(value) + "\n")
        f.close()

    return


def plotFunction(frequencyData, dBmData, fileName, plotFolder, showPlots, savePlots, useGHz, title='', color='black'):
    if useGHz:
        frequencyData = frequencyData / 1.0e9

    plt.plot(frequencyData, dBmData, color=color)

    if useGHz:
        plt.xlabel("Frequency (GHz)")
    else:
        plt.xlabel("Frequency (Hz)")

    plt.ylabel("dBm")
    plt.title(title)

    if showPlots:
        plt.show()

    if savePlots:
        plt.savefig(os.path.join(plotFolder, fileName.replace(".csv", ".png")))

    plt.clf()

    return


def initPlotDict(plot_file_name, y_label, frequency_type="GHz", xminmax=(None, None),
                 title="", show_plot=False, save_plot=False, verbose=False):
    xmin, xmax = xminmax
    # initialize the plotting dictionary an the options you want to select
    plot_dict = {}
    # These options must be a single value
    plot_dict['verbose'] = verbose
    plot_dict['doShow'] = show_plot
    plot_dict['savePlot'] = save_plot
    plot_dict['title'] = title
    plot_dict['plotFileName'] = plot_file_name
    plot_dict['ylabel'] = y_label
    if frequency_type.lower() == "ghz":
        plot_dict['xlabel'] = "frequency (GHz)"
    elif frequency_type.lower() == "mhz":
        plot_dict['xlabel'] = "frequency (MHz)"
    elif frequency_type.lower() == "khz":
        plot_dict['xlabel'] = "frequency (kHz)"
    else:
        plot_dict['xlabel'] = "frequency (Hz)"
    plot_dict['legendAutoLabel'] = False
    plot_dict['doLegend'] = True
    plot_dict['legendLoc'] = 0
    plot_dict['legendNumPoints'] = 3
    plot_dict['legendHandleLength'] = 3
    plot_dict['legendFontSize'] = "medium"  # xx-small, x-small, small, medium, large, x-large, xx-large
    plot_dict['clearAtTheEnd'] = True
    plot_dict["xmin"] = xmin
    plot_dict["xmax"] = xmax
    # These can be a list or a single value
    plot_dict['yData'] = []
    plot_dict['xData'] = []
    plot_dict["colors"] = []
    plot_dict['ls'] = "solid"
    plot_dict['legendLabel'] = []
    plot_dict['fmt'] = "None"
    return plot_dict


def appendToPlotDict(plot_dict, xData, yData, color, legendLable, frequency_type="Ghz"):
    if frequency_type.lower() == "ghz":
        xData = xData * 1.0e-9
    elif frequency_type.lower() == "mhz":
        xData = xData * 1.0e-6
    elif frequency_type.lower() == "khz":
        xData = xData * 1.0e-3
    plot_dict["xData"].append(xData)
    plot_dict["yData"].append(yData)
    plot_dict["colors"].append(color)
    plot_dict["legendLabel"].append(legendLable.replace("_", " ").replace("/", " "))
    return plot_dict


class AgilentData():
    def __init__(self, fileNames, parentFolder):
        self.parentFolder = parentFolder
        [self.S11_fileNames, self.S12_fileNames, self.S21_fileNames, self.S22_fileNames] = [[], [], [], []]
        [self.S11_dataDicts, self.S12_dataDicts, self.S21_dataDicts, self.S22_dataDicts] = [[], [], [], []]

        for fileName in fileNames:
            lowerFileName = fileName.lower()
            if "s11" in lowerFileName:
                self.S11_fileNames.append(fileName)
            elif "s12" in lowerFileName:
                self.S12_fileNames.append(fileName)
            elif "s21" in lowerFileName:
                self.S21_fileNames.append(fileName)
            elif "s22" in lowerFileName:
                self.S22_fileNames.append(fileName)


    def readData(self):
        for S11_fileName in self.S11_fileNames:
            self.S11_dataDicts.append(readAgilentData(os.path.join(self.parentFolder, S11_fileName)))

        for S12_fileName in self.S12_fileNames:
            self.S12_dataDicts.append(readAgilentData(os.path.join(self.parentFolder, S12_fileName)))

        for S21_fileName in self.S21_fileNames:
            self.S21_dataDicts.append(readAgilentData(os.path.join(self.parentFolder, S21_fileName)))

        for S22_fileName in self. S22_fileNames:
            self.S22_dataDicts.append(readAgilentData(os.path.join(self.parentFolder, S22_fileName)))


    def plotSparams(self, show_plots=True, save_plots=False, frequency_type="GHz",
                    xminmax=(None, None), title="", verbose=False):
        # make the plot folder if there is not one already
        plotFolder = os.path.join(self.parentFolder, "plots")
        if save_plots:
            if not os.path.lexists(plotFolder):
                os.mkdir(plotFolder)
        # S11
        plot_dict = initPlotDict(plot_file_name=os.path.join(plotFolder, title + "_S11"),
                                 y_label="S11 (dBm)",
                                 frequency_type=frequency_type,
                                 xminmax=xminmax,
                                 title=title.replace("_", " "),
                                 show_plot=show_plots,
                                 save_plot=save_plots,
                                 verbose=verbose)
        for (index, S11_dataDict) in list(enumerate(self.S11_dataDicts)):
            S11_fileName = self.S11_fileNames[index]
            color = colors[index % len(colors)]
            plot_dict = appendToPlotDict(plot_dict = plot_dict,
                                         xData=S11_dataDict["frequency"],
                                         yData=S11_dataDict["formatteddata"],
                                         color=color,
                                         legendLable=S11_fileName,
                                         frequency_type=frequency_type)
        quickPlotter(plot_dict)

        # S12
        plot_dict = initPlotDict(plot_file_name=os.path.join(plotFolder, title + "_S12"),
                                 y_label="S12 (dBm)",
                                 frequency_type=frequency_type,
                                 xminmax=xminmax,
                                 title=title.replace("_", " "),
                                 show_plot=show_plots,
                                 save_plot=save_plots,
                                 verbose=verbose)
        for (index, S12_dataDict) in list(enumerate(self.S12_dataDicts)):
            S12_fileName = self.S12_fileNames[index]
            color = colors[index % len(colors)]
            plot_dict = appendToPlotDict(plot_dict = plot_dict,
                                         xData=S12_dataDict["frequency"],
                                         yData=S12_dataDict["formatteddata"],
                                         color=color,
                                         legendLable=S12_fileName,
                                         frequency_type=frequency_type)
        quickPlotter(plot_dict)

        # S21
        plot_dict = initPlotDict(plot_file_name=os.path.join(plotFolder, title + "_S21"),
                                 y_label="S21 (dBm)",
                                 frequency_type=frequency_type,
                                 xminmax=xminmax,
                                 title=title.replace("_", " "),
                                 show_plot=show_plots,
                                 save_plot=save_plots,
                                 verbose=verbose)
        for (index, S21_dataDict) in list(enumerate(self.S21_dataDicts)):
            S21_fileName = self.S21_fileNames[index]
            color = colors[index % len(colors)]
            plot_dict = appendToPlotDict(plot_dict = plot_dict,
                                         xData=S21_dataDict["frequency"],
                                         yData=S21_dataDict["formatteddata"],
                                         color=color,
                                         legendLable=S21_fileName,
                                         frequency_type=frequency_type)
        quickPlotter(plot_dict)

        # S22
        plot_dict = initPlotDict(plot_file_name=os.path.join(plotFolder, title + "_S22"),
                                 y_label="S22 (dBm)",
                                 frequency_type=frequency_type,
                                 xminmax=xminmax,
                                 title=title.replace("_", " "),
                                 show_plot=show_plots,
                                 save_plot=save_plots,
                                 verbose=verbose)
        for (index, S22_dataDict) in list(enumerate(self.S22_dataDicts)):
            S22_fileName = self.S22_fileNames[index]
            color = colors[index % len(colors)]
            plot_dict = appendToPlotDict(plot_dict = plot_dict,
                                         xData=S22_dataDict["frequency"],
                                         yData=S22_dataDict["formatteddata"],
                                         color=color,
                                         legendLable=S22_fileName,
                                         frequency_type=frequency_type)
        quickPlotter(plot_dict)



filesToConvert = [
        ("June11_2018", "RandS_A3_300K_2.78V_22mA.csv", "A3_300K_2.78V_22mA.csv"),
        ("June11_2018", "RandS_B3_300K_3.06V_30mA.csv", "B3_300K_3.06V_30mA.csv"),
        ("June11_2018", "RandS_C2_300K_0.00V_0mA.csv", "C2_300K_0.00V_0mA.csv"),
        ("June11_2018", "RandS_C3_300K_0.00V_0mA.csv", "C3_300K_0.00V_0mA.csv"),
        ("June11_2018", "RandS_C1_300K_3.17V_22mA.csv", "C1_300K_3.17V_22mA.csv"),
        ("June11_2018", "RandS_A2_300K_0.00V_0mA.csv", "A2_300K_0.00V_0mA.csv"),
        ("June11_2018", "RandS_A1_300K_0.00V_0mA.csv", "A1_300K_0.00V_0mA.csv"),
        ("June11_2018", "RandS_B1_300K_0.00V_0mA.csv", "B1_300K_0.00V_0mA.csv"),
        ("June11_2018", "RandS_B1_to_A1_300K_SupCondCable.csv", "B1_to_A1_300K.csv"),
    ]

setsOfFileNames =[
    {"title":"TolTEC1_Port2_A3_300K",
     "file_names":[os.path.join("March25_2018", "A3_S11_300K_2.10V.csv"),
                   os.path.join("March25_2018", "A3_S12_300K_2.10V.csv"),
                   os.path.join("March25_2018", "A3_S21_300K_2.10V.csv"),
                   os.path.join("March25_2018", "A3_S22_300K_2.10V.csv"),
                   os.path.join("April27_2018", "A3_S11_300K_2.81V.csv"),
                   os.path.join("April27_2018", "A3_S12_300K_2.81V.csv"),
                   os.path.join("April27_2018", "A3_S21_300K_2.81V.csv"),
                   os.path.join("April27_2018", "A3_S22_300K_2.81V.csv"),
                   os.path.join("June11_2018", "S11_A3_300K_2.78V_22mA.csv"),
                   os.path.join("June11_2018", "S12_A3_300K_2.78V_22mA.csv"),
                   os.path.join("June11_2018", "S21_A3_300K_2.78V_22mA.csv"),
                   os.path.join("June11_2018", "S22_A3_300K_2.78V_22mA.csv"),
                   ]},
    {"title": "TolTEC2_Port2_B3_300K",
     "file_names":[os.path.join("March25_2018", "B3_S11_300K_1.54V.csv"),
                   os.path.join("March25_2018", "B3_S12_300K_1.54V.csv"),
                   os.path.join("March25_2018", "B3_S21_300K_1.54V.csv"),
                   os.path.join("March25_2018", "B3_S22_300K_1.54V.csv"),
                   os.path.join("April27_2018", "B3_S11_300K_2.35V.csv"),
                   os.path.join("April27_2018", "B3_S12_300K_2.35V.csv"),
                   os.path.join("April27_2018", "B3_S21_300K_2.35V.csv"),
                   os.path.join("April27_2018", "B3_S22_300K_2.35V.csv"),
                   os.path.join("June11_2018", "S11_B3_300K_3.06V_30mA.csv"),
                   os.path.join("June11_2018", "S12_B3_300K_3.06V_30mA.csv"),
                   os.path.join("June11_2018", "S21_B3_300K_3.06V_30mA.csv"),
                   os.path.join("June11_2018", "S22_B3_300K_3.06V_30mA.csv"),
                   ]},
    {"title": "TolTEC1_Port1_C2_300K",
     "file_names":[os.path.join("March25_2018", "C2_S11_300K.csv"),
                   os.path.join("March25_2018", "C2_S12_300K.csv"),
                   os.path.join("March25_2018", "C2_S21_300K.csv"),
                   os.path.join("March25_2018", "C2_S22_300K.csv"),
                   os.path.join("April27_2018", "C2_S11_300K.csv"),
                   os.path.join("April27_2018", "C2_S12_300K.csv"),
                   os.path.join("April27_2018", "C2_S21_300K.csv"),
                   os.path.join("April27_2018", "C2_S22_300K.csv"),
                   os.path.join("June11_2018", "S11_C2_300K_0.00V_0mA.csv"),
                   os.path.join("June11_2018", "S12_C2_300K_0.00V_0mA.csv"),
                   os.path.join("June11_2018", "S21_C2_300K_0.00V_0mA.csv"),
                   os.path.join("June11_2018", "S22_C2_300K_0.00V_0mA.csv"),
                   ]},
    {"title": "TolTEC2_Port1_C3_300K",
     "file_names":[os.path.join("March25_2018", "C3_S11_300K.csv"),
                   os.path.join("March25_2018", "C3_S12_300K.csv"),
                   os.path.join("March25_2018", "C3_S21_300K.csv"),
                   os.path.join("March25_2018", "C3_S22_300K.csv"),
                   os.path.join("April27_2018", "C3_S11_300K.csv"),
                   os.path.join("April27_2018", "C3_S12_300K.csv"),
                   os.path.join("April27_2018", "C3_S21_300K.csv"),
                   os.path.join("April27_2018", "C3_S22_300K.csv"),
                   os.path.join("June11_2018", "S11_C3_300K_0.00V_0mA.csv"),
                   os.path.join("June11_2018", "S12_C3_300K_0.00V_0mA.csv"),
                   os.path.join("June11_2018", "S21_C3_300K_0.00V_0mA.csv"),
                   os.path.join("June11_2018", "S22_C3_300K_0.00V_0mA.csv"),
                   ]},
    {"title": "Eds_Port2_C1_300K",
         "file_names":[os.path.join("June11_2018", "S11_C1_300K_3.17V_22mA.csv"),
                       os.path.join("June11_2018", "S12_C1_300K_3.17V_22mA.csv"),
                       os.path.join("June11_2018", "S21_C1_300K_3.17V_22mA.csv"),
                       os.path.join("June11_2018", "S22_C1_300K_3.17V_22mA.csv"),
                       ]},
    {"title": "Eds_Port1_A2_300K",
         "file_names":[os.path.join("June11_2018", "S11_A2_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S12_A2_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S21_A2_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S22_A2_300K_0.00V_0mA.csv"),
                       ]},
    {"title": "SuperConducting_Port1_A1_300K",
         "file_names":[os.path.join("June11_2018", "S11_A1_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S12_A1_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S21_A1_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S22_A1_300K_0.00V_0mA.csv"),
                       ]},
    {"title": "SuperConducting_Port2_B1_300K",
         "file_names":[os.path.join("June11_2018", "S11_B1_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S12_B1_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S21_B1_300K_0.00V_0mA.csv"),
                       os.path.join("June11_2018", "S22_B1_300K_0.00V_0mA.csv"),
                       ]},
    {"title": "SuperConductingCable_B1_to_A1",
         "file_names":[os.path.join("June11_2018", "S11_B1_to_A1_300K.csv"),
                       os.path.join("June11_2018", "S12_B1_to_A1_300K.csv"),
                       os.path.join("June11_2018", "S21_B1_to_A1_300K.csv"),
                       os.path.join("June11_2018", "S22_B1_to_A1_300K.csv"),
                       ]},
    {"title": "Nanowire_Through_300K",
     "file_names": [os.path.join("April27_2018", "nanowire_through_300K", "S11_3.04V_0.22A.csv"),
                    os.path.join("April27_2018", "nanowire_through_300K", "S12_3.04V_0.22A.csv"),
                    os.path.join("April27_2018", "nanowire_through_300K", "S21_3.04V_0.22A.csv"),
                    os.path.join("April27_2018", "nanowire_through_300K", "S22_3.04V_0.22A.csv")]},
    {"title": "Amplifier_X_300K",
     "file_names": [os.path.join("April27_2018", "Amplifier_X", "S11_2.88V.csv"),
                    os.path.join("April27_2018", "Amplifier_X", "S12_2.88V.csv"),
                    os.path.join("April27_2018", "Amplifier_X", "S21_2.88V.csv"),
                    os.path.join("April27_2018", "Amplifier_X", "S22_2.88V.csv")]},
     {"title": "Amplifier_Z_300K",
      "file_names": [os.path.join("April27_2018", "Amplifier_Z", "S11_2.89V.csv"),
                     os.path.join("April27_2018", "Amplifier_Z", "S12_2.89V.csv"),
                     os.path.join("April27_2018", "Amplifier_Z", "S21_2.89V.csv"),
                     os.path.join("April27_2018", "Amplifier_Z", "S22_2.89V.csv")]}
]


if getuser() == "chw3k5":
    parentFolder = os.path.join("/Users", "chw3k5", "Documents", "ASUpostdoc", "BabyBeluga", "Sparams")

    for (dataPath, RandS_fileName, convertedBaseName) in filesToConvert:
        convertRandS_toAgilent(os.path.join(parentFolder, dataPath), RandS_fileName, convertedBaseName)


    for set_dict in setsOfFileNames:
        paramGroup = AgilentData(set_dict["file_names"], parentFolder)
        paramGroup.readData()
        paramGroup.plotSparams(show_plots=False, save_plots=True, frequency_type="GHz",
                               xminmax=(None, 5),
                               title=set_dict["title"], verbose=True)


elif getuser() == "Rebop":
    parentFolder = os.path.join("C:\\", "Users", "Rebop", "Google Drive", "BabyBeluga", "Sparams")

    for (dataPath, RandS_fileName, convertedBaseName) in filesToConvert:
        convertRandS_toAgilent(os.path.join(parentFolder, dataPath), RandS_fileName, convertedBaseName)


    for set_dict in setsOfFileNames:
        paramGroup = AgilentData(set_dict["file_names"], parentFolder)
        paramGroup.readData()
        paramGroup.plotSparams(show_plots=False, save_plots=True, frequency_type="GHz",
                               xminmax=(None, 5),
                               title=set_dict["title"], verbose=True)

else:
    print("Your username is:", getuser())
    print("This program takes different actions based on the user.")
    print("The default action is these three print statements. ")