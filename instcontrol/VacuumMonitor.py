"""
This is for the the Bayard-Alpert Pirani Gauge BPG400 family of vacuum gauges from INFICON.
It is anticipated that you you are using a RS232 (9 pin serial cable) to read this gauge.
For more information needed to wire the the RS232 cable, consult the operating manual for this device.
"""

from matplotlib import pyplot as plt
import numpy as np
import os, sys,time, serial

from instcontrol.SerialTests import findSerialPort


"""
This tries to open a serial port where the vacuum gauge is located. 
How serial ports are named is operating system dependent. In windows it is simple, 
on Unix and OSX it is a little more complex.
"""
deviceID = ""
baudrate = 9600
bytesize = 8
stopbits = 1
timeout=2

serialPortName = findSerialPort(deviceID, baudrate, bytesize, stopbits, timeout)

vacGauge = serial.Serial(port=serialPortName, baudrate=baudrate, bytesize=bytesize, stopbits=stopbits, timeout=timeout)

def getPressure():
    RxD = vacGauge.read()

    pressureTorr =  10.0**(((highByte * 256.0 + lowByte) / 4000.0) - 12.625)
    return


def makeTestPlot():
    return


if __name__ == "__main__":
    pass