import numpy as np
import time
from datetime import datetime
from threading import Timer
from instcontrol.keithley2230 import Keithley2230

max_current_He4Pump = 0.100 # Amps
max_current_He3InterPump = 0.100 # Amps
max_current_UltraPump = 0.050 # Amps
max_current_switches = 0.003 # Amps
switch_voltage = 5 # Volts

default_voltage_He4Pump = 4.400 # Volts
default_voltage_He3InterPump = 5.100 # Volts
default_voltage_UltraPump = 7.200 # Volts

start_cycle_at_hour = 6 # hours in local 24 hour time
start_cycle_at_minute = 30 # minutes after the hour
step2_to_step3 = 30 * 60 # in seconds
step3_to_step4 = 90 * 60 # in seconds
step4_to_recycle = 12 * 60 *60 # in seconds

class Frig_Keithleys():
    def __init__(self, verbose=False, innerVerbose=False):
        self.verbose = verbose
        self.innerVerbose = innerVerbose
        if self.verbose:
            print(" The Simon-Chase Heluim 3 refrigerator Keithley control class is initializing...\n")
        self.yellowKeithley = Keithley2230(portName="USB0::0x05E6::0x2230::9030255::INSTR", verbose=innerVerbose)
        self.redKeithley = Keithley2230(portName="USB0::0x05E6::0x2230::9030212::INSTR", verbose=innerVerbose)
        self.yellowKeithley.turn_off_all_channels()
        self.redKeithley.turn_off_all_channels()
        if self.innerVerbose:
            print()

        """
        Initialize the states for the output of the Keithley 2230 power supplies.
        """
        # Helium 4 switch - yellow electrical tape - Channel 2, red Keithley
        self.redKeithley.channel_select(channel_number=2)
        self.redKeithley.set_current_limit(max_current_switches)
        self.redKeithley.set_voltage(switch_voltage)
        if self.innerVerbose:
            print()

        # Intermediate Helium 3 switch - green electrical tape - Channel 3, yellow Keithley
        self.yellowKeithley.channel_select(channel_number=3)
        self.yellowKeithley.set_current_limit(max_current_switches)
        self.yellowKeithley.set_voltage(switch_voltage)
        if self.innerVerbose:
            print()

        # Ultra Helium 3 switch - white electrical tape - Channel 3, red Keithley
        self.redKeithley.channel_select(channel_number=3)
        self.redKeithley.set_current_limit(max_current_switches)
        self.redKeithley.set_voltage(switch_voltage)
        if self.innerVerbose:
            print()

        # Helium 4 pump - red electrical tape - Channel 1, yellow Keithly
        self.yellowKeithley.channel_select(channel_number=1)
        self.yellowKeithley.set_current_limit(max_current_He4Pump)
        if self.innerVerbose:
            print()

        # Intermediate Helium 3 pump - purple electrical tape - Channel 2, yellow Keithley
        self.yellowKeithley.channel_select(channel_number=2)
        self.yellowKeithley.set_current_limit(max_current_He3InterPump)
        if self.innerVerbose:
            print()

        # Ultra Helium 3 pump - Orange electrical tape - Channel 1, red Keithley
        self.redKeithley.channel_select(channel_number=1)
        self.redKeithley.set_current_limit(max_current_UltraPump)
        if self.innerVerbose:
            print()

    def He4Switch(self, state):
        # Helium 4 switch - yellow electrical tape - Channel 2, red Keithley
        self.redKeithley.channel_select(2)
        if state:
            self.redKeithley.turnOutput_ON()
            if self.verbose:
                print("Turned On Helium 4 switch - yellow electrical tape - Channel 2, red Keithley\n")
        else:
            self.redKeithley.turnOutput_OFF()
            if self.verbose:
                print("Turned Off Helium 4 switch - yellow electrical tape - Channel 2, red Keithley\n")

    def He3InterSwitch(self, state):
        # Intermediate Helium 3 switch - green electrical tape - Channel 3, yellow Keithley
        self.yellowKeithley.channel_select(3)
        if state:
            self.yellowKeithley.turnOutput_ON()
            if self.verbose:
                print("Turned On Intermediate Helium 3 switch - green electrical tape - Channel 3, yellow Keithley\n")
        else:
            self.yellowKeithley.turnOutput_OFF()
            if self.verbose:
                print("Turned Off Intermediate Helium 3 switch - green electrical tape - Channel 3, yellow Keithley\n")

    def He3UltraSwitch(self, state):
        # Ultra Helium 3 switch - white electrical tape - Channel 3, red Keithley
        self.redKeithley.channel_select(3)
        if state:
            self.redKeithley.turnOutput_ON()
            if self.verbose:
                print("Turned OnUltra Helium 3 switch - white electrical tape - Channel 3, red Keithley\n")
        else:
            self.redKeithley.turnOutput_OFF()
            if self.verbose:
                print("Turned Off Ultra Helium 3 switch - white electrical tape - Channel 3, red Keithley\n")

    def He4Pump(self, state=None, voltage=None):
        # Helium 4 pump - red electrical tape - Channel 1, yellow Keithly
        self.yellowKeithley.channel_select(1)
        if voltage is not None:
            self.yellowKeithley.set_voltage(voltage)
            if self.verbose:
                print("Set the Helium 4 pump voltage to", voltage, "Volts")
        if state is not None:
            if state:
                self.yellowKeithley.turnOutput_ON()
                if self.verbose:
                    print("Turned On the Helium 4 pump - red electrical tape - Channel 1, yellow Keithly\n")
            else:
                self.yellowKeithley.turnOutput_OFF()
                if self.verbose:
                    print("Turned Off the Helium 4 pump - red electrical tape - Channel 1, yellow Keithly\n")

    def He3InterPump(self, state, voltage=None):
        # Intermediate Helium 3 pump - purple electrical tape - Channel 2, yellow Keithley
        self.yellowKeithley.channel_select(2)
        if voltage is not None:
            self.yellowKeithley.set_voltage(voltage)
            if self.verbose:
                print("Set the Helium 3 intermediate pump voltage to", voltage, "Volts")
        if state is not None:
            if state:
                self.yellowKeithley.turnOutput_ON()
                if self.verbose:
                    print("Turned On the Intermediate Helium 3 pump - purple electrical tape - Channel 2, yellow Keithley\n")
            else:
                self.yellowKeithley.turnOutput_OFF()
                if self.verbose:
                    print("Turned Off the Intermediate Helium 3 pump - purple electrical tape - Channel 2, yellow Keithley\n")

    def He3UltraPump(self, state, voltage=None):
        # Ultra Helium 3 pump - Orange electrical tape - Channel 1, red Keithley
        self.redKeithley.channel_select(1)
        if voltage is not None:
            self.redKeithley.set_voltage(voltage)
            if self.verbose:
                print("Set the Helium 3 ultra pump voltage to", voltage, "Volts")
        if state is not None:
            if state:
                self.redKeithley.turnOutput_ON()
                if self.verbose:
                    print("Turned On the Ultra Helium 3 pump - Orange electrical tape - Channel 1, red Keithley\n")
            else:
                self.redKeithley.turnOutput_OFF()
                if self.verbose:
                    print("Turned Off the Ultra Helium 3 pump - Orange electrical tape - Channel 1, red Keithley\n")

    def recycle_equilibrium(self):
        print("   Recycle Equilibrium state for frig keithleys")
        print(datetime.today())
        self.He4Switch(state=False)
        self.He3InterSwitch(state=False)
        self.He3UltraSwitch(state=False)
        self.He4Pump(state=True, voltage=default_voltage_He4Pump)
        self.He3InterPump(state=True, voltage=default_voltage_He3InterPump)
        self.He3UltraPump(True, voltage=default_voltage_UltraPump)

    def step2(self):
        print("   Step 2: Turing Off Helium 4 pump with other pumps still on, all switch not powered")
        print(datetime.today())
        self.He4Switch(state=False)
        self.He3InterSwitch(state=False)
        self.He3UltraSwitch(state=False)
        self.He4Pump(state=False)
        self.He3InterPump(state=True, voltage=default_voltage_He3InterPump)
        self.He3UltraPump(True, voltage=default_voltage_UltraPump)

    def step3(self):
        print("   Step 3: Powering Helium 4 switch, intermediate and ultra pumps still on,")
        print("intermediate and ultra switches not powered")
        print(datetime.today())
        self.He4Switch(state=True)
        self.He3InterSwitch(state=False)
        self.He3UltraSwitch(state=False)
        self.He4Pump(state=False)
        self.He3InterPump(state=True, voltage=default_voltage_He3InterPump)
        self.He3UltraPump(True, voltage=default_voltage_UltraPump)

    def step4(self):
        print("   Step 4: Powering intermediate and ultra switches, turing intermediate and ultra pumps off,")
        print("all pumps are not powered, all switches are powered.")
        print("This is where it gets cold.")
        print(datetime.today())
        self.He4Switch(state=True)
        self.He3InterSwitch(state=True)
        self.He3UltraSwitch(state=True)
        self.He4Pump(state=False)
        self.He3InterPump(state=False)
        self.He3UltraPump(state=False)


    def all_channels_off(self):
        self.yellowKeithley.turn_off_all_channels()
        self.redKeithley.turn_off_all_channels()
        if self.verbose:
            print("All refrigerator channels have been turned OFF\n")

    def close(self):
        self.yellowKeithley.close()
        self.redKeithley.close()
        if self.verbose:
            print("The Connection to the Keiltley has been closed, call __init__ to open them again.")
            print("Have a nice night!")

# """
# Warning definitions
# """
#
# def highTempWarning(highTemp):
#     print("Warning the temperature has exceeded the threshold value.", highTemp)
#     return
#
# def highCurrentWarning(He4PumpMax, IHPumpMax, UHPumpMax):
#     print("Warning the current has exceeded the threshold value.")
#     return
#
# def lowCurrentWarning(lowCurrent):
#     print("Warning the current is too low.", lowCurrent)
#     return
#
# def highVoltageWarning(highVolts):
#     print("Warning the voltage has exceeded the threshold value.", highVolts)
#     return
#
#
# """
# step 0 only monitors the temperature
# know when to turn on pumps
# """
# def step0(goalTemp, sleepTime=5.0, highTemp=305.0, verbose=True):
#     finish = False
#     tempHe4Pump = 80.0
#     tempInterPump = 80.0
#     tempUltraPump = 80.0
#
#     while not finish:
#         if verbose:
#             print("Temperature of He4 pump is, ",tempHe4Pump)
#             print("Temperature of interpump is, ",tempInterPump)
#             print("Temperature of Ultra pump is, ",tempUltraPump,"\n")
#
#         tempHe4Pump -= 1.0
#         tempInterPump -= 1.0
#         tempUltraPump -= 1.0
#         if tempHe4Pump < goalTemp:
#             finish = True
#         if tempInterPump < goalTemp:
#             finish = True
#         if tempUltraPump < goalTemp:
#             finish = True
#         time.sleep(sleepTime)
#
#         if tempHe4Pump > highTemp:
#             highTempWarning(highTemp)
#         if tempInterPump > highTemp:
#             highTempWarning(highTemp)
#         if tempUltraPump > highTemp:
#             highTempWarning(highTemp)
#
#     return
#
# """Step1 turn on pumps when pumps are between 50-55K
# receives current(in mA) and voltage"""
#
# def step1(goalTemp, He4PumpMax=100.0, IHPumpMax=100.0, UHPumpMax=50.0, sleepTime=5.0, verbose=True):
#     finish = False
#     tempHe4Pump = 55.0
#     tempInterPump = 55.0
#     tempUltraPump = 55.0
#
#     tempHe4Switch = 55.0
#     tempInterSwitch = 55.0
#     tempUltraSwitch = 55.0
#
#     He4Switch = 0.0
#     He4Pump = 18.0
#     IHSwitch = 0.0
#     IHPump = 12.0
#     UHSwitch = 0.0
#     UHPump = 20.0
#
#     while not finish:
#         if verbose:
#             print("Temperature of He4-pump is, ",tempHe4Pump)
#             print("Temperature of Inter-pump is, ",tempInterPump)
#             print("Temperature of Ultra-pump is, ",tempUltraPump,"\n")
#             print("Current in He4-pump is, ", He4Pump)
#             print("Current in Inter-pump is, ", IHPump)
#             print("Current in Ultra-pump is, ", UHPump, "\n")
#
#             print("Voltage of He4-switch is, ", He4Switch)
#             print("Voltage of Inter-switch is, ", IHSwitch)
#             print("Voltage of Ultra-switch is, ", UHSwitch, "\n")
#
#         tempHe4Pump -= 1.0
#         tempInterPump -= 1.0
#         tempUltraPump -= 1.0
#
#         tempHe4Switch -= 1.0
#         tempInterSwitch -= 1.0
#         tempUltraSwitch -= 1.0
#
#         if tempHe4Pump < goalTemp:
#             finish = True
#         if tempInterPump < goalTemp:
#             finish = True
#         if tempUltraPump < goalTemp:
#             finish = True
#             time.sleep(sleepTime)
#
#         if He4Pump > He4PumpMax:
#             highCurrentWarning(He4PumpMax)
#         if IHPump > IHPumpMax:
#             highCurrentWarning(IHPumpMax)
#         if UHPump > UHPumpMax:
#             highCurrentWarning(UHPumpMax)
#
#     return
#
# def step2(goalTemp, He4PumpMax=100.0, IHPumpMax=100.0, UHPumpMax=50.0, sleepTime=5.0, verbose=True):
#     return

def time_until_cycle_start(verbose=False):
    # get the current data and time
    x = datetime.today()
    # if it is after 6:00 pm start the cycle the following day
    if 18 <= x.hour:
        extra_day = 1
    else:
        extra_day = 0
    # make the time you want to start something
    y = x.replace(day=x.day + extra_day, hour=start_cycle_at_hour, minute=start_cycle_at_minute, second=0, microsecond=0)
    # get the difference between now and the time you want to start
    delta_t = y - x
    # get that deference time in seconds
    secs = delta_t.seconds + 1
    if verbose:
        print("cycle start:", y)
        print("seconds until then:", secs, "measured from", x)
    return secs


def cycle_frig(verbose=False):
    print("\nsleeping until " + str("%02i" % start_cycle_at_hour) + ":" + str("%02i" %start_cycle_at_minute) + "\n")
    time.sleep(time_until_cycle_start(verbose=verbose))
    frig_keithleys = Frig_Keithleys(verbose=verbose)
    frig_keithleys.step2()
    if verbose:
        print("\nSleeping for " + str("%3.2f" % (step2_to_step3 / 60.0)) +" minutes\n")
    time.sleep(step2_to_step3)
    frig_keithleys.step3()
    if verbose:
        print("\nSleeping for " + str("%3.2f" % (step3_to_step4 / 60.0)) + " minutes\n")
    time.sleep(step3_to_step4)
    frig_keithleys.step4()
    if verbose:
        print("\nSleeping for " + str("%3.2f" % (step4_to_recycle / 60.0)) + " minutes\n")
    time.sleep(step4_to_recycle)
    frig_keithleys.recycle_equilibrium()
    frig_keithleys.close()



if __name__ == "__main__":
    while True:
        cycle_frig(True)

