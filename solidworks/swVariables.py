"""
This script generates the txt files that SolidWorks can reference for global variables and equations within parts.
"""
import os


def putInQuotes(var):
    return "\"" + var + "\""


def makeLine(varName, value, units):
    return putInQuotes(varName) + "=" + str(value) + units + "\n"


class equationsFile():
    def __init__(self, fullFilePath, fileName="equations"):
        self.saveName = os.path.join(fullFilePath, fileName + ".txt")
        self.fileContent = []


    def addVarLine(self, varName, value, units):
        self.fileContent.append(makeLine(varName, value, units))


    def addRefLine(self, ref, var):
        self.fileContent.append(putInQuotes(ref) + "=" + putInQuotes(var) + "\n")


    def writeFile(self, appendMode=False):
        if appendMode:
            f = open(self.saveName, "a")
        else:
            f = open(self.saveName, "w")
        for singleLine in self.fileContent:
            f.write(singleLine)
        f.close()


if __name__ == "__main__":
    shellSection = equationsFile(fullFilePath="C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\" +
                                              "Universal Readout Harness\\ASU Test Cryostat\\EDM Shell")
    innerLength_str = "innerLength"
    innerWidth_str = "innerWidth"
    innerDepth_str = "innerDepth"
    wallThickness_str = "wallThickness"
    inch_str = "in"
    shellSection.addVarLine(innerLength_str, 30, inch_str)
    shellSection.addVarLine(innerWidth_str, 20, inch_str)
    shellSection.addVarLine(innerDepth_str, 10, inch_str)
    shellSection.addVarLine(wallThickness_str, 0.25, inch_str)
    shellSection.addRefLine("D1@sketch1", innerLength_str)
    shellSection.addRefLine("D2@sketch1", innerWidth_str)
    shellSection.addRefLine("D1@Boss-Extrude2", innerDepth_str)
    #shellSection.writeFile()
    print(shellSection.fileContent)


