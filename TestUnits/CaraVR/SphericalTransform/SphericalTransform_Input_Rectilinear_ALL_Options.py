import sphericalTransformTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.sphericalTransformTemplate(__file__)
#Return the node created - In this case C_CameraSolver
STNode = CS.returnNode()

''' Variables '''
STNode['projTypeInput'].setValue('Rectilinear')
nuke.tprint('setting K Input')
STNode['KInput'].setValue([2.0,2.0,2.0])
nuke.tprint('created K Input')

nuke.tprint('setting shift Input')
STNode['shiftInput'].setValue([2.0,2.0])
nuke.tprint('created shift Input')

nuke.tprint('setting focal Input')
STNode['focalInput'].setValue(2)
nuke.tprint('created focal Input')

nuke.tprint('setting sensorInput ')
STNode['sensorInput'].setValue([2.0,2.0])
nuke.tprint('created sensorInput')

nuke.tprint('setting sensorInput ')
STNode['sensorInput'].setValue([2.0,2.0])
nuke.tprint('created sensorInput')

nuke.tprint('setting positionInput ')
STNode['positionInput'].setValue([2.0,2.0,2.0])
nuke.tprint('created positionInput')


#Write out the result and then compare that with the reference images
CS.compare()

