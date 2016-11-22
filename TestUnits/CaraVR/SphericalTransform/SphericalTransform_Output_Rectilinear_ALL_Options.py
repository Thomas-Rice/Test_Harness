import basicCaraTestClass as BCTC
import sphericalTransformTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.sphericalTransformTemplate(__file__)
#Return the node created - In this case C_CameraSolver
STNode = CS.returnNode()
''' Variables '''
STNode['projTypeOutput'].setValue('Rectilinear')
nuke.tprint('setting K output')
STNode['KOutput'].setValue([2.0,2.0,2.0])
nuke.tprint('created K output')

nuke.tprint('setting shift output')
STNode['shiftOutput'].setValue([2.0,2.0])
nuke.tprint('created shift output')

nuke.tprint('setting focal output')
STNode['focalOutput'].setValue(2)
nuke.tprint('created focal output')

nuke.tprint('setting sensorOutput ')
STNode['sensorOutput'].setValue([2.0,2.0])
nuke.tprint('created sensorOutput')

nuke.tprint('setting sensorOutput ')
STNode['sensorOutput'].setValue([2.0,2.0])
nuke.tprint('created sensorOutput')

nuke.tprint('setting positionOutput ')
STNode['positionOutput'].setValue([2.0,2.0,2.0])
nuke.tprint('created positionOutput')


#Write out the result and then compare that with the reference images
CS.compare()

