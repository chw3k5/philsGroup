"""
Comments - This is a multi-line comment
This is a brief introduction to python, written in Python 3
"""

# this is a single line comment

"""
The print state statement
"""

# simple example
print("Here is a simple print example.")

# compound example, the elements in the print statement are separated by commas ,
print("number ninety-nine:", 99, 'here is another string')

# the \n (newline) character. This charater is used print statements or other text is on multiple lines
print('\nThis newline character \n', "here is a 2nd line\n")



"""
Numbers - basic single value numbers Integers and floats.
"""

### integers (no decimal point)
anInt = 9
notherInt = 7

# ** is the power operator
print(anInt ** notherInt, ":: An example of the power operator")

# Tricky division
print(anInt / notherInt, " for new coders Interger division is a little tricky")
print("the result division with two integers is always an integer")

# The modulus operator
counter = 17
loopLen = 6
print("This modulus operation:", counter % 6, "it give the remainder.")
print("This how many times something can be divided", counter / loopLen, "it is another example of integer division.")


### float (floating point number, has a decimal point)
float1 = 55.8
float2 = 63.0
float3 = 1.4563e-122
# intuitive division.
print('\nintuitive division', float1 / float2, "Floats lead to the expected division.")

# is you do not know if a variable is a float or an int, or even something else you can use the type() function
print(type(float2), type(anInt))

# conversion to an integer
print(type(int(float1)), int(float1), int(round(float1)))

# conversion from an integer
print(type(float(anInt)), float(anInt))

# when used with an integer in math
print(float1 ** float2, float3, "\n")



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
print(stringVar)

# double quotes
stringVar = "This is Caleb 2"
print(stringVar)
stringVar = "This is Caleb's string, ain't it grand?"
print(stringVar)

# conversion to a number
aNumberString = '99'
print(int(aNumberString), float(aNumberString), type(aNumberString))

# concatenation of stings, use the + operator
print(stringVar + ' A number I like -> ',  aNumberString, "\n")
# split method
dataExample = "Sometimes*data*is*delimited*with*strange*characters"
splitData = dataExample.split("*")
for datum in splitData:
    print(datum, "is a split element from dataExample")


# replace method, sometimes you want to find and replace characters or stings within a string
print(dataExample.replace("*", "!!"))


"""
Tuples - pronounced 2-ple
 These are a grouping of data in an immutable structure. Immutable means the length of the tuple
 (I think of it as a container that is not allowed to change like and egg carton)
 Tuples are enclosed in round brackets () and the values are separated by commas, the values in a tuple are
 accessed using integers starting with 0 and then going 0, 1, 2,.... Access the last value in the tuple 
 starting with -1 and count backward as -1, -2, -3.
"""

# coordinates example
threeSpace = (99, 55, 8.7)
print(threeSpace)

### unpacking and packing

# unpack
x, y, z = threeSpace
print(x, y, z)

# and pack
nuSpace = (z, x, y)
print(nuSpace)


# calling a single value.
print(threeSpace[0], 'is the first value and', threeSpace[-1], "is the last value")

# Here is an example of a tuple made of a mixture of data types stings and floats.
bankInfo = ('Caleb', '0938583892', -88.8)
print(bankInfo, 'is my bank info')

# this is a number formating example, the formatting is based on "C"-code number formatting
name, bankAccountNum, balance = bankInfo
print("$" + str('%2.2f' % balance) + " is my balance")

# tuple of tuples, a tuple can be made of other tuples
tupOfTup = (threeSpace, bankInfo)
print(tupOfTup, '\n')


"""
Lists
    These a grouping of data in an mutable structure. Use a list when your data is being collected or for any other
    reason that its length might change.
    (I think of lists as a train that can have cars added or subtracted at different stations along it journey)
    Lists are enclosed in square brackets [] and the values are separated by commas, the values in a list are
    accessed using integers starting with 0. Access that last value in the list starting with -1.
"""

# list example
basicList = ['rrrrrr', 5, 'rrrrrr']
print(basicList)

# the empty list
basicList = []
print(basicList)

# The append method
basicList = ['rrrrrr', 5, 'rrrrrr']
basicList.append('aString')
# add a single element to the end of a list
print(basicList)

# the extend method
diffList = [63498, "skejkg", 77777, ('he', 4)]
# concatenate 2 lists together.
basicList.extend(diffList)
print(basicList, '\n')

# list of tuples
tupleOne = (1, 2, 3)
tupleTwo = (4, 5, 6, 7)
tupleThree = (8, 9, 0)
listOfTuples = [tupleOne, tupleTwo, tupleThree, (11, 12)].append((13, 14))

# get the last tuple in the list
print(listOfTuples[4], "equivenently", listOfTuples[-1])

# get the 2nd element in the last tuple in the list
print(listOfTuples[-1][1])

"""
Dictionaries
    A dictionary is a way to store data using key-value pairs. While a list or a tuple uses an integer to access
    stored data, a dictionary value is assessed using a key, which can be an integer, string, float, or
    even more complex data types, I have used some crazy keys.
    Dictionaries are enclosed in curly brackets {} and have and use a colon : to link
    key:value pairs. The key value pairs are separated by commas. To get a list of all the keys
    in a given dictionary, use the .keys() method.
"""

# dictionary example
aDict = {'apple':'is a piece of red fruit'}
print(aDict['apple'])

# empty dictionary
aDict = {}

# add a key value pair
aDict['4'] = ' this is a string of stuff'
aDict['puppy'] = ' Here is my pup!'
aDict[7.7] = 'This key is a float'
print(aDict)
print(aDict[7.7])

# get all the keys for a dictionary
print(aDict.keys())


"""
The for loop
"""

# using the range function to make a counter
for aNumber in range(10):
    print(aNumber)


# using a list
aList = ["Sing a song,", "If the sun refused to shine,", "I don't mind, I don't mind."]
for aLyric in aList:
    print(aLyric)

# using enumerate

# with a break

# with an else


"""
the try statement
"""




"""
A definition
"""




