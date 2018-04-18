import numpy as np
import time

def highTempWarning(highTemp):
    print("Warning the temperature has exceeded the threshold value.", highTemp)
    return

def highCurrentWarning(He4PumpMax, IHPumpMax, UHPumpMax):
    print("Warning the current has exceeded the threshold value.")
    return

def lowCurrentWarning(lowCurrent):
    print("Warning the current is too low.", lowCurrent)
    return

def highVoltageWarning(highVolts):
    print("Warning the voltage has exceeded the threshold value.", highVolts)
    return


"""step 0 only monitors the temoerature
know when to turn on pumps"""
def step0(goalTemp, sleepTime=5.0, highTemp=305.0, verbose=True):
    finish = False
    tempHe4Pump = 80.0
    tempInterPump = 80.0
    tempUltraPump = 80.0

    while not finish:
        if verbose:
            print("Temperature of He4 pump is, ",tempHe4Pump)
            print("Temperature of interpump is, ",tempInterPump)
            print("Temperature of Ultra pump is, ",tempUltraPump,"\n")

        tempHe4Pump -= 1.0
        tempInterPump -= 1.0
        tempUltraPump -= 1.0
        if tempHe4Pump < goalTemp:
            finish = True
        if tempInterPump < goalTemp:
            finish = True
        if tempUltraPump < goalTemp:
            finish = True
        time.sleep(sleepTime)

        if tempHe4Pump > highTemp:
            highTempWarning(highTemp)
        if tempInterPump > highTemp:
            highTempWarning(highTemp)
        if tempUltraPump > highTemp:
            highTempWarning(highTemp)

    return

"""Step1 turn on pumps when pumps are between 50-55K 
receives current(in mA) and voltage"""

def step1(goalTemp, He4PumpMax=100.0, IHPumpMax=100.0, UHPumpMax=50.0, sleepTime=5.0, verbose=True):
    finish = False
    tempHe4Pump = 55.0
    tempInterPump = 55.0
    tempUltraPump = 55.0

    tempHe4Switch = 55.0
    tempInterSwitch = 55.0
    tempUltraSwitch = 55.0

    He4Switch = 0.0
    He4Pump = 18.0
    IHSwitch = 0.0
    IHPump = 12.0
    UHSwitch = 0.0
    UHPump = 20.0

    while not finish:
        if verbose:
            print("Temperature of He4-pump is, ",tempHe4Pump)
            print("Temperature of Inter-pump is, ",tempInterPump)
            print("Temperature of Ultra-pump is, ",tempUltraPump,"\n")
            print("Current in He4-pump is, ", He4Pump)
            print("Current in Inter-pump is, ", IHPump)
            print("Current in Ultra-pump is, ", UHPump, "\n")

            print("Voltage of He4-switch is, ", He4Switch)
            print("Voltage of Inter-switch is, ", IHSwitch)
            print("Voltage of Ultra-switch is, ", UHSwitch, "\n")

        tempHe4Pump -= 1.0
        tempInterPump -= 1.0
        tempUltraPump -= 1.0

        tempHe4Switch -= 1.0
        tempInterSwitch -= 1.0
        tempUltraSwitch -= 1.0

        if tempHe4Pump < goalTemp:
            finish = True
        if tempInterPump < goalTemp:
            finish = True
        if tempUltraPump < goalTemp:
            finish = True
            time.sleep(sleepTime)

        if He4Pump > He4PumpMax:
            highCurrentWarning(He4PumpMax)
        if IHPump > IHPumpMax:
            highCurrentWarning(IHPumpMax)
        if UHPump > UHPumpMax:
            highCurrentWarning(UHPumpMax)

    return

def step2(goalTemp, He4PumpMax=100.0, IHPumpMax=100.0, UHPumpMax=50.0, sleepTime=5.0, verbose=True)








if __name__ == "__main__":
    step0(goalTemp=55.0, sleepTime=0.5, highTemp=305.0, verbose=True)
    step1(goalTemp=4.0, sleepTime=0.5, verbose=True)
