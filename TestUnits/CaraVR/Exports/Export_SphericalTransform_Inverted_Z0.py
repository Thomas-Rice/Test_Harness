# import os
import basicCaraTestClass as BCTC

'''
    Written by Thomas Rice Research QA - Any Questions Please Ask - thomas.rice@thefoundry.co.uk 27/07/2016
'''

#CameraSolver creation and solve
node = BCTC.createNode('C_CameraSolver1_0')
BCTC.loadImages(node)
BCTC.CS_matchCameras(node)
BCTC.CS_solveCameras(node)
#ColourMatcher creation and solve
STnode = BCTC.createNode('C_SphericalTransform1_0')
BCTC.setExportOption(STnode, 0)
BCTC.exportSelection(STnode)

nodeConnectionSet = BCTC.checkNodeConnections("C_CameraSolver1", "C_SphericalTransform2")


#The Format and connections that should be present
originalNodes =	set([
					('C_SphericalTransform1', 'C_SphericalTransform2'), 
					('C_SphericalTransform2',)])



result = nodeConnectionSet.difference(originalNodes)

if result != set([]):
    nuke.tprint('Test failed as the there was a difference in the node connections, they were .. ' , result )
    sys.exit(1)
else:
    nuke.tprint('Test passed as there were no differences in the two sets')
    pass
    sys.exit(0) 






