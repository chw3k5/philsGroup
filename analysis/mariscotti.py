# Purpose:
#  Rudimentary peak finder based on the algorithm
#  developed by Mariscotti [1967] for high resolution
#  gamma ray spectroscopy.
#
#  Mariscotti, M.A., A method for automatic identification of 
#   peaks in the presence of background and its application 
#   to spectrum analysis, Nuclear Instruments and Methods
#   Volume 50, Issue 2, 1 May 1967, Pages 309-320. 
#
# Method:
#  The generalized second derivative (GSD) is calculated and
#  zero crossings are found.  The upper channel for
#  each positive crossing is stored along with the 
#  lower channel for each negative crossing. Pairs
#  of crossings are sought within which the GSD is positive
#  (top of the sombrero). Such pairs contain peaks.
#  Valid peaks are those for which the peak GSD value
#  is greater than some factor times the propogated 
#  uncertainty of the peak GSD value.  
#
#  Two methods are available for determining the 
#  peak channel.  The default is to find the maximum
#  function (y) value within the two crossing channels.
#  If pk_gsd is set, then the maximum value of the
#  GSD (peak of the sombrero) is used. The pk_gsd
#  method might be preferred if the data are very
#  noisy.
#
# Inputs:
#  y         - vector of values representing a spectrum
#              containing peaks
#  err       - keyword, contains the
#              uncertainty in the y values.  If not set,
#              then the y values are assumed to be
#              Poisson random variates (counts)
#  nsmooth   - keyword, contains the number
#              of smoothing steps (must be greater than 0).
#              if not set, then 5 smoothing steps are used
#  errFactor - keyword, for peak detection, the generalized
#              second derivative (GSD) at candidate peak
#              locations must by greater than factor times
#              the GSD uncertainty. The default is
#              errfactor=1.
#  plot     -  keyword, if set produces a diagnostic plot
#  pk_gsd   -  keyword, if set uses the maximum GSD value
#              to identify the peak channel# otherwise,
#              the maximum y value is used to determine the
#              peak channel.
#  
# Outputs:
#  gaussParametersArray   - 'None' or [] or numpy array
#    if no crossing points (inflection points) are found for the generalized second derivative,
#       None is returned
#
#    if there are crossing points but none are selected by the algorithim as peaks,
#       [] the empty list is returned
#
#    if peaks are identified by the algorithm,
#       A numpy array is returned of the Gaussian parameters.
#       The parameters [A, B, and C] = gaussParametersArray[peakNum,:] for the
#       parameters for a single peak with index equal to peakNum
#       where A gaussian distribution is defined as G(x)=A * exp((x-B)^2 / (2 * C^2)).
#       The amplitudes (A) of the peaks can be found as gaussParametersArray[:,0],
#       the peak index value or mean (B) of the peaks can be found as gaussParametersArray[:,1],
#       and the standard deviation or sigma (C) of the peaks can be found as gaussParametersArray[:,2],
#
#
#
# Concerns:
#  The function does not close out plot windows and generates
#  new ones every time it is called with /plot. The user needs
#  to close windows periodically to avoid making a mess (e.g.,
#  using closewin.pro).
#
#  When the max y approach (default) is used to find 
#  the peak location, the channel number for max y
#  in each candidate peak region is used to test if
#  the GSD is factor times greater than uncertainty
#  in the GSD value.  As a result, fewer peaks are
#  identified using the max y method than for the
#  pk_gsb method when the data are noisy.  A future 
#  improvement might be to always select a peak region
#  based on peak GSD and have the option to select
#  the channel within the accepted region as max y.
#
# Revision history:
# $Id: mariscotti.pro,v 1.2 2010/06/16 02:58:24 jpmorgen Exp $
#  v1.0 Thomas H. Prettyman (THP), Planetary Science Institute
#  26-Mar-2010 (THP) 
#     corrected the GSD standard deviation estimate:
#      err=sqrt(1./float(m)^5*err) --> err=sqrt(1./float(m)^m*err)
#     adjusted the index range for gsd so that nsmooth=0 and 1 will
#      work
#     updated documentation
#     added the pk_gsd option
## v1.2 Jeff Morgenthaler (jpm), Planetary Science Institute
# 15-Jun-2010 (jpm)
# Experimented with IDL native deriv and derivsig functions.  Failed
# miserably.  Cleaned up plotting.
#
# On March 1 2017, this code was translated form IDL to python 2.7 by
# Caleb Wheeler for the Fisk Cube sat program.
#
import numpy
from smoothing import boxCar
from quickPlots import quickPlotter, rescale
from operator import itemgetter


def mariscotti(y, **kwargs):

    keys = kwargs.keys()
    y = numpy.array(y)

    # defaults
    vary = y
    f1 = float(1.0)

    # kwargs nsmooth
    if 'nsmooth' in keys:
        m = kwargs['nsmooth']
    else:
        m = 5

    # kwargs err
    if 'err' in keys:
        err = kwargs['err']
        vary=float(err) ** 2.0

    # kwargs factor
    if 'errFactor' in keys:
        factor = float(kwargs['errFactor'])
        f1=factor

    # kwargs pk_gsd
    if 'pk_gsd' in keys:
        pk_gsd = kwargs['pk_gsd']
    else:
        pk_gsd = None

    # kwargs pk_gsd
    if 'plot' in keys:
        showPlot = kwargs['plot']
    else:
        showPlot = False

    # kwargs pk_gsd
    if 'verbose' in keys:
        verbose = kwargs['verbose']
    else:
        verbose = False

    if verbose:
        print("Starting the Mariscotti peak finding and Gaussian parametrization algorithm.")

    # rudimentary peak finder based on Mariscotti [1966]
    kernel1 = numpy.array([-1,2,-1])
    # gsd stands for generalized second derivative
    gsd = numpy.convolve(y, kernel1, 'same')

    #   The line below was translated form IDL code that was in a mysterious loop that seemed to make the exact
    #   same variable assignment 'm' times.
    gsd = boxCar(gsd, kernalSize=m, mode='same')

    kernel2 = numpy.array([1, 4, 1])
    err = numpy.convolve(vary, kernel2, 'same')

    #   The line below was translated form IDL code that was in a mysterious loop that seemed to make the exact
    #   same variable assignment 'm' times.
    err = boxCar(err, kernalSize=m, mode='same')
    # standard deviation of the GSD
    err = ((float(1.0) / (float(m) ** m)) * err) ** float(0.5)


    # find the zero crossings
    l1 = int(4 * (m - 1) / 2 + 1)
    l2 = int(len(vary) - l1)
    icross = []
    for i in range(l1 + 1, l2):
        if (gsd[i] < 0.) and (gsd[i-1] > 0.):
            icross.append(i - 1)
        if (gsd[i] > 0.) and (gsd[i-1] < 0.):
            icross.append(i)

    if icross == []:
        print('No places where the second derivative crosses zero, so no peaks were found by Mariscotti algorithm.')
        if showPlot:
            plotDict = {}
            plotDict['verbose'] = verbose
            # plot formatting for index (x) and spectrum values (y) where the gsd (generalized 2nd derivative)
            # crosses zero (this is marks a boundaries for finding local extrema)
            x = range(len(y))
            # plot formatting for the gsd (generalized second derivative)
            gsd_rescaled = rescale(y, gsd)
            gsd_zeroLine = rescale(y, gsd, numpy.zeros(len(y)))
            # These can be a list or a single value
            plotDict['yData'] = [y, gsd_rescaled, gsd_zeroLine]
            plotDict['xData'] = [x, x, x]
            plotDict['colors'] = ['firebrick', 'darkorchid', "black"]
            plotDict['legendLabel'] = ['The data', '2nd derivative', '2nd deri = 0']
            plotDict['fmt'] = ['None', 'None', 'None']
            plotDict['markersize'] = [5, 5, 5]
            plotDict['alpha'] = [1.0, 1.0, 1.0]
            plotDict['ls'] = ['-', 'dashed', 'dotted']
            plotDict['lineWidth'] = [2, 1, 1]
            # These must be a single value
            plotDict['title'] = '2nd Derivative Zero Crossing Zero (None Found!)'
            plotDict['xlabel'] = 'Channel Number'
            plotDict['legendAutoLabel'] = False
            plotDict['doLegend'] = True
            plotDict['legendLoc'] = 0
            plotDict['legendNumPoints'] = 3
            plotDict['legendHandleLength'] = 5
            plotDict['doShow'] = True
            quickPlotter(plotDict=plotDict)
        if verbose:
            print("Mariscotti algorithm completed.\n")
        return []

    # defined the outputs
    gaussParameters = []

    # find the peaks
    maxAllowedError = f1 * err
    for i in range(len(icross) - 1):
        icrossStart = icross[i]
        icrossStop = icross[i + 1]
        # check that that there are no subsections of zero length (can happen because of the cautious crossover finder
        # used on a noising part of the data)
        if icrossStart != icrossStop:
            gsd_subSample = gsd[icrossStart:icrossStop]
            # Determine is the subset is a peak of a vally
            gsd_subSample_lessThenZero = gsd_subSample[gsd_subSample < 0.0]
            count_gsd_subSample_lessThenZero = len(gsd_subSample_lessThenZero)
            # this is true if the subsection is a peak
            if count_gsd_subSample_lessThenZero == 0:
                indexList = numpy.arange(len(gsd_subSample))
                if pk_gsd is not None:
                    maxval = max(gsd_subSample)
                    indexOfPeak_gsd_subSample = list(indexList[gsd_subSample == maxval])
                else:
                    y_subSmaple = y[icrossStart:icrossStop]
                    maxval = max(y_subSmaple)
                    indexOfPeak_gsd_subSample = list(indexList[y_subSmaple == maxval])
                numOfIndexWithPeakValue = len(indexOfPeak_gsd_subSample)
                if 1 == numOfIndexWithPeakValue:
                    indexOfPeak_y = indexOfPeak_gsd_subSample[0] + icross[i]
                # if more than one index with the max value, take the max GSD value closest to the max y value
                elif 1 < numOfIndexWithPeakValue:
                    highestValueGSD = float('-Inf')
                    chooseIndex = None
                    for testIndex in indexOfPeak_gsd_subSample:
                        currentValueGSD = gsd_subSample[testIndex]
                        if highestValueGSD < currentValueGSD:
                            highestValueGSD = currentValueGSD
                            chooseIndex = testIndex

                    indexOfPeak_y = chooseIndex + icross[i]
                else:
                    indexOfPeak_y = None
                if indexOfPeak_y is not None:
                    if maxAllowedError[indexOfPeak_y] < gsd[indexOfPeak_y]:
                        sigma = float(icrossStop - icrossStart)/float(2.0)
                        gaussParameters.append((maxval, indexOfPeak_y, sigma))

    if gaussParameters == []:
        print("No peaks were found by the Mariscotti algorithm, "+ \
              "but there were places where the second derivative crossed zero.")
        print("This can happen if the maximum allowed error at a peak is greater then the generalized "+\
              "second derivative (gsd) at that point.")
        print("The 'errFactor' =", factor, "can be set using the kwarg 'errFactor' to scale the "+\
              "maximum allowed error.")
        if showPlot:
            plotDict = {}
            plotDict['verbose'] = verbose
            # plot formatting for index (x) and spectrum values (y) where the gsd (generalized 2nd derivative)
            # crosses zero (this is marks a boundaries for finding local extrema)
            y_icrossVals = [y[icrossVal] for icrossVal in icross]
            x = range(len(y))
            # plot formatting for the gsd (generalized second derivative)
            gsd_rescaled = rescale(y, gsd)
            gsd_zeroLine = rescale(y, gsd, numpy.zeros(len(y)))
            gsd_zeroLine_icrossVals = rescale(y, gsd, numpy.zeros(len(icross)))
            maxAllowedError_rescaled  = rescale(y, gsd, maxAllowedError)

            # These can be a list or a single value
            plotDict['yData'] = [y, maxAllowedError_rescaled, gsd_rescaled, gsd_zeroLine, gsd_zeroLine_icrossVals, y_icrossVals]
            plotDict['xData'] = [x, x, x, x, icross, icross]
            plotDict['colors'] = ['firebrick', 'LawnGreen', 'darkorchid', "black", 'black', 'dodgerblue']
            plotDict['legendLabel'] = ['The data', 'max allowed error', '2nd derivative', '2nd deri = 0', 'cross point', 'cross point']
            plotDict['fmt'] = ['None', 'None', 'None', 'None', 'x', 'o']
            plotDict['markersize'] = [5, 5, 5, 5, 10, 9]
            plotDict['alpha'] = [1.0, 1.0, 1.0, 1.0, 0.7, 0.7]
            plotDict['ls'] = ['-', '-', 'dashed', 'dotted', 'None', 'None']
            plotDict['lineWidth'] = [2, 1, 1, 1, 1, 1]
            # These must be a single value
            plotDict['title'] = '2nd Derivative Zero Crossing Zero and Peaks Found'
            plotDict['xlabel'] = 'Channel Number'
            plotDict['legendAutoLabel'] = False
            plotDict['doLegend'] = True
            plotDict['legendLoc'] = 0
            plotDict['legendNumPoints'] = 3
            plotDict['legendHandleLength'] = 5
            plotDict['doShow'] = True
            quickPlotter(plotDict=plotDict)
        if verbose:
            print("Mariscotti algorithm completed.\n")
        return gaussParameters

    else:
        gaussParametersArray = numpy.array(gaussParameters)
        numOfPeaksFound = len(gaussParametersArray[:,0])
        if verbose:
            optional_s = ''
            optional_es = ''
            if 1 < numOfPeaksFound:
                optional_s += 's'
                optional_es += 'es'
            print("A gaussian distribution is defined as G(x)=A * exp((x-B)^2 / (2 * C^2))")
            print("The Mariscotti algorithm has identified", numOfPeaksFound , "peak" + optional_s + ".")
            print("The index" + optional_es + " of the data where the peak can be found (B) are:", gaussParametersArray[:,1])
            print("And the corresponding data value" + optional_s + " for the peak" + optional_s + " (A) are data values:", gaussParametersArray[:,0])
            print("Finally, the sigma value" + optional_s + " (C) of the peak" + optional_s + " (calculated from the inflection points) are", gaussParametersArray[:,2])

        if showPlot:
            plotDict = {}
            plotDict['verbose'] = verbose
            # plot formatting for index (x) and spectrum values (y) where the gsd (generalized 2nd derivative)
            # crosses zero (this is marks a boundaries for finding local extrema)
            y_icrossVals = [y[icrossVal] for icrossVal in icross]
            x = range(len(y))
            # plot formatting for the gsd (generalized second derivative)
            gsd_rescaled = rescale(y, gsd)
            gsd_zeroLine = rescale(y, gsd, numpy.zeros(len(y)))
            gsd_zeroLine_icrossVals = rescale(y, gsd, numpy.zeros(len(icross)))
            maxAllowedError_rescaled  = rescale(y, gsd, maxAllowedError)

            # These can be a list or a single value
            plotDict['yData'] = [y, maxAllowedError_rescaled, gsd_rescaled, gsd_zeroLine, gsd_zeroLine_icrossVals, y_icrossVals, gaussParametersArray[:,0]]
            plotDict['xData'] = [x, x, x, x, icross, icross, gaussParametersArray[:,1]]
            plotDict['colors'] = ['firebrick', 'LawnGreen', 'darkorchid', "black", 'black', 'dodgerblue', 'darkorange']
            plotDict['legendLabel'] = ['The data', 'max allowed error', '2nd derivative', '2nd deri = 0', 'cross point','cross point', 'found peaks']
            plotDict['fmt'] = ['None', 'None', 'None', 'None', 'x', 'o', 'd']
            plotDict['markersize'] = [5, 5, 5, 5, 10, 9, 10]
            plotDict['alpha'] = [1.0, 1.0, 1.0, 1.0, 0.7, 0.7, 0.7]
            plotDict['ls'] = ['-', '-', 'dashed', 'dotted', 'None', 'None', 'None']
            plotDict['lineWidth'] = [2, 1, 1, 1, 1, 1, 1]
            # These must be a single value
            plotDict['title'] = '2nd Derivative Zero Crossing Zero and Peaks Found'
            plotDict['xlabel'] = 'Channel Number'
            plotDict['legendAutoLabel'] = False
            plotDict['doLegend'] = True
            plotDict['legendLoc'] = 0
            plotDict['legendNumPoints'] = 3
            plotDict['legendHandleLength'] = 5
            plotDict['doShow'] = True
            quickPlotter(plotDict=plotDict)
        if verbose:
            print("Mariscotti algorithm completed.\n")
        return gaussParametersArray


def peakFinder(spectrum,
               x,
               numberOfIndexesToSmoothOver=1,
               errFactor=1,
               showPlot_peakFinder=False,
               verbose=True):
    # apply the mariscotti peak finding algorithm
    gaussParametersArray = numpy.array(mariscotti(spectrum, nsmooth=numberOfIndexesToSmoothOver,
                                                  errFactor=errFactor, plot=showPlot_peakFinder, verbose=verbose))

    # apply some simple offset so that this can work with energy units or channel numbers.
    if len(gaussParametersArray) == 0:
        return []
    else:
        energyOffset = float(x[0])
        energySpacing = (float(x[-1]) - float(x[0]))/float(len(x) - 1)
        gaussParametersArray_absouleUnits = gaussParametersArray
        for (valIndex, meanVal) in list(enumerate(gaussParametersArray[:,1])):
            gaussParametersArray_absouleUnits[valIndex,1] = x[int(meanVal)]
        gaussParametersArray_absouleUnits[:,2] = gaussParametersArray[:,2] * energySpacing

        # Sort the peaks from highest to lowest and put them in a list
        guessParametersSet = sorted(gaussParametersArray_absouleUnits, key=itemgetter(0), reverse=True)
        return guessParametersSet




if __name__ == '__main__':
    from dataGetter import getTableData
    # A few options for this data
    endIndex = 100
    verbose = True
    numberOfIndexesToSmoothOver = 5
    errFactor = 50
    showPlot = True

    # Get the test data
    testDataFile = "Am-241.csv"
    if verbose:
        print("Getting the test data in the file.", testDataFile)
    testData = getTableData(testDataFile)
    chan = testData['chan'][:endIndex]
    data = testData['data'][:endIndex]

    # apply the mariscotti peak finding algorithm
    gaussParametersArray = numpy.array(mariscotti(data, nsmooth=numberOfIndexesToSmoothOver,
                                                  errFactor=errFactor, plot=showPlot, verbose=verbose))


