import os, sys

parentDirectory = "C:\\Users\\ffarama1\\Documents"

fileName = "SupportsEquations.txt"

fullFileName = os.path.join(parentDirectory, fileName)

textFile = open(fullFileName, "w")
textFile.write("\"fiberglass_height\"=160mm\n")
textFile.write("\"fiberglass_width\"=160mm\n")
textFile.write("\"slot_length\"=\"fiberglass_width\"\n")
textFile.write("\"D1@Sketch1\"=\"fiberglass_width\"\n")
textFile.write("\"D2@Sketch1\"=\"fiberglass_height\"\n")
textFile.write("\"D3@Sketch1\"=\"slot_length\"\n")


textFile.close()
print("wrote file:", fullFileName)


import os, sys

parentDirectory = "C:\\Users\\ffarama1\\Documents"

fileName = "SupportsEquations2.txt"

fullFileName = os.path.join(parentDirectory, fileName)

textFile = open(fullFileName, "w")
textFile.write("\"fiberglass_height\"=160mm\n")
textFile.write("\"fiberglass_width\"=160mm\n")
textFile.write("\"slot_length\"=\"fiberglass_width\"\n")
textFile.write("\"D3@Sketch1\"=\"slot_length\"\n")


textFile.close()
print("wrote file:", fullFileName)


import os, sys

parentDirectory = "C:\\Users\\ffarama1\\Documents"

fileName = "SupportsEquations3.txt"

fullFileName = os.path.join(parentDirectory, fileName)

textFile = open(fullFileName, "w")
textFile.write("\"fiberglass_height\"=160mm\n")
textFile.write("\"fiberglass_width\"=160mm\n")
textFile.write("\"slot_length\"=\"fiberglass_width\"\n")
textFile.write("\"D3@Sketch1\"=\"slot_length\"\n")


textFile.close()
print("wrote file:", fullFileName)