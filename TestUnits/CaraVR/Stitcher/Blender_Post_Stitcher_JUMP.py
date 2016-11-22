import stitcherTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.stitcherTemplate(__file__)
#Return the node created - In this case C_CameraSolver
stitcher = CS.returnJumpNode()
stitcher['enableStereo'].setValue(1)

OneView = nuke.createNode("OneView")
OneView['view'].setValue('right')

''' Variables '''
# Create the blender
joinViews = BCTC.createAndConnectJoinViews(stitcher)
joinViews.connectInput(7, OneView)
blender = BCTC.createNode('C_Blender1_0')


#Write out the result and then compare that with the reference images
CS.compare()



