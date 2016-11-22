import FnNukeTestUtils, FnImageSequence
import FnTestUtils
import os
import glob


'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 27/07/2016
'''
# Override to generate a cara licsense
def MakeCaraTest(BaseClass):
    class CaraTest(BaseClass):

        def getLicense(self, licRequester):
            super(CaraTest, self).getLicense(licRequester)
            from FnLicensing import FnLicenseDescription
            licenceDescription = FnLicenseDescription(product="caravr_nuke",
                                                      licenseType = FnLicenseDescription.TYPE_RLM,
                                                      generator = FnLicenseDescription.GENERATOR_FNHASHLIC,
                                                      verByNum = '1.0',
                                                      rlmAllowVM = True)
            licRequester.addLicense(licenceDescription)
    return CaraTest


def GetTests(testSpecifierObj):
    tests = []
    specialRequirementsTests = []
    testIdentifier = None
    test = None
    time = 30
    pyScriptsDir = "TestUnits/CaraVR"
    path = '/Users/Tom/Desktop/nuketests/Tests/Apps/CaraVR/TestUnits/CaraVR/'
    # Get all directories in this directory [1] is the directory part of the tuple [0] is the root and [2] is files
    directories = os.walk(path).next()[1]



    '''################################################################## TestS pecifier Dictionary ################################################################'''
                                                    #Test Type , Time
    testSpecifierDict = {   'Test_Dir'           : ['Com', 500]}
                            #'SphericalTransform' : ['Z0', 60],
                            #'Stitcher'           : ['Z0', 300],
                             #'CameraSolver'       : ['Z0', 60],
                             #'ColourMatcher'      : ['Z0', 60],
                             #'General'            : ['Z0', 60],
                             #'Exports'            : ['Z0', 60]}

    '''################################################################## Special Requirements Tests #############################################################'''
                                                                # TimeOut, testIdentifier, Keywords
    specialRequirementsList =  {'CameraSolver_Solve_Compare_Z0' : [300, None]}



    #Search each folder and depending on the folder name do something special
    for directory in directories:
        if directory in testSpecifierDict:
            testIdentifier = testSpecifierDict[directory][0]
            time = testSpecifierDict[directory][1]

            for pyFile in os.listdir(os.path.join(path, directory)):
                if '.DS_Store' not in pyFile:
                    if 'Template' not in pyFile:
                        if testIdentifier == 'Z0':
                            test = MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName= pyFile, timeout=time, scriptName = os.path.join(pyScriptsDir, directory, pyFile))
                        elif testIdentifier == 'NZ0':
                            test = MakeCaraTest(FnNukeTestUtils.FnCheckNonZeroExitStatus)( testName= pyFile, scriptName = os.path.join(pyScriptsDir, directory, pyFile))
                        elif testIdentifier == 'Out':
                            test = MakeCaraTest(FnNukeTestUtils.CheckOutputTest)( testName= pyFile, scriptName = os.path.join(pyScriptsDir, directory, pyFile), expectedOutput="Asserted that Compare worked as expected.", unexpectedOutput='Asserted that Compare FAILED.')
                        elif testIdentifier == 'OutC':
                            test = MakeCaraTest(FnNukeTestUtils.FnCheckOutputContains)( testName= pyFile, scriptName = os.path.join(pyScriptsDir, directory, pyFile))
                        elif testIdentifier == 'OutNC':
                            test = MakeCaraTest(FnNukeTestUtils.FnCheckOutputDoesNotContain)( testName= pyFile, scriptName = os.path.join(pyScriptsDir, directory, pyFile))
                        elif testIdentifier == 'OutFC':
                            test = MakeCaraTest(FnNukeTestUtils.FnCheckFilesExistTest)( testName= pyFile, scriptName = os.path.join(pyScriptsDir, directory, pyFile))
                        elif testIdentifier == 'Com':
                            test = MakeCaraTest(FnNukeTestUtils.CompareFilesTest)(testName= pyFile,
                                                                                    scriptName = os.path.join(pyScriptsDir, directory, pyFile),
                                                                                    referenceFootageDir="/Volumes/netqa/netqa/Testing/TestHarness/Research/CaraVR/CameraSolver/",
                                                                                    timeout = 500,
                                                                                    expectedOutputFiles = ['CameraSolver_Convergence_Depth.%V.exr'])

                    


                        if test != None:
                            test.runInGui = True
                            test.runInTerminal = False
                            # Add the test Keyword
                            test.addKeywords(directory)
                            tests.append(test)
                    else:
                        print 'Skipping'

    return tests
                         
                        # for item in specialRequirementsList:
                        #     if item in pyFile:
                        #         time = specialRequirementsList[item][0]
                        #         testIdentifier = specialRequirementsList[item][1]
                        
                        # if testIdentifier != None:
                        #     test = getSpecificTest(testIdentifier)
                        # else:
                        #     #Default to compare Zero Exit for this test 
                        #     test = MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName= test_name, timeout=time, scriptName = os.path.join(pyScriptsDir, directory, pyFile))

            

    # specialRequirementsTests = [
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Convergence Depth", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Convergence_Depth.py")),
    #                 ]



# def GetTests(testSpecifierObj):
    # exportTests = []
    # tests = []
    # myDir = "TestUnits/CaraVR"
    # pyScriptsDir = os.path.join(myDir, "SphericalTransform")

''' 
    FOR EACH TEST THAT IS IN A FILE I HAVE , 
    READ EACH TEST  
    TAKE EACH VARIABLE
    INSERT THIS VARIABLE INTO THE TEMPLATE TEST FOR THIS OPERATION
    RUN TESTS
'''

    # exportTests = [ MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CS Export - Split", scriptName = os.path.join(pyScriptsDir,"Export_CameraSolver_Split.py" ))]

    # for test in exportTests:
    #     test.runInGui = True
    #     test.runInTerminal = False
    #     test.addKeywords("Exports")
    #     tests.append(test)


# def GetTests(testSpecifierObj):
#     exportTests = []
#     tests = []
#     cameraSolverTests = []
#     colourMatcherTests = []
#     myDir = '/Users/macadmin/Desktop/nuketests/Tests/Apps/CaraVR/TestUnits/CaraVR/'

    # cameraSolverScriptsDir = os.path.join(myDir, "CameraSolver/")
    # cameraSolverTests = [
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Convergence Depth", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Convergence_Depth.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Rig Preset F360-H3", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Import_Preset_F360-H3.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Rig Preset F360B-H3", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Import_Preset_F360B-H3.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Rig Preset Jaunt ONE", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Import_Preset_Jaunt_ONE.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Rig Preset PRO6-H3", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Import_Preset_PRO6-H3.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Rig Preset PRO7-H3", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Import_Preset_PRO7-H3.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Rig Preset PRO14-H3", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Import_Preset_PRO14-H3.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Output Format Check", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_OutputFormat.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Rig Size", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_RigSize.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Translate Rotate", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Translate_Rotate.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - Uniform Scale", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Uniform_Scale.py"))
    #                 ]



    # for test in cameraSolverTests:
    #     test.runInGui = True
    #     test.runInTerminal = False
    #     test.addKeywords("CameraSolver")
    #     tests.append(test)
    # return tests

    

    # colourMatcherScriptsDir = os.path.join(myDir, "ColourMatcher/")
    # colourMatcherTests = [
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="ColourMatcher - Input Projection", scriptName = os.path.join(colourMatcherScriptsDir,"ColourMatcher_Input_Projection.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="ColourMatcher - Colour and Exposure", scriptName = os.path.join(colourMatcherScriptsDir,"ColourMatcher_Match_Colour_And_Exposure.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="ColourMatcher - Exposure", scriptName = os.path.join(colourMatcherScriptsDir,"ColourMatcher_Match_Exposure.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="ColourMatcher - Global Exposure", scriptName = os.path.join(colourMatcherScriptsDir,"ColourMatcher_Match_Global_Exposure.py"))
    #                 ]



    # for test in colourMatcherTests:
    #     test.runInGui = True
    #     test.runInTerminal = False
    #     test.addKeywords("ColourMatcher")
    #     tests.append(test)
    # return tests




    # exportsScriptsDir = os.path.join(myDir, "Exports/")
    # exportTests = [ MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CS Export - Split", scriptName = os.path.join(exportsScriptsDir,"Export_CameraSolver_Split_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CS Export - Separate", scriptName = os.path.join(exportsScriptsDir,"Export_CameraSolver_Separate_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CS Export - Manual2D", scriptName = os.path.join(exportsScriptsDir,"Export_CameraSolver_Manual2D_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CS Export - Manual3D", scriptName = os.path.join(exportsScriptsDir,"Export_CameraSolver_Manual3D_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CS Export - Ingest Separate", scriptName = os.path.join(exportsScriptsDir,"Export_CameraSolver_Ingest_Separate.py")),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CS Export - Ingest Joined", scriptName = os.path.join(exportsScriptsDir,"Export_CameraSolver_Ingest_Joined.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CS Export - Cameras", scriptName = os.path.join(exportsScriptsDir,"Export_CameraSolver_Cameras_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CM Export - Split", scriptName = os.path.join(exportsScriptsDir,"Export_ColourMatcher_Split_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CM Export - Separate", scriptName = os.path.join(exportsScriptsDir,"Export_ColourMatcher_Separate_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CM Export - OCIO - Split", scriptName = os.path.join(exportsScriptsDir,"Export_ColourMatcher_OCIO_Split_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CM Export - OCIO - Separate", scriptName = os.path.join(exportsScriptsDir,"Export_ColourMatcher_OCIO_Separate_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="ST Export - Inverted", scriptName = os.path.join(exportsScriptsDir,"Export_SphericalTransform_Inverted_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="S Export - Manual STMap Split", scriptName = os.path.join(exportsScriptsDir,"Export_Stitcher_Manual_STMap_Split_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="S Export - Manual STMap Separate", scriptName = os.path.join(exportsScriptsDir,"Export_Stitcher_STMap_Serarate_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="T Export - Metadata Match Move", scriptName = os.path.join(exportsScriptsDir,"Export_Tracker_C_MetadataTransform_Match-Move_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="T Export - Metadata Stabilise", scriptName = os.path.join(exportsScriptsDir,"Export_Tracker_C_MetadataTransform_Stabilise_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="T Export - SphericalTransform Match Move", scriptName = os.path.join(exportsScriptsDir,"Export_Tracker_C_SphericalTransform_Match-Move_Z0.py" )),
    #                 MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="T Export - SphericalTransform Stabilise", scriptName = os.path.join(exportsScriptsDir,"Export_Tracker_C_SphericalTransform_Stabilise_Z0.py" ))]

    # for test in exportTests:
    #     test.runInGui = True
    #     test.runInTerminal = False
    #     test.addKeywords("Exports")
    #     tests.append(test)


     
                   
                           
                              
'''



    sphericalTransformTests = [
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Image_LL-Cross", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Image_LL-Cross.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Image_6x1", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Image_6x1.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Image_6x2", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Image_6x2.py")),
                    # MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Views", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Views.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Face_+X", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Face_+X.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Face_-X", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Face_-X.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Face_+Y", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Face_+Y.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Face_-Y", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Face_-Y.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Face_-Z", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Face_-Z.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Cubemap_Face_+Z", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Cubemap_Face_+Z.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Fisheye_Stereographic", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Fisheye_Stereographic.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Fisheye_Equidistant", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Fisheye_Equidistant.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Fisheye_Equisolid", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Fisheye_Equisolid.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Fisheye_Orthographic", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Fisheye_Orthographic.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_Look", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_Look.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_From-To_To", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_From-To_To.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_From-To_From", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_From-To_From.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_PTR", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_PTR.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_RotationAngles_XYZ", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_RotationAngles_XYZ.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_RotationAngles_XZY", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_RotationAngles_XZY.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_RotationAngles_YXZ", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_RotationAngles_YXZ.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_RotationAngles_YZX", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_RotationAngles_YZX.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_RotationAngles_ZXY", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_RotationAngles_ZXY.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rotation_RotationAngles_ZYX", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rotation_RotationAngles_ZYX.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Latlong", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Latlong.py")),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="SphericalTransform_Output_Rectilinear", scriptName = os.path.join(pyScriptsDir,"SphericalTransform_Output_Rectilinear.py"))]

MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="UndoRedo-AllNodes", scriptName = os.path.join(cameraSolverScriptsDir,"undoAllNodes.py" ))
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver_Solve_Compare_Z0", timeout=180 , scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_Solve_Compare_Z0.py" )),
                    MakeCaraTest(FnNukeTestUtils.CheckZeroExitStatus)( testName="CameraSolver - SetKeyFrames", scriptName = os.path.join(cameraSolverScriptsDir,"CameraSolver_SetKeyFrames.py")),
    for test in sphericalTransformTests:
        test.runInGui = True
        test.runInTerminal = False
        test.addKeywords("ST")
        tests.append(test)

    return tests







 '''