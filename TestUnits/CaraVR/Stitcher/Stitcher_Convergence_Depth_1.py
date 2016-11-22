import stitcherTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.stitcherTemplate(__file__)
#Return the node created - In this case C_CameraSolver
stitcher = CS.returnNode()

''' Variables '''
stitcher['convergenceDepth'].setValue(1)

#Write out the result and then compare that with the reference images
CS.compare()