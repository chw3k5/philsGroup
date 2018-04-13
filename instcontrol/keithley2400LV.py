"""
This is for the Keithley 2400-LV source meter, this work in window but the packages that are used at platform
independent.
"""
import time, serial, os, sys


portName = "COM4"
baudrate = 57600
bytesize = 8
stopbits = 1
parity = "N"
timeout = 2


# this is the folder where you can keep the data
dataLogFolder = os.path.join("LED_sweep")
dataFileName = "April_12_2018.csv"

# This an attempt at writing platform independent code.
if sys.platform == "win32":
    rootName = "C:\\"
else:
    rootName = "/"

# if the directory does not exist you can make it

if not os.path.exists(rootName + dataLogFolder):
    os.mkdir(rootName + dataLogFolder)

# the base file name
fullDataPath = os.path.join(rootName + dataLogFolder, dataFileName)



def openKeithley2400LV():
    keithley2400LV = serial.Serial(port=portName, baudrate=baudrate, bytesize=bytesize,
                                   stopbits=stopbits, parity=parity, timeout=timeout)
    return keithley2400LV


def readKeithley(keithley2400LV):
    oneByte = b""
    byteString = b""
    while oneByte is not  b'\n':
        oneByte = keithley2400LV.read()
        byteString += oneByte
        # print(oneByte)
    return byteString

def numberFormat(number):
    formatedString = bytes(str('%1.6e' % number), "UTF-8")
    return formatedString



def getKeithley2400LV_voltage(verbose=False):
    keithley2400LV = openKeithley2400LV()
    keithley2400LV.write(b'MEAS:VOLT?\n')
    voltage = readKeithley(keithley2400LV)
    keithley2400LV.close()
    if verbose:
        print(voltage, "is the read voltage from the Keithley 2400-LV")
    return voltage

def setKeithley2400LV_voltage(setVoltage, verbose=False):
    keithley2400LV = openKeithley2400LV()
    keithley2400LV.write(b":FUNC VOLT\n")
    writeString = b":SOUR:VOLT " + numberFormat(setVoltage) + b"\n"
    keithley2400LV.write(writeString)
    keithley2400LV.close()
    if verbose:
        print("Keithley 2400-LV was set to a voltage of", setVoltage)
    return

def getKeithley2400LV_current(verbose=False):
    keithley2400LV = openKeithley2400LV()
    keithley2400LV.write(b'SOUR:CURR?\n')
    current = float(readKeithley(keithley2400LV))
    keithley2400LV.close()
    if verbose:
        print(current, "is the read current from the Keithley 2400-LV")
    return current

def setKeithley2400LV_current(setCurrent, verbose=False):
    keithley2400LV = openKeithley2400LV()
    keithley2400LV.write(b"SOUR:FUNC CURR\n")
    writeString = b":SOUR:CURR " + numberFormat(setCurrent) + b"\n"
    keithley2400LV.write(writeString)
    keithley2400LV.close()
    if verbose:
        print("Keithley 2400-LV was set to a current of", setCurrent, "Amps")
    return


def init_Keithley2400LV(currentRange):
    keithley2400LV = openKeithley2400LV()
    keithley2400LV.write(b"SOUR:CURR:RANG MIN\n")
    keithley2400LV.write(b"SOUR:CURR:RANG UP\n")
    keithley2400LV.write(b"SOUR:CURR:RANG UP\n")
    keithley2400LV.write(b"SENS:FUNC \"VOLT\"\n")
    keithley2400LV.write(b"SENS:VOLT:PROT " + numberFormat(2) + b"\n")
    keithley2400LV.write(b"SYST:RSEN ON\n")
    keithley2400LV.close()
    return


def getRange_Keithley2400LV(verbose=False):
    keithley2400LV = openKeithley2400LV()
    writeString = b":CURR:RANG?\n"
    keithley2400LV.write(writeString)
    theRange = readKeithley(keithley2400LV)
    keithley2400LV.close()
    if verbose:
        print(theRange, "is the current RANGE from the Keithley 2400-LV")
    return


def turnOutput_ON_keithley2400LV(verbose=False):
    keithley2400LV = openKeithley2400LV()
    keithley2400LV.write(b"OUTPUT ON\n")
    if verbose:
        print("The output for the Keithley 2400-LV at " + portName + " has been set to ON")
    return

def turnOutput_OFF_keithley2400LV(verbose=False):
    keithley2400LV = openKeithley2400LV()
    keithley2400LV.write(b"OUTPUT OFF\n")
    if verbose:
        print("The output for the Keithley 2400-LV at " + portName + " has been set to OFF")
    return


if __name__ == "__main__":
    verbose = False


    init_Keithley2400LV(currentRange=1.05E-4)
    turnOutput_ON_keithley2400LV(verbose=verbose)

    for microAmps in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]:
        setKeithley2400LV_current(microAmps * 1.0E-6, verbose=verbose)
        if microAmps == 0:
            f = open(fullDataPath, 'w')
        else:
            f = open(fullDataPath, 'a')
        f.write(str(getKeithley2400LV_voltage(verbose=verbose)))
        f.close()

    #turnOutput_OFF_keithley2400LV(verbose=verbose)

