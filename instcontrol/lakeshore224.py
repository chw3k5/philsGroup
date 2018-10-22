import serial
"""
On a new computer you may need to install: 
The "Lakeshore Temperature monitor" device drivers for USB: http://sp.lakeshore.com/software/Pages/default.aspx
    -> direct download (if this link still works): http://sp.lakeshore.com/Documents/LakeShoreUSBDriverv6.7.zip

Once at the software is installed:
You can look up the port name using Windows device manager. Type 'device manager' into the window search bar to launch 
the application. The Lake Shore 336 temperature controller will be listed under 'Ports (COM & LPT)' then 
'Lake Shore Model 224 Temperature Controller Port (COM?)
"""
portName = "COM17"
baudrate = 57600
bytesize = 7
startbits = 1
stopbits = 1
parity = "O"
timeout = 2

channelToName = {"A" :"UltraHead",
                 "B" :"InterHead",
                 "C1":"He4Buffer",
                 "C4":"He4Switch",
                 "C3":"He3InterSwitch",
                 "C2":"He3UltraSwitch",
                 "D2":"He3InterPump",
                 "D3":"He4Pump",
                 "C5":"UltraPump"}

def readLS224(verbose=False):
    lakeShore224 = serial.Serial(port=portName, baudrate=baudrate, bytesize=bytesize,
                                 stopbits=stopbits, parity=parity, timeout=timeout)
    temperatureDict = {}
    for key in channelToName.keys():
        writeString = b"KRDG? " + bytes(key, encoding='UTF-8') + b"\n"
        # print(writeString)
        lakeShore224.write(writeString)
        temperatureDict[channelToName[key]] = float(lakeShore224.read(10))
        if verbose:
            print(temperatureDict[channelToName[key]], "K, at", key, "(" + channelToName[key] + ")")
    lakeShore224.close()
    return temperatureDict


if __name__ == "__main__":
    tempDict = readLS224(verbose=True)