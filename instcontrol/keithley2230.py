"""
This is for the Keithley 2230-30-1 triple channel power supply. It uses National instruments Visa.
This was tested to work on Windows 10
with the Visa backend of NI-Visa 17.5
with pyVisa 1.9.0
in python 3.6
on May 10, 2018
"""
import time, visa, sys
"""
This is the class to control the Keithley 2230-30-1 triple channel power supply.
"""
class Keithley2230():
    def __init__(self, portName, verbose=False):
        self.serialDevice = None
        self.portName = portName
        self.verbose = verbose
        self.current_channel = None
        self.rm = visa.ResourceManager()
        self.device = self.rm.open_resource(portName)
        self.device.write("*RST")
        self.device.write("SYSTEM:REMOTE")

    def channel_select(self, channel_number):
        if channel_number in [1, 2, 3]:
            self.device.write("instrument:nselect " + str(channel_number))
            self.current_channel = channel_number
            if self.verbose:
                print("Switched to channel number", channel_number)
        else:
            raise ValueError(channel_number, "is the channel, but the channel number must be 1, 2, or 3")


    def turnOutput_ON(self):
        self.device.write("CHANNEL:OUTPUT ON")
        if self.verbose:
            print("Turned channel " + str(self.current_channel) + "'s output to ON")

    def turnOutput_OFF(self):
        self.device.write("CHANNEL:OUTPUT OFF")
        if self.verbose:
            print("Turned channel " + str(self.current_channel) + "'s output to OFF")

    def turn_off_all_channels(self):
        for channel_number in [1, 2, 3]:
            self.channel_select(channel_number=channel_number)
            self.turnOutput_OFF()

    def set_voltage(self, voltage):
        self.device.write("Voltage " + str(voltage))
        if self.verbose:
            print("Turned channel " + str(self.current_channel) + "'s voltage to "
                  + str("%1.3e" % voltage) + "Volts")

    def set_current_limit(self, current_limit):
        self.device.write("Current " + str(current_limit))
        if self.verbose:
            print("Turned channel " + str(self.current_channel) + "'s current limit to "
                  + str("%1.3e" % current_limit) + " Amps")

    def close(self):
        self.device.close()



if __name__ == "__main__":

    yellowKeithley = Keithley2230(portName='USB0::0x05E6::0x2230::9030255::INSTR', verbose=True)
    yellowKeithley.channel_select(channel_number=1)
    yellowKeithley.turnOutput_OFF()
    yellowKeithley.set_voltage(voltage=1.1)
    yellowKeithley.set_current_limit(current_limit=0.010)
    yellowKeithley.turnOutput_ON()
    time.sleep(10)
    yellowKeithley.turnOutput_OFF()
    yellowKeithley.close()




