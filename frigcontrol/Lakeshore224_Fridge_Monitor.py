###############################################################################
# Monitor Temperatures
#Clear All variables
def clearall():
    all = [var for var in globals() if var[0] != "_"]
    for var in all:
        del globals()[var]
clearall()
###############################################################################
import serial, signal, time
#import numpy as np
#import matplotlib.pyplot as plt
###############################################################################
# User  settings
###############################################################################

serial_port = 'COM3'

# Data Folder
#folder ='C:\\Users\\cryo\\Desktop\\'
#Date File Name
filename = 'Temp_He3_Fridge_Temp_Tantalum.txt'

Delay = 1
###############################################################################
# Connect and Configure the Instrument
###############################################################################
# configure the serial connections
lakeshore = serial.Serial(port=serial_port,
                          baudrate='57600',
                          bytesize =7 ,
                          stopbits =1,
                          parity = 'O',
                          timeout= 5) # use null modem cable
lakeshore.isOpen()
###############################################################################
# Interrupt handler
###############################################################################
class GracefulInterruptHandler(object):

    def __init__(self, sig=signal.SIGINT):
        self.sig = sig

    def __enter__(self):

        self.interrupted = False
        self.released = False

        self.original_handler = signal.getsignal(self.sig)

        def handler(signum, frame):
            self.release()
            self.interrupted = True

        signal.signal(self.sig, handler)

        return self

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):

        if self.released:
            return False

        signal.signal(self.sig, self.original_handler)

        self.released = True
def terminate():
    print "Closing Instrument ..."
    lakeshore.close()
###############################################################################
# Acquire Data function
###############################################################################
def get_temp(ch):
     lakeshore.write('KRDG? ' +  ch + ' \r\n')
     #wait some time before reading output.
     time.sleep(0.2)
     #pdata = ''
     data  = ''
     while (lakeshore.inWaiting() > 0) :
         data   +=  lakeshore.read(1)
         #leybold.write('COM,1\r\n')
     time.sleep(.2)
     if ( len(data)  > 2) or (data != '') :
         data  = data.rsplit(',')
         temp = float(data[0])
     else:
         temp = 0
     return temp
###############################################################################
# Initialize Data Plotting and saving
###############################################################################

#plt.close('all')
#figure1 = plt.figure(num= None, figsize=(8,8), dpi=80, facecolor='w', edgecolor='w')
#plt.figure()
#figure.patch.set_facecolor('white') # White background instead of the boring grey
#plt.suptitle("Temperature", fontsize=10)

#start new file
datafile=open(filename ,'w')

###############################################################################
# Measurement Loop
###############################################################################
with GracefulInterruptHandler() as h:
    while True :
        tempA = get_temp('A')
        tempB = get_temp('B')
        tempC1 = get_temp('C1')
        tempC2 = get_temp('C2')
        tempC3 = get_temp('C3')
        tempC4 = get_temp('C4')
        tempC5 = get_temp('C5')
        tempD2 = get_temp('D2')
        tempD3 = get_temp('D3')
        tempD4 = get_temp('D4')
        time.sleep(Delay)
        print " %s   %f %f  %f %f  %f %f  %f %f  %f %f  "%(time.strftime("%a, %d %b %Y %H:%M:%S "),tempA, tempB, tempC1,tempC2,tempC3,tempC4,tempC5,tempD2,tempD3,tempD4) #,pressure)
        datafile.write(" %s  %f %f  %f %f  %f %f  %f %f  %f %f  \n"%(time.strftime("%a, %d %b %Y %H:%M:%S "),tempA, tempB, tempC1,tempC2,tempC3,tempC4,tempC5,tempD2,tempD3,tempD4)) #,pressure))
        if h.interrupted:
            print " Interrupted ... Exiting gracefully"
            terminate()
            break # Break the loop
if h.interrupted == False:
    terminate()
# #\r\n is for device terminators set to CR LF
# lakeshore.write('KRDG? ' + str(n)+ ' \r\n')
# #wait some time before reading output.
# time.sleep(1)
# #pdata = ''
# data  = ''
# while (lakeshore.inWaiting() > 0) :
#  data   +=  lakeshore.read(1)
# #leybold.write('COM,1\r\n')
# time.sleep(1)
# #while (leybold.inWaiting() > 0):
#   #pdata = leybold.readline()
# if ( len(data)  > 2) or (data != '') :
#  data  = data.rsplit(',')
#  temp = np.float(data[0])
# else:
#  temp = 0
# #if ( len(pdata)  >  2 ) or ( pdata != '') :
# # pdata = pdata.rsplit(',')
# # pressure = np.float(pdata[1])
# #else:
#  #pressure = 0
