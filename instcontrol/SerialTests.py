import os, sys, serial


def testSerialPortHasDeviceWindows(serialPortName, deviceID, baudrate, bytesize, stopbits, timeout=2):
    st = serial.Serial(port=serialPortName, baudrate=baudrate, bytesize=bytesize, stopbits=stopbits, timeout=timeout)

    return True


# This is no yet working
def testSerialPortHasDeviceOSX(serialPortName, deviceID):
    if os.path.lexists(serialPortName):
        return True
    else:
        return False



def findSerialPort(deviceID, baudrate, bytesize, stopbits, timeout=2):
    serialPort = ""
    nMax = 40

    # Windows Case (The case that this code is used from a Windows computer)
    if sys.platform == 'win32':
        n = 1
        while serialPort == "":
            testSerialPort = "COM" + str(n)
            if testSerialPortHasDeviceWindows(testSerialPort, deviceID, baudrate, bytesize, stopbits, timeout=timeout):
                serialPort = testSerialPort
            elif nMax < n:
                print("COM1 through COM" + str(n) + " is not open for a device with the ID:")
                print(deviceID)
                print("Exiting the code from the 'Windows Case' in the 'findSerialPort' definition in 'SerialTest.py'")
                sys.exit()

    # # For the Macintosh Operating System (OSX) use shell$ ls /dev/cu* to display the device name after you plug it in.
    # elif platform == 'darwin':
    #     test_serial_port = '/dev/' # this has not been updated

    # Unknown OS case
    else:
        print("The platform that this code is running on:", sys.platform)
        print("has not been made to work with this code yet. Looks like you will need to do some programming :/")
        print("Exiting the code from the 'Unknown OS case' in the 'findSerialPort' definition in 'SerialTest.py'")
        sys.exit()


    return serialPort