
class PhysicalParams:
    def __init__(self):
        """Controlled Values"""
        self.inch_str = "in"
        self.mm_str = "mm"

        # in inches (unless otherwise specified)
        # for Vacuum shell components
        self.inch_to_mm = 25.4
        (self.workingWidth, self.workingDepthBottom, self.workingDepthTop) = (22.0, 9.0, 9.0)
        self.shellThickness = 0.375
        self.bottomWallShellThickness = 0.5
        self.lidThickness = 0.5
        self.oringInsetDistance = 0.4
        self.millRadius = 2.0
        self.flangeWidth = 1.5
        self.flangeThickness = 0.5
        self.flangeHoleInset = 0.4
        self.tolerance = 0.05
        self.coldhead_insert_clearance = 0.5

        # Collar Extension for Coldhead
        self.collar_ID = 5
        self.collar_boltCircleDiameter = 6.693
        self.collar_OD = 7.5
        self.collar_oringID = 5.5
        self.collar_oringWidth = 0.181
        self.collar_oringDepth = 0.110
        self.collar_height = 4
        self.underHeadThruDistance = (60.0 - 6.0)  # in millimeters

        # 40 K shield (in millimeters)
        self.shieldThickness = (1.0 / 8.0)  # inches
        self.rearExtensionDistance = 40.0
        self.leftExtensionDistance = self.rearExtensionDistance
        self.rightExtensionDistance = self.rearExtensionDistance
        self.frontExtensionDistance = 150.0

        self.shieldSpace_4K_40K = 15.0
        self.shieldSpace_40K_300K = 15.0

        """
        measured values (in millimeters)
        """
        # 300 K Insert Flange measurements (millimeters)
        self.vacuumInsertWidth = 360.2
        self.vacuumInsertLen = 461.8

        # cold head measurements (millimeters)
        self.coldhead_OD = 180.0

        # 40K shield related measurements
        self.insert40K_X = 300.0
        self.insert40K_Z = 400.0
        self.expected_edgeOverLap = 15.0

        self.refHole_to_edgeX = 10.935
        self.refHole_to_edgeZ = 14.58

        # 2 corner holes, 4 edge holes
        self.refHole_to_smallSideNextHoleX = 53.721
        self.refHole_to_smallSideNextHoleZ = 7.0485
        self.smallSideHole_CenterToCenter = 56.896

        # 2 corner holes, 6 edge holes
        self.refHole_to_largeSideNextHoleX = 3.175
        self.refHole_to_largeSideNextHoleZ = 47.9425
        self.largeSideHole_CenterToCenter = 54.991

        # insert measurements
        self.cryoFloorTo40K_InsertBottom = 94.3
        self.insert_40KThickness = 6.35
        self.workingDist_40K_4K = 104.0
        self.insert_4KThickness = 6.35
        self.rearOfInsert300K_edgeTo40K_edge = 30.1

        # Calculation for Bottom Vacuum Wall (inches)
        self.insertDist = (self.rearExtensionDistance - self.rearOfInsert300K_edgeTo40K_edge +
                           self.shieldSpace_40K_300K)
        self.workingLen = (self.insertDist + self.vacuumInsertWidth
                           + (self.coldhead_insert_clearance * self.inch_to_mm)
                           + (self.collar_OD * self.inch_to_mm / 2.0) + (self.coldhead_OD / 2.0)) / self.inch_to_mm

        # Calculations for Left Bottom Flange
        self.leftBottomFlangeCornerReferenceScrewInsetX = self.rearExtensionDistance + self.refHole_to_edgeX
        self.leftBottomFlangeCornerReferenceScrewInsetZ = self.expected_edgeOverLap - self.refHole_to_edgeZ
        self.leftBottomFlange_lengthX = self.rearExtensionDistance + self.insert40K_X + self.frontExtensionDistance
        self.leftBottomFlange_widthZ = self.expected_edgeOverLap + self.leftExtensionDistance

        # Flange Thicknesses
        self.bottomFlangeThickness = self.shieldThickness  # inches
        self.topFlangeThickness = self.shieldThickness  # inches
        self.lid_shieldThickness = self.shieldThickness  # inches
        self.totalShieldThickness = (self.bottomFlangeThickness + self.lid_shieldThickness) * self.inch_to_mm

        # Calculations for 40K shield Wall height
        self.shield_40K_workingHeight = ((self.workingDepthBottom + self.workingDepthTop) * self.inch_to_mm) \
                                        - self.cryoFloorTo40K_InsertBottom - self.insert_40KThickness \
                                        - self.totalShieldThickness - self.shieldSpace_40K_300K

        # Calculations for 4K shield Wall height
        self.shield_4K_workingHeight = ((self.workingDepthBottom + self.workingDepthTop) * self.inch_to_mm) \
                                   - self.cryoFloorTo40K_InsertBottom - self.insert_40KThickness \
                                   - self.workingDist_40K_4K - self.insert_4KThickness \
                                   - (2.0 * self.totalShieldThickness) - self.shieldSpace_40K_300K \
                                   - self.shieldSpace_4K_40K
