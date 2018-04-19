"""
Comments - This is a multiline comment
"""

# this is a single line comment

"""
The print state statement
"""

# simple example
print "Here is a simple print example."

# compound example
print "here is number", 99, 'here is another string'

# the \n (newline) character
print '\nThis newline character \n', "here is a 2nd line\n"



"""
Numbers - basic single value numbers Integers and floats.
"""

### integers (no decimal point)
anInt = 9
notherInt = 7

# ** is the power operator
print anInt ** notherInt

# Tricky divstion
print anInt / notherInt

# The modulus operator
counter = 17
loopLen = 6
print "this modulus", counter % 6, "this how many times some is divided", counter / loopLen


### float (floating point number, has a decimal point)
float1 = 55.8
float2 = 63.0
float3 = 1.4563e-122
# intuitive division.
print '\nintuitive division', float1 / float2
print type(float2), type(anInt)

# conversion to an integer
print type(int(float1)), int(float1), int(round(float1))

# conversion from an integer

print type(float(anInt)), float(anInt)

# when used with an integer in math
print float1 ** float2, float3, "\n"



"""
Strings
 Strings can be groups of numbers or letters that are enclosed in quotes.
 Single quotes '' or double "" quotes will both work. However, if you use an apostrophe '
 Then you must enclose the apostrophe in double quotes to be be used in the string.
    For Example:
    stringVar = "This is Caleb's string, ain't it grand?"
"""

# single quotes
stringVar = 'This is Caleb'
print stringVar

# double quotes
stringVar = "This is Caleb 2"
print stringVar
stringVar = "This is Caleb's string, ain't it grand?"
print stringVar

# conversion to a number
aNumberString = '99'
print int(aNumberString), float(aNumberString), type(aNumberString)

# concatenation
print stringVar + ' A number I like -> ',  aNumberString, "\n"
# split method

# replace method

"""
Tuples - pronounced 2-ple
 These are a grouping of data in an immutable structure. Immutable means the length of the tuple
 (I think of it as a container is not allowed to changed)
 Tuples are enclosed in round brackets () and the values are separated by commas, the values in a tuple are
 accessed using integers starting with 0. Access that last value in the tuple starting with -1.
"""

# coordinates example
threeSpace = (99, 55, 8.7)
print threeSpace

# unpacking and packing
x, y, z = threeSpace
print x, y, z

# calling a single value.
print threeSpace[0], 'is the first value'

# tuple of mixed types.
bankInfo = ('Caleb', '0938583892', -88.8)
print bankInfo, 'is my bank info'
name, bankAccountNum, balance = bankInfo
print "$" + str('%2.2f' % balance) + " is my balance"

# tuple of tuples
tupOfTup = (threeSpace, bankInfo)
print tupOfTup, '\n'


"""
Lists
    These a grouping of data in an mutable structure. Use a list when you data is being collected or for any other
    reason that its length might change.
    (I think of lists as a train that can have cars added or subtracted at different stations along it journey)
    Lists are enclosed in square brackets [] and the values are separated by commas, the values in a list are
    accessed using integers starting with 0. Access that last value in the list starting with -1.
"""

# list example
basicList = ['rrrrrr', 5, 'rrrrrr']
print basicList

# the empty list
basicList = []
print basicList

# The append method
basicList = ['rrrrrr', 5, 'rrrrrr']
basicList.append('aString')
print basicList

# the extend method
diffList = [63498, "skejkg", 77777, ('he', 4)]
basicList.extend(diffList)
print basicList, '\n'

# list of tuples

# get the last value

"""
Dictionaries
    A dictionary is a way to store data using key-value pairs. While a list or a tuple use an integer to access
    stored data, a dictionary value is assessed using a key, which can be an integer, string, float, or
    even more complex data types.
    Dictionaries are enclosed in curly brackets {} and have and use a colon : to link
    key:value pairs. The key value pairs are separated by commas. To get a list of all the keys
    in a given dictionary, use the .keys() method.
"""

# dictionary example
aDict = {'apple':'is a piece of red fruit'}
print aDict['apple']

# empty dictionary
aDict = {}

# add a key value pair
aDict['4'] = ' this is a string of stuff'
aDict['puppy'] = ' Here is my pup!'
aDict[7.7] = 'This key is a float'
print aDict
print aDict[7.7]

# get all the keys for a dictionary
print aDict.keys()


"""
The for loop
"""

# using the range function

# using a list

# using enumerate

# with a break

# with an else


"""
the try statement
"""




"""
A definition
"""




