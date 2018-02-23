import numpy as np

"""
All units are SI (meters, kilograms, seconds)
"""

kb = 1.38064852E-23 # m^2 kg s^-2 K^-1
h = 6.62607004E-34 # m^s kg s^-1

def calcPhotonShotNoiseTES(frequency, totalRadPower, photonOccupationNumber, opticalEfficiency):
    return np.sqrt(2.0 * h * frequency * totalRadPower * (1.0 + (photonOccupationNumber * opticalEfficiency)))


def calcPhononNoiseTES(baseTemperature, tesTemperature, conductancePrefactorK, fitted_n):
    tempRatio = baseTemperature / tesTemperature
    heatPower = conductancePrefactorK * ((tesTemperature**fitted_n) - (baseTemperature**fitted_n))
    tempModelFactor = (1.0 + (tempRatio**(fitted_n + 1.0))) / (1.0 - (tempRatio**fitted_n))
    return np.sqrt(2.0 * kb * tesTemperature * heatPower * fitted_n * tempModelFactor)


def calcNEC_TES(NEP_TES, NEP_phonon, powerCurrentDerivative):
    return (NEP_TES + NEP_phonon) ** powerCurrentDerivative



def calcNEC_TESandSQUID(NEC_TES, NEC_SQUID):
    return np.sqrt(NEC_SQUID**2.0 + NEC_SQUID**2.0)


def calcNEV_total(NEC_TESandSQUID, squidInductanceCurrentDerivative, resonantFrequencySquidCurrentDerivative,
                  S_21ResonantFrequencyDerivative, readoutVoltageS_21Derivative):
    NEV_total = NEC_TESandSQUID * squidInductanceCurrentDerivative * resonantFrequencySquidCurrentDerivative \
                * S_21ResonantFrequencyDerivative * readoutVoltageS_21Derivative
    return NEV_total


if __name__ == "__main__":
    """
    From Hannes Hubmayr (johanneshubmayr@gmail.com) to Phil Mauskopf on February 15, 2018 
    Message is coped below
    'The mutual inductance from TES input to SQUID is 230 pH.  A half a flux quanta shifts the resonator frequency on
    the order of the bandwidth, which is 100kHz for this design.  Brad can give you a better of the frequency shift 
    based on recent measurements.'
    """
    resonantFrequencySquidCurrentDerivative = 100.0E3 / 230.0E-12 # Hz / Henry

    NEC_TESandSQUID = 1.0
    squidInductanceCurrentDerivative = 1.0
    S_21ResonantFrequencyDerivative = 1.0
    readoutVoltageS_21Derivative = 1.0


    NEV = calcNEV_total(NEC_TESandSQUID, squidInductanceCurrentDerivative, resonantFrequencySquidCurrentDerivative,
                        S_21ResonantFrequencyDerivative, readoutVoltageS_21Derivative)