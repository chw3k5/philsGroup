"""
This is for the Keithley 2400-LV source meter.

This is designed to be platform independent and work for python 2 and 3
"""
import time, serial, os, sys

"""
These are definitions that are used by many methods in the Keithley2400LV class below.
"""
def readKeithley(keithley2400LV):
    if sys.version_info.major == 3:
        oneByte = b""
        byteString = b""
        while oneByte is not  b'\n':
            oneByte = keithley2400LV.read()
            byteString += oneByte
    else:
        oneByte = None
        byteString = ""
        while oneByte is not "":
            oneByte = keithley2400LV.read()
            byteString += oneByte
    return byteString


def numberFormat(number):
    if sys.version_info.major == 3:
        formattedString = bytes(str('%1.6e' % number), "UTF-8")
    else:
        formattedString = str("%1.6e" % number)
    return formattedString


"""
This is the class to control the Keithley 2400 LV
"""
class Keithley2400LV():
    def __init__(self, portName, verbose=False):
        self.serialDevice = None
        self.portName = portName
        self.verbose = verbose
        self.baudrate = 57600
        self.bytesize = 8
        self.stopbits = 1
        self.parity = "N"
        self.timeout = 2
        self.fullDataPath = None


    def openPort(self):
        self.serialDevice = serial.Serial(port=self.portName,
                                          baudrate=self.baudrate,
                                          bytesize=self.bytesize,
                                          stopbits=self.stopbits,
                                          parity=self.parity,
                                          timeout=self.timeout)


    def closePort(self):
        self.serialDevice.close()


    def turnOutput_ON(self):
        self.serialDevice.write(b"OUTPUT ON\n")
        if self.verbose:
            print("The output for the Keithley 2400-LV at " + self.portName + " has been set to ON")


    def turnOutput_OFF(self):
        self.serialDevice.write(b"OUTPUT OFF\n")
        if self.verbose:
            print("The output for the Keithley 2400-LV at " + self.portName + " has been set to OFF")


    def getMeasermentVoltage(self):
        self.serialDevice.write(b'MEAS:VOLT?\n')
        voltageStr = readKeithley(self.serialDevice)
        if self.verbose:
            print(voltageStr, "is the read voltage from the Keithley 2400-LV")
        return voltageStr


    def setKeithley2400LV_voltage(self, setVoltage):
        self.serialDevice.write(b":FUNC VOLT\n")
        writeString = b":SOUR:VOLT " + numberFormat(setVoltage) + b"\n"
        self.serialDevice.write(writeString)
        if self.verbose:
            print("Keithley 2400-LV was set to a voltage of", setVoltage)


    def getSourceCurrent(self):
        self.serialDevice.write(b'SOUR:CURR?\n')
        current = float(readKeithley(self.serialDevice))
        if self.verbose:
            print(current, "is the read current from the Keithley 2400-LV")


    def setSourceCurrent(self, setCurrent):
        self.serialDevice.write(b"SOUR:FUNC CURR\n")
        writeString = b":SOUR:CURR " + numberFormat(setCurrent) + b"\n"
        self.serialDevice.write(writeString)
        if self.verbose:
            print("Keithley 2400-LV was set to a current of", setCurrent, "Amps")


    def initLEDsweep(self):
        self.serialDevice.write(b"SOUR:CURR:RANG MIN\n")
        self.serialDevice.write(b"SOUR:CURR:RANG UP\n")
        self.serialDevice.write(b"SOUR:CURR:RANG UP\n")
        self.serialDevice.write(b"SENS:FUNC \"VOLT\"\n")
        self.serialDevice.write(b"SENS:VOLT:PROT " + numberFormat(2) + b"\n")
        self.serialDevice.write(b"SYST:RSEN ON\n")



    def getRange_Keithley2400LV(self):
        writeString = b":CURR:RANG?\n"
        self.serialDevice.write(writeString)
        theRange = readKeithley(self.serialDevice)
        if self.verbose:
            print(theRange, "is the current RANGE from the Keithley 2400-LV")
        return theRange




def ledSweep():
    verbose = False
    portName = "COM4"

    # this is the folder where you can keep the data
    dataLogFolder = os.path.join("LED_sweep")
    dataFileName = "April_12_2018.csv"

    # This an attempt at writing platform independent code.
    if sys.platform == "win32":
        rootName = "C:\\"
    else:
        rootName = "~/"

    # if the directory does not exist you can make it
    if not os.path.exists(rootName + dataLogFolder):
        os.mkdir(rootName + dataLogFolder)

    # the base file name
    fullDataPath = os.path.join(rootName + dataLogFolder, dataFileName)

    # Here were start send commands to the Keithley 2400 LV
    keithley2400LV = Keithley2400LV(portName=portName, verbose=verbose)
    keithley2400LV.openPort()

    keithley2400LV.turnOutput_ON()
    keithley2400LV.initLEDsweep()

    for microAmps in range(0, 61, 5):
        keithley2400LV.setSourceCurrent(microAmps * 1.0E-6)
        if microAmps == 0:
            f = open(fullDataPath, 'w')
        else:
            f = open(fullDataPath, 'a')
        f.write(str(keithley2400LV.getMeasermentVoltage()))
        f.close()
        time.sleep(5)

    keithley2400LV.turnOutput_OFF()
    keithley2400LV.closePort()
    return

if __name__ == "__main__":
    ledSweep()
    # portName = "COM4"
    # verbose = False
    # mkeithley2400LV = Keithley2400LV(portName=portName, verbose=verbose)
    # keithley2400LV.openPort()

    # keithley2400LV.turnOutput_ON_P2()
    # keithley2400LV.initLEDsweep()
    # time.sleep(10)
    # keithley2400LV.turnOutput_OFF_P2()
    # keithley2400LV.closePort()

