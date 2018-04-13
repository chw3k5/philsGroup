"""
This is for the Keithley 2230-30-1 triple channel power supply.

This is designed to be platform independent and work for python 2 and 3
"""
import time, serial, os, sys, usb.core, usb.util

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
This is the class to control the Keithley 2230-30-1 triple channel power supply.
"""
class Keithley2230():
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
        pass

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

# def get_backend_libusb10():
#     libusb01_location = os.getcwd()
#
#     # load-library (ctypes.util.find_library) workaround: also search the current folder
#     is_current_folder_in_search_path = True
#     if None == usb.backend.libusb10.get_backend():
#         is_current_folder_in_search_path = libusb01_location in os.environ['PATH']
#         if not is_current_folder_in_search_path:
#             os.environ['PATH'] += os.pathsep + libusb01_location
#
#     backend = usb.backend.libusb10.get_backend()
#
#     if not is_current_folder_in_search_path:
#         os.environ['PATH'] = os.environ['PATH'].replace(os.pathsep + libusb01_location, "")
#
#     return backend


if __name__ == "__main__":
    # get_backend_libusb10()
    dev = usb.core.find(idVendor=0xfffe, idProduct=0x0001)



