"""
File that makes scrolling plots
"""
import getpass, os, sys
import numpy as np
from matplotlib import pyplot as plt

from analysis.dataGetter import read_csv_file
from analysis.plotting.quickPlots import quickPlotter


class MonitorDataSet:
    def __init__(self, xdata, ydata, units, dataName, plotColor, plotls):
        self.xdata = np.array(xdata)
        self.ydata = np.array(ydata)
        self.units = units
        self.dataName = dataName
        self.plotColor = plotColor
        self.plotls = plotls


class MonitorPlots:
    def __init__(self, doShow=True, doSave=False, time_type="days", verbose=False):
        """
        :param logData:
        :param verbose:
        :return:
        """
        self.verbose = verbose
        self.time_type = time_type
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

        # initialize the plotting dictionary an the options you want to select
        self.temperaturePlotDict = {}
        self.pressurePlotDict = {}

        # These must be a single value
        self.temperaturePlotDict['verbose'] = self.verbose
        self.pressurePlotDict['verbose'] = self.verbose

        self.temperaturePlotDict['doShow'] = doShow
        self.pressurePlotDict['doShow'] = doShow

        self.temperaturePlotDict['saveplot'] = doSave
        self.pressurePlotDict['savePlot'] = doSave

        # these are defaults that can be changed in temperaturePlotDictSpecifics or pressurePlotDictSpecifics
        self.temperaturePlotDict['plotFileName'] = 'temperaturePlot'
        self.pressurePlotDict['plotFileName'] = 'pressurePlot'

        if self.time_type == "weeks":
            self.temperaturePlotDict['xlabel'] = 'Relative time (weeks)'
            self.pressurePlotDict['xlabel'] = 'Relative time (weeks)'
        elif self.time_type == "days":
            self.temperaturePlotDict['xlabel'] = 'Relative time (days)'
            self.pressurePlotDict['xlabel'] = 'Relative time (days)'
        elif self.time_type == "hours":
            self.temperaturePlotDict['xlabel'] = 'Relative time (hours)'
            self.pressurePlotDict['xlabel'] = 'Relative time (hours)'
        elif self.time_type == "minutes":
            self.temperaturePlotDict['xlabel'] = 'Relative time (minutes)'
            self.pressurePlotDict['xlabel'] = 'Relative time (minutes)'
        elif self.time_type == "seconds":
            self.temperaturePlotDict['xlabel'] = 'Relative time (s)'
            self.pressurePlotDict['xlabel'] = 'Relative time (s)'
        else:
            self.temperaturePlotDict['xlabel'] = 'Absolute Computer Time (s)'
            self.pressurePlotDict['xlabel'] = 'Absolute Computer Time (s)'

        self.temperaturePlotDict['legendAutoLabel'] = False
        self.pressurePlotDict['legendAutoLabel'] = False

        self.temperaturePlotDict['doLegend'] = True
        self.pressurePlotDict['doLegend'] = True

        self.temperaturePlotDict['legendLoc'] = 0
        self.pressurePlotDict['legendLoc'] = 0

        self.temperaturePlotDict['legendNumPoints'] = 3
        self.pressurePlotDict['legendNumPoints'] = 3

        self.temperaturePlotDict['legendHandleLength'] = 3
        self.pressurePlotDict['legendHandleLength'] = 3

        self.temperaturePlotDict['yLog'] = True
        self.pressurePlotDict['yLog'] = True

        self.temperaturePlotDict['clearAtTheEnd'] = True
        self.pressurePlotDict['clearAtTheEnd'] = True

        # These can be a list or a single value
        self.temperaturePlotDict['yData'] = []
        self.pressurePlotDict['yData'] = []

        self.temperaturePlotDict['xData'] = []
        self.pressurePlotDict['xData'] = []

        self.temperaturePlotDict["colors"] = []
        self.pressurePlotDict["colors"] = []

        self.temperaturePlotDict['ls'] = []
        self.pressurePlotDict['ls'] = []

        self.temperaturePlotDict['legendLabel'] = []
        self.pressurePlotDict['legendLabel'] = []

        self.temperaturePlotDict['fmt'] = "None"
        self.pressurePlotDict['fmt'] = "None"


    def loadData(self, logData):
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
                self.pressure = MonitorDataSet(time, logData[key], units, dataName, color, ls)

            elif key == "UltraHead_K":
                color = "darkorchid"
                ls = "solid"
                self.ultrahead_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)
            elif key == "InterHead_K":
                color = "dodgerblue"
                ls = "solid"
                self.interhead_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)

            elif key == "He4Switch_K":
                color = "Salmon"
                ls = "dotted"
                self.he4Switch_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)
            elif key == "He3InterSwitch_K":
                color = "slateblue"
                ls = "dotted"
                self.interSwitch_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)
            elif key == "He3UltraSwitch_K":
                color = "Violet"
                ls = "dotted"
                self.ultraSwitch_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)

            elif key == "He4Pump_K":
                color = "firebrick"
                ls = "dashed"
                self.he4Pump_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)
            elif key == "He3InterPump_K":
                color = "CornflowerBlue"
                ls = "dashed"
                self.interPump_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)
            elif key == "UltraPump_K":
                color = "Plum"
                ls = "dashed"
                self.ultraPump_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)

            elif key == "He4Buffer_K":
                color = "yellow"
                ls = "solid"
                self.He4Buffer_K = MonitorDataSet(time, logData[key], units, dataName, color, ls)

            elif (key == "forty_Kplate_K") or (key == "40Kplate_K"):
                color = "Chartreuse"
                ls = "dashdot"
                self.fortyKplate_temp = MonitorDataSet(time, logData[key], units, dataName, color, ls)
            else:
                print(key, "is not a recognized key.")



    def temperaturePlotDictSpecifics(self, plotFileName=None, title=None, yLog=True):
        if title is not None:
            self.pressurePlotDict['title'] = title
        if plotFileName is not None:
            self.pressurePlotDict['plotFileName'] = plotFileName
        self.temperaturePlotDict['legendFontSize'] = 'x-small' # xx-small, x-small, small, medium, large, x-large, xx-large
        self.temperaturePlotDict['yLog'] = yLog
        self.temperaturePlotDict['ylabel'] = 'Temperature (Kelvin)'


    def pressurePlotDictSpecifics(self, plotFileName=None, title=None):
        if title is not None:
            self.pressurePlotDict['title'] = title
        if plotFileName is not None:
            self.pressurePlotDict['plotFileName'] = plotFileName
        self.pressurePlotDict['legendFontSize'] = 'small' # xx-small, x-small, small, medium, large, x-large, xx-large
        self.pressurePlotDict['ylabel'] = 'Pressure (Torr)'


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

        if self.He4Buffer_K is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.He4Buffer_K)

        if self.fortyKplate_temp is not None:
            self.appendMonitorDataToTemperaturePlotDict(self.fortyKplate_temp)


    def appendPressureData(self):
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

    monitor = MonitorPlots(doShow=True, doSave=True, time_type="days", verbose=True)
    monitor.loadData(logData=logData)

    monitor.temperaturePlotDictSpecifics(plotFileName=plotfilename + "_All_Temperatures",
                                         title="Baby Beluga Temperature Monitor",
                                         yLog=False)
    monitor.appendAllTempData()
    monitor.make_temperature_plot()

    monitor.pressurePlotDictSpecifics(plotFileName=plotfilename + "_Pressure",
                                      title="Baby Beluga Pressure Monitor")
    monitor.appendPressureData()
    monitor.make_pressure_plot()


