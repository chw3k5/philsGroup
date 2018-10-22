import serial
"""
On a new computer you may need to install: 
The "Lakeshore Temperature monitor" device drivers for USB: http://sp.lakeshore.com/software/Pages/default.aspx
    -> direct download (if this link still works): http://sp.lakeshore.com/Documents/LakeShoreUSBDriverv6.7.zip

Once at the software is installed:
You can look up the port name using Windows device manager. Type 'device manager' into the window search bar to launch 
the application. The Lake Shore 336 temperature controller will be listed under 'Ports (COM & LPT)' then 
'Lake Shore Model 336 Temperature Controller Port (COM?)
"""
portName = "COM18"
baudrate = 57600
bytesize = 7
startbits = 1
stopbits = 1
parity = "O"
timeout = 2

# channelToName = {"C" :"40Kplate"}
channelToName = {"A": "4Knanowire", "B": "mKplate", "C": "40Kplate"}

def readLS336(verbose=False):
    lakeShore336 = serial.Serial(port=portName, baudrate=baudrate, bytesize=bytesize,
                                 stopbits=stopbits, parity=parity, timeout=timeout)
    temperatureDict = {}
    for key in channelToName.keys():
        writeString = b"KRDG? " + bytes(key, encoding='UTF-8') + b"\n"
        # print(writeString)
        lakeShore336.write(writeString)
        temperatureDict[channelToName[key]] = float(lakeShore336.read(10))
        if verbose:
            print(temperatureDict[channelToName[key]], "K, at", key, "(" + channelToName[key] + ")")
    lakeShore336.close()
    return temperatureDict


if __name__ == "__main__":
    temperatureDict = readLS336(verbose=True)