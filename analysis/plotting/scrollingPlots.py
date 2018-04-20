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
        self.plotDict = None
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



    def creatPlotDict(self, doShow=True, doSave=False, plotFileName='plot', title=None):
        # initialize the plotting dictionary an the options you want to select
        self.plotDict = {}
        self.plotDict['verbose'] = self.verbose
        # These must be a single value
        if title is None:
            self.plotDict['title'] = ""
        else:
            self.plotDict['title'] = title
        if self.time_type == "weeks":
            self.plotDict['xlabel'] = 'Relative time (weeks)'
        elif self.time_type == "days":
            self.plotDict['xlabel'] = 'Relative time (days)'
        elif self.time_type == "hours":
            self.plotDict['xlabel'] = 'Relative time (hours)'
        elif self.time_type == "minutes":
            self.plotDict['xlabel'] = 'Relative time (minutes)'
        elif self.time_type == "seconds":
            self.plotDict['xlabel'] = 'Relative time (s)'
        else:
            self.plotDict['xlabel'] = 'Absolute Computer Time (s)'
        self.plotDict['ylabel'] = 'Temperature (Kelvin)'
        self.plotDict['legendAutoLabel'] = False
        self.plotDict['doLegend'] = True
        self.plotDict['legendLoc'] = 0
        self.plotDict['legendNumPoints'] = 3
        self.plotDict['legendHandleLength'] = 3
        self.plotDict['legendFontSize'] = 'x-small' # xx-small, x-small, small, medium, large, x-large, xx-large
        self.plotDict['yLog'] = True
        self.plotDict['doShow'] = doShow

        # These can be a list or a single value
        self.plotDict['yData'] = []
        self.plotDict['xData'] = []
        self.plotDict["colors"] = []
        self.plotDict['ls'] = []
        self.plotDict['legendLabel'] = []
        self.plotDict['fmt'] = "None"

        if doSave:
            self.plotDict['savePlot'] = True
            self.plotDict['plotFileName'] = plotFileName
        else:
            self.plotDict['savePlot'] = False
            self.plotDict['plotFileName'] = ''


    def appendMonitorDataToPlotDict(self, monitor_data):
        self.plotDict['xData'].append(monitor_data.xdata)
        self.plotDict['yData'].append(monitor_data.ydata)
        self.plotDict['colors'].append(monitor_data.plotColor)
        self.plotDict['ls'].append(monitor_data.plotls)
        self.plotDict['legendLabel'].append(monitor_data.dataName + " (" + monitor_data.units + ")")

    def appendAllTempData(self):
        if self.plotDict is None:
            self.creatPlotDict()

        if self.ultrahead_temp is not None:
            self.appendMonitorDataToPlotDict(self.ultrahead_temp)
        if self.interhead_temp is not None:
            self.appendMonitorDataToPlotDict(self.interhead_temp)

        if self.he4Switch_temp is not None:
            self.appendMonitorDataToPlotDict(self.he4Switch_temp)
        if self.interSwitch_temp is not None:
            self.appendMonitorDataToPlotDict(self.interSwitch_temp)
        if self.ultraSwitch_temp is not None:
            self.appendMonitorDataToPlotDict(self.ultraSwitch_temp)

        if self.he4Pump_temp is not None:
            self.appendMonitorDataToPlotDict(self.he4Pump_temp)
        if self.interPump_temp is not None:
            self.appendMonitorDataToPlotDict(self.interPump_temp)
        if self.ultraPump_temp is not None:
            self.appendMonitorDataToPlotDict(self.ultraPump_temp)

        if self.fortyKplate_temp is not None:
            self.appendMonitorDataToPlotDict(self.fortyKplate_temp)


    def make_plots(self):
        quickPlotter(self.plotDict)


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

    monitor = monitorPlots()
    monitor.loadData(logData=logData, verbose=True, time_type="days")
    monitor.creatPlotDict(doShow=True, doSave=True, plotFileName=plotfilename, title="Baby Beluga Monitor")
    monitor.appendAllTempData()
    monitor.make_plots()
