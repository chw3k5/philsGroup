pi = 3.14159265359
class PhysicalParams:
    def __init__(self):
        """Controlled Values"""
        self.inch_str = "in"
        self.mm_str = "mm"

        # in inches (unless otherwise specified)
        # for Vacuum shell components
        self.inch_to_mm = 25.4
        (self.workingDepthBottom, self.workingDepthTop) = (9.0, 9.0)
        self.shellThickness = 0.75
        self.bottomWallShellThickness = 0.5
        self.lidThickness = 0.5
        self.oringInsetDistance = 0.4
        self.millRadius = 2.0
        self.flangeWidth = 1.5
        self.flangeThickness = 0.5
        self.flangeHoleInset = 0.4
        self.tolerance = 0.005
        self.coldhead_insert_clearance = 0.5

        # Collar Extension for Coldhead
        self.collar_ID = 5
        self.collar_boltCircleDiameter = 6.693
        self.collar_OD = 7.5
        self.collar_oringID = 5.5
        self.collar_oringWidth = 0.181
        self.collar_oringDepth = 0.110
        self.collar_height = 4.0
        self.underHeadThruDistance = (60.0 - 6.0)  # in millimeters

        # 40 Cold head Heat strapping
        self.coldhead40K_clearanceForID = 2.0 # millimeters
        self.coldhead40K_OD_overshoot = 10.0

        # 4k Cold-head heat strapping
        self.coldhead4K_clearanceForID = self.coldhead40K_clearanceForID
        self.heatStrap4K_overshoot = 4.0

        self.heatPlate_leftOffsetFromRefScrew = 15.0
        self.heatPlate_rightOffsetFromRefScrew = 10.0

        # 40 K shield (in millimeters)
        self.shieldThickness = (1.0 / 8.0)  # inches
        self.rearExtensionDistance = 40.0
        self.leftExtensionDistance = self.rearExtensionDistance
        self.rightExtensionDistance = self.rearExtensionDistance
        self.frontExtensionDistance = 150.0


        self.shieldSpace_40K_300K = 15.0

        self.shieldsTopFlangeThickness = 3.0/8.0  # inches
        self.shieldsTopFlangeWidth = 20.0

        self.shieldsLeftAndRightTopFlangeScrewInsertDist = 0.25  # inches

        self.lidInsetFromInnerWalls = 3.0

        # 4 K shield (in millimeters)
        self.shieldThickness_4K = (1.0 / 8.0)  # inches
        self.rearExtensionDistance_4K = 40.0
        self.leftExtensionDistance_4K = self.rearExtensionDistance_4K
        self.rightExtensionDistance_4K = self.rearExtensionDistance_4K
        self.frontExtensionDistance_4K = 150.0

        self.shieldSpace_4K_40K = 15.0

        self.shieldsTopFlangeThickness_4K = 3.0/8.0  # inches
        self.shieldsTopFlangeWidth_4K = 20.0

        self.shieldsLeftAndRightTopFlangeScrewInsertDist_4K = 0.25 # inches

        self.lidInsetFromInnerWalls_4K = 3.0


        """
        measured values (in millimeters)
        """
        # 300 K Insert Flange measurements (millimeters)
        self.vacuumInsertWidth = 360.2
        self.vacuumInsertLen = 461.8

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
        self.cryoFloorTo40K_InsertBottom = 94.3
        self.insert_40KThickness = 6.35
        self.workingDist_40K_4K = 104.0
        self.insert_4KThickness = 6.35
        self.rearOfInsert300K_edgeTo40K_edge = 30.1

        """Calculation for Bottom Vacuum Wall (inches)"""
        self.insertDist = (self.rearExtensionDistance - self.rearOfInsert300K_edgeTo40K_edge +
                           self.shieldSpace_40K_300K)
        self.workingLen = (self.insertDist + self.vacuumInsertWidth
                           + (self.coldhead_insert_clearance * self.inch_to_mm)
                           + (self.collar_OD * self.inch_to_mm / 2.0) + (self.coldhead_OD / 2.0)) / self.inch_to_mm
        self.workingWidth = (self.rightExtensionDistance + self.insert40K_Z + self.leftExtensionDistance
                             + (2.0 * self.shieldSpace_40K_300K)) / self.inch_to_mm

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

        # Flange Thicknesses
        self.bottomFlangeThickness = self.shieldThickness  # inches
        self.lid_shieldThickness = self.shieldThickness  # inches
        self.totalShieldThickness = (self.bottomFlangeThickness + self.lid_shieldThickness) * self.inch_to_mm

        # Calculations for 40K wall
        self.Wall40K_halfWidthZ = (self.rearBottomFlange_widthZ / 2.0) + self.leftBottomFlange_widthZ

        # Calculations for 40K shield Wall height
        self.shield_40K_workingHeight = ((self.workingDepthBottom + self.workingDepthTop) * self.inch_to_mm) \
                                        - self.cryoFloorTo40K_InsertBottom - self.insert_40KThickness \
                                        - self.totalShieldThickness - self.shieldSpace_40K_300K

        # Calculations for 40K shield Top flanges
        self.RearAndFrontTopFlangeBendRadius = self.millRadius - self.shieldThickness
        self.RearAndFrontTopFlangeLenX = self.rearBottomFlange_widthZ + (2.0 *self.leftBottomFlange_widthZ) \
                                         - (2.0 * self.shieldThickness * self.inch_to_mm)
        self.LeftAndRightTopFlangeLen = self.leftBottomFlange_lengthX \
                                        - (2.0 * (self.millRadius + self.tolerance) * self.inch_to_mm)

        # Calculations for 40K shield Lid
        self.LidMillRadius = (self.RearAndFrontTopFlangeBendRadius * self.inch_to_mm) - self.lidInsetFromInnerWalls
        self.LidRearFrontLen = self.RearAndFrontTopFlangeLenX - (2.0 * self.lidInsetFromInnerWalls)
        self.LidLeftRightLen = self.LeftAndRightTopFlangeLen \
                               + (2.0 * self.RearAndFrontTopFlangeBendRadius * self.inch_to_mm) \
                               - (2.0 * self.lidInsetFromInnerWalls)
        self.LidHoles_InsetDist = (self.shieldsTopFlangeWidth / 2.0) - self.lidInsetFromInnerWalls

        """4K shield"""
        # Calculations for Left Bottom Flange
        self.leftBottomFlangeCornerReferenceScrewInsetX_4K = self.rearExtensionDistance_4K \
                                                             + self.smallSideRefHole_to_edgeX_4K
        self.leftBottomFlangeCornerReferenceScrewInsetZ_4K = self.expected_edgeOverLap_4K \
                                                             - self.smallSideRefHole_to_edgeZ_4K
        self.leftBottomFlange_lengthX_4K = (self.workingLen * self.inch_to_mm) \
                                            - (2.0 * self.shieldSpace_40K_300K) \
                                            - (2.0 * self.shieldThickness) \
                                            - (2.0 * self.shieldSpace_4K_40K)
        self.leftBottomFlange_widthZ_4K = self.expected_edgeOverLap_4K + self.leftExtensionDistance_4K

        # Calculations for Rear Bottom Flange
        self.rearBottomFlangeCornerReferenceScrewInsetX_4K = self.rearExtensionDistance_4K \
                                                             + self.largeSideRefHole_to_edgeX_4K
        self.rearBottomFlangeCornerReferenceScrewInsetZ_4K = abs(self.expected_edgeOverLap_4K - self.largeSideRefHole_to_edgeZ_4K)
        self.rearBottomFlange_lengthX_4K = self.rearExtensionDistance_4K + self.expected_edgeOverLap_4K
        self.rearBottomFlange_widthZ_4K = self.insert4K_Z - (2.0 * self.expected_edgeOverLap_4K)

        # Flange Thicknesses
        self.bottomFlangeThickness_4K = self.shieldThickness_4K  # inches
        self.lid_shieldThickness_4K = self.shieldThickness_4K  # inches
        self.totalShieldThickness_4K = (self.bottomFlangeThickness_4K + self.lid_shieldThickness_4K) * self.inch_to_mm

        # Calculations for 40K wall
        self.Wall4K_halfWidthZ = (self.rearBottomFlange_widthZ_4K / 2.0) + self.leftBottomFlange_widthZ_4K

        # calculations for 40 Half moon
        shellFloor_To40KInsertTop = self.cryoFloorTo40K_InsertBottom + self.insert_40KThickness
        shellFloor_To40KColdheadTop = self.topOf300KFlange_toTopOf40KFlange - (self.collar_height * self.inch_to_mm) \
                                      - (self.bottomWallShellThickness * self.inch_to_mm)
        self.halfMoonHeight = shellFloor_To40KInsertTop - shellFloor_To40KColdheadTop
        self.halfMoon_OD = self.coldhead40K_OD + self.coldhead40K_OD_overshoot

        # calculations for 40k Heat Plate
        self.fortyK_heatPlate_ID = self.coldhead_40Kto4K_shaft_OD + self.coldhead40K_clearanceForID
        self.halfMoonConductionArea = pi * (((self.halfMoon_OD / 2.0)**2.0)
                                             - ((self.coldhead40K_ID / 2.0) + self.coldhead40K_clearanceForID)**2.0)
        forty_k_edge_to_three_hundred_k_edge_insert = (self.vacuumInsertWidth - self.insert40K_X) / 2.0
        forty_k_edge_to_three_hundred_k_edge_coldhead = (self.collar_OD * self.inch_to_mm - self.halfMoon_OD) / 2.0
        # This is calculation to make the heat plate have the same conducive area as the half moon
        self.fortyK_heatPlate_height = self.halfMoonConductionArea / self.halfMoon_OD

        self.fortyK_heatPlate_extensionDistance = forty_k_edge_to_three_hundred_k_edge_coldhead \
                                                   + (self.coldhead_insert_clearance * self.inch_to_mm) \
                                                   + forty_k_edge_to_three_hundred_k_edge_insert \
                                                   + self.heatStrappingInset40K
        self.forty_heatPlate_widening \
            = max(self.coldhead40K_clearanceForID,
                  self.coldhead40K_clearanceForID + ((self.halfMoonConductionArea
                                                      / (self.heatStrappingInset40K - self.MLI_inset40K)) / 2.0)
                                                      - ((self.halfMoon_OD / 2.0) - self.coldhead40K_clearanceForID))
        # Calculations for 4K shield Wall height
        self.shield_4K_workingHeight = ((self.workingDepthBottom + self.workingDepthTop) * self.inch_to_mm) \
                                       - self.cryoFloorTo40K_InsertBottom - self.insert_40KThickness \
                                       - self.workingDist_40K_4K - self.insert_4KThickness \
                                       - self.totalShieldThickness_4K - self.totalShieldThickness \
                                       - self.shieldSpace_40K_300K - self.shieldSpace_4K_40K

        # Calculations for 4K shield Top flanges
        self.RearAndFrontTopFlangeBendRadius_4K = self.millRadius - self.shieldThickness_4K
        self.RearAndFrontTopFlangeLenX_4K = self.rearBottomFlange_widthZ_4K + (2.0 *self.leftBottomFlange_widthZ_4K) \
                                            - (2.0 * self.shieldThickness_4K * self.inch_to_mm)
        self.LeftAndRightTopFlangeLen_4K = self.leftBottomFlange_lengthX_4K \
                                           - (2.0 * (self.millRadius + self.tolerance) * self.inch_to_mm)

        # Calculations for 4K shield Lid
        self.LidMillRadius_4K = (self.RearAndFrontTopFlangeBendRadius_4K * self.inch_to_mm) - self.lidInsetFromInnerWalls_4K
        self.LidRearFrontLen_4K = self.RearAndFrontTopFlangeLenX_4K - (2.0 * self.lidInsetFromInnerWalls_4K)
        self.LidLeftRightLen_4K = self.LeftAndRightTopFlangeLen_4K \
                                  + (2.0 * self.RearAndFrontTopFlangeBendRadius_4K * self.inch_to_mm) \
                                  - (2.0 * self.lidInsetFromInnerWalls_4K)
        self.LidHoles_InsetDist_4K = (self.shieldsTopFlangeWidth_4K / 2.0) - self.lidInsetFromInnerWalls_4K

        # calculations for 4k Heat heat strapping
        self.heatStrap4K_OD = (self.heatStrap4K_overshoot * 2.0) + self.coldhead4K_OD
        coldhead_conduction_area = pi * ((self.heatStrap4K_OD / 2.0)**2.0)
        self.heatStrappingHeight4K = coldhead_conduction_area / (2.0 * self.heatStrap4K_OD)




        self.fourK_heatPlate_lengthX = 192.05 + self.expected_edgeOverLap_4K
        self.fourK_heatPlate_refScrewX = self.expected_edgeOverLap_4K - self.largeSideRefHole_to_edgeX_4K

        baseline_of_extention_dist_for_4K_plate = self.heatPlate_leftOffsetFromRefScrew \
                                                  + self.heatPlate_rightOffsetFromRefScrew \
                                                  + 4.0 * self.largeSideHole_CenterToCenter_4K
        fourK_heat_plate_overlab_area1 = self.expected_edgeOverLap_4K * self.rearBottomFlange_widthZ_4K

        self.fourK_heatConductionExtensionDistance = max(5.0, (coldhead_conduction_area
                                                               - fourK_heat_plate_overlab_area1)
                                                         / baseline_of_extention_dist_for_4K_plate)

        self.fourK_plateHeight = max(3.0 * self.inch_to_mm / 8.0,
                                     coldhead_conduction_area / self.rearBottomFlange_widthZ_4K)
        shellFloor_To4KInsertTop = shellFloor_To40KInsertTop + self.workingDist_40K_4K + self.insert_4KThickness
        shellFloor_To4KColdheadTop = shellFloor_To40KColdheadTop + self.topOf40KFlange_toTopOf4KFlange
        self.heatStrappingLowerExtensionDistance = shellFloor_To4KColdheadTop - shellFloor_To4KInsertTop \
                                                   - self.fourK_plateHeight
