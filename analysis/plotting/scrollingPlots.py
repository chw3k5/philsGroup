"""
File that makes scrolling plots
"""
import getpass, os, sys
from matplotlib import pyplot as plt

from analysis.dataGetter import read_csv_file

# get the current users username
username = getpass.getuser()
# prints the current user's user name
print("Your username is", username)

# determine the current operating system
if sys.platform == "win32":
    # root folder in windows
    rootfolder = "C:\\"
else:
    # root folder in mac and unix
    rootfolder = "/Users/" + username + "/"
# looking for file on my own computer
if username == "meganmoore":
    filename = os.path.join(rootfolder, "Downloads", "April_12_2018.csv")
elif username == "Rebop":
    filename = os.path.join(rootfolder, "Users", "Rebop", "Documents", "CryoStuff", "April_12_2018.csv")
    # platform independent way of joining folders together with the filename
else:
    filename = os.path.join(rootfolder, "cryolog", "April_12_2018.csv")
# read the file using the definition in this file
dataDictonary = read_csv_file(filename=filename)
# make a simple test plot
plt.plot(dataDictonary["ctime_s"], dataDictonary["UltraHead_K"])
#
plt.xlabel("Computer time (s)")
# show the plot
plt.show()