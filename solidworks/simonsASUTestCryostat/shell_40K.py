import sys
from solidworks.swVariables import equationsFile
from solidworks.simonsASUTestCryostat.rectangleCryoShell import inch_str, mm_str, inch_to_mm,\
    workingLen, workingWidth, workingDepthBottom, workingDepthTop

parentDir = "C:\\Users\\chwheele.ASURITE\\Documents\\GrabCAD\\SO\\" + \
            "Universal Readout Harness\\ASU Test Cryostat\\40 K"
valuesDict = {}

rearExtensionDistance = 40.0
leftExtensionDistance = rearExtensionDistance
rightExtensionDistance = rearExtensionDistance
frontExtensionDistance = 150.0
# measured values
insert40K_X = 300.0
insert40K_Z = 400.0
expected_edgeOverLap = 15.0

refHole_to_edgeX = 10.935
refHole_to_edgeZ = 9.065

# 2 corner holes, 4 edge holes
refHole_to_smallSideNextHoleX = 53.721
refHole_to_smallSideNextHoleZ = 7.0485
smallSideHole_CenterToCenter = 56.896

# 2 corner holes, 6 edge holes
refHole_to_largeSideNextHoleX = 3.175
refHole_to_largeSideNextHoleZ = 47.9425
largeSideHole_CenterToCenter = 54.991

# Calculations for Left Bottom Flange
leftBottomFlangeCornerReferenceScrewInsetX = rearExtensionDistance + refHole_to_edgeX
leftBottomFlangeCornerReferenceScrewInsetZ = expected_edgeOverLap - refHole_to_edgeZ
leftBottomFlange_lengthX = rearExtensionDistance + insert40K_X + frontExtensionDistance
leftBottomFlange_widthZ = expected_edgeOverLap + leftExtensionDistance

# Left side (viewed from above and with the cold head at the "front") bottom flange at 40k
leftBottomFlangeCornerReferenceScrewInsetX_str = "leftBottomFlangeCornerReferenceScrewInsetX"
valuesDict[leftBottomFlangeCornerReferenceScrewInsetX_str] = (leftBottomFlangeCornerReferenceScrewInsetX, mm_str)
leftBottomFlangeCornerReferenceScrewInsetZ_str = "leftBottomFlangeCornerReferenceScrewInsetZ"
valuesDict[leftBottomFlangeCornerReferenceScrewInsetZ_str] = (leftBottomFlangeCornerReferenceScrewInsetZ, mm_str)

leftBottomFlange_lengthX_str = "leftBottomFlange_lengthX"
valuesDict[leftBottomFlange_lengthX_str] = (leftBottomFlange_lengthX, mm_str)
leftBottomFlange_widthZ_str = "leftBottomFlange_widthZ"
valuesDict[leftBottomFlange_widthZ_str] = (leftBottomFlange_widthZ, mm_str)


bottomShellStringList = [leftBottomFlangeCornerReferenceScrewInsetX_str, leftBottomFlangeCornerReferenceScrewInsetZ_str,
                         leftBottomFlange_lengthX_str, leftBottomFlange_widthZ_str]

leftBottomFlange = equationsFile(fullFilePath=parentDir, fileName="leftBottomFlangeEquations")
leftBottomFlange.listAddVarLine(bottomShellStringList, valuesDict)
leftBottomFlange.addRefLine("D1@sketch1", leftBottomFlangeCornerReferenceScrewInsetX_str)
leftBottomFlange.addRefLine("D2@sketch1", leftBottomFlangeCornerReferenceScrewInsetZ_str)
leftBottomFlange.addRefLine("D3@sketch1", leftBottomFlange_lengthX_str)
leftBottomFlange.addRefLine("D4@sketch1", leftBottomFlange_widthZ_str)

if sys.platform == "win32":
    leftBottomFlange.writeFile()
else:
    print(leftBottomFlange.fileContent)
