import os, sys

parentDirectory = "C:\\Users\\ffarama1\\Documents"

fileName = "SupportsEquations.txt"

fullFileName = os.path.join(parentDirectory, fileName)

textFile = open(fullFileName, "w")
textFile.write("\"fiberglass_height\"=160mm\n")
textFile.write("\"fiberglass_width\"=150mm\n")
textFile.write("\"D1@Sketch1\"=\"fiberglass_width\"\n")
textFile.write("\"D2@Sketch1\"=\"fiberglass_height\"\n")


textFile.close()
print("wrote file:", fullFileName)
