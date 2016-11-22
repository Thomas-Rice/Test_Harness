import basicCaraTestClass as BCTC
import optparse

''' Setup '''
parser = optparse.OptionParser()
# Create CameraSolver and Read nodes
CMSetup = BCTC.colourMatcherOps(__file__)
# Do Specific Test Setup and get variables
node, filePath = CMSetup.setup()

''' Variables '''
# Take in the command line arguement from CaraVR.py to define what the variable will be for the test.
parser.add_option("--Var")
opts, _ = parser.parse_args()
#Apply the variable to the script.
node[opts.Var].setValue(1)

''' WRITE OUT '''
#Get the path to the images so we can compare
pathToCompare = CMSetup.writeOut(node)

''' Compare '''
#Create the compare node etc
CompareObj = BCTC.compareImages(0.001, filePath, 1, 1)
#Compare the reult to the ref image
CompareObj.compare()





