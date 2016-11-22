import basicCaraTestClass as BCTC

''' Setup '''
# Create CameraSolver and Read nodes
SSetup = BCTC.stitcherOps(__file__)
# Return the node and path to reference frames
stitcher, filePath = SSetup.setup()

''' Variables '''
stitcher['enableStereo'].setValue(1)
stitcher['consistency'].setValue(1.2)

''' WRITE OUT '''
#Get the path to the images so we can compare
pathToCompare = SSetup.writeOut(stitcher)

''' Compare '''
#Create the compare node with all settings
CompareObj = BCTC.compareImages(0.001, filePath, 1, 1)
#Compare the reult to the ref image
CompareObj.stitcherCompare(pathToCompare)