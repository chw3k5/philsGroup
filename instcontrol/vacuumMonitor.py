"""
This is for the the Bayard-Alpert Pirani Gauge BPG400 family of vacuum gauges from INFICON.
It is anticipated that you you are using a RS232 (9 pin serial cable) to read this gauge.
For more information needed to wire the the RS232 cable, consult the operating manual for this device.
"""
import time, serial

"""
This tries to open a serial port where the vacuum gauge is located. 
How serial ports are named is operating system dependent. In windows it is simple, 
on Unix and OSX it is a little more complex.
"""
portName = "COM5"
baudrate = 9600
bytesize = 8
stopbits = 1
timeout = 2

def getPressure(verbose=False):
    vacGauge = serial.Serial(port=portName, baudrate=baudrate, bytesize=bytesize, stopbits=stopbits, timeout=timeout)
    for sleepTime in [0.0, 0.1, 0.2, 1.0]:
        byteOrder = "little"
        lenOfDataString = -1
        start_time = time.time()
        while lenOfDataString != 7:
            lenOfDataString = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
            if timeout < (time.time() - start_time):
                break
        time.sleep(sleepTime)
        pageNumber = -1
        while pageNumber != 5:
            pageNumber = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
        time.sleep(sleepTime)
        status = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
        time.sleep(sleepTime)
        error = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
        time.sleep(sleepTime)
        highByte = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
        time.sleep(sleepTime)
        lowByte = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
        time.sleep(sleepTime)
        solfwareVersion = -1
        while solfwareVersion != 44:
            solfwareVersion = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
        time.sleep(sleepTime)
        sensorType = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
        time.sleep(sleepTime)
        checkSum = int.from_bytes(vacGauge.read(), byteorder=byteOrder)
        measSum = (pageNumber + status + error + highByte + lowByte + solfwareVersion + sensorType) % 256

        if verbose:
            print(lenOfDataString, "is the length of data string byte, should be 7")
            print(pageNumber, "is the page number byte, should be 5")
            print(status, "is the status byte")
            print(error, "is the error byte")
            print(highByte, "is the high measurement byte need to calculate the pressure")
            print(lowByte, "is the low measurement byte need to calculate the pressure")
            print(solfwareVersion, "is the software version byte,", float(solfwareVersion) / 20.0,
                  "is the software version")
            print(sensorType, "is the sensor type byte, should be 10 for BPG400 vacuum gauge")
            print(checkSum, "is the check sum byte, used for synchronization ")
            print(measSum, "is the measured sum and should be equal to the check sum")

            print()
        if measSum == checkSum:
            break
    vacGauge.close()
    if measSum == checkSum:
        pressureTorr = 10.0 ** (((float(highByte) * 256.0 + float(lowByte)) / 4000.0) - 12.625)
    else:
        print("Something is wrong with the vacuum gauge measSum is not equal to checkSum")
        print(lenOfDataString, "is the length of data string byte, should be 7")
        print(pageNumber, "is the page number byte, should be 5")
        print(status, "is the status byte")
        print(error, "is the error byte")
        print(highByte, "is the high measurement byte need to calculate the pressure")
        print(lowByte, "is the low measurement byte need to calculate the pressure")
        print(solfwareVersion, "is the software version byte,", float(solfwareVersion) / 20.0,
              "is the software version")
        print(sensorType, "is the sensor type byte, should be 10 for BPG400 vacuum gauge")
        print(checkSum, "is the check sum byte, used for synchronization ")
        print(measSum, "is the measured sum and should be equal to the check sum")
        print("Setting pressure to -1.0 to flag as an error for later!\n")
        pressureTorr = -1.0
    print(str("%2.2e" % pressureTorr), " Torr\n")
    return pressureTorr

def getFormattedPressure(verbose=False):
    return str('%1.3e' % getPressure(verbose=verbose))

if __name__ == "__main__":
    print(getFormattedPressure(True), "torr")