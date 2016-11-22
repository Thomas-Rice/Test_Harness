import cameraSolverTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.cameraSolverTemplate(__file__)
#Return the node created - In this case C_CameraSolver
node = CS.returnNode()

''' Variables '''
node['outputFormat'].setValue('PC_Video')

#Write out the result and then compare that with the reference images
CS.compare()