# import cameraSolverTemplate as CST
# import basicCaraTestClass as BCTC

sys.path.append("/Users/macadmin/Desktop/nuketests/Tests/Apps/CaraVR/TestUtilModules")
import basicCaraTestClass as BCTC

sys.path.append("/Users/macadmin/Desktop/nuketests/Tests/Apps/CaraVR/TestUnits/CaraVR/cameraSolver")
import cameraSolverTemplate as CST

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.cameraSolverTemplate(__file__)
#Return the node created - In this case C_CameraSolver
node = CS.returnNode()

''' Variables '''
node['convergenceDepth'].setValue(1)

#Write out the result and then compare that with the reference images
CS.compare()


import sys
sys.exit(0)


# #Setup a cameraSolver and readnodes all connected from the template class
# CS = CST.cameraSolverTemplate(__file__)
# #Return the node created - In this case C_CameraSolver
# node = CS.returnNode()
