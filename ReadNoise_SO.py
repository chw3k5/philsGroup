import numpy as np

"""
All units are SI (meters, kilograms, seconds)
"""

kb = 1.38064852E-23 # m^2 kg s^-2 K^-1
h = 6.62607004E-34 # m^s kg s^-1


def dBmToWatts(dBm):
    return 10.0**((dBm - 30.0 ) / 10.0)


def calcPhotonShotNoiseTES(frequency, totalRadPower, photonOccupationNumber, opticalEfficiency):
    return np.sqrt(2.0 * h * frequency * totalRadPower * (1.0 + (photonOccupationNumber * opticalEfficiency)))


def calcPhononNoiseTES(baseTemperature, tesTemperature, conductancePrefactorK, fitted_n):
    tempRatio = baseTemperature / tesTemperature
    heatPower = conductancePrefactorK * ((tesTemperature**fitted_n) - (baseTemperature**fitted_n))
    tempModelFactor = (1.0 + (tempRatio**(fitted_n + 1.0))) / (1.0 - (tempRatio**fitted_n))
    return np.sqrt(2.0 * kb * tesTemperature * heatPower * fitted_n * tempModelFactor)


def calcNEC_TES(NEP_TES, NEP_phonon, currentPowerDerivative):
    return (NEP_TES + NEP_phonon) * currentPowerDerivative



def calcNEC_TESandSQUID(NEC_TES, NEC_SQUID):
    return np.sqrt(NEC_SQUID**2.0 + NEC_SQUID**2.0)


def calcNEV_total(NEC_TESandSQUID, squidInductanceCurrentDerivative, resonantFrequencySquidCurrentDerivative,
                  S_21ResonantFrequencyDerivative, readoutVoltageS_21Derivative):
    NEV_total = NEC_TESandSQUID * squidInductanceCurrentDerivative * resonantFrequencySquidCurrentDerivative \
                * S_21ResonantFrequencyDerivative * readoutVoltageS_21Derivative
    return NEV_total


def calcReadNoise(verbose=False):
    """
    From Hannes Hubmayr (johanneshubmayr@gmail.com) to Phil Mauskopf on February 15, 2018 
    Message is coped below
    'The mutual inductance from TES input to SQUID is 230 pH.  A half a flux quanta shifts the resonator frequency on
    the order of the bandwidth, which is 100kHz for this design.  Brad can give you a better of the frequency shift 
    based on recent measurements.'
    """
    resonantFrequencySquidCurrentDerivative = 100.0E3 / 230.0E-12 # Hz / Henry

    """
    The following is from 
    "Microwave SQUID Multiplexer Demonstration for Cosmic Microwave Background Imagers" by B Dober, D.T. Becker, 
    D.A. Bennett, S.A. Bryan, and 9 others. December 16, 2017
    
    NEC_SQUID = 98.1 pA/sqrt(Hz)
    conductancePrefactorK = 8765 pW / K
    fitted_n = 3.6 # unitlesss
    baseTemperature = 50 mK
    tesTemperature = 182.5 mK
    totalRadPower = 10.04 pW
    frequency = 150.0 # GHz
    powerCurrentDerivative = V = 233 nV
    
    From the top of Phillip Mauskopf's head:
    readoutVoltageS_21Derivative = -70 dBm / V
    
    """

    totalRadPower = 10.04E-12  # Watts
    # inBandPhotonFraction = 1.0 # no units, between 0 and 1
    frequency = 150.0E9 # Hertz

    photonOccupationNumber = 1

    opticalEfficiency = 1.0 # no units, represents number of photons
    baseTemperature = 150.0E-3 # Kelvin
    tesTemperature = 182.5E-3 # Kelvin
    conductancePrefactorK = 8765.0E-12 # Watts / Kelvin
    fitted_n = 3.6 # unitlesss



    NEP_photon = calcPhotonShotNoiseTES(frequency, totalRadPower, photonOccupationNumber, opticalEfficiency)
    NEP_phonon = calcPhononNoiseTES(baseTemperature, tesTemperature, conductancePrefactorK, fitted_n)
    currentPowerDerivative =  1.0 / 233.0E-9 # Volts
    NEC_TES = calcNEC_TES(NEP_photon, NEP_phonon, currentPowerDerivative)
    NEC_SQUID = 98.1E-12  # A / Hz^(1/2)
    NEC_TESandSQUID = calcNEC_TESandSQUID(NEC_TES, NEC_SQUID)


    squidInductanceCurrentDerivative = 1.0 ###################
    S_21ResonantFrequencyDerivative = 1.0 # W / Hz ###############
    readoutVoltageS_21Derivative_dBm = -70.0 # dBm
    readoutVoltageS_21Derivative_W = dBmToWatts(readoutVoltageS_21Derivative_dBm) # Watts


    NEV = calcNEV_total(NEC_TESandSQUID, squidInductanceCurrentDerivative, resonantFrequencySquidCurrentDerivative,
                        S_21ResonantFrequencyDerivative, readoutVoltageS_21Derivative_W)

    if verbose:
        print(totalRadPower * 1.0E12, "pW  is the Total Absorbed Radiative Power.")
        # print(inBandPhotonFraction,
        #       "is the Fraction of In-Band Photons that are included in the Total Absorbed Radiative Power.")
        print(("%3.1f" % (frequency/1.0E9)), "GHz is the average frequency of in-band photons.")
        print("%1.3E" % photonOccupationNumber, "is the photon occupation number")

        print("%1.3E" % (NEP_photon), "W / Hz^(1/2) is the calculated Noise Equivalent Power from PHOTONS in the TES.")
        print("%1.3E" % (NEP_phonon), "W / Hz^(1/2) is the calculated Noise Equivalent Power from PHONONS in the TES.")
        print("%1.3E" % (currentPowerDerivative), 'A / W = 1 / V is the power current derivative.')

        print("%1.3E" % (NEP_photon * currentPowerDerivative),
              "A / Hz^(1/2) is the calculated Noise Equivalent Current from PHOTONS in the TES detector.")
        print("%1.3E" % (NEP_phonon * currentPowerDerivative) ,
              "A / Hz^(1/2) is the calculated Noise Equivalent Current from PHONONS in the TES detector.")

        print("%1.3E" % NEC_TES, "A / Hz^(1/2) is the calculated Noise Equivalent Current from the TES detector.")
        print("%1.3E" % NEC_SQUID, "A / Hz^(1/2) is the Noise Equivalent Current from the SQUID.")
        print("%1.3E" % NEC_TESandSQUID, "A / Hz^(1/2) is the Noise Equivalent Current from the TES-SQUID chain.")

        print(' ')
        print("%1.3E" % squidInductanceCurrentDerivative, "H / A is the SQUID Inductance to Current derivative.")
        print("%1.3E" % resonantFrequencySquidCurrentDerivative,
              "Hz / H Resonant Frequency Shift to SQUID Inductance derivative.")
        print("%1.3E" % S_21ResonantFrequencyDerivative,
              "W / Hz is the Change in Resonator Power at the Carrier Frequency to the change in Resonant Frequency derivative.")

        print("%1.3f" % readoutVoltageS_21Derivative_dBm,
              "V / dBm is the Voltage Resister to Change in Resonator Power at the Carrier Frequency conversion.")
        print("%1.3E" % readoutVoltageS_21Derivative_W,
              "V / W is the Voltage Resister to Change in Resonator Power at the Carrier Frequency conversion.")

        print(" ")
        print("%1.3E" % NEV, "V / Hz^(1/2) is the Noise Equivalent Voltage at the Readout")
    return NEV

if __name__ == "__main__":
    NEV = calcReadNoise(verbose=True)

