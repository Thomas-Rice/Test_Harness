import stitcherTemplate as CST
import basicCaraTestClass as BCTC

#Setup a cameraSolver and readnodes all connected from the template class
CS = CST.stitcherTemplate(__file__)
#Return the node created - In this case C_CameraSolver
stitcher = CS.returnNode()
stitcher['enableStereo'].setValue(1)

OneView = nuke.createNode("OneView")
OneView['view'].setValue('left')
OneView.connectInput(0, stitcher)

OneView2 = nuke.createNode("OneView")
OneView2['view'].setValue('right')
OneView2.connectInput(0, stitcher)

OneView3 = nuke.createNode("OneView")
OneView3['view'].setValue('main')
OneView3.connectInput(0, stitcher)



''' Variables '''
# Create the blender
joinViews = BCTC.createAndConnectJoinViews(stitcher)
joinViews.connectInput(7, OneView)
joinViews.connectInput(8, OneView2)
joinViews.connectInput(0, OneView3)
blender = BCTC.createNode('C_Blender1_0')
blender['blendType'].setValue('Multi-Band')


#Write out the result and then compare that with the reference images
CS.compare()



