import sphericalTransformTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.sphericalTransformTemplate(__file__)
#Return the node created - In this case C_CameraSolver
STNode = CS.returnNode()
''' Variables '''
STNode['modeOutput'].setValue('Rotation Angles')
STNode['rotationOrderOutput'].setValue(3)
STNode['rotationAnglesOutput'].setValue(100)

#Write out the result and then compare that with the reference images
CS.compare()



