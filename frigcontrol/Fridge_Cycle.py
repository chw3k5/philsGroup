import visa, time
#import numpy as np
#import matplotlib.pyplot as plt
###############################################################################
# User  settings
###############################################################################

start_with_heating_switches = True

print('Connecting to Instruments ...')

rm = visa.ResourceManager()
ps1= rm.open_resource('USB0::0x05E6::0x2230::9030255::INSTR')
ps2= rm.open_resource('USB0::0x05E6::0x2230::9030212::INSTR')

ps1.write('*RST')
ps2.write('*RST')

ps1.write('SYSTEM:REMOTE')
ps2.write('SYSTEM:REMOTE')
time.sleep(1)

###############################################################################
#He4 Switch:  PS2, CH2 --> 10V 
#He3 IC:      PS1, CH3 --> 6 V
#He3 UC:      PS2, CH3 --> 6V
#
#He4 Pump:    PS1, CH1 -->21V @ mA
#He3 IC Pump: PS1, CH2 -->14V @ mA
#He3 UC Pump: PS2, CH1 -->10V @ mA

# He4 Switch 
ps2.write('instrument:nselect 2')
ps2.write('Voltage 10')
ps2.write('Current 0.1')
ps2.write('CHANNEL:OUTPUT off')
time.sleep(2)
# He3 IC Switch 
ps1.write('instrument:nselect 3')
ps1.write('Voltage 6')
ps1.write('Current 0.1')
ps1.write('CHANNEL:OUTPUT off')
time.sleep(2)

# He3 UC Switch 
ps2.write('instrument:nselect 3')
ps2.write('Voltage 6')
ps2.write('Current 0.1')
ps2.write('CHANNEL:OUTPUT off')

if start_with_heating_switches:
	###########################  Turn ON Switches #################################
	print(' Turning ON ALL Switches ...')
	# He4 Switch 
	ps2.write('instrument:nselect 2')
	ps2.write('Voltage 10')
	ps2.write('Current 0.1')
	ps2.write('CHANNEL:OUTPUT on')
	time.sleep(2)

	# He3 IC Switch 
	ps1.write('instrument:nselect 3')
	ps1.write('Voltage 6')
	ps1.write('Current 0.1')
	ps1.write('CHANNEL:OUTPUT on')
	time.sleep(2)

	# He3 UC Switch 
	ps2.write('instrument:nselect 3')
	ps2.write('Voltage 6')
	ps2.write('Current 0.1')
	ps2.write('CHANNEL:OUTPUT on')
	time.sleep(2)

	print( 'All Switches are turned ON ...')
	time.sleep(15*60) 

	###########################  Turn OFF Switches#################################
	# He4 Switch 
	ps2.write('instrument:nselect 2')
	ps2.write('CHANNEL:OUTPUT off')
	time.sleep(2)

	# He3 IC Switch 
	ps1.write('instrument:nselect 3')
	ps1.write('CHANNEL:OUTPUT off')
	time.sleep(2)

	# He3 UC Switch 
	ps2.write('instrument:nselect 3')
	ps2.write('CHANNEL:OUTPUT off')
	time.sleep(2)

	print('Waiting 20 Minutes')
	time.sleep(20*60) 

###########################  Turn ON ALL PUMPS   ##############################
print('Turning ON all 3 pumps ...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
# He4 Pump 
ps1.write('instrument:nselect 1')
ps1.write('Voltage 21')
ps1.write('Current 1')
ps1.write('CHANNEL:OUTPUT on')
time.sleep(2)

# He3 IC Pump
ps1.write('instrument:nselect 2')
ps1.write('Voltage 14')
ps1.write('Current 1')
ps1.write('CHANNEL:OUTPUT on')
time.sleep(2)

# He3 UC Pump 
ps2.write('instrument:nselect 1')
ps2.write('Voltage 10')
ps2.write('Current 1')
ps2.write('CHANNEL:OUTPUT on')
time.sleep(2)

print('All pumps are ON ...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
print('Waiting 36 minmutes ...Starting @ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
time.sleep(36*60) 

###########################  Turn OFF He4 Pump   ##############################
print('Turning OFF He4 Pump ...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
# He4 Pump 
ps1.write('instrument:nselect 1')
ps1.write('CHANNEL:OUTPUT off')
print('Waiting 8 minutes ...Starting @ ' + str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
time.sleep(8*60)

###########################  Turn ON He4  Switch   ############################
print('Turning ON He4 Switch ...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
# He4 Switch 
ps2.write('instrument:nselect 2')
ps2.write('CHANNEL:OUTPUT on')
print('Waiting 9 minutes ...Starting @ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
time.sleep(9*60)

###########################  Turn ON He3 IC Pump High #########################
print('Turning ON He3 IC Pump HIGH...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
# He3 IC Pump
ps1.write('instrument:nselect 2')
ps1.write('Voltage 15') # was 18
ps1.write('Current 1')
ps1.write('CHANNEL:OUTPUT on')
print('Waiting 12 minutes ...Starting @ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
time.sleep(12*60.0)

###########################  Turn ON He3 IC Pump Low #########################
print('Turning ON He3 IC Pump LOW...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
# He3 IC Pump
ps1.write('instrument:nselect 2')
ps1.write('Voltage 7') # was 10
ps1.write('Current 1')
ps1.write('CHANNEL:OUTPUT on')
print('Waiting 8 minutes ...Starting @ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
time.sleep(8*60)

###########################  Turn OFF He3 Pumps IC and UC  #####################
print('Turning OFF He3 IC and UC Pumps ...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
# He3 IC Pump
ps1.write('instrument:nselect 2')
ps1.write('CHANNEL:OUTPUT off')


# He3 UC Pump 
ps2.write('instrument:nselect 1')
ps2.write('CHANNEL:OUTPUT off')

time.sleep(2 * 60)
print('Waiting 2 minutes ...Starting @ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))

###########################  Turn ON UC and IC Switches #####################
print ('Turning ON IC and UC switches ...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))
# He3 IC Switch 
ps1.write('instrument:nselect 3')
ps1.write('CHANNEL:OUTPUT on')
time.sleep(2)

# He3 UC Switch 
ps2.write('instrument:nselect 3')
ps2.write('CHANNEL:OUTPUT on')
time.sleep(2)

print('All switches are ON, All pumps are OFF')
print('End of cycle ...@ '+ str(time.strftime("%a, %d %b %Y %H:%M:%S ")))