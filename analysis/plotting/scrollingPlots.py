"""
File that makes scrolling plots
"""
import getpass, os, sys
import numpy as np
from matplotlib import pyplot as plt

from analysis.dataGetter import read_csv_file
from analysis.plotting.quickPlots import quickPlotter


class monitorData():
    def __init__(self, xdata, ydata, units, dataName, plotColor, plotls):
        self.xdata = np.array(xdata)
        self.ydata = np.array(ydata)
        self.units = units
        self.dataName = dataName
        self.plotColor = plotColor
        self.plotls = plotls


class monitorPlots():
    def __int__(self):
        """
        :param logData:
        :param verbose:
        :return:
        """
        self.verbose = None
        self.time_type = None
        self.temperaturePlotDict = None
        self.pressurePlotDict = None
        self.pressure = None
        self.ultrahead_temp = None
        self.interhead_temp = None
        self.he4Switch_temp = None
        self.interSwitch_temp = None
        self.ultraSwitch_temp = None
        self.he4Pump_temp = None
        self.interPump_temp = None
        self.ultraPump_temp = None
        self.fortyKplate_temp = None

    def loadData(self, logData, verbose, time_type="days"):
        self.verbose = verbose
        self.time_type = time_type

        timeString = "ctime_s"
        logTime = np.array(logData[timeString])
        if self.time_type == "weeks":
            time = (logTime - logTime[0]) / (60.0 * 60.0 * 24.0 * 7.0)
        elif self.time_type == "days":
            time = (logTime - logTime[0]) / (60.0 * 60.0 * 24.0)
        elif self.time_type == "hours":
            time = (logTime - logTime[0]) / (60.0 * 60.0)
        elif self.time_type == "minutes":
            time = (logTime - logTime[0]) / 60.0
        elif self.time_type == "seconds":
            time = (logTime - logTime[0])
        else:
            time = logTime
        self.dataKeys = list(logData.keys())
        self.dataKeys.remove(timeString)

        for key in self.dataKeys:
            dataName, units = key.split("_")
            if key == "pressure_torr":
                color = "seagreen"
                ls = "solid"
                self.pressure = monitorData(time, logData[key], units, dataName, color, ls)

            elif key == "UltraHead_K":
                color = "darkorchid"
                ls = "solid"
                self.ultrahead_temp = monitorData(time, logData[key], units, dataName, color, ls)
            elif key == "InterHead_K":
                color = "dodgerblue"
                ls = "solid"
                self.interhead_temp = monitorData(time, logData[key], units, dataName, color, ls)

            elif key == "He4Switch_K":
                color = "Salmon"
                ls = "dotted"
                self.he4Switch_temp = monitorData(time, logData[key], units, dataName, color, ls)
            elif key == "He3InterSwitch_K":
                color = "slateblue"
                ls = "dotted"
                self.interSwitch_temp = monitorData(time, logData[key], units, dataName, color, ls)
            elif key == "He3UltraSwitch_K":
                color = "Violet"
                ls = "dotted"
                self.ultraSwitch_temp = monitorData(time, logData[key], units, dataName, color, ls)

            elif key == "He4Pump_K":
                color = "firebrick"
                ls = "dashed"
                self.he4Pump_temp = monitorData(time, logData[key], units, dataName, color, ls)
            elif key == "He3InterPump_K":
                color = "CornflowerBlue"
                ls = "dashed"
                self.interPump_temp = monitorData(time, logData[key], units, dataName, color, ls)
            elif key == "UltraPump_K":
                color = "Plum"
                ls = "dashed"
                self.ultraPump_temp = monitorData(time, logData[key], units, dataName, color, ls)

            elif (key == "forty_Kplate_K") or (key == "40Kplate_K"):
                color = "Chartreuse"
                ls = "dashdot"
                self.fortyKplate_temp = monitorData(time, logData[key], units, dataName, color, ls)

            else:
                color = "black"
                ls = "solid"
                self.pressure = monitorData(time, logData[key], units, dataName, color, ls)



    def createTemperaturePlotDict(self, doShow=True, doSave=False, plotFileName='temperaturePlot', title=None):
        # initialize the plotting dictionary an the options you want to select
        self.temperaturePlotDict = {}
        self.temperaturePlotDict['verbose'] = self.verbose
        # These must be a single value
        if title is None:
            self.temperaturePlotDict['title'] = ""
        else:
            self.temperaturePlotDict['title'] = title
        if self.time_type == "weeks":
            self.temperaturePlotDict['xlabel'] = 'Relative time (weeks)'
        elif self.time_type == "days":
            self.temperaturePlotDict['xlabel'] = 'Relative time (days)'
        elif self.time_type == "hours":
            self.temperaturePlotDict['xlabel'] = 'Relative time (hours)'
        elif self.time_type == "minutes":
            self.temperaturePlotDict['xlabel'] = 'Relative time (minutes)'
        elif self.time_type == "seconds":
            self.temperaturePlotDict['xlabel'] = 'Relative time (s)'
        else:
            self.temperaturePlotDict['xlabel'] = 'Absolute Computer Time (s)'
        self.temperaturePlotDict['ylabel'] = 'Temperature (Kelvin)'
        self.temperaturePlotDict['legendAutoLabel'] = False
        self.temperaturePlotDict['doLegend'] = True
        self.temperaturePlotDict['legendLoc'] = 0
        self.temperaturePlotDict['legendNumPoints'] = 3
        self.temperaturePlotDict['legendHandleLength'] = 3
        self.temperaturePlotDict['legendFontSize'] = 'x-small' # xx-small, x-small, small, medium, large, x-large, xx-large
        self.temperaturePlotDict['yLog'] = True
        self.temperaturePlotDict['doShow'] = doShow

        # These can be a list or a single value
        self.temperaturePlotDict['yData'] = []
        self.temperaturePlotDict['xData'] = []
        self.temperaturePlotDict["colors"] = []
        self.temperaturePlotDict['ls'] = []
        self.temperaturePlotDict['legendLabel'] = []
        self.temperaturePlotDict['fmt'] = "None"

        if doSave:
            self.temperaturePlotDict['savePlot'] = True
            self.temperaturePlotDict['plotFileName'] = plotFileName
        else:
            self.temperaturePlotDict['savePlot'] = False
            self.temperaturePlotDict['plotFileName'] = ''


    def createPressurePlotDict(self, doShow=True, doSave=False, plotFileName='pressurePlot', title=None):
        # initialize the plotting dictionary an the options you want to select
        self.pressurePlotDict = {}
        self.pressurePlotDict['verbose'] = self.verbose
        # These must be a single value
        if title is None:
            self.pressurePlotDict['title'] = ""
        else:
            self.pressurePlotDict['title'] = title
        if self.time_type == "weeks":
            self.pressurePlotDict['xlabel'] = 'Relative time (weeks)'
        elif self.time_type == "days":
            self.pressurePlotDict['xlabel'] = 'Relative time (days)'
        elif self.time_type == "hours":
            self.pressurePlotDict['xlabel'] = 'Relative time (hours)'
        elif self.time_type == "minutes":
            self.pressurePlotDict['xlabel'] = 'Relative time (minutes)'
        elif self.time_type == "seconds":
            self.pressurePlotDict['xlabel'] = 'Relative time (s)'
        else:
            self.pressurePlotDict['xlabel'] = 'Absolute Computer Time (s)'
        self.pressurePlotDict['ylabel'] = 'pressure (Torr)'
        self.pressurePlotDict['legendAutoLabel'] = False
        self.pressurePlotDict['doLegend'] = True
        self.pressurePlotDict['legendLoc'] = 0
        self.pressurePlotDict['legendNumPoints'] = 3
        self.pressurePlotDict['legendHandleLength'] = 3
        self.pressurePlotDict['legendFontSize'] = 'small' # xx-small, x-small, small, medium, large, x-large, xx-large
        self.pressurePlotDict['yLog'] = True
        self.pressurePlotDict['doShow'] = doShow

        # These can be a list or a single value
        self.pressurePlotDict['yData'] = []
        self.pressurePlotDict['xData'] = []
        self.pressurePlotDict["colors"] = []
        self.pressurePlotDict['ls'] = []
        self.pressurePlotDict['legendLabel'] = []
        self.pressurePlotDict['fmt'] = "None"

        if doSave:
            self.pressurePlotDict['savePlot'] = True
            self.pressurePlotDict['plotFileName'] = plotFileName
        else:
            self.pressurePlotDict['savePlot'] = False
            self.pressurePlotDict['plotFileName'] = ''


    def appendMonitorDataToTemperaturePlotDict(self, monitor_data):
        self.temperaturePlotDict['xData'].append(monitor_data.xdata)
        self.temperaturePlotDict['yData'].append(monitor_data.ydata)
        self.temperaturePlotDict['colors'].append(monitor_data.plotColor)
        self.temperaturePlotDict['ls'].append(monitor_data.plotls)
        self.temperaturePlotDict['legendLabel'].append(monitor_data.dataName + " (" + monitor_data.units + ")")


    def appendMonitorDataToPressurePlotDict(self, monitor_data):
        self.pressurePlotDict['xData'].append(monitor_data.xdata)
        self.pressurePlotDict['yData'].append(monitor_data.ydata)
        self.pressurePlotDict['colors'].append(monitor_data.plotColor)
        self.pressurePlotDict['ls'].append(monitor_data.plotls)
        self.pressurePlotDict['legendLabel'].append(monitor_data.dataName + " (" + monitor_data.units + ")")


    def appendAllTempData(self):
        if self.temperaturePlotDict is None:
            self.createTemperaturePlotDict()

        if self.ultrahead_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.ultrahead_temp)
        if self.interhead_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.interhead_temp)

        if self.he4Switch_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.he4Switch_temp)
        if self.interSwitch_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.interSwitch_temp)
        if self.ultraSwitch_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.ultraSwitch_temp)

        if self.he4Pump_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.he4Pump_temp)
        if self.interPump_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.interPump_temp)
        if self.ultraPump_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.ultraPump_temp)

        if self.fortyKplate_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.fortyKplate_temp)


    def appendPressureData(self):
        if self.pressurePlotDict is None:
            self.createPressurePlotDict()
        if self.pressure is not None:
            self.appendMonitorDataToPressurePlotDict(self.pressure)



    def make_temperature_plot(self):
        quickPlotter(self.temperaturePlotDict)


    def make_pressure_plot(self):
        quickPlotter(self.pressurePlotDict)


if __name__ == "__main__":
    """
    User and operating system specific options
    """
    # get the current users username
    username = getpass.getuser()
    # prints the current user's user name
    print("Your username is", username)

    # determine the current operating system
    if sys.platform == "win32":
        # root folder in windows
        rootfolder = "C:\\"
    else:
        # root folder in mac and unix
        rootfolder = "/Users/" + username + "/"
    # looking for file on my own computer
    # os.path.join is platform independent way of joining folders together with the filename
    if username == "meganmoore":
        logFolder = os.path.join(rootfolder, "Downloads")
        plotFolder = os.path.join(rootfolder, "Downloads", "plots")
    elif username == "Rebop":
        logFolder = os.path.join(rootfolder, "Users", "Rebop", "Documents", "CryoStuff")
        plotFolder = os.path.join(rootfolder, "Users", "Rebop", "Documents", "CryoStuff", "plots")
    elif username == "Kanishka":
        logFolder = os.path.join(rootfolder, "Desktop/CryoStat")
        plotFolder = os.path.join(rootfolder,"Desktop/CryoStat", "plots")
    else:
        logFolder = os.path.join(rootfolder, "cryolog")
        plotFolder = os.path.join(rootfolder, "cryolog", "plots")

    # check to see if the log file's folder exists on the current computer
    if os.path.exists(logFolder):
        # make the plot folder if it does not already exist, but only if the log file was found first
        if not os.path.exists(plotFolder):
            os.mkdir(plotFolder)

    # write the final file names, windows has trouble with eps plots
    basename = "April_12_2018"
    logfilename = os.path.join(logFolder, basename + ".csv")
    plotfilename = os.path.join(plotFolder, basename)

    # read the file using the definition in this file
    logData = read_csv_file(filename=logfilename)
    # make a simple test plot
    print(logData.keys(), " are the data types that can be plotted from datDictionary")

    """
    Edit the plot options in the definition "initializeTestPlots"
    Only a few options are available in the input of this definition
    """
    verbose = True
    time_type = "days"
    show_plots = True
    save_plots = True


    monitor = monitorPlots()
    monitor.loadData(logData=logData, verbose=verbose, time_type=time_type)

    monitor.createTemperaturePlotDict(doShow=show_plots, doSave=save_plots,
                                      plotFileName=plotfilename + "_All_Temperatures",
                                      title="Baby Beluga Temperature Monitor")
    monitor.appendAllTempData()
    monitor.make_temperature_plot()

    monitor.createPressurePlotDict(doShow=show_plots, doSave=save_plots,
                                   plotFileName=plotfilename + "_Pressure",
                                   title="Baby Beluga Pressure Monitor")
    monitor.appendPressureData()
    monitor.make_pressure_plot()


