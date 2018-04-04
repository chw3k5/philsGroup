import numpy as np
import time

def highTempWarning(highTemp):
    print("Warning the temperature has exceeded the threshold value.", highTemp)
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

"""Step1"""










if __name__ == "__main__":
    step0(goalTemp=60.0, sleepTime=0.5, highTemp=305.0, verbose=True)

