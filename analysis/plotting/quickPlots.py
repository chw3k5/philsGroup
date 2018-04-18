import matplotlib.pyplot as plt
import random, numpy




colors=['BlueViolet','Brown','CadetBlue','Chartreuse', 'Chocolate','Coral','CornflowerBlue','Crimson','Cyan',
        'DarkBlue','DarkCyan','DarkGoldenRod', 'DarkGreen','DarkMagenta','DarkOliveGreen','DarkOrange',
        'DarkOrchid','DarkRed','DarkSalmon','DarkSeaGreen','DarkSlateBlue','DodgerBlue','FireBrick','ForestGreen',
        'Fuchsia','Gold','GoldenRod','Green','GreenYellow','HotPink','IndianRed','Indigo','LawnGreen',
        'LightCoral','Lime','LimeGreen','Magenta','Maroon', 'MediumAquaMarine','MediumBlue','MediumOrchid',
        'MediumPurple','MediumSeaGreen','MediumSlateBlue','MediumTurquoise','MediumVioletRed','MidnightBlue',
        'Navy','Olive','OliveDrab','Orange','OrangeRed','Orchid','PaleVioletRed','Peru','Pink','Plum','Purple',
        'Red','RoyalBlue','SaddleBrown','Salmon','SandyBrown','Sienna','SkyBlue','SlateBlue','SlateGrey',
        'SpringGreen','SteelBlue','Teal','Tomato','Turquoise','Violet','Yellow','YellowGreen']

ls = ['solid', 'dotted', 'dashed', 'dashdot']
lenls = len(ls)

hatches = ['/', '*', '|', '\\', 'x', 'o', '-', '.', '0', '+']


default_plotDict = {}

# These can be a list or a single value
random.shuffle(colors)
random.shuffle(hatches)
default_plotDict['colors'] = colors

default_plotDict['fmt'] = 'o'
default_plotDict['markersize'] = 5
default_plotDict['alpha'] = 1.0
default_plotDict['ls'] = '-'
default_plotDict['marker'] = None
default_plotDict['lineWidth'] = 1

default_plotDict['ErrorMaker'] = '|'
default_plotDict['ErrorCapSize'] = 4
default_plotDict['Errorls'] = 'None'
default_plotDict['Errorliw'] = 1
default_plotDict['xErrors'] = None
default_plotDict['yErrors'] = None
default_plotDict['legendAutoLabel'] = True
default_plotDict['legendLabel'] = ''


# These must be a single value
default_plotDict['title'] = ''
default_plotDict['xlabel'] = ''
default_plotDict['ylabel'] = ''

default_plotDict['doLegend'] = False
default_plotDict['legendLoc'] = 0
default_plotDict['legendNumPoints'] = 3
default_plotDict['legendHandleLength'] = 5

default_plotDict['savePlot'] = False
default_plotDict['plotFileName'] = 'plot'
default_plotDict['doEPS'] = False
default_plotDict['doShow'] = False
default_plotDict['clearAtTheEnd'] = True

default_plotDict['xLog'] = False
default_plotDict['yLog'] = False

# this definition uses the default values defined above is there is no user defined value in dataDict
def extractPlotVal(plotDict, valString, listIndex=0, keys=None):
    # extract the plot value for the list or use a the singleton value
    if keys is not 'None':
        keys = plotDict.keys()
    if valString in keys:
        if isinstance(plotDict[valString], list):
            val = plotDict[valString][listIndex]
        else:
            val = plotDict[valString]
    else:
        val = default_plotDict[valString]
    return val

def quickPlotter(plotDict):
    keys = plotDict.keys()
    if 'verbose' in keys:
        verbose = plotDict['verbose']
    else:
        verbose = True
    if verbose: print('Starting the quick plotting program...')

    # decide if the user wants to plot a legend
    if 'doLegend' in keys:
        doLegend = plotDict['doLegend']
    else:
        doLegend = default_plotDict['doLegend']
    leglabels = []
    leglines = []

    # plot the lists of data
    for (listIndex, yData) in list(enumerate(plotDict['yData'])):
        # Extract the x data for this plot, or use the length of the yData to make x array
        if 'xData' not in keys:
            if verbose: print('no axis found, using the length of the yData')
            xData = range(len(yData))
        else:
            xData = plotDict['xData'][listIndex]

        # extract the plot color for this yData
        if 'colors' in keys:
            if isinstance(plotDict['colors'], list):
                color = plotDict['colors'][listIndex]
            else:
                color = plotDict['colors']
        else:
            color = default_plotDict['colors'][listIndex]

        # extract the plot line style
        ls = extractPlotVal(plotDict, 'ls', listIndex, keys=keys)
        # extract the plot line width
        lineWidth = extractPlotVal(plotDict, 'lineWidth', listIndex, keys=keys)
        # extract the plot marker format
        fmt = extractPlotVal(plotDict, 'fmt', listIndex, keys=keys)
        # exact the marker size
        markersize = extractPlotVal(plotDict, 'markersize', listIndex, keys=keys)
        # extract the marker transparency
        alpha = extractPlotVal(plotDict, 'alpha', listIndex, keys=keys)
        # extract the error marker
        ErrorMaker = extractPlotVal(plotDict, 'ErrorMaker', listIndex, keys=keys)
        # extract the error marker's cap  size
        ErrorCapSize = extractPlotVal(plotDict, 'ErrorCapSize', listIndex, keys=keys)
        # extract the error marker line style
        Errorls = extractPlotVal(plotDict, 'Errorls', listIndex, keys=keys)
        # extract the erro marker line width
        Errorliw = extractPlotVal(plotDict, 'Errorliw', listIndex, keys=keys)

        if doLegend:
            # create the legend line and label
            leglines.append(plt.Line2D(range(10), range(10),
                                       color=color, ls=ls,
                                       linewidth=lineWidth, marker=fmt,
                                       markersize=markersize, markerfacecolor=color,
                                       alpha=alpha))
            leglabels.append(extractPlotVal(plotDict, 'legendLabel', listIndex, keys=keys))

        # this is where the data is plotted
        if verbose:
            print('plotting data in index', listIndex)

        # plot the yData in Linear-Linear for this loop
        plt.plot(xData, yData,linestyle=ls, color=color,
                 linewidth=lineWidth, marker=fmt, markersize=markersize,
                 markerfacecolor=color, alpha=alpha)
        # are there errorbars on this plot?
        if (('xErrors' in keys) or ('yErrors' in keys)):

            # extract the x error (default is "None")
            xError = extractPlotVal(plotDict, 'xErrors', listIndex, keys=keys)
            # extract the y error (default is "None")
            yError = extractPlotVal(plotDict, 'yErrors', listIndex, keys=keys)
            if (xError is not None) or (yError is not None):
                plt.errorbar(xData, yData, xerr=xError, yerr=yError,
                             marker=ErrorMaker, color=color, capsize=ErrorCapSize,
                             linestyle=Errorls, elinewidth=Errorliw)


        # options for dyplayining Log plots
        if extractPlotVal(plotDict, 'xLog', keys=keys):
            plt.xscale('log')
        if extractPlotVal(plotDict, 'yLog', keys=keys):
            plt.yscale('log')





    # now we will add the title and x and y axis labels
    plt.title(extractPlotVal(plotDict, 'title', keys=keys))
    plt.xlabel(extractPlotVal(plotDict, 'xlabel', keys=keys))
    plt.ylabel(extractPlotVal(plotDict, 'ylabel', keys=keys))

    # now we will make the legend (doLegend is True)
    if doLegend:
        # extract the legend info
        if verbose: print('rendering a legend for this plot')
        legendLoc = extractPlotVal(plotDict, 'legendLoc', keys=keys)
        legendNumPoints = extractPlotVal(plotDict, 'legendNumPoints', keys=keys)
        legendHandleLength = extractPlotVal(plotDict, 'legendHandleLength', keys=keys)
        # call the legend command
        plt.legend(leglines, leglabels, loc=legendLoc, numpoints=legendNumPoints, handlelength=legendHandleLength)

    # here the plot can be saved
    if extractPlotVal(plotDict, 'savePlot', keys=keys):
        plotFileName = extractPlotVal(plotDict, 'plotFileName', keys=keys)
        if extractPlotVal(plotDict, 'doEPS', keys=keys):
            plotFileName += '.eps'
        else:
            plotFileName += '.png'
        if verbose: print('saving the plot', plotFileName)
        plt.savefig(plotFileName)

    # here the plot can be shown
    if extractPlotVal(plotDict, 'doShow', keys=keys):
        if verbose: print('showing the plot in a pop up window')
        plt.show()

    if extractPlotVal(plotDict, 'clearAtTheEnd', keys=keys):
        plt.clf()
        plt.close('all')
        print("Closing all plots.")
    if verbose:
        print('...the quick plotting program has finished.')
    return


def rescale(desired, current, target=None):
    if target is None:
        target = current
    maxDesired = max(desired)
    minDesired = min(desired)
    maxCurrent = max(current)
    minCurrent = min(current)

    rangeDesired = float(maxDesired - minDesired)
    rangeCurrent = float(maxCurrent - minCurrent)

    if rangeCurrent == float(0.0):
        # This is the case where current is an array of all the same number.
        # Here we take the middle value of the desired scale and make an array
        # that is only made up of the middle value.
        middleDesired = (rangeDesired / 2.0) + minDesired
        rescaledTarget1 = (target * float(0.0)) + middleDesired
        return rescaledTarget1
    else:
        # 1) set the minimum value of the current to zero
        rescaledTarget1 = target - minCurrent

        # 2) set the maximum value of the rescaledCurrent1 to 1.0
        # (max of rescaledCurrent2 is 1.0, min is 0.0)
        rescaledTarget2 = rescaledTarget1 / rangeCurrent

        # 3 make the range of rescaledCurrent2 the same as the range of the desired
        # (max of rescaledCurrent3 is rangeDesired, min is zero)
        rescaledTarget3 = rescaledTarget2 * rangeDesired

        # 4 make the min of rescaledCurrent3 equal to the min of desired
        # (max of rescaledCurrent3 is rangeDesired + minDesired = maxDesired, min is minDesired)
        rescaledTarget4 = rescaledTarget3 + minDesired

        return rescaledTarget4



def quickHistograms(dataDict, columns=1, bins=10, keys=None,
                    plotFileName='hist', savePlots=False, doEps=False, showPlots=True,
                    verbose=True):
    if keys is None:
        keys = list(dataDict.keys())
    if len(keys) < 3:
            columns = 1
    numOfSubPlots = len(keys)
    rows = int(numpy.ceil(float(numOfSubPlots)/float(columns)))
    if columns == 1:
        f, axarr = plt.subplots(rows)
    else:
        f, axarr = plt.subplots(rows, columns)
    f.tight_layout()
    f.set_size_inches(10, 8)
    row = -1
    histDict = {}


    for (keyIndex, key) in list(enumerate(keys)):
        column = keyIndex % columns
        if column == 0:
            row += 1
        hist, bin_edges = numpy.histogram(dataDict[key], bins=bins)
        binCenters = [(bin_edges[n + 1] + bin_edges[n]) / 2.0 for n in range(bins)]
        binWidth = (binCenters[-1] - binCenters[0]) / float(bins)
        histDict[key] = (hist, binCenters)


        xlabel_str = ''
        if key == 'integral':
            xlabel_str += "Integral V * s"
            color = 'dodgerblue'
            hatch = '/'
        elif key == 'fittedCost':
            xlabel_str += "'Cost' of fitting function"
            color = 'Crimson'
            hatch = '*'
        elif key == 'fittedAmp1':
            xlabel_str += "Fitted Amplitude 1"
            color = 'SaddleBrown'
            hatch = '|'
        elif key == 'fittedTau1':
            xlabel_str += "Fitted Tau 1"
            color = 'darkorchid'
            hatch = '\\'
        elif key == 'fittedAmp2':
            xlabel_str += "Fitted Amplitude 2"
            color = 'GoldenRod'
            hatch = 'x'
        elif key == 'fittedTau2':
            xlabel_str += "Fitted Tau 2"
            color = 'firebrick'
            hatch = 'o'
        elif key == 'fittedAmp3':
            xlabel_str += "Fitted Amplitude 3"
            color = 'forestGreen'
            hatch = '-'
        elif key == 'fittedTau3':
            xlabel_str += "Fitted Tau 3"
            color = 'Fuchsia'
            hatch = '+'
        elif key == 'fittedAmp4':
            xlabel_str += "Fitted Amplitude 4"
            color = 'Chocolate'
            hatch = '.'
        elif key == 'fittedTau4':
            xlabel_str += "Fitted Tau 4"
            color = 'Magenta'
            hatch = '0'
        elif key == 'deltaX':
            xlabel_str += "length of trimmed file (s)"
            color = 'DarkOrange'
            hatch = '+'

        else:
            xlabel_str = str(key)
            color = colors[keyIndex]
            hatch = hatches[keyIndex]


        if xlabel_str != '':
            xlabel_str += ' '
        if columns == 1:
            axarr[row].set_title(xlabel_str)
            axarr[row].bar(binCenters, hist, binWidth, color=color, hatch=hatch)
            axarr[row].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        else:
            axarr[row, column].set_title(xlabel_str)
            axarr[row, column].bar(binCenters, hist, binWidth, color=color, hatch=hatch)
            axarr[row, column].ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        ### Save Plots ###
    if savePlots:
        plt.draw()
        if doEps:
            plotFileName += '.eps'
        else:
            plotFileName += '.png'
        if verbose:
            print("saving file:", plotFileName)
        plt.savefig(plotFileName)


    if showPlots:
        plt.show()

    plt.clf()
    plt.close()
    return histDict




