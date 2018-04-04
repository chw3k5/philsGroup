__author__ = 'chw3k5'
import numpy, copy
from operator import itemgetter
from scipy.optimize import curve_fit
from mariscotti import mariscotti, peakFinder
from quickPlots import quickPlotter
from dataGetter import getTableData



def gaussian(x, a, b, c):
    x = numpy.array(x)
    a = float(a)
    b = float(b)
    c = float(c)
    return a * numpy.exp(float(-1.0) * ((x - b)**2.0) / (2.0 * (c**2)))


def singleGaussFitter(spectrum, x, guessParameters, peakName='', showPlot=False, plotDict=None):
    if plotDict is None and showPlot:
        print "Cannot show plot, no plotDict was passed. Setting showPlot to False."
        showPlot = False

    (guessAplitude, guessMean, guessSigma) = guessParameters
    x = numpy.array(x)
    # here is where the fitting is calculated
    modelParams, pcov = curve_fit(gaussian, x, spectrum, p0=guessParameters)
    paramsError = numpy.sqrt(numpy.diag(pcov))

    if showPlot:
        plotDict['yData'].extend([gaussian(x, guessAplitude, guessMean, guessSigma), gaussian(x, *modelParams)])
        plotDict['xData'].extend([x, x])
        plotDict['legendLabel'].extend(['guess' + peakName, 'fitted' + peakName])
        plotDict['fmt'].extend(['o', 'x'])
        plotDict['markersize'].extend([6, 6])
        plotDict['alpha'].extend([0.3, 0.5])
        plotDict['ls'].extend(['dashed', 'dotted'])
        plotDict['lineWidth'].extend([1, 1])
        return modelParams, paramsError, plotDict
    else:
        return modelParams, paramsError


def listGaussFitter(spectrum, x,
                    errFactor=1, numberOfIndexesToSmoothOver=1, showPlot_peakFinder=False,
                    showPlot_gaussFitters=False, verbose=False):
    # apply the mariscotti peak finding algorithm
    guessParametersSet = peakFinder(spectrum, x,
                                    numberOfIndexesToSmoothOver=numberOfIndexesToSmoothOver,
                                    errFactor=errFactor,
                                    showPlot_peakFinder=showPlot_peakFinder,
                                    verbose=verbose)

    # piloting initialization and defaults
    if showPlot_gaussFitters:
        plotDict = {}
        plotDict['verbose'] = verbose
        plotDict['doShow'] = showPlot_gaussFitters

        # These can be a list or a single value, here we initialize a list.
        plotDict['yData'] = []
        plotDict['xData'] = []
        plotDict['legendLabel'] = []
        plotDict['fmt'] = []
        plotDict['markersize'] = []
        plotDict['alpha'] = []
        plotDict['ls'] = []
        plotDict['lineWidth'] = []

        # These must be a single value
        plotDict['title'] = ''
        plotDict['xlabel'] = 'Channel Number'
        plotDict['legendAutoLabel'] = False
        plotDict['doLegend'] = True
        plotDict['legendLoc'] = 0
        plotDict['legendNumPoints'] = 3
        plotDict['legendHandleLength'] = 5
        plotDict['clearAtTheEnd'] = False

        # append the plot values for the raw spectrum
        plotDict['yData'].append(spectrum[:])
        plotDict['xData'].append(x)
        plotDict['legendLabel'].append('rawData')
        plotDict['fmt'].append('None')
        plotDict['markersize'].append(5)
        plotDict['alpha'].append(1.0)
        plotDict['ls'].append('solid')
        plotDict['lineWidth'].append(3)
    else:
        plotDict = None

    # get the model parameters and Error for all the found peaks in the list.
    # list of tuple, [(modelParam, paramsError), ]
    # where modelParam = [amplitude, mean, sigma],  paramsError = [amplitude error, mean error, sigma error]
    modelInfo = []
    numOfFitsInList = len(guessParametersSet)
    formatStr = '%1.4f'
    spectrumForFitter = copy.copy(spectrum)
    for (fitNum, guessParameters) in list(enumerate(guessParametersSet)):
        modelParams, paramsError, plotDict = \
            singleGaussFitter(spectrumForFitter, x, guessParameters,
                              peakName=' peak ' + str(fitNum + 1),
                              showPlot=True,
                              plotDict=plotDict)
        # quickPlotter(plotDict=plotDict)
        # subtract the fit from the spectrum so that the next peak can't find it.
        spectrumForFitter -= gaussian(x, *modelParams)
        modelInfo.append((modelParams, paramsError))
        if verbose:
            print "fitting for the found peak", fitNum + 1, "of", numOfFitsInList
            print "in amplitude (guess, fitted, error) = (" + \
                  str(formatStr % guessParameters[0]) + ", " +\
                  str(formatStr % modelParams[0]) + ", " +\
                  str(formatStr % paramsError[0]) + ")"
            print "in mean (guess, fitted, error) = (" + \
                  str(formatStr % guessParameters[1]) + ", " +\
                  str(formatStr % modelParams[1]) + ", " +\
                  str(formatStr % paramsError[1]) + ")"
            print "in sigma (guess, fitted, error) = (" + \
                  str(formatStr % guessParameters[2]) + ", " +\
                  str(formatStr % modelParams[2]) + ", " +\
                  str(formatStr % paramsError[2]) + ")\n"


    if showPlot_gaussFitters:
        quickPlotter(plotDict=plotDict)

    return modelInfo


def deconvolveGaussFitter():
    # loop through and see if it is worth trying to fit to the other local maxima
    gg_init=models.Gaussian1D(modelParamsList[0])
    len_maximaList = len(maximaList)
    if 1 < len_maximaList:
        for loopIndex in range(1,len_maximaList):
            R_last = R_val_current
            (x_mean,x_apml) = maximaList[loopIndex]
            gg_init=current_models+models.Gaussian1D(x_apml, x_mean, 5)
            gg_Fit = fitter(gg_init,x,counts)
            fit_info = fitter.fit_info
            R_val_current = fit_info['final_func_val']
            if showFitterPlots: testSpecPlotting(counts,x,gg_Fit,gg_init, showPlot=True)
            if R_val_current <= R_last*(1.-fractionalRimprovment):
                modelParamsList.append((gg_Fit.parameters[0], gg_Fit.parameters[1], gg_Fit.parameters[2]))
                current_models += models.Gaussian1D(modelParamsList[loopIndex])
            else:
                break

    return





if __name__ == '__main__':
    # A few options for this data
    endIndex = 100
    verbose = True
    numberOfIndexesToSmoothOver = 5
    errFactor = 50
    showPlot_peakFinder = False
    showPlot_gaussFitters = True


    # Get the test data
    testDataFile = "/Users/jmo/Desktop/Data/Cs137_10uCi_32cm_PMT.TKA"
    if verbose:
        print "Getting the test data in the file.", testDataFile
    testData = getTableData(testDataFile)
    chan = testData['chan'][:endIndex]
    spectrum = testData['data'][:endIndex]


    modelInfo = listGaussFitter(spectrum, chan,
                                errFactor=errFactor,
                                numberOfIndexesToSmoothOver=numberOfIndexesToSmoothOver,
                                showPlot_peakFinder=showPlot_peakFinder,
                                showPlot_gaussFitters=showPlot_gaussFitters,
                                verbose=verbose)







