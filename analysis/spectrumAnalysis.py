# Name: spectrumAnalysis.py
# Author: Jenna E. Moore
# Email: jenna.moore94@gmail.com
# Date: July 19, 2017
# Summary: Complete gamma spectrum analysis. Energy calibration, peak ID, curve fitting,
#			plotting, fwhm and energy resolution calculations.

# import relevant libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import argrelmax

# energy calibration - convert channels/bins into keV by calibrating a known peak
# takes: channel array, counts array, peak location in keV
# returns: calibrated energy and counts arrays
def calibration(channels, counts, peakEV):
    topChans = argrelmax(counts, order=100, mode='wrap')[0]
    peakChan = sorted(topChans, reverse = True)[0]
    scaleFactor = peakEV / peakChan
    energy = scaleFactor * channels
    b = counts - energy
    scaledCounts = energy + b
    return energy, scaledCounts


# gaussian function
# takes: energy array, values for peak amplitude, position, and standard deviation
# returns: gaussian function for the given parameters
def gaussian(energy, amplitude, position, stdDev):
    a = float(amplitude)
    b = float(position)
    c = float(stdDev)
    return a * np.exp(-(energy - b) ** 2 / (2 * c ** 2))


# generate optimized peak amplitude, position, and standard deviation values
# as of 7/20/17, only gaussian is available. may add poisson later.
# takes: a function to fit, energy array, counts array, initial guess values
# returns: optimized fit parameters
def fit(f, energy, scaledCounts, guessParams):
    fitParams, pcov = curve_fit(f, energy, scaledCounts, p0=guessParams)
    return fitParams


# calculate the fwhm and energy resolution of the peak
# takes: optimized fit parameters
# returns: fwhm, energy resolution (percentile) to two decimal places
def characteristics(fitParams):
    amplitude, position, stdDev = fitParams
    fwhm = abs(stdDev) * 2.355  # for gaussian
    er = (fwhm / position) * 100
    fwhm = round(fwhm, 2)
    er = round(er, 2)
    return fwhm, er


# generate plot
# takes: function to fit, energy array, counts array, guess values, plot title
# returns: a plot of the raw data and the fitted function with fwhm and er displayed
def makePlot(f, energy, scaledCounts, guessParams, plotTitle):
    fitParams = fit(f, energy, scaledCounts, guessParams)
    fitCurve = gaussian(energy, *fitParams)
    fwhm, er = characteristics(fitParams)
    plt.plot(energy, fitCurve, 'r', linewidth=2, label='Fit')
    plt.plot(energy, scaledCounts, 'b', label='Spectrum')
    plt.legend(loc=2)
    plt.xlabel('Energy (keV)')
    plt.ylabel('Counts')
    plt.title(plotTitle, size='xx-large')
    plt.text(150, 200, "FWHM = %s \nEnergy Resolution = %s%%" % (fwhm, er))
    plt.savefig('%s.png' % (plotTitle))

#find multiple peaks within a mixed-source spectra
# def findPeaks(f, energy, scaledCounts, guessParams, numPeaks)
#     sortedCounts = sorted(scaledCounts)
#     peaks =

if __name__ == '__main__':
    # replace with filepath of raw data
    dataFile = '/Users/jmo/Documents/Data/Cs-137,Co57, Ba133, Na22,PMT900V, 10us, 10-8-00, lld 0,0_16384_t22,7deg.TKA'

    # read in raw data, create arrays of channels and counts
    counts = np.loadtxt(dataFile, int)
    channels = np.arange(len(counts))

    #replace with calibration peak location (in keV)
    peakEV = float(1274.53)

    #calibrate raw data
    energy, scaledCounts = calibration(channels, counts, peakEV)

    #optional: plot raw data to estimate some guess parameters
    plt.plot(energy, scaledCounts)
    plt.show()

    # replace a, b, with initial guess values for peak amplitude, standard dev.
    # guessParams = [a, peakEV, b]
    #
    # replace with desired plot title
    # plotTitle = 'plotTitle'
    #
    # generate plot
    # makePlot(gaussian, energy, scaledCounts, guessParams, plotTitle)
    #

    #
    # plt.plot(channels, counts)
    # for topChan in topChans:
    #     plt.annotate('peak', xy = (topChan, counts[topChan]))
    # plt.show()