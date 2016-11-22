import sphericalTransformTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.sphericalTransformTemplate(__file__)
#Return the node created - In this case C_CameraSolver
STNode = CS.returnNode()
''' Variables '''
STNode['projTypeOutput'].setValue('Fisheye')
STNode['fisheyeTypeOutput'].setValue(3)

#Write out the result and then compare that with the reference images
CS.compare()


