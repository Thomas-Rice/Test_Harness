import stitcherTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.stitcherTemplate(__file__)
#Return the node created - In this case C_CameraSolver
stitcher = CS.returnNode()

''' Variables '''
stitcher['blendType'].setValue('Multi-Band')

#Write out the result and then compare that with the reference images
CS.compare()