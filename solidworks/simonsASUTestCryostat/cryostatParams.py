pi = 3.14159265359

import getpass

class PhysicalParams:
    def __init__(self):
        if getpass.getuser() == "jemoor15":
            self.base_directory = "C:\\Users\\jemoor15\\Documents\\"
        else:
            self.base_directory = "C:\\Users\\chw3k5\\Documents\\"


        """Controlled Values"""
        self.inch_str = "in"
        self.mm_str = "mm"

        # in inches (unless otherwise specified)
        # for Vacuum shell components
        self.inch_to_mm = 25.4   # Do not change, set by an order to the machine shop
        (self.workingDepthBottom, self.workingDepthTop) = (6.0, 6.0)  # Do not change
        self.shellThickness = 1.0  # Do not change, set by an order to the machine shop
        self.bottomWallShellThickness = 0.5  # Do not change, set by an order to the machine shop
        self.lidThickness = 0.5  # Do not change, set by an order to the machine shop
        self.oringInsetDistance = 0.4  # Do not change, set by an order to the machine shop
        self.millRadius = 2.0  # Do not change, set by an order to the machine shop
        self.flangeWidth = 1.5  # Do not change, set by an order to the machine shop
        self.flangeThickness = 0.5  # Do not change, set by an order to the machine shop
        self.flangeHoleInset = 0.4  # Do not change, set by an order to the machine shop
        self.tolerance = 0.010  # Do not change, set by an order to the machine shop
        self.coldhead_insert_clearance = 0.5  # Do not change, set by an order to the machine shop

        # Collar Extension for Coldhead
        self.collar_ID = 5  # Do not change, set by an order to the machine shop
        self.collar_boltCircleDiameter = 170  # mm,   # Do not change, set by an order to the machine shop
        self.collar_OD = 7.5   # Do not change, set by an order to the machine shop
        self.collar_oringID = 5.5  # Do not change, set by an order to the machine shop
        self.collar_oringWidth = 0.181  # Do not change, set by an order to the machine shop
        self.collar_oringDepth = 0.110  # Do not change, set by an order to the machine shop
        self.collar_height = 4.0  # Do not change, set by an order to the machine shop
        self.underHeadThruDistance = (60.0 - 6.0)  # in millimeters  # Do not change, set by an order to the machine shop

        # 40 Cold head Heat strapping
        self.coldhead40K_clearanceForID = 2.0  # millimeters
        self.coldhead40K_OD_overshoot = 10.0

        # 4k Cold-head heat strapping
        self.coldhead4K_clearanceForID = self.coldhead40K_clearanceForID
        self.heatStrap4K_overshoot = 4.0

        self.heatPlate_leftOffsetFromRefScrew = 15.0
        self.heatPlate_rightOffsetFromRefScrew = 10.0

        # 40 K shield (in millimeters)
        # https://www.protocase.com/products/materials-components-finishes/materials/aluminum.php
        self.shieldSpace_40K_300K = 10.0  # Updated Variable for shields version 2

        self.shieldThickness = 2.06  # millimeters: 2.06 is gauge 12, 1.63 is gauge 14, 1.30 is gauge 16
        self.shieldThickness_heatConduction = (1.0 / 8.0) * self.inch_to_mm  # Updated Variable for shields version 2
        self.rearExtensionDistance = 55.0 - self.shieldSpace_40K_300K  # Updated Variable for shields version 2
        self.leftExtensionDistance = self.rearExtensionDistance  # Updated Variable for shields version 2
        self.rightExtensionDistance = self.rearExtensionDistance  # Updated Variable for shields version 2


        self.shieldsFlangeThickness = 10.00  # Updated Variable for shields version 2
        self.shieldsFlangeWidth = 24  # Updated Variable for shields version 2
        self.shieldsFlange_holeInset = 8.128  # Updated Variable for shields version 2

        self.HMS_bottomFlangeThickness = (3.0 / 16.0) * self.inch_to_mm  # Updated Variable for shields version 2
        self.HMS_topFlangeThickness = (3.0 / 16.0) * self.inch_to_mm  # Updated Variable for shields version 2
        self.coldhead40K_flange_thickness = 10.0  # Updated Variable for shields version 2
        self.coldhead40K_flange_Z = 185.0 - self.shieldSpace_40K_300K  # Updated Variable for shields version 2

        # 4 K shield (in millimeters)
        self.shieldSpace_4K_40K = 10.0  # Updated Variable for shields version 2
        self.fourK_plateHeight = (3.0 / 8.0) * self.inch_to_mm  # Updated Variable for shields version 2

        self.heatStrappingHeight4K = 28.0  # Updated Variable for shields version 2
        self.heatStrap4K_OD = 72.0  # Updated Variable for shields version 2
        self.heatStrappingLowerExtensionDistance = 57.675  # Updated Variable for shields version 2


        """
        measured values (in millimeters)
        """
        # 300 K Insert Flange measurements (millimeters)
        self.vacuumInsertWidth = 370.0  # Cannot Change, Part exists
        self.vacuumInsertLen = 470.0  # Cannot Change, Part exists

        """Coldhead measurements"""
        # 300K cold head measurements (millimeters)
        self.coldhead_OD = 180.0
        self.topOf300KFlange_toTopOf40KFlange = 156.0
        self.topOf40KFlange_toTopOf4KFlange = 236.5

        # 40 K coldhead measurements
        self.coldhead40K_ID = 90.0
        self.coldhead40K_boltCircle = 110.0
        self.coldhead40K_OD = 125.00
        self.coldhead40K_holeDiameter = 5.0
        self.coldhead40K_lowColdHeight = 23.5
        self.coldhead40K__highColdHeight = 36.0
        self.coldhead40K_flangeThickness = 6.5

        # 4 K coldhead measurements
        self.coldhead4K_ID = 46.0
        self.coldhead4K_boltCircle = 54.0
        self.coldhead4K_boltCircle = 54.0
        self.coldhead4K_OD = 64.0
        self.coldhead4K_holeDiameter = 5.0
        self.coldhead4K_lowColdHeight = 61.5
        self.coldhead4K_flangeThickness = 6.0

        self.coldhead_40Kto4K_shaft_OD = 39.05

        """40K shield related measurements"""
        self.insert40K_X = 300.0
        self.insert40K_Z = 400.0
        self.expected_edgeOverLap = 15.0

        self.refHole_to_edgeX = 10.935
        self.refHole_to_edgeZ = 14.58

        self.heatStrappingInset40K = 50.0
        self.MLI_inset40K = 5.0

        # 2 corner holes, 4 edge holes
        self.refHole_to_smallSideNextHoleX = 53.721
        self.refHole_to_smallSideNextHoleZ = 7.0485
        self.smallSideHole_CenterToCenter = 56.896

        # 2 corner holes, 6 edge holes
        self.refHole_to_largeSideNextHoleX = 3.175
        self.refHole_to_largeSideNextHoleZ = 47.9425
        self.largeSideHole_CenterToCenter = 54.991

        """4K shield related measurements"""
        self.insert4K_X = 264.0
        self.insert4K_Z = 364.0
        self.expected_edgeOverLap_4K = 15.0

        # small side 0 corner holes, 4 edge holes
        self.smallSideRefHole_to_edgeX_4K = 55.8
        self.smallSideRefHole_to_edgeZ_4K = 7.0
        self.smallSideHole_CenterToCenter_4K = 50.8
        #
        # 0 corner holes, 6 edge holes
        self.largeSideRefHole_to_edgeX_4K = 7
        self.largeSideRefHole_to_edgeZ_4K = 55
        self.largeSideHole_CenterToCenter_4K = 50.8

        """ General insert measurements"""
        self.cryoFloorTo40K_InsertBottom = 92.65
        self.insert_40KThickness = 8
        self.workingDist_40K_4K = 102.35
        self.insert_4KThickness = 8
        self.rearOfInsert300K_edgeTo40K_edge = 35

        """
        Calculation for Bottom Vacuum Wall (inches)
        
        These values have been hard coded on January 15, 2019, after the parts were sent
        out to the ASU machine shop for fabrication. 
        """
        self.insertDist = 20.0  # millimeters
        self.workingLen = 23.147638  # inches
        self.workingWidth = 20.07874  # inches

        """40K shield"""
        # Calculations for Left Bottom Flange
        self.leftBottomFlangeCornerReferenceScrewInsetX = self.rearExtensionDistance + self.refHole_to_edgeX
        self.leftBottomFlangeCornerReferenceScrewInsetZ = self.expected_edgeOverLap - self.refHole_to_edgeZ
        self.leftBottomFlange_lengthX = (self.workingLen * self.inch_to_mm) \
                                        - (2.0 * self.shieldSpace_40K_300K)
        self.leftBottomFlange_widthZ = self.expected_edgeOverLap + self.leftExtensionDistance

        # Calculations for Rear Bottom Flange
        self.rearBottomFlangeCornerReferenceScrewInsetX = self.rearExtensionDistance + self.refHole_to_edgeX
        self.rearBottomFlangeCornerReferenceScrewInsetZ = abs(self.expected_edgeOverLap - self.refHole_to_edgeZ)
        self.rearBottomFlange_lengthX = self.rearExtensionDistance + self.expected_edgeOverLap
        self.rearBottomFlange_widthZ = self.insert40K_Z - (2.0 * self.expected_edgeOverLap)

        self.total40K_FlangeWidth = self.rearBottomFlange_widthZ + (2.0 * self.leftBottomFlange_widthZ)
        #
        # Flange Thicknesses
        self.baseFlangeThickness = (1.0 / 8.0)  * self.inch_to_mm  # updated for version 2
        self.lid_shieldThickness = self.shieldThickness
        self.totalShieldThickness = (self.baseFlangeThickness + self.lid_shieldThickness) * self.inch_to_mm

        # 40 K coldhead shielding in g flanges
        self.coldheadShieldWall_height = 65.45 - self.shieldsFlangeThickness
        self.coldhead_flangeScrewInset = (self.shieldsFlangeWidth
         + self.shieldThickness_heatConduction) / 2.0

        # Calculations for 40K wall
        # self.Wall40K_halfWidthZ = (self.rearBottomFlange_widthZ / 2.0) + self.leftBottomFlange_widthZ
        #
        # Calculations for 40K shield Wall height
        self.shield_40K_workingHeight = ((self.workingDepthBottom + self.workingDepthTop) * self.inch_to_mm) \
                                        - self.cryoFloorTo40K_InsertBottom - self.insert_40KThickness \
                                        - self.totalShieldThickness - self.shieldSpace_40K_300K \
                                        - self.baseFlangeThickness - self.HMS_topFlangeThickness


        """
        4K Calculations
        """

        # 4K Bottom plate calculations
        self.shieldOffset_4K = self.shieldsFlangeWidth + self.shieldSpace_4K_40K  # Updated Variable for shields version2
        self.total4K_flangeWidth = self.total40K_FlangeWidth - (2.0 * self.shieldOffset_4K)  # Updated Variable for shields version2
        self.total4K_flangeLength = self.leftBottomFlange_lengthX - (2.0 * self.shieldOffset_4K)  # Updated Variable for shields version2

        self.shieldExtensionFromColdHeadCenter = 56.0 - self.shieldSpace_4K_40K  # Updated Variable for shields version2

        self.shieldsFlangeWidth_4K = 12.0 + self.shieldThickness
        self.shieldsFlange_holeInset_4K = ((self.shieldsFlangeWidth_4K - self.shieldThickness) / 2.0) \
                                          + self.shieldThickness
        # # Flange Thicknesses
        # self.bottomFlangeThickness_4K = self.shieldThickness_4K  # inches
        # self.lid_shieldThickness_4K = self.shieldThickness_4K  # inches
        # self.totalShieldThickness_4K = (self.bottomFlangeThickness_4K + self.lid_shieldThickness_4K) * self.inch_to_mm

