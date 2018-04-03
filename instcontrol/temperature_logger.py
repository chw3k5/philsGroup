import serial
import time
import os
import subprocess
import re
import platform
if platform.system()=='Linux':
    from blessings import Terminal
    term = Terminal()

# set the serial number of the lakeshore device
LakeshoreSerialNumber='336AAJ5'

# look for the port corresponding to this serial number
def search_dmesg_for_serial_number(serialnumber_string):
    # call the dmesg command in linux and look through the output to find the tty number of the specified device
    # or alternately, in Windows admit defeat and interactively prompt the user to manually type in the COM port
    if platform.system()=='Windows':
        # prompt to manually enter the com port
        port_string = raw_input('Manually enter the COM port for S/N ' + serialnumber_string + '\n(Example, type COM3 if that is the port) : ')
        # return this
        return port_string
    elif platform.system()=='Linux':
        # call dmesg
        out = subprocess.check_output('dmesg')

        # search through it with oddly-specific regular expression
        m = list(re.finditer(serialnumber_string+\
                             '(.+?now attached to ttyUSB)(?P<tty>.)',out,flags=re.DOTALL))
        
        # if we found anything
        if m:
            # go to the last element in that list
            # i.e. the most recent time this devices was plugged in
            # note that this does not necessarily mean the device is plugged in right now
            port_string = '/dev/ttyUSB' + str(m[-1].group('tty'))
        else:
            # otherwise return dev null
            # note that this does mean the device isn't plugged in right now!
            port_string = '/dev/null'
            print 'Device ' + serialnumber_string + ' has never been plugged in, returning /dev/null'

        return port_string
    else:
        # if the platform somehow can't be detected
        print 'Platform detected as \'' + platform.system() + '\'\nCannot parse that, returning \\dev\\null'
        # return \dev\null and don't throw an error
        return '\\dev\\null'
port = search_dmesg_for_serial_number(LakeshoreSerialNumber)

# choose which directory to log data into
log_dir = 'thermometer_runs'

# set permissions on the port
os.system('sudo chmod o+rw ' + port)
# you will probably be prompted to enter a sudoer password

# send a command down the line and listen
# just to clean out the buffer
def dry_run():
    # create the pyserial object for the lakeshore
    ser = serial.Serial(port=port,\
                        baudrate=57600,\
                        bytesize=serial.SEVENBITS,\
                        stopbits=serial.STOPBITS_ONE,\
                        parity=serial.PARITY_ODD)
    # send a command down the line to ask for the A tepmerature
    ser.write(str('KRDG?A\n')) # used to be ser.write(unicode('KRDG?A\n'))
    # set the timeout
    ser.timeout = 1;
    # read back the string
    returned_string = ser.read(10)

    return 0
dry_run()


def get_temps(port):
    # create the pyserial object for the lakeshore 336
    ser = serial.Serial(port=port,\
                        baudrate=57600,\
                        bytesize=serial.SEVENBITS,\
                        stopbits=serial.STOPBITS_ONE,\
                        parity=serial.PARITY_ODD)

    # send a command down the line to ask for the A tepmerature
    ser.write(str('KRDG?A\n')) # used to be ser.write(unicode('KRDG?A\n'))

    # set the timeout
    ser.timeout = 1;

    # read back the string
    returned_string_A = ser.read(10)

    # send a command down the line to ask for the B tepmerature
    ser.write(str('KRDG?B\n')) # used to be ser.write(unicode('KRDG?B\n'))

    # set the timeout
    ser.timeout = 1;

    # read back the string
    returned_string_B = ser.read(10)

    return time.time(),float(returned_string_A),float(returned_string_B)

# make the filename
filename = log_dir + '/' + \
           str(int(time.time())) + '-' + time.strftime('%b-%d-%Y-%H-%M-%S') + '.dat'

# print info
print 'serial port = ' + port
print 'logging to ' + filename
print ' '
print '(Ctrl-c to stop)'
print ' '
print ' '

while 1:
    # get a sample
    now,tempA,tempB = get_temps(port)

    # only do the realtime text printing if we're in linux
    if platform.system()=='Linux':
        # print the results to the screen
        print '    ctime: ' + '%10.2f' % now + \
              '    Temp. A: ' + '%3.4f' % tempA + \
              '    Temp. B: ' + '%3.4f' % tempB

        # move back up a line to overwrite the last line next time
        print term.move_up() + term.move_up() + term.move_x(1)

    # write the data to the file
    with open(filename, 'a') as myfile:
        myfile.write('%10.2f' % now + ' ' + '%3.4f' % tempA + ' ' + '%3.4f' % tempB + '\n')

    # wait 5 seconds before taking another data point
    time.sleep(5)